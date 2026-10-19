# CoW DAO Grants: the live 2026 competition (33 threads, read 2026-10-19)

Source: the full forum threads (fetched 2026-10-19 via the Discourse JSON API) plus `forum.cow.fi/u/<name>.json` for 26 accounts. Digests truncate very long posts mid-sentence, so where a first post is cut off (3383, 3640, 3642, 3643) I say so rather than guess. The forum's anonymous profile JSON does not expose `post_count`; for hidden (TL0) accounts only the numeric user id is visible, so account age for those is interpolated from neighbouring ids with known `created_at`.

Two housekeeping flags before the per-thread table:

- **Tag mislabels.** `grants-root-3434` (Quantir) and `grants-root-3330` (ethcontract-rs) carry the `grant-funded` tag in the digest header, but both were rejected in-thread (Sov, 2026-04-27; mfw78, 2026-01-07). Treat the tag as noise.
- **Committee cast.** Sov (steward/process; signs nearly every rejection), mfw78 (technical reviewer; `cowgrantscommittee` group, account since 2022-03-10), Chim9 (payments). Core devs who spoke in this batch: anxolin (3346), harisang and felixhenneke (3476). No posts from Master_CoW, fleupold, shoom3301, alfetopito, m-lord-renkse or sunce86 in any of these 33 threads.

---

## Part 1. Thread-by-thread

### 3346 — Programmatic Orders API (bleu) — 2026-01-27 — CLOSED OUT, PAID
- **Author:** @bleu (bleu.builders). Account 2023-08-24, TL2, 18 badges, ~50h read time. ~2y5m old at posting. "10+ grants for CoW Protocol."
- **Proposal:** Ponder-based indexer + GraphQL API for all Composable CoW order types (TWAP, stop-loss, perpetual, GAT, TAT), flash-loan helper-contract ownership, CoWShed→EOA mapping, orderbook sync.
- **Amount:** originally larger; revised 2026-02-04 to 27k xDAI / 9 weeks, then 24k xDAI after anxolin's pushback on M3, plus 40k COW vested 12 months for maintenance.
- **Milestones:** M1 Composable CoW tracking 6k; M2 flash-loan + CoWShed 4.5k; M3 orderbook integration 9k (cut from 12k); M4 review/docs 4.5k.
- **Evidence:** links to prior deliverables (composable-cow-api PoC on Railway), public repo `cow-programmatic-orders-api`, live playground at cow-programmatic-order.bleu.blue.
- **RFP or proactive:** proactive, but framed around core-team need (CoW Swap frontend integration).
- **Committee/core replies (verbatim):**
  - anxolin 2026-02-18: "I believe this initiative is very valuable and I would vouch for it. I just think the (3.) Orderbook integration, if I understand properly, should not be that complicated. 4 weeks might be too much buffer." (then a Solidity snippet showing the ERC1271Forwarder decode path, and a question about skipped TWAP parts)
  - anxolin 2026-02-20: "Sounds great! Thanks for clarifying. It looks like a good proposal" / "Given I'm familiar with this, I volunteer to help with the reviewing process for milestone payments"
  - Sov 2026-02-20: "Thanks @anxolin I'll flag my support for this as well. @bleu I think you should take this to snapshot but let's wait until early next week since we are heading into the weekend."
  - Sov 2026-02-27: "Thanks and congratulations. As always, just keep us updated on your progress."
  - anxolin 2026-06-01: "M1 + M2: fully done. Recommend releasing the payments. M3: code is complete and the scope items are present, but it doesn't fully work yet (TWAP part tracking misses some real fills, Gnosis flash-loan tracking is unwired). I'd suggest either 50% now, or 100% conditional on those fixes landing before M4 closes"
  - Chim9 2026-06-09: "we have executed the payments for Milestone 1, Milestone 2, and the first half of Milestone 3."
  - anxolin 2026-09-22: "The indexer will be used soon in a new feature, therefore has been adapted to be prod-ready. I see most of the concerns have been addressed, and therefore I consider all milestones complete."
  - Sov 2026-10-02: "With all milestones now signed off, the committee is closing this grant out."
  - Chim9 2026-10-07: "the 40.000 COW vesting payment for maintenance has just been processed and the 1-year vesting just started."
- **Applicant response quality:** high. Took the M3 duration cut without argument, posted a status table every 2–4 weeks, absorbed a 50% holdback on M3 without complaint, fixed what the reviewer flagged.
- **Status:** approved, delivered, closed 2026-10-02.
- **Assessment:** Textbook win: core dev wanted the thing, volunteered as reviewer, applicant cut scope on request. Nothing AI-looking; committee did not raise it.

### 3374 — Railgun–CoW SDK (Gnosis Guild / auryn) — 2026-02-18 — DEAD; LANE RE-OPENED BY A THIRD PARTY
- **Author:** @auryn. Account 2023-08-07, TL1. ~2.5y old at posting.
- **Proposal:** LGPL SDK wrapping CoW SDK with Railgun-shielded balance flows; Zodiac integration as validation (unfunded).
- **Amount:** 50,000 xDAI, one milestone, half up front.
- **Evidence:** Zodiac PoC of Railgun→CoWSwap claimed, no link.
- **RFP or proactive:** proactive.
- **Committee replies:**
  - mfw78 2026-02-24: "IMO the SDK and any contracts should be ERC-7579 based rather than tied to the Zodiac/Safe stack. The deliverable needs to be genuinely composable, with standalone end-to-end examples that work independently of any closed-source app." / "The fixed milestone grant should cover the open-source SDK and end-to-end examples, that's the deliverable. For downstream integrations that actually drive volume (Railway, Zodiac, or otherwise), we incentivise those through volume-based rewards." / "for production integrations we'd want to see Railway rather than just Zodiac. Zodiac alone is unlikely to move the needle on volume."
  - mfw78 2026-02-26: "We do not hold up grant completion contingent on merging into externally controlled repositories."
  - Sov 2026-03-06: "what moves the needle for us here is native Railgun integration, not just a Zodiac module sitting on top. If private order flow anywhere near the scale that 0x is reportedly routing through Railgun can be directed to CoW instead, that's meaningful. Let us know if that can be reflected in a revised proposal."
  - Sov 2026-09-09 (to @mtvl, Vacuumlabs, hidden TL0 account created ~2026-09-01): "From the committee's side, we don't have an active grant for this. If you want to take it on, it would need to be a fresh proposal rather than a continuation of this one. Our perspective is that a Railgun integration is worth having, but on its own it doesn't justify funding. The value to the DAO is trading volume settled through CoW Protocol, and that is what we would measure: volume attributable to the integration once it is live."
- **Applicant response:** auryn engaged once, then 2026-05-14: "the Zodiac team ended up deciding to deprioritize this work."
- **Status:** withdrawn. Vacuumlabs asked about taking it over 2026-09-03; no proposal since.
- **Assessment:** A 50k ask with an up-front half from a Gnosis-adjacent team still got pushed to "show volume". The committee wants native Railgun/Railway, paid by volume, not an SDK.

