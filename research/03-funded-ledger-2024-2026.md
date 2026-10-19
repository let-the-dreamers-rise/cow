# Funded ledger, 2024 to October 2026

Every grant that reached a Snapshot vote in the `cowgrants.eth` space from 2024 onwards (98 proposals in the space in total; the pre-2024 ones are omitted here), joined to its forum thread. Snapshot data pulled 2026-10-19 from the Snapshot hub; thread ids open at `https://forum.cow.fi/t/<id>`. Every vote since 2023 passed unanimously with 3 to 7 committee votes. The committee never votes something down on Snapshot; proposals die in the thread, or by silence, before they get there.

## 2026 (ten months)

| Snapshot date | Grant | Thread | Who | Amount | How it got there | Outcome |
|---|---|---|---|---|---|---|
| 2026-10-01 | Signed-Order / EIP-712 / UID conformance corpus for cow-rs | 3569 | @satya_98402, account created the day of first post | $2,000 DAI (asked $5,500, cut on request) | Exploratory thread 3546 on 27 Aug, one pointer from mfw78, six weeks of unpaid verification work in public, narrow proposal | Approved 8 Oct; M1 PR (cow-rs #63) filed within a day |
| 2026-08-04 | CoW Swap UI translation, phase 1 (ES, PT-BR, RU, FR) | 3481 | Four individuals (@aspnxdd123, @flaviampsilva, @just2102, @armand) | 900, 1,000, ~1,000, 950 USD per language | RFP by Sov; 10+ bids; native-speaker sample review; "best value wins, not lowest cost" | Delivered 21 Aug, paid 7 Oct. Phase 2 refused 16 Oct |
| 2026-07-02 | Bring Your Own Solver | 3476 | @bleu | not visible in thread (multi-milestone, audit, two deploys) | RFP by Chim9 (3469); bleu beat Chainza | M1 signed off Aug, M2 "looks good" 8 Oct; staging on BNB |
| 2026-05-15 | Community-built Rust SDK, phase 1 | 3406 | Thread by mfw78; paid to @bleu | 8,500 xDAI pool, "divided amongst contributors" | Replacement for a cancelled Nov-2025 single-entity Rust SDK grant (3224, no code in 5 months) | Parity confirmed 30 Jun; whole pool went to bleu; CoBuilders and 0xSymbiotic rejected, one as "AI SLOP" |
| 2026-03-02 | Value Distribution Mechanism (research) | 3328 | Aragon | not stated in thread | RFP by Chim9; 6 applied, 3 interviewed | Delivered 5 May, paid 11 May; fed the core team's May framework (3454) |
| 2026-02-23 | Programmatic Orders API | 3346 | @bleu | 24,000 xDAI + 40,000 COW (12-month vesting) for maintenance | Proactive, but anxolin (core) "would vouch for it" and volunteered as reviewer; M3 cut from 12k to 9k | Closed 2 Oct; now powers TWAP-for-EOA discovery on CoW Swap |
| 2026-01-26 | Playground Performance Testing Suite | 3263 | @bleu | 27,000 xDAI + 27,000 COW (from thread milestones) | RFP by mfw78 (3218) | Signed off 15 May, paid 9 Jun |

Approved in December 2025 and paid in 2026: Retrospective funding for 15 merged PRs (@dinesh11515, 1,200 xDAI, about $80 per PR, thread 3321); swap.cow.fi bundle optimisation (@crutch12, 800 xDAI + 1,000 COW, thread 3315, first rejected as spam then rescued when shoom3301 from the frontend team vouched); Playground Block Explorer (CoBuilders, $7,500, thread 3284, RFP response filed after the deadline); Playground Offline Mode (@bleu, 16,800 xDAI + 16,800 COW, thread 3262, after mfw78 said the first scope was "out of our budgetary range"); Viem/Wagmi migration (@bleu, about 21,000 xDAI from thread milestones, thread 3308); Shepherd (mfw78's own company, thread 3288, approved with mfw78 abstaining, late and still running its 7-day test on 13 Oct 2026).

Closed out in 2026 at a discount: Tycho CoW AMM integration (@markus / Propeller, thread 2843): $10,000 asked, 50% paid in Oct 2026 after mfw78 personally built and verified the branch because "there's no transaction or usage evidence" for milestone 2. CCXT connector (retro round, thread 3226): $15k asked, $6k paid, remainder terminated when the CCXT maintainer wanted $40k to merge.

## Money that reached people with no prior CoW history, 2026

| Who | Money | Weeks from first post to approval |
|---|---|---|
| satya_98402 | $2,000 | 6 |
| four translators | ~$3,850 total | 5 (RFP) |
| CoBuilders (Dec 2025) | $7,500 | 1 (RFP, with a working demo in the first post) |
| crutch12 (Dec 2025) | ~$1,000 | 2 (rescued by a core dev) |
| dinesh11515 (Dec 2025) | $1,200 | 1 (retro, PRs already merged) |

Everything else in 2026 went to bleu (five grants), Aragon (RFP) or mfw78 (committee member). Bleu's own retrospective (thread 3637, 16 Oct 2026) counts "10+ grants" and three years of work; the Q3 2025 review had them at $6k of the $9k cow-py pool, plus the framework-agnostic SDK, the stop-loss Safe app, hooks dApps, the Dune governance dashboard, the CoW AMM deployer, the subgraph redeploy, and more.

## 2025

| Snapshot date | Grant | Thread | Who | Amount | Notes |
|---|---|---|---|---|---|
| 2025-12-31 | Retro: 15 merged PRs | 3321 | dinesh11515 | 1,200 xDAI | mfw78 asked the frontend team to estimate internal time first |
| 2025-12-22 | swap.cow.fi bundle optimisation | 3315 | crutch12 | 800 xDAI + 1,000 COW | sister proposal (prerender HTML, 3301) rejected: "would make more sense for this to be done by the internal team" |
| 2025-12-15 | Shepherd | 3288 | mfw78 | not stated | anxolin: "essentially proposes rebuilding the watchtower logic for a second time" |
| 2025-12-15 | Viem/Wagmi migration | 3308 | bleu | ~21k xDAI | shoom3301 reviewer; held payments until QA done |
| 2025-12-02 | Playground Block Explorer | 3284 | CoBuilders | $7,500 | 0xmitch's competing RFP response rejected for "rolling a complete block explorer... fragility" |
| 2025-12-02 | Playground Offline Mode | 3262 | bleu | 16,800 xDAI + 16,800 COW | |
| 2025-11-13 | Core Contributor Researcher | (core-contrib) | core-team adjacent | | |
| 2025-11-08 | Rust SDK | 3224 | pstylez78 | 8,500 xDAI | Cancelled April 2026, zero code delivered, zero paid |
| 2025-11-04 | CCXT connector (retro) | 3226 | tantodefi | 15k xDAI + 15k COW, cut to 12k, paid 6k | |
| 2025-10-14 | i18n setup v2 | 3214 | BootNode (@manu) | 60% of original ask | Built "at their own risk" while the RFP was paused; paid at a discount for working outside process |
| 2025-06-11 | PolySwap | 3052 | intermarch3, Pybast | not stated, xDAI + COW | First version (2895) sent back for architecture; completed Jan 2026 after mfw78 caught a mock Polymarket handler in the live deploy |
| 2025-05-13 | Closure vote, MEV Blocker verification tool | 2510 | april | terminated | 11 working days estimated, 10 months elapsed, M2 and M3 refused |
| 2025-04-05 | CoW AMM trade-envy pipeline | 2836 | tommel | 3,750 xDAI (75 h) | harisang reviewer; completed July 2025 |
| 2025-03-25 | Framework-agnostic SDK | 2811 | bleu | not stated | Completed Sept 2025, "actively integrated and used within CoW Swap itself" |
| 2025-03-04 | ZeroMEV infra maintenance | 2859 | Blackhawk | $2,650 for 60 h + 2,500 COW | Devops, public good, sponsored by middleway.eth |
| 2025-02-28 | CoW AMM and LP tokens in Tycho | 2843 | markus (Propeller) | $10,000 | 50% paid Oct 2026 |
| 2025-02-21 | Data pipeline for solver team, part 2 | 2838 | butter_fly | 6,000 EUR (3 months) | harisang: "leading towards a very clean and robust accounting" |
| 2025-01-28 | Core Contributor Solver Engineer | (core-contrib) | | | |

## 2024

Automated fee withdrawal (meetm), Settlement wrapper contract plus retrospective (meetm), Authenticated hooks (meetm), E2E tests to Foundry (meetm, RFP by mfw78), Leakage analysis (butter_fly), Data pipeline for solver team (butter_fly), MEV Blocker billing automation (cowanator), Dune Sync V2 (cowanator / bh2smith), CoW AMM LP oracle (bh2smith and lumoswiz, RFP by fleupold; bleu's competing bid lost for "a lack of smart contract work"), CoW Hooks dApps (bleu), CoW AMM expansion (bleu), CoW AMM deployer retrospective (bleu), subgraph redeploy retrospective (bleu), Dune governance dashboard (bleu, RFP by c3rnst, beat Curia Lab and TogetherCrew on price and "not having to handle another front-end long-term"), Stop-loss Safe app (bleu), ZeroMEV open-sourcing (Pmcgoohan), MEV Blocker verification tool (april, later terminated), two solver bounties (LP tokens, CoW AMM integration) run by the solver team itself.

## What the ledger says

1. Four names (bleu, meetm, cowanator/bh2smith, butter_fly) plus the committee's own members took most of the 2024 to 2025 money. Every one of them had a core developer who wanted the output and said so in the thread before Snapshot.
2. Newcomer money in 2026 is about $15k across five people, and all five either answered an RFP, had PRs already merged, or spent six weeks in a thread before asking.
3. The committee sets the price, not the applicant. "A day or two of dedicated, effective time" was priced at $2,000 (3569). 75 hours was 3,750 xDAI (2836). Nobody's 2026 ask survived intact except the RFP bids.
4. Grants that depended on someone else (CCXT upstream, solver adoption for Tycho, Polymarket's real API for PolySwap) were paid late, partially, or after the committee did the verification work itself. Since 3226 the rule is explicit: "We do not hold up grant completion contingent on merging into externally controlled repositories" (mfw78, 3374).
5. Volume incentives (4.99M COW reserved under CIP-82) have paid nobody through the forum in 2026. The RFP closed 30 Sept 2025 and the only 2026 pointer to it was a hypothetical for Railgun/Railway.
