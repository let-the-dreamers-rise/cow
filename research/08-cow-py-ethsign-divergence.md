# Finding: cow-py signs ETHSIGN orders over the wrong digest (19 of 19 services vectors fail)

Date: 19 October 2026. Checked against `cowdao-grants/cow-py` at `f4c95a2` (main, "feat: add Linea/Plasma/Ink chains", version 1.0.1) and the conformance fixture in `cowdao-grants/cow-rs` PR #63 (`ss1738:grant/m1-conformance-generator`, 6 commits, generated from `cowprotocol/services` at `df6a14b12eab016f1ae939aa5b666658208b0bc0`).

## What was checked

The cow-rs fixture is 19 order vectors (the full OrderKind x SellTokenSource x BuyTokenDestination matrix plus receiver, amount and validTo boundaries) on chain 1, settlement `0x9008...ab41`, signed by Hardhat account 0. For each vector it records, as computed by services' own `model::order` and `model::signature` code: domain separator, struct hash, EIP-712 digest, EthSign digest, both signatures with recovered owners, and the order UID.

The harness `tools/cowpy_conformance_check.py` builds the same order with cow-py's `Order`, hashes it with `hash_order`, derives the UID with `compute_order_uid`, and signs it with `sign_order` under both `SigningScheme.EIP712` and `SigningScheme.ETHSIGN`, using the same test key.

## Result

| Check | Vectors passing |
|---|---|
| domain separator | 19 / 19 |
| struct hash | 19 / 19 |
| EIP-712 digest | 19 / 19 |
| order UID | 19 / 19 |
| EIP-712 signature and recovered owner | 19 / 19 |
| EthSign digest (independently recomputed) | 19 / 19 |
| **ETHSIGN signature from `sign_order(..., SigningScheme.ETHSIGN)`** | **0 / 19** |

Under the ETHSIGN scheme every cow-py signature recovers to a different, meaningless address (for example `0x0d9d83ecb7...` for the first vector instead of `0xf39f...9266`).

## Cause

`cowdao_cowpy/contracts/sign.py`:

```python
def ecdsa_sign_typed_data(owner, domain_data, message_types, message_data) -> SignedMessage:
    return Account._sign_hash(
        hash_typed_data(domain_data, message_types, message_data), owner.key
    )

def sign_order(domain, order, owner, scheme) -> EcdsaSignature:
    normalized_order = normalize_order(order)
    signed_data = ecdsa_sign_typed_data(owner, domain, {"Order": ORDER_TYPE_FIELDS}, normalized_order)
    return EcdsaSignature(scheme=scheme, data=to_hex(signed_data.signature))
```

The `scheme` argument only labels the result. The bytes signed are the raw EIP-712 digest whichever scheme is requested. The same path is used by `sign_order_cancellation(s)`.

services (`crates/model/src/signature.rs` at the pinned commit) signs and recovers EthSign against a different 32 bytes:

```rust
fn hashed_ethsign_message(domain_separator: &DomainSeparator, struct_hash: &[u8; 32]) -> B256 {
    let mut message = [0u8; 60];
    message[..28].copy_from_slice(b"\x19Ethereum Signed Message:\n32");
    message[28..].copy_from_slice(hashed_eip712_message(domain_separator, struct_hash).as_slice());
    keccak256(message)
}
```

The settlement contract (`GPv2Signing`) and the reference TypeScript SDK do the same; `@cowprotocol/contracts` `src/ts/sign.ts` handles ETHSIGN with `owner.signMessage(ethers.utils.arrayify(hashTypedData(domain, types, data)))`, and `signMessage` applies the EIP-191 prefix.

## Impact

- The default `swap_tokens` flow in `cowdao_cowpy/cow/swap.py` hard-codes `SigningScheme.EIP712`, so the shipped happy path is unaffected. That is why the SDK's reported volume ($18M, 8,800 orders) does not show the bug.
- Anyone calling the public `contracts.sign.sign_order` or `sign_order_cancellation(s)` with `SigningScheme.ETHSIGN` (the scheme a wallet that only supports `eth_sign` must use) posts an order whose recovered owner does not match `from`. The orderbook's `order_validation.rs` returns `WrongOwner`, so the order is rejected; the same applies to cancellations under that scheme.
- The existing unit test `tests/contracts/test_sign.py::test_sign_order[ETHSIGN]` only asserts that the last byte of the signature is `1b` or `1c`. `test_sign_order_cancellation[1]` recovers against the unprefixed hash, so it encodes the wrong expectation and passes. Neither can catch this.

## Fix (branch `fix/ethsign-scheme-digest` in the local cow-py checkout; patch in `patches/`)

- `ecdsa_sign_typed_data` takes the scheme, signs the EIP-712 digest for EIP712, and for ETHSIGN signs `encode_defunct(primitive=digest)` (eth-account's EIP-191 `"\x19Ethereum Signed Message:\n32"` path), raising on EIP1271/PRESIGN. `sign_order` and `sign_order_cancellations` pass the scheme through. No signature change for EIP712 callers; `ecdsa_sign_typed_data` keeps its old behaviour as the default.
- `tests/contracts/test_conformance_vectors.py` plus the fixture: 58 parametrised checks (hashing/UID, EIP-712 signature, ETHSIGN signature) against the services-generated vectors. Fails 19 before the fix, passes after.
- `tests/contracts/test_sign.py`: the two existing tests now recover the signer under each scheme instead of inspecting `v`, and a new test asserts ETHSIGN equals a wallet's `eth_sign` of the EIP-712 digest.

Test runs on the branch: `tests/contracts` 71 passed; whole suite minus e2e 243 passed, 5 skipped. Lint: `ruff check`/`ruff format` clean on the changed test files; `sign.py` carries five pre-existing `UP0xx` findings on untouched lines (present at `HEAD` too), left alone to keep the diff minimal.

## Two smaller things seen on the way (not in the patch)

1. `hash_order_cancellation(s)` return `HexBytes.hex()`, which has no `0x` prefix on hexbytes >= 1.0 while the docstring says "hex-encoded"; `hash_order` returns bytes. Inconsistent return types in the same module.
2. `normalize_order` raises on `receiver == address(0)`. services and the settlement contract treat a zero receiver as "owner receives" and the fixture's `receiver_zero` and `receiver_none` vectors hash identically. The TypeScript SDK raises too, so this is an inherited design choice rather than a bug, but it is a conformance gap worth a docstring.

## Why this matters for the grant question

This is the Python twin of the cow-rs corpus the committee funded on 8 October ($2,000). It arrives with a concrete divergence, a failing-then-passing test, a fix under 30 lines, and the same services pin, which is the shape mfw78 asked for in thread 3546 ("services is the 'source of truth'... tested against properties / invariants etc derived from services"). The PR itself needs no grant. The grant-sized follow-on, if a maintainer wants it, is the generator side: regenerating the fixture for cow-py from the pinned services crate so the two SDKs share one corpus, plus the appData and cancellation vectors the current fixture scopes out.