### 3383 — Safe EIP-1271 Watch Tower (bleu) — 2026-03-04 — NO VISIBLE COMMITTEE RESPONSE
- **Author:** @bleu (as above).
- **Proposal:** off-chain service that watches Safe message confirmations via Safe Events webhooks, aggregates owner signatures into an EIP-1271 signature at threshold, posts order/cancellation to the orderbook. Modular for other 1271 wallets.
- **Amount/milestones:** not visible — digest cuts off in the architecture section.
- **Evidence:** PoC repo `cow-safe-messages-watch-tower` + demo video.
- **RFP or proactive:** proactive.
- **Committee replies:** none in the digest.
- **Status:** stalled/unanswered (7.5 months).
- **Assessment:** Even bleu's PoC-backed proposals die silently when no core dev claims the need. Not AI-looking.

### 3394 — Aegis SDK (mani67) — 2026-03-13 — REJECTED SAME DAY
- **Author:** @mani67. Hidden TL0 profile; id 1793 sits between accounts created 2025-11-27 and 2026-05-15, so created early 2026, likely days before posting.
- **Proposal:** React "SafeSwapUI" + TWAP executor wrapper, pegged to the 2026-03-12 $50.4M USDT→AAVE slippage incident.
- **Amount:** $22,000 (8k UI, 10k TWAP executor, 4k docs).
- **Evidence:** GitHub Mani678/aegis-sdk.
- **Committee replies:**
  - mfw78 2026-03-13: "Research on CoW related properties will show you that: CoW Swap already has this functionality. Infrastructure for TWAP already exists on-chain as noted by this grant application. I'm closing this application as it is not relevant, and seeks to misconstrue recent events."
- **Status:** rejected and closed.
- **Assessment:** Incident-chasing with a product that duplicates CoW Swap's own warnings. Text reads as an AI-drafted pitch deck ("built yesterday", dollar breakdown table); committee did not comment on AI, only on relevance.

### 3402 — CoW Skills (bleu) — 2026-03-24 — REJECTED
- **Proposal:** SKILL.md bundle for Claude Code/Cursor plus an MCP server (get_quote, post_order, cancel) and an eval suite. Amount not visible (digest truncates the eval section).
- **Committee replies:**
  - Sov 2026-04-13: "the committee has decided not to move forward with this as a standalone grant. To be clear, we think the skills themselves are useful and we'd encourage you to open source them for the community. We just don't think a separate funding track is the right approach here."
  - Sov 2026-04-14: "I think, for now, we'd like to see the current grants completed and closed out then we can look at potential follow on opportunities after that. Overall, I don't think skills like this would be something we would fund unless it was clear we'd see enough adoption to justify."
- **Applicant response:** bleu correctly pointed out the skills don't exist yet so there's nothing to open-source; offered alternative structures. Polite, no traction.
- **Third party:** @krzysu 2026-04-30 posted an independent MIT `cow-mcp` server.
- **Status:** rejected.
- **Assessment:** Adoption-gated. Also note the committee's explicit "finish what you have first" to its most-funded incumbent.

