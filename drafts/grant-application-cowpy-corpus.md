# Grant Application - Shared services-generated conformance corpus for cow-py and cow-rs

(Post in https://forum.cow.fi/c/cow-grants-program/10 as a new topic, only after a maintainer has replied on PR #86, the #63 thread or the forum post. Fill the two FILL fields. Use the current template; keep the T&C line and the note to the committee.)

## Grant Title

Grant Application - Shared services-generated conformance corpus for cow-py and cow-rs

## Author(s)

Ashwin Goyal, forum @[FILL], GitHub let-the-dreamers-rise

## Experiences and qualifications

- cowdao-grants/cow-py PR #86: found that cow-py signs ETHSIGN orders over the unprefixed EIP-712 digest (0/19 services vectors; 11 live ETHSIGN orders in the current auction), fixed it, added the v1 and v2 conformance tests.
- Extended cow-rs `tools/conformance-gen` (PR #63 branch) with a v2 fixture from the same services pin: all ten orderbook chains, partially fillable orders, both cancellation types, app-data hash/CID/validation. v1 regenerates byte-identical.
- Verified the fixed cow-py against 11,653 open orders across the ten chains: UID and ECDSA owner recovery match on every order.
- Elsewhere: merged PR to bitcoin/bips (BIP-360 reference implementation, two consensus-relevant bugs found by differential testing against the spec).

## Grant Description

cow-rs (grant approved 8 Oct 2026) and cow-py (completed 2025) now have fixtures generated from `cowprotocol/services`, but nothing keeps them current: the pin is a constant in one Rust file, cow-rs has no consumer test yet (M2 of PR #63), cow-py cannot sign the single-order cancellation type the orderbook accepts, and the solver-feed DTO that integrators rebuild orders from is undocumented. This grant finishes the loop so that a services change that alters hashing, signing, UIDs, cancellations or app-data handling fails a test in both SDKs within one regeneration, and so that both SDKs cover the full signing surface the orderbook exposes.

Everything lands as pull requests into cowdao-grants repositories, so completion does not depend on any third party. Reviewer suggested: @mfw78 (as on PR #63), with @bleu for cow-py.

## Type of Grant

Milestone-based.

## Milestones

| Milestone | Title | Due date | Funding request |
|---|---|---|---|
| 1 | Pin-bump workflow and v2 consumer in cow-rs | 3 weeks after approval | $1,200 |
| 2 | Single-order cancellation type and v2 coverage in cow-py | 5 weeks after approval | $1,000 |
| 3 | Solver-feed DTO note in docs and corpus handover | 6 weeks after approval | $800 |

### Specifics

**Milestone 1 ($1,200).** In cow-rs: a `just conformance-regen SERVICES_SHA` recipe that updates the pin in `Cargo.toml` and `main.rs`, regenerates v1 and v2, and fails if the fixtures changed without the pin changing; a CI job that runs the generator at the pinned sha and diffs against the committed fixtures; a `cowprotocol-signing` integration test consuming v2 (chains, partial fills, both cancellation types, app-data) alongside the v1 consumer from PR #63 M2. Deliverable: merged PRs to cowdao-grants/cow-rs, or PRs open with reviewer sign-off if merge is blocked on #63.

**Milestone 2 ($1,000).** In cow-py: `hash_order_cancellation` / `sign_order_cancellation` produce the `OrderCancellation(bytes orderUid)` type and the existing batch functions keep the batch type; `OrderBookApi.delete_order` gains the single-order endpoint; the strict xfail in `test_conformance_vectors_v2.py` becomes a passing test; a CI check fails if `services_sha` differs between the two fixture files. Deliverable: merged PR to cowdao-grants/cow-py.

**Milestone 3 ($800).** In cowprotocol/docs: a short page or section for solver and SDK authors on rebuilding a signed order from the auction DTO (`fullSellAmount`/`fullBuyAmount`, `sellTokenSource`/`buyTokenDestination`, signed fee only on the orderbook record), with the live-check script linked. Handover: a one-page RUNBOOK in cow-rs on bumping the pin, plus a forum post summarising the corpus. Deliverable: docs PR open with maintainer response, runbook merged, forum post.

## Length

6 weeks.

## Funding Request

$3,000 in DAI on Ethereum mainnet, paid per milestone after reviewer approval. No COW requested. If the committee prefers a smaller scope, Milestone 1 alone is $1,200.

## Ethereum mainnet address (to receive the grant)

[FILL]

## Other Information

- Everything that led here is public: cowdao-grants/cow-py#86 and the branch https://github.com/let-the-dreamers-rise/cow-rs/tree/feat/conformance-v2. Harnesses and results: https://github.com/let-the-dreamers-rise/cow (research/08, research/09).
- No prior compensation from CoW DAO or anyone else for this work. No conflicts.

## Terms and Conditions

By submitting this grant application, I acknowledge and agree to be bound by the CoW DAO Participation Agreement and the CoW DAO Grant Agreement Terms.

## Note to committee

Please notify the Grantee of their reviewer and their steward in the thread and latest upon successful approval of the Grant on Snapshot.
