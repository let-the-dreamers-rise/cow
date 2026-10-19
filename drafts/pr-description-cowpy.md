# PR title

fix(sign): sign ETHSIGN orders and cancellations over the EIP-191-prefixed digest; add services conformance vectors

# PR body

## Problem

`contracts.sign.ecdsa_sign_typed_data` signs the raw EIP-712 digest regardless of the requested `SigningScheme`; `scheme` only labels the result. For `SigningScheme.ETHSIGN` the settlement contract, `cowprotocol/services` (`model::signature::hashed_ethsign_message`) and `@cowprotocol/contracts` `sign.ts` all expect a signature over `keccak256("\x19Ethereum Signed Message:\n32" || eip712_digest)`. An ETHSIGN order or cancellation produced by cow-py therefore recovers to the wrong address and the orderbook rejects it with `WrongOwner`.

Checked against the services-generated conformance fixture from `cowdao-grants/cow-rs` (PR #63, services `df6a14b12eab016f1ae939aa5b666658208b0bc0`): hashing, UID and EIP-712 signing match on all 19 vectors; ETHSIGN signing matches on 0 of 19.

## Change

- `ecdsa_sign_typed_data` takes `scheme` (default `EIP712`, so existing callers are unchanged). EIP712 signs the digest as before. ETHSIGN signs `encode_defunct(primitive=digest)`. Other schemes raise.
- `sign_order` and `sign_order_cancellations` pass the scheme through.
- `tests/contracts/fixtures/conformance_vectors.v1.json` (copied verbatim from cow-rs; `services_sha` recorded in the file) and `tests/contracts/test_conformance_vectors.py`: domain separator, struct hash, EIP-712 digest, UID, EIP-712 signature and ETHSIGN signature for every vector. 19 fail on `main`, all pass here.
- `tests/contracts/test_sign.py`: `test_sign_order` and `test_sign_order_cancellation` now recover the signer under each scheme instead of checking `v`; new `test_ethsign_order_signature_is_an_eth_sign_of_the_eip712_digest`.

## Not changed

`swap_tokens` hard-codes EIP712, so the default swap flow was never affected. `sign.py` has five pre-existing `ruff` `UP0xx` findings on lines this PR does not touch; left alone to keep the diff reviewable.

## Verification

```
pytest tests/contracts            # 71 passed
pytest tests --ignore=tests/e2e   # 243 passed, 5 skipped
ruff check / ruff format          # clean on the new and changed test files
```
