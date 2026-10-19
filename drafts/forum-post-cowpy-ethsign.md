# Draft forum post (Technical category, not Grants)

Title: cow-py: ETHSIGN orders signed over the unprefixed digest (0/19 services vectors), plus a shared services-generated corpus for cow-py and cow-rs

While checking the Python SDK against the services-generated conformance vectors from the cow-rs grant (cowdao-grants/cow-rs PR #63, services pinned at `df6a14b`), cow-py matched on everything except one scheme.

**Result, 19 vectors, chain 1, Hardhat account 0:**

- domain separator, struct hash, EIP-712 digest, UID: 19/19
- EIP-712 signature and recovered owner: 19/19
- `sign_order(..., SigningScheme.ETHSIGN)`: 0/19. The signature recovers to a random address.

**Cause.** `cowdao_cowpy/contracts/sign.py` signs `hash_typed_data(...)` directly for every scheme; `scheme` only labels the output. services' `hashed_ethsign_message` (and `GPv2Signing`, and the TS SDK via `signer.signMessage(arrayify(hashTypedData(...)))`) sign `keccak256("\x19Ethereum Signed Message:\n32" || eip712_digest)` for EthSign. Cancellations under ETHSIGN go through the same path.

**Impact.** `swap_tokens` hard-codes EIP712, so the default flow is fine. Any caller using ETHSIGN (wallets that only expose `eth_sign`) gets `WrongOwner` from the orderbook. The existing `test_sign_order[ETHSIGN]` only checks that `v` is `1b`/`1c`, so it could not catch it. ETHSIGN is in real use: 11 of the 11,653 open orders in the newest auction across the ten chains were signed with it.

**PR to cow-py:** <link>. Fixes `ecdsa_sign_typed_data` to honour the scheme, adds the v1 fixture with a parametrised test (fails 19 before, passes after), and tightens the two existing tests. No change for EIP712 callers.

**Shared corpus (v2), proposed to cow-rs:** <link>. A `v2.rs` module in the same generator, same services pin, emitting next to v1: domain separators, digests, signatures and UIDs on all ten orderbook chains; partially fillable orders; `OrderCancellation` and `OrderCancellations` struct hashes under both schemes; app-data hash, CIDv1 and `Validator` results for seven documents. cow-py consumes it in a second test file: 22 pass, and one strict xfail records that cow-py lacks the single-order cancellation type. cow-rs can consume the same file in its M2 test.

**Live check.** With the fix, cow-py's UID derivation and both ECDSA digests agree with the orderbook on all 11,653 open orders across the ten chains (auction bodies from the public solver-instances bucket, re-verified against `GET /orders/{uid}` where the auction DTO differs from the signed order). One doc note from that: the auction DTO carries remaining amounts and omits the signed fee, so anyone rebuilding orders from the solver feed needs `fullSellAmount`/`fullBuyAmount` and the orderbook record.

Harness and write-up: <link to cow repo>.

---

Posting notes for the author:
- Post in Technical (`tech-spells`), not the grants category. Tag nobody in the first post; reply to @mfw78, @bleu or @ss1738 only if they engage.
- Open both PRs first, then post with the links. New accounts cannot post more than two links; drop the repo link if needed.
- Do not mention a grant anywhere in the post. If a maintainer asks what else is worth doing, the answer is: consuming v2 in cow-rs's M2 test, adding the single-cancellation type to cow-py, and regenerating both fixtures whenever the services pin moves.