### 3406 — Community-built Rust SDK (authored by mfw78) — 2026-04-02 — PHASE 1 PAID TO BLEU
- **Author:** @mfw78 (committee). Recused from voting.
- **Proposal:** cow-py-style collective grant; contributors PR into `cowdao-grants/cow-rs`; committee splits 8,500 xDAI by assessed contribution; supersedes a cancelled Nov-2025 Rust SDK grant.
- **Committee replies:**
  - mfw78 (top post): "Warning: Submitting AI slop PRs will result in your submission being immediately closed."
  - mfw78 2026-04-10 (to CoBuilders, who submitted PR #1 scaffold and a milestone plan): "Unlike the previous Rust SDK grant, we will not entertain the grant allocation going to a single entity, there's a lot of initial scaffolding and we'd rather see things unfold organically"
  - mfw78 2026-04-11 (to @0xSymbiotic's branch): "it is evident from the submission that this is not implemented with Rust idiomacy, and therefore the submission will NOT be accepted. ... DO NOT SUBMIT CODE PULLS HERE. ... AI SLOP WILL NOT BE TOLERATED AND YOUR SUBMISSION WILL BE IMMEDIATELY CLOSED AS AI SPAM. IT IS AN EXPECTATION THAT THE SDK BE PRODUCED IN A MAINTAINABLE MANNER."
  - mfw78 2026-06-30 (after bleu's PR #5 and #38): "Great work. I can confirm that the current state of cow-rs is at feature parity to the JS SDK ... I suggest now that the Grants Committee consider this grant as met for Phase 1 and pay out. @bleu: Can you please kindly advise your payment address on mainnet?"
- **Status:** Phase 1 complete 2026-06-30; Phase 2 (maintenance, 1 year) ongoing. The crate is published as `cowprotocol` (alpha).
- **Assessment:** The only thread where the committee explicitly polices AI output, and it did so in capitals. The "collective" grant ended up as a single-entity payout to bleu anyway. CoBuilders (TL2, Nov-2025 account) and 0xSymbiotic both lost on this.

### 3456 — cow-intent-guard (ILE_LABS) — 2026-05-16 — REJECTED
- **Author:** @ILE_LABS. Created 2026-05-15, posted 2026-05-16 (one day old). TL1, 464 profile views, ~34 min read time. Four threads in this batch (3456, 3464, 3559, 3575).
- **Proposal:** Rust CLI/SDK: offline EIP-712 + ComposableCoW decoder, Anvil fork simulation, phishing "risk tiers", WASM build. Hooked to the April 2026 cow.fi DNS hijack.
- **Amount:** $28,500 / 3 months (9.5k, 10k, 9k).
- **Evidence:** none linked; "proven track record ... (Solana, MultiversX, Arbitrum)" with no URLs; "Our previous work includes:" followed by nothing.
- **Replies:**
  - @kernelwhisperer 2026-05-20 (community): "I disagree with the approach of creating another sdk in Rust, while we already have one in Typescript ... Who will maintain it?"
  - Sov 2026-05-20: "Thanks @ILE_LABS for the writeup and for engaging with the recent cow.fi incident. We've discussed internally and won't be moving forward with this one."
- **Status:** rejected.
- **Assessment:** Strongly AI-shaped (a "Project Pulse & Tracking" table, "Local Trusted Frontier", a generic "dedicated sub-team of 3 developers" answer). Committee didn't say so; it just declined in two sentences.

### 3464 — Integration Quickstarts & Precision Parameter Reference (ILE_LABS) — 2026-06-08 — REJECTED
- **Proposal:** TS + Rust 10-minute quickstarts, parameter tables, error-code lookup, GitHub Pages payload calculator. "Track B (Targeted Long-Form)". $12,000 in COW over 6 weeks, 2 milestones.
- **Evidence:** names four team members with GitHub/LinkedIn placeholders; cites "lightning-payjoin-kit".
- **Reply:** Sov 2026-06-10: "We've decided (for now) to keep integration documentation as a core-team-owned function rather than scoping it to external contributors via the grants council. We've closed that workstream and aren't taking on proposals against it right now, so we won't be moving this one forward."
- **Status:** rejected.
- **Assessment:** Docs are closed to outsiders; this was announced here and nobody who applied afterwards seems to have read it.

### 3467 — Polytope pre-flight SMT verification (VedantaHazra) — 2026-06-10 — REJECTED SAME DAY
- **Author:** @VedantaHazra. Hidden TL0; id 1838 falls between 2026-05-15 and 2026-06-13 creations, so ≤3 weeks old at posting. Fresh IIT Kharagpur graduate, hackathon wins.
- **Proposal:** Go module transpiling GPv2 settlement payloads to Z3 SMT-LIB to reject infeasible batches pre-simulation. 12,000 xDAI over 5 milestones / 12 weeks. Claims a PoC at <40 ms; no link.
- **Reply:** Sov 2026-06-10: "thanks for the application and for building a PoC before applying. The council is declining this proposal as we'd need to see solver express interest in something like this before exploring further. If a solver team confirms they'd integrate this, we're open to revisiting."
- **Status:** rejected, reopenable with a solver sponsor.
- **Assessment:** First explicit statement of the "a solver must ask for it" rule that later kills 3566 and shapes 3612/3619. Prose is polished-academic; not obviously AI.

### 3476 — BYOS, Bring Your Own Solver (bleu) — 2026-06-26 — FUNDED, M1 SIGNED OFF, M2 "LOOKS GOOD"
- **Proposal:** full BYOS RFP: bonded solver engine, per-sub-solver Trampoline, immutable Escrow, EIP-712-gated Proposal API, audit, gnosis+mainnet deploy. Amount not visible in digest (truncated). Responds to the **BYOS RFP** explicitly.
- **Evidence:** PoC crates, then public repos `bleu/byos-contracts`, `bleu/byos-service`, later `byos-service-ts`; staging instance on BNB with 2 internal sub-solvers; a settled order from a Fynd sub-solver.
- **Replies:**
  - felixhenneke 2026-08-20: "I had a look at the progress of the project and discussed several design decision with the @bleu team. They have adapted the design accordingly and I am quite satisfied with the progress. I am confident that @harisang, the official reviewer from the core team, will be able to sign off on the first milestone next week."
  - Sov 2026-08-20: "Great thanks for the update @felixhenneke and thanks to the @bleu team for the work thus far."
  - harisang 2026-08-31: "due to various reasons, review on my end was very slow (apologies for this), but I should be able to be done with it in the next 2-3 days."
  - harisang 2026-10-08: "Just wanted to post a quick update that things look good for M2! Thanks to the @bleu team for all their work and proactivity!"
- **Other activity:** an auditor (@Arctekaudits) cold-pitched in-thread; an external sub-solver (@ghislain.ott) found the staging auction feed empty and production access still undecided; bleu pointed them to kaisersolver's cow-backtester (which 3624 later cites as validation).
- **Status:** active, M2 under review. Service rewritten Rust→TypeScript mid-grant without objection.
- **Assessment:** The flagship. Core-team reviewer assigned, RFP-aligned, incumbent team. Review latency (harisang) is the only friction.

### 3546 — "Exploring a Rust Solver Correctness & Verification Grant" (satya_98402) — 2026-08-27 — EXPLORATORY, SPAWNED 3569
- **Author:** @satya_98402 (Satyawan Singh, GitHub ss1738). Created 2026-08-27, posted the same day. TL1, 12 badges, ~6h read time.
- **Proposal:** none yet; asks maintainers what correctness problem is worth solving.
- **Committee replies:**
  - mfw78 2026-09-01: "I'd refer you to GitHub - cowdao-grants/cow-rs and GitHub - cowprotocol/services. Essentially the services is the 'source of truth', and cow-rs would be tested against properties / invariants etc derived from services. This would be the path that I would recommend in order to arrive at a grant that is soundly scoped (and useful)."
  - mfw78 2026-09-06: "Apologies, I've corrected it inline above, in that the cow-rs properties / teseting would be done against services, as that is ultimately where the data goes."
  - mfw78 2026-09-13: "As mentioned, I'd like to see a concrete proposal. I think the feedback that has been provided is appropriate, albeit minimalist guidance."
- **Community:** @kaisersolver (production solver) supplied cow-certify fixtures, a CIP-87 penalty-cap replay (256 vectors), and iterated three releases (0.5.0→0.5.2) in four days in response to satya's verification. Satya built a Rust test in services that passes all 256 vectors and reported a CIP-87 text-vs-code discrepancy (cap basis is raw signed amounts, not the fee-adjusted "quote").
- **Status:** converted into 3569.
- **Assessment:** The model path: ask first, follow the one pointer given, do unpaid verification work in public, then propose narrowly. Note satya openly corrected his own earlier statements twice. Prose is formal but evidently human (self-corrections, specific line numbers).

### 3559 — BCoW factory/helper status (ILE_LABS) — 2026-09-08 — MOOT
- **Proposal:** question about a read-only config-drift conformance PoC for CoW AMM factory/helper mapping.
- **Reply:** mfw78 2026-09-15: "As far as I'm aware, cowamm has been deprecated (refer to now mention anymore on cow.fi domains). Therefore any new work regarding this is somewhat moot / irrelevant."
- **Assessment:** Applicant researched a deprecated product. Signals ILE Labs is scanning old repo threads for openings rather than following current roadmap.

### 3565 — Execution Evidence Lab / Settlement Decoder (Decentralised News) — 2026-09-10 — REJECTED
- **Author:** @decentralised. Hidden TL0; id 1948 → created ~early Sept 2026, days before posting.
- **Proposal:** plain-language settlement decoder web tool, 100-order dataset, 4 articles, 3 long videos, 8 shorts. Amount not visible (truncated).
- **Evidence:** links to their own CoW comparison articles. The "Experience and Qualifications" block is pasted twice verbatim.
- **Reply:** Sov 2026-09-18: "We've reviewed this internally and won't be moving forward. CoW Explorer already covers most of what the decoder would surface, so we don't see enough added value to fund a second interface over the same data. Your CoW coverage is good, and we'd encourage you to keep it up."
- **Status:** rejected.
- **Assessment:** Media outlet asking the DAO to fund its content calendar. Duplicate section is a copy-paste/LLM tell; not commented on.

### 3566 — Structural (TDA) MEV detection (SimplexTDA) — 2026-09-10 — REJECTED
- **Author:** @SimplexTDA (Uri Yacobi Keller). Created 2026-08-31, posted 10 days later. TL1.
- **Proposal:** extend Flashbots Pre-FRP TDA sandwich research to CoW auction/solver data; 3 milestones, amount not visible.
- **Evidence:** open-source Ethereum TDA repo with 0.943 ROC-AUC; a 3,824-settlement CoW pilot with 2 confirmed sandwiches.
- **Replies:**
  - mfw78 2026-09-15: "Just wondering what @harisang / @solver_cow may have to say about this research and if it seems tangibly useful / non-duplicative."
  - Sov 2026-10-02: "The committee asked for a view from the solver side on whether this research would be useful and non-duplicative, and that interest hasn't materialised, so we won't be moving forward with funding it."
- **Status:** rejected after 3 weeks of silence from core.
- **Assessment:** Serious, evidenced research killed by the "solver side must want it" filter. The applicant never pinged the named core devs directly. Human-written (self-deprecating formatting correction).

### 3569 — Signed-Order / EIP-712 / UID Conformance Corpus for cow-rs (satya_98402) — 2026-09-13 — APPROVED 2026-10-08, M1 PR SUBMITTED
- **Proposal:** services-generated fixture corpus consumed by a cow-rs integration test. Initially $5,500 (M1 $3,000 services-side generator; M2 $2,500 cow-rs consumer). Revised to generator living in cow-rs with services pinned as a git dependency. Final: **$2,000 DAI** (2 × $1,000).
- **Evidence:** ss1738/cargo-vouch; a 57-case prototype; a compiling standalone crate pinned to services rev cfa13b03.
- **Committee replies:**
  - mfw78 2026-09-15: "Structurally, why is the normalised v an issue as cow-rs / services is currently written? The corpus would be beneficial ... Having said this, I think the scope of this is somewhat small, and mixing it in with things like deduplication of aspects of cow-rs is blurring the lines of what the grant should be seeking to do. Additionally, as you are referencing multiple repositories (services / cow-rs), I think you should be a little more specific about what happens where, as maintainer upstreaming into services makes the grant contingent on an externality which may not be achievable and leave the state in deadlock. Generally, I'm in favour of the corpus, but would like to see the scope more coherent and narrow (and demonstrate understanding of the code bases, and their dependencies)."
  - Sov 2026-09-23: "thanks for working through mfw's points in your last post. When you're ready, could you append the proposal here with the updated milestones and funding request?"
  - mfw78 2026-09-29: "I think the corpus is relatively well established, but I think that we are relatively some distance apart on what the value / pricing would be for this grant. Effectively, I don't see how this would be more than a day or two of dedicated, effective time in order to achieve the outcome of this grant, and therefore the current quoted costs are too high."
  - mfw78 2026-09-29 (after the cut to $2,000): "I'm happy to signal my support at this level, please kindly submit it to snapshot. Please make sure that the snapshot isn't started / run over the weekend (Sat/Sun), and ensure that the template used is the latest. Kindly note as well that the payment address would be an ethereum mainnet address, and not gnosis chain as we migrated the treasury a while ago."
  - Sov 2026-10-02: "For the record, @Sov will be steward and @mfw78 the reviewer for this grant."
  - Sov 2026-10-09 (onboarding): "congratulations, your grant proposal has been approved by the CoW Grants Council via Snapshot. ... Amount: $2,000 in DAI, two milestones of $1,000 ... When you complete a milestone, post in this thread with a link to the pull request and tag @Sov and @mfw78. Your Reviewer responds within 7-14 days. Approved milestones enter the next end-of-month payout cycle, with funds arriving by the 15th of the following month."
  - Sov 2026-10-12: "Thanks @satya_98402, received. @mfw78 will review the PR and follow up here."
- **Applicant response quality:** exemplary. Conceded the v-normalisation point ("I overstated 0/1 coverage as a gap"), removed the cross-repo dependency, cut price 64% within hours, corrected his own Snapshot-threshold mistake, shipped M1 (cow-rs PR #63) one day after onboarding.
- **Status:** approved; M1 awaiting mfw78 review (7–14 day SLA, due by ~Oct 24).
- **Assessment:** The only new-account applicant to get funded in this entire batch, and it took a 6-week courtship for $2k. That is the price of entry now.

### 3575 — Isolated parallel E2E testing (ILE_LABS) — 2026-09-17 — DECLINED
- **Proposal:** asks whether services issue #4894 is open to external contributors and whether a benchmark would help.
- **Reply:** Sov 2026-09-18: "Those questions are for the service maintainers; best asked on the issue itself. We wouldn't fund this, and if it lands as help wanted the repo's own reward program covers it."
- **Assessment:** The committee is redirecting issue-sized work to the repo bounty program, not grants.

### 3588 — Chinese Research & Education Kit (daotrading-zh) — 2026-09-27 — DISCOURAGED
- **Author:** @daotrading-zh ("DAO Trading Research"). Hidden TL0; id 2010 → created ~Sept 24–27, days before posting. Self-described "newly formed".
- **Proposal:** CC0 Chinese research report, 10 infographics, 3 video scripts, 200-term EN→ZH glossary. $8–12k over 8 weeks. Positioned as additive to the UI Translation RFP.
- **Reply:** Sov 2026-09-29: "Long-form educational content isn't something the committee is prioritising for funding right now, so we wouldn't encourage a formal application. If you do publish Chinese-language material on CoW independently, feel free to share it here on the forum."
- **Status:** withdrawn gracefully ("We'll proceed with publishing Chinese-language material independently").
- **Assessment:** Well-pitched RFC, wrong category. Note the applicant quotes a committee "sourcing challenge — the same few teams reply to every RFP" from outside this batch.

### 3603 — Token-2022 warnings + Squads proposal helper RFC (naina) — 2026-10-01 — DECLINED
- **Author:** @naina. Hidden TL0; id 2031 → created ~Sept 28–Oct 1, i.e. hours to days before posting. Four threads in 16 days (3603, 3606, 3609, 3638).
- **Proposal:** TS package beside `@cowprotocol/sdk-trading-solana` for Squads multisig wrapping and Token-2022 preflight warnings. No funding requested yet.
- **Reply:** Sov 2026-10-02: "Most of the questions here are already covered in the existing docs: Squads / multisig: the sdk-trading-solana README covers using buildOrder ... Token-2022: the solana-programs DESIGN.md explains how Token-2022 and its extensions are handled ... Since the Solana SDK is still marked experimental, the committee isn't looking to fund wrapper tooling around it at this stage."
- **Assessment:** RTFM rejection.

### 3606 — "[Scope Check] Current CoW grant priorities" (naina) — 2026-10-02 — ANSWERED, NO LANE OFFERED
- **Proposal:** asks which 1–2 areas need external discovery, whether unsolicited apps are welcome, whether the Volume RFP is open.
- **Reply:** Sov 2026-10-02: "The Volume-Based Integration RFP closed to applications on 30 September 2025 (RFP: Volume-Based Integration), and the committee isn't publishing new problem areas or RFPs right now, so there isn't a specific area we can point you to. CIP-82 and the application template remain the public reference for anything submitted, but we wouldn't recommend investing in a research sprint in the expectation of a grant."
- **Assessment:** The single most important committee statement in the batch for a prospective applicant: no RFPs, no named gaps, don't expect a grant.

### 3608 — 33Jane permissioned RWA execution layer (Mateo / Mushee) — 2026-10-05 — REJECTED
- **Author:** @Mateo. Created 2026-10-05, posted same day. TL1. Ex-BitMart/Bitget.
- **Proposal:** eligibility-aware routing (OpenEden KYC manager, issuer pause state, min/max) returning only executable routes to CoW. 20,000 xDAI (8k/6k/6k), MVP self-funded at 0.
- **Evidence:** GitHub mushee-io/33jane, live console, OpenAPI docs.
- **Reply:** Sov 2026-10-09: "thanks for putting this together and for building a working demo before applying. After reviewing it, the committee has decided not to move forward with this application. CoW already handles tokenized RWAs through its existing token lists, and a separate issuer-eligibility layer is not something this program is looking to fund."
- **Status:** rejected; applicant thanked them.
- **Assessment:** Built-first, decent demo, zero demand signal from CoW side. Writing is choppy short-line LLM style; not commented on.

### 3609 — Contributor Introduction (naina) — 2026-10-05 — UNANSWERED
- Asks for "a Maintainer-Selected CoW Protocol Task". No reply in 14 days.

### 3612 — Solver Score Conformance Test Set (ZeroNine) — 2026-10-05 — STALLED / EFFECTIVELY DECLINED BY mfw78
- **Author:** @ZeroNine (GitHub C-09-07, runs a shadow-competition solver on Plasma). Created 2026-09-23, posted 12 days later. TL1, 9 badges, ~3h read time.
- **Proposal:** published fee+score vector set generated/checked by services at a pinned commit so any solver can test its model. 12,000 USDC / 7 weeks. Cites services PRs #3978, #4669, #5010, #2857, #3340 and exact file:line references. Explicitly scoped off mfw78's "source of truth" guidance in 3546.
- **Evidence:** ZeroNineSolver/cow-score-test-set (10 vectors + CI against winner-selection), a 57-trade Plasma fee-policy audit, a merged PR to KaiserSolver/cow-backtester.
- **Committee replies:**
  - Sov 2026-10-09: "Before we take this further, the main thing we'd like to understand is who would use it. The pull requests you cite show the fee and score arithmetic has diverged before, but we haven't seen a services maintainer or a solver team say that a published vector set is something they would run. Has anyone told you they would? You mention KaiserSolver. If @kaisersolver plans to use it, a note here would help. On scope: the source map, schema, and first 10 vectors are already public. Could you say which parts of Milestone 1 are new work? Two small template items while you're here: the terms section needs the links to the Participation Agreement and the Grant Agreement Terms, and the note to the committee is missing."
  - kaisersolver 2026-10-10: "confirming: yes, we plan to use it. KaiserSolver would run the vectors in cow-certify's CI ... and in our own engine's tests"
  - mfw78 2026-10-13: "For something that is integral to the solver competition, such as solver score conformance tests, having golden vectors written by the core team is significantly more appropriate than having 3rd party assembled work - for example, new solvers may come to rely on something that may indeed contain errors or omissions, and cause consternation later should solvers follow the 3rd party tooling. Solvers are incentivised by CoW Protocol, and any work that is done that addresses actions taken within the solver competition requires very careful consideration from the core team / solver team to ensure appropriate competition dynamics. I remain severely hesitant to enact any grant, retrospective or otherwise, that may influence the solver competition without this being thoroughly vetted and understood by the core / solver team (if not actually requested specifically by them)."
- **Applicant response:** long, careful; offered to move repo under cowdao-grants, let core approve the case grid, make core definitions authoritative. Deleted and re-posted one reply.
- **Status:** awaiting; realistically dead unless the solver team requests it.
- **Assessment:** Did everything 3546/3569 taught (source of truth, public prototype, a solver endorsement) and still hit a new wall: anything touching competition economics must originate from core. mfw78's reply is verbatim identical to his 3620 reply the same day.

### 3619 — Fiberscope solver analytics (Fibrous / kermo) — 2026-10-12 — AWAITING, ONE SOLVER ENDORSEMENT
- **Author:** @kermo. Hidden TL0; id 2044 is the next id after Mateo (created 2026-10-05), so ≤1 week old. Fibrous: DEX aggregator, active CoW solver on Base since July 2026 and on BNB.
- **Proposal:** extend the live Base dashboard (fiberscope.org, MIT) to 9 more chains, per-solution scores/quote winners/fees, public JSON API. 14,000 USDC across 3 milestones (~5 weeks) + 15,000 COW vesting for 12 months maintenance. Conflict of interest disclosed.
- **Evidence:** live site, repo, validation vs Dune/Solver Info to ~0.1%, 24,534/24,534 batches credited correctly. Motivated by Dune's Sept-2026 move to paid-only query refresh.
- **Replies:**
  - Sov 2026-10-12: "Before this goes further: who would use Fiberscope and the API beyond Fibrous? Since Fibrous also competes in these auctions, it would help to hear from another solver team or someone on the core team who relies on the entry and win-rate figures."
  - @gabari (Nexroute, solver on Base/BNB; TL2, account June 2026) 2026-10-13: "yes, we'd use this. We've been rebuilding bits of it by hand on our side. Nice work, the methodology page is solid." plus feature requests; "Would also be very nice to have BNBChain".
- **Status:** awaiting committee after endorsement.
- **Assessment:** Best-positioned pending application: live product, independent solver endorsement within 24h, modest ask. Risk: mfw78's "competition dynamics" doctrine may extend to analytics run by a competitor.

### 3620 — CIP-88 Quote Reward Analysis (apsarthsumit) — 2026-10-12 — WITHDRAWN
- **Author:** @apsarthsumit. Hidden TL0; id 2062 → created ~Oct 6–12. Discloses: "I used an AI coding assistant to write the first version of the analysis code for this proposal."
- **Proposal:** exact CIP-88 pipeline, reconciliation vs the CIP thread's simulation, sensitivity analysis, refresh script. 3,500 xDAI / 65 h / 5 weeks.
- **Evidence:** a pipeline reproducing best-quote share within 4 points per chain; a prior repo that "has not yet passed its live test, and I say so in the README".
- **Reply:** mfw78 2026-10-13: "Please note however, we won't proceed with this. For something that is integral to the solver competition, such as the quote reward dynamics, having golden vectors written by the core team is significantly more appropriate than having 3rd party assembled work ..." (remainder identical to the 3612 reply).
- **Applicant:** withdrew the same day and took the repo private "so nothing here will be mistaken for official tooling."
- **Assessment:** Honest, cheap, and dead on the competition-dynamics rule. Only applicant to disclose AI use; the committee didn't react to the disclosure, only to the topic.

### 3624 — Solver Readiness Spec v1 + Single-Order Replay (kaisersolver / Fiftysix LLC) — 2026-10-13 — AWAITING (6 days, no reply)
- **Author:** @kaisersolver (Kaiser). Created 2026-08-07, TL2, 9 badges, ~5.5h read time; KYC'd bonding-pool solver live on Arbitrum, Base, BNB since May 2026. Most cross-thread-active applicant (3546, 3612, 3624; cited in 3476).
- **Proposal:** v1 spec + one-command readiness check (cow-backtester 1.0), single-order replay for BYOS-style engines, shareable report. 6,000 USD / 15 working days / 6 weeks; optional Solana item capped at 3,200 USD gated on CoW publishing Solana auction data.
- **Evidence:** cow-backtester and cow-certify on PyPI; public readiness runs over 9,098 auctions; merged docs PR #652; data contributions to CIP-87 and solver-rewards #507; another solver already ran it on Plasma and contributed a fix; bleu pointed a BYOS sub-solver to it (3476 #17).
- **Committee replies:** none yet.
- **Assessment:** Pre-answers Sov's "who would use it" with three named users and ties into the funded BYOS grant. Still exposed to mfw78's doctrine because readiness verdicts touch onboarding to the competition.

### 3634 — zh-CN localization Phase 2 (answer77777) — 2026-10-15 — REJECTED
- **Author:** @answer77777 (Zheng). Hidden TL0; id 2081 → created ~Oct 13–15. Prior Rocket Pool GMC application.
- **Proposal:** ~1,500 strings / 8,800 words in Crowdin, glossary, QA, 3 months maintenance. **1,000 USDC** (600/300/100). Includes a 29-string sample translation with terminology rationale.
- **Reply:** Chim9 2026-10-16: "thanks for the application and for doing a work sample in advance, it's clear you put effort in. The committee isn't planning a Phase 2 of the CoW Swap UI localization at this time, so we won't be taking this application forward. Phase 1 (ES, PT-BR, RU, FR) was just completed, and we'd like to see how it lands before deciding anything about more languages. If that changes, we'll post it on the forum."
- **Assessment:** Cheapest, most evidenced application in the batch; rejected because the lane is closed. Clearly human (the glossary argument about 盈余 vs 剩余 is real translator reasoning).

### 3638 — ZK Winner-Selection Parity Hardening (naina) — 2026-10-16 — AWAITING (3 days)
- **Proposal:** differential test + CI between the production winner-selection crate and cowprotocol/Zk-benchmark's Zisk guest; fix agreed divergences. $4,500 USDC, 2 milestones, 4 weeks. Explicitly: "This project will treat cowprotocol/services as the source of truth. It will not define independent solver competition rules."
- **Evidence (claimed, not published):** 80,000-execution harness; winner set differed in 7,209 of 20,000 generated auctions; 131/961 winning solutions in a 632-auction mainnet sample exceed u128 intermediates. "I can provide the harness, raw results and exact reproduction commands for technical review."
- **Committee replies:** none.
- **Assessment:** naina's fourth thread and the first with substance; carefully worded to dodge both the "source of truth" and "competition dynamics" objections. But the harness isn't public, the author is a 2-week-old hidden account, and Zk-benchmark is a research repo — expect the "is this active / does a maintainer want it" question.

### 3640 — CoW Convert, East African stablecoin widget (carl) — 2026-10-18 — AWAITING (1 day)
- **Author:** @carl. Hidden TL0; id 2085 → created ~Oct 15–18.
- **Proposal:** mobile-first USDC/USDT conversion widget with limit and TWAP modes, English+Swahili, off-ramp deep links, fork-me template, custom appCode. Amount/milestones not visible (digest truncated before them).
- **Evidence:** none linked.
- **Assessment:** Only "novel application" pitch in the batch. Untested against the committee's volume lens; expect "what volume will it attribute".

### 3642 — x402.cow.fi conformance & regression suite (zynor) — 2026-10-18 — AWAITING
- **Author:** @zynor (GitHub zynorr). Hidden TL0; id 2087 → created ~Oct 16–18.
- **Proposal:** black-box conformance harness for the new pay-per-quote x402 API: offline engine, 40 fixtures, live verifier with $25 spend cap, 3-of-4 payment options, scheduled CI. $8,000 (2k/3k/3k) over 6 weeks.
- **Evidence:** x402-Sentinel (Hedera) with 69 checks, 54 fixtures.
- **Assessment:** Template-perfect, highly structured, numbers-everywhere text with no CoW-specific prior contact; reads as LLM-assembled from the 3569/3612 playbook. The service is days old and core-owned; most likely "core team owns this".

### 3643 — Same-Run Payout Attestation (lOCKEDIN / steven3002) — 2026-10-18 — AWAITING
- **Author:** @lOCKEDIN. Hidden TL0; id 2088, the newest account in the set.
- **Proposal:** complete draft PR #643 in solver-rewards (MultiSend decoder, Safe tx-hash recompute, same-run plan capture) into a pre-flight or signer-facing verification route. Hybrid hourly, capped 4,500 xDAI-equivalent for ≤100 h at 45/h; 0 COW.
- **Evidence:** draft PR #643 with "193 locally passing offline unit tests"; references issue #529 and PR #635.
- **Assessment:** Only applicant who already has a PR open in a CoW repo before asking. But it is a draft, unreviewed, and the committee has already said (3575) issue-sized work belongs to the repo reward program. Also touches solver payouts, which is competition-adjacent.

### 3434 — Quantir Risk Intelligence Layer — 2026-04-25 — REJECTED (digest tag "grant-funded" is wrong)
- **Author:** @Quantir. Hidden TL0; id 1815 → created ~April 2026, shortly before posting.
- **Proposal:** CoW module for an existing risk-scoring/alerting SaaS. 35,000 xDAI (10k/15k/10k), 9 weeks. Wallet field left as "[Add Gnosis Chain wallet address]".
- **Reply:** Sov 2026-04-27: "Thanks for the submission and your interest in COW Grants. We have reviewed this internally and, at this time, we're not interested in moving forward."
- **Assessment:** Generic vendor pitch; AI-templated (every milestone is "Define… Map… Implement… Produce a short technical note"). Not commented on.

### 3330 — ethcontract-rs → Alloy (No-rush) — 2026-01-07 — REJECTED (tag "grant-funded" is wrong)
- **Author:** @No-rush (AK, GitHub abhishekkochar). Created 2025-01-23, TL1; ~1 year old at posting.
- **Proposal:** 13,000 xDAI / 13 weeks / 5 milestones to migrate ethcontract-rs off web3/ethabi/parity-common.
- **Reply:** mfw78 2026-01-07: "The CoW Protocol services is currently being migrated to alloy, at which point ethcontract-rs will be deprecated, so I don't think that this is in alignment / of value for the CoW DAO ecosystem."
- **Applicant:** "Make sense. Thanks for the info."
- **Assessment:** Well-formed, wrong target; killed in one line because the applicant didn't check the roadmap.

### retro-3333 — Hummingbot Gateway connector (tantodefi) — 2026-01-12 — WITHDRAWN
- **Author:** @tantodefi. Created 2025-10-22, TL1; ~3 months old. Prior CCXT connector proposal ("stalled in upstream" per mfw78).
- **Proposal:** retro round, 10,000 xDAI + 20,000 vested COW for a Hummingbot Gateway router connector; MVP in a fork.
- **Replies:**
  - @fengtality (Hummingbot Foundation) 2026-01-26/27: raised maintenance and the Foundation's paid connector-bounty model.
  - mfw78 2026-01-27: "I don't think the value proposition for a HummingBot integration is well defined. The mechanism and API within CoW Protocol is not designed for high frequency trading, with some endpoints being extremely costly. Given the previous CCXT connector integration (which has stalled in upstream), and the lack of any validation for a net benefit to CoW Protocol from such a trading integration, I signal that I would not be in favour of this grant in any form without validation of other HFT and backend API changes that would facilitate such."
- **Applicant:** "I'll close these PRs and Issues given the overall lack of support." Hummingbot's founder then said "I think we should integrate LlamaSwap instead."
- **Assessment:** Bot-framework integrations are dead on arrival unless volume is proven; the counterparty foundation also wanted to be paid.

---

## Part 2. Author profile summary

| Account | Created | TL | Age at first post in batch | Notes |
|---|---|---|---|---|
| bleu | 2023-08-24 | 2 | 2y5m | 18 badges, ~50h read; 4 threads, 2 funded + cow-rs payout, 1 rejected, 1 unanswered |
| mfw78 | 2022-03-10 | 2 | committee | `cowgrantscommittee` group; 22 badges |
| auryn | 2023-08-07 | 1 | 2.5y | Gnosis Guild |
| No-rush | 2025-01-23 | 1 | ~1y | |
| tantodefi | 2025-10-22 | 1 | ~3m | |
| CoBuilders.xyz | 2025-11-27 | 2 | ~4.5m | lost cow-rs allocation |
| mani67 | hidden (id 1793) | 0 | likely days | |
| Quantir | hidden (id 1815) | 0 | likely days | |
| ILE_LABS | 2026-05-15 | 1 | 1 day | 4 threads, 0 traction |
| VedantaHazra | hidden (id 1838) | 0 | ≤3 weeks | |
| gabari (Nexroute) | 2026-06-13 | 2 | endorser | |
| kaisersolver | 2026-08-07 | 2 | ~2m | live solver; most cross-thread engagement |
| satya_98402 | 2026-08-27 | 1 | 0 days | the one new-account success |
| SimplexTDA | 2026-08-31 | 1 | 10 days | |
| mtvl (Vacuumlabs) | hidden (id 1930) | 0 | days | |
| decentralised | hidden (id 1948) | 0 | days | |
| ZeroNine | 2026-09-23 | 1 | 12 days | |
| daotrading-zh | hidden (id 2010) | 0 | days | |
| naina | hidden (id 2031) | 0 | ~0–3 days | 4 threads in 16 days |
| Mateo | 2026-10-05 | 1 | 0 days | |
| kermo (Fibrous) | hidden (id 2044) | 0 | ≤1 week | |
| apsarthsumit | hidden (id 2062) | 0 | ≤1 week | |
| answer77777 | hidden (id 2081) | 0 | ≤2 days | |
| carl | hidden (id 2085) | 0 | ≤3 days | |
| zynor | hidden (id 2087) | 0 | ≤2 days | |
| lOCKEDIN | hidden (id 2088) | 0 | ≤2 days | |

Thirteen of 23 thread authors are TL0 with hidden profiles. Of the eight applications filed 2026-10-12 or later, seven come from accounts created within a week of posting. Nobody with a hidden profile has been funded.

---

## A. What the committee is saying in Sept–Oct 2026

**On what gets measured.** Sov, 3374, 2026-09-09: "Our perspective is that a Railgun integration is worth having, but on its own it doesn't justify funding. The value to the DAO is trading volume settled through CoW Protocol, and that is what we would measure: volume attributable to the integration once it is live."

**On whether there is anything to apply for.** Sov, 3606, 2026-10-02: "the committee isn't publishing new problem areas or RFPs right now, so there isn't a specific area we can point you to. CIP-82 and the application template remain the public reference for anything submitted, but we wouldn't recommend investing in a research sprint in the expectation of a grant." The Volume-Based Integration RFP "closed to applications on 30 September 2025".

**On who must want it before they'll fund it.** Sov, 3612, 2026-10-09: "the main thing we'd like to understand is who would use it ... we haven't seen a services maintainer or a solver team say that a published vector set is something they would run. Has anyone told you they would?" Sov, 3619, 2026-10-12: "who would use Fiberscope and the API beyond Fibrous? ... it would help to hear from another solver team or someone on the core team who relies on the entry and win-rate figures." Sov, 3566, 2026-10-02: "The committee asked for a view from the solver side on whether this research would be useful and non-duplicative, and that interest hasn't materialised, so we won't be moving forward." (Same rule stated in June, 3467: "we'd need to see solver express interest in something like this before exploring further.")

**On anything touching the solver competition.** mfw78, 3612 and 3620, 2026-10-13 (identical text): "having golden vectors written by the core team is significantly more appropriate than having 3rd party assembled work ... I remain severely hesitant to enact any grant, retrospective or otherwise, that may influence the solver competition without this being thoroughly vetted and understood by the core / solver team (if not actually requested specifically by them)."

**On scoping and pricing.** mfw78, 3546, 2026-09-01: "Essentially the services is the 'source of truth', and cow-rs would be tested against properties / invariants etc derived from services. This would be the path that I would recommend in order to arrive at a grant that is soundly scoped (and useful)." mfw78, 3569, 2026-09-15: "maintainer upstreaming into services makes the grant contingent on an externality which may not be achievable and leave the state in deadlock. Generally, I'm in favour of the corpus, but would like to see the scope more coherent and narrow (and demonstrate understanding of the code bases, and their dependencies)." mfw78, 3569, 2026-09-29: "I don't see how this would be more than a day or two of dedicated, effective time in order to achieve the outcome of this grant, and therefore the current quoted costs are too high."

**On what is closed (full quotes in Part 1).** Docs: "a core-team-owned function ... We've closed that workstream" (Sov, 3464). Long-form education: "isn't something the committee is prioritising for funding right now" (Sov, 3588, 09-29). Localization: "isn't planning a Phase 2 ... we'd like to see how it lands" (Chim9, 3634, 10-16). Solana wrappers: "still marked experimental ... isn't looking to fund wrapper tooling" (Sov, 3603, 10-02). Second interfaces over Explorer data: "don't see enough added value to fund a second interface over the same data" (Sov, 3565, 09-18). RWA eligibility layers: "not something this program is looking to fund" (Sov, 3608, 10-09). CoW AMM: "deprecated ... somewhat moot / irrelevant" (mfw78, 3559, 09-15).

**On where small work should go instead.** Sov, 3575, 2026-09-18: "Those questions are for the service maintainers; best asked on the issue itself. We wouldn't fund this, and if it lands as help wanted the repo's own reward program covers it."

**On process mechanics.** mfw78, 3569, 2026-09-29: "Please make sure that the snapshot isn't started / run over the weekend (Sat/Sun), and ensure that the template used is the latest. Kindly note as well that the payment address would be an ethereum mainnet address, and not gnosis chain as we migrated the treasury a while ago." Sov, 3612: "the terms section needs the links to the Participation Agreement and the Grant Agreement Terms, and the note to the committee is missing." Sov, 3569 onboarding: "Your Reviewer responds within 7-14 days. Approved milestones enter the next end-of-month payout cycle, with funds arriving by the 15th of the following month."

**On fatigue / flood.** No committee member uses those words in these threads. The evidence is behavioural: Sov's rejections are two to three sentences and arrive 1–8 days after posting; mfw78 pasted one paragraph into two threads on the same day; 3609 and 3383 simply never got answered; and the only explicit tone escalation is the 3406 capitals: "AI SLOP WILL NOT BE TOLERATED AND YOUR SUBMISSION WILL BE IMMEDIATELY CLOSED AS AI SPAM." The one applicant who quoted a committee "sourcing challenge — the same few teams reply to every RFP" (3588) was told that lane is closed anyway.

**On what they're asking applicants to do first.** In order of how often it appears: (1) get a solver team or core dev to say in-thread that they want it (3467, 3566, 3612, 3619); (2) pick services as the source of truth and scope one narrow, non-blocking deliverable (3546, 3569); (3) post an exploratory thread before a formal application and wait for a concrete pointer (3546→3569 is the only path that worked); (4) take issue-sized work to the repo's own issue tracker and reward program (3575); (5) use the current template, link the T&Cs, mainnet address, no weekend Snapshot (3569, 3612).

**Named gaps they say they want filled.** Almost none. The only positively-stated wants in Sept–Oct are: volume attributable to a native Railgun/Railway integration (3374); and, implicitly, BYOS sub-solvers (bleu is "prospecting potential subsolvers" and core is still deciding production orderbook access, 3476). Everything else is phrased as what they won't fund.

---

## B. Crowded vs empty lanes

**Crowded (2+ live or recent applications):**

1. **Solver testing / conformance / verification** — 6 threads: 3546→3569 (approved, $2k), 3612 (score vectors, stalled), 3624 (readiness spec, pending), 3638 (ZK parity, pending), 3467 (Polytope, rejected), 3643 (payout attestation, pending). Four of these cite 3546 or each other. This is where the "third-party tooling must not shape the competition" doctrine is now being enforced; only the SDK-side corpus (no competition impact) got through.
2. **Solver analytics / economics** — 3619 (Fiberscope, pending with endorsement), 3620 (CIP-88, withdrawn), 3566 (TDA MEV, rejected), 3434 (Quantir, rejected), 3565 (decoder, rejected). Dune going paid-only in Sept 2026 is pulling applicants in; the committee's response so far is "who would use it" and "Explorer exists".
3. **Chinese-language** — 3588 (research kit, discouraged) and 3634 (UI zh-CN, rejected). Both lanes closed by name.
4. **Rust** — 3406 (cow-rs, paid), 3456 (intent-guard, rejected), 3330 (ethcontract-rs, rejected), 3569 (approved). Rust is fundable only inside cow-rs and only idiomatically.
5. **Pre-flight / security guards** — 3394 (Aegis), 3456 (intent-guard), 3642 (x402 conformance), 3643 (payout attestation), 3638. Two rejected, three pending; none requested by core.
6. **Docs / AI-agent onboarding** — 3464, 3402, 3603. All rejected; docs are core-owned.
7. **Consumer-facing apps / integrations** — 3640 (CoW Convert), 3608 (33Jane), 3333 (Hummingbot), 3374 (Railgun). Zero funded; the only yardstick offered is attributable volume, and the Volume RFP is closed.

**Empty (stated priorities with zero applications):**

- **Volume-attributable integrations with a named counterparty** (Railway/Railgun native, per Sov and mfw78 in 3374). Vacuumlabs asked in September and has not filed.
- **BYOS sub-solvers** — the one funded infrastructure piece is actively looking for external sub-solvers (3476), and the only outsider who showed up (ghislain.ott) is not a grant applicant.
- **Hooks / hook dApps / CoW Shed tooling** — the category bleu built its reputation on has no applicant in this window.
- **Core-team-authored golden vectors for fee/score/quote rewards** — mfw78 says these "written by the core team" are what's appropriate (3612/3620); nobody from core has volunteered, so the gap he describes stays open.
- **Native-speaker reviewers for localization** — the Phase 1 RFP needed them per 3634; the committee has frozen the lane rather than fill it.
- **Anything under CIP-82's "strategic ecosystem alignment"** — no application in this batch even claims it.

---

## C. Applicant archetypes

### Failing

1. **The day-old account with a polished pitch.** mani67, Quantir, VedantaHazra, decentralised, daotrading-zh, naina, Mateo, kermo, apsarthsumit, answer77777, carl, zynor, lOCKEDIN — thirteen hidden TL0 profiles, zero grants. Six were rejected within 48 hours. The committee doesn't say "new account" is the reason, but no hidden-profile applicant has yet cleared "who asked for this".
2. **The serial pivoter.** ILE_LABS (intent-guard → quickstarts → BCoW → E2E testing, May–Sept) and naina (Solana RFC → scope-check → contributor intro → ZK parity, 1–16 Oct). Each new thread is in a different lane; each reads as LLM-structured ("Project Pulse & Tracking", "evidence-first research sprint"). ILE Labs: 0 for 4. naina: 0 for 3, one pending.
3. **The incident-chaser.** Aegis after the $50M slippage trade; intent-guard after the DNS hijack. mfw78's verdict on the first: "seeks to misconstrue recent events." Sov's on the second: two sentences.
4. **Third-party reference tooling for the competition.** ZeroNine and apsarthsumit did the research, cited line numbers, got a solver endorsement, priced modestly — and ran into "golden vectors written by the core team is significantly more appropriate." Kaisersolver's 3624 is next in line for the same test.
5. **Content, media and localization.** Decentralised News, daotrading-zh, answer77777. All three lanes are named-closed. answer77777's 1,000 USDC application with a 29-string sample is the cheapest thing rejected in the batch.
6. **Build-the-product-then-ask.** 33Jane (live console), Quantir (live SaaS), Polytope (PoC), Execution Evidence Lab. "Thanks for building a working demo before applying" precedes the rejection each time; a demo is not a demand signal.
7. **Trading-bot and privacy integrations without volume proof.** Hummingbot, CCXT (prior), Railgun. mfw78: "lack of any validation for a net benefit to CoW Protocol from such a trading integration."
8. **Anyone who didn't check the roadmap.** ethcontract-rs (services already migrating to alloy), BCoW config (deprecated), Token-2022 (covered in DESIGN.md), docs (core-owned since June).

### Working

1. **The incumbent with a core-dev sponsor.** bleu: Programmatic Orders API (anxolin volunteered as reviewer, closed and paid Oct 2–7), BYOS (RFP-aligned, felixhenneke/harisang reviewing, M2 "looks good" Oct 8), cow-rs Phase 1 (mfw78 confirmed parity and paid). bleu still lost CoW Skills and got silence on the Watch Tower, so even the incumbent only wins when a named core dev wants the output.
2. **The ask-first, cheap, maintainer-steered newcomer.** satya_98402: exploratory thread → one pointer from mfw78 → six weeks of visible unpaid verification work with a solver → narrow proposal → conceded every technical objection → cut from $5,500 to $2,000 on request → Snapshot → PR within a day. It is the only hidden-or-new account funded in the window, and the template others (3612, 3638, 3642) are now visibly copying without the courtship.
3. **Live solver operators who bring other solvers.** kaisersolver (cow-certify, cow-backtester, in-thread support from satya and bleu) and Fibrous/kermo (Fiberscope, endorsed by Nexroute within 24 h). Neither is funded yet, but both got engagement questions rather than form rejections, and both pre-empted "who would use it".
4. **Committee-authored collective grants.** cow-rs is the committee's own vehicle for getting the SDK it wants at a price it sets (8,500 xDAI), with AI-slop filtering done by mfw78 personally.

### Explicit notes on AI-generated text

Likely AI-drafted or heavily AI-structured: 3394 (Aegis), 3456 and 3464 (ILE Labs), 3434 (Quantir), 3565 (duplicated section), 3608 (33Jane), 3603/3606/3609 (naina's first three), 3642 (x402). Disclosed AI use: 3620 (code only). Clearly human: 3346, 3374, 3546/3569 (self-corrections), 3566, 3612, 3619, 3624, 3634, 3330, 3333.

The committee commented on AI exactly once, in the thread it authored itself (3406): a top-post warning and a capitalised rejection of 0xSymbiotic's branch as "not implemented with Rust idiomacy ... AI SLOP". In every other case the rejection cites relevance, demand, or a closed lane — never the prose. Applicants should assume AI-shaped text isn't what's being rejected, but that it also buys nothing: the thing that gets a reply is a solver or core dev saying they want it.
