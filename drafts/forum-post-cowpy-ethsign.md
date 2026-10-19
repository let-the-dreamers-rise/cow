# Draft forum post (Technical category, not Grants)

Title: cow-py: ETHSIGN orders are signed over the unprefixed EIP-712 digest (0/19 services vectors), fix and conformance test attached

While checking the Python SDK against the services-generated conformance vectors from the cow-rs grant (cowdao-grants/cow-rs PR #63, services pinned at `df6a14b`), cow-py matched on everything except one scheme.

**Result, 19 vectors, chain 1, Hardhat account 0:**

- domain separator, struct hash, EIP-712 digest, UID: 19/19
- EIP-712 signature and recovered owner: 19/19
- `sign_order(..., SigningScheme.ETHSIGN)`: 0/19. The signature recovers to a random address.

**Cause.** `cowdao_cowpy/contracts/sign.py` signs `hash_typed_data(...)` directly for every scheme; `scheme` only labels the output. services' `hashed_ethsign_message` (and `GPv2Signing`, and the TS SDK via `signer.signMessage(arrayify(hashTypedData(...)))`) sign `keccak256("\x19Ethereum Signed Message:\n32" || eip712_digest)` for EthSign. Cancellations under ETHSIGN go through the same path.

**Impact.** `swap_tokens` hard-codes EIP712, so the default flow is fine. Any caller using ETHSIGN (wallets that only expose `eth_sign`) gets `WrongOwner` from the orderbook. The existing `test_sign_order[ETHSIGN]` only checks that `v` is `1b`/`1c`, and `test_sign_order_cancellation[ETHSIGN]` recovers against the unprefixed hash, so neither could catch it.

**PR:** <link> adds the fixture and a parametrised conformance test (fails 19 before, passes after), fixes `ecdsa_sign_typed_data` to honour the scheme, and tightens the two existing tests. `tests/contracts`: 71 passed. No change for EIP712 callers.

Harness and write-up: <link to cow repo>. Happy to add the generator side (shared corpus for cow-py and cow-rs from the same services pin, plus appData and cancellation vectors) if a maintainer wants it; that is the only part that would be grant-sized.

---

Posting notes for the author:
- Post in Technical (`tech-spells`), not the grants category. Tag nobody in the first post; reply to @mfw78 and @bleu only if they engage.
- Open the PR first, then post with the link. New accounts cannot post more than two links; keep it to the PR and the repo.
- Do not mention a grant in the title. The last paragraph is the only place it appears, framed as "if a maintainer wants it".
