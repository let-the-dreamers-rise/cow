# cow-py against 11,653 live orders on ten chains (19 October 2026)

Method: for each chain, take the newest auction body from the public solver-instances bucket (`prod/<chain>/auction/<id>.json`, the same feed solvers receive), rebuild every order with cow-py's `Order`, and check two things against what the orderbook published: the order UID from `compute_order_uid`, and, for the two ECDSA schemes, that the published signature recovers to the published owner when verified over the digest cow-py computes (EIP-712 digest for `eip712`; EIP-191-prefixed digest for `ethsign`, i.e. the fix in `patches/0001`). Orders whose auction-DTO fields differ from the signed order (the DTO carries remaining amounts and omits the signed fee) were re-fetched from `GET /api/v1/orders/{uid}` and checked on the canonical record. `presign` and `eip1271` orders get the UID check only.

Harness: `tools/cowpy_live_auction_check.py` then `tools/cowpy_live_auction_recheck.py` (read-only; two public endpoints).

| Chain | Auction | eip712 | ethsign | eip1271 | presign | Matched |
|---|---|---|---|---|---|---|
| mainnet | 13840372 | 4733 | 10 | 111 | 142 | 4996 / 4996 |
| base | 29159803 | 1651 | 1 | 638 | 30 | 2320 / 2320 |
| bnb | 25587735 | 2107 | | 61 | 2 | 2170 / 2170 |
| arbitrum-one | 8980538 | 969 | | 179 | 30 | 1178 / 1178 |
| polygon | 40432281 | 446 | | 79 | 3 | 528 / 528 |
| avalanche | 33897341 | 163 | | 33 | 3 | 199 / 199 |
| xdai | 17307834 | 169 | | 2 | 17 | 188 / 188 |
| linea | 36384835 | 55 | | | | 55 / 55 |
| ink | 5151711 | 10 | | | | 10 / 10 |
| plasma | 9194305 | 9 | | | | 9 / 9 |
| **Total** | | 10,312 | 11 | 1,103 | 227 | **11,653 / 11,653** |

What this shows:

1. With the fix applied, cow-py's order hashing, UID derivation and both ECDSA digests agree with the orderbook on every live order on every chain CoW runs on, including the ten chains' domain separators (cow-py's `Chain` enum covers all ten).
2. ETHSIGN is not a theoretical scheme: 11 live orders (10 on mainnet, 1 on Base) were signed with it. On unfixed cow-py, signatures for those would verify against the wrong digest; the fix verifies all 11.
3. The auction DTO is not the signed order. Anyone rebuilding orders from the solver feed must use `fullSellAmount`/`fullBuyAmount`, `sellTokenSource`/`buyTokenDestination`, and fetch `feeAmount` from the orderbook; 821 orders in this sample differ between the two representations. Worth a sentence in the docs for solver and SDK authors.
