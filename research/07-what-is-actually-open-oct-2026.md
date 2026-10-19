# What is actually open, 19 October 2026

The forum category shows no open RFP, but the forum is not where the committee plans. Its planning lives in a public Notion site (the "CoW Grants Hub", linked from docs.cow.fi) with a weekly council update every Monday since November 2025, a pipeline database with stages from Ideation to Complete, and a handful of public Google Docs and HackMD one-pagers linked from those updates. All of it was read on 19 October 2026. This file lists every channel through which money can reach an outsider right now, what the committee is building toward, and what the core team has asked for in writing.

Sources: `sovs.notion.site` (CoW Grants Hub, Weekly Updates weeks 44/2025 to 42/2026, Pipeline), `cownation.notion.site` (core team's "GrantsDAO: List of ideas & RFPs & Grantees", Anxo's three scoping pages), Google Docs "CoW Grants Q4 2025: Action Plan", "CoW Grants Council - Q4 Work Plan", "CoW Grants: RFP Ideas for Discussion", "COW: Grants x Core - Twice Monthly" notes, "COW Grants Council Weekly Sync" notes, "H2 2026 Grant Ideas: Propose & Earn", and mfw78's Methane and Fee Automation one-pagers on HackMD. The CoWPath one-pager is private (403).

## 1. The seven channels that are open to an outsider

| Channel | Status on 19 Oct 2026 | Money | Evidence |
|---|---|---|---|
| Unsolicited application in the forum | Open. "Inbound applications remain open in the meantime" while "new grant sourcing is paused while roadmap priorities are aligned" | Whatever the committee prices it at; $2,000 was the last newcomer award | Weekly updates weeks 35 and 36; satya_98402 approved 8 Oct |
| `help wanted` issues in `cowprotocol/services` | Open; exactly one such issue exists (#2394, since Feb 2024) | 100 DAI per merged PR | services CONTRIBUTING.md; Sov in thread 3575 |
| Retroactive grant for merged PRs | Open in practice (dinesh11515, 15 PRs, 1,200 xDAI, Dec 2025); the formal Retro Round was a 2025 programme and has not been reopened | About $80 per merged PR | Thread 3321; weekly update week 2 |
| Volume-based integration rewards | RFP closed 30 Sept 2025, but the committee keeps offering the structure to anyone with volume (Railgun, Arcadia, R SDK) and runs a "Community-built Python SDK volume-rewards assessment" at the one-year mark | 5,000 COW at $1M, 30,000 at $25M, 75,000 at +$100M, 150,000 at +$250M; 12-month vesting | Threads 2993, 3374, 3220, 3281; weekly updates weeks 31 to 42 |
| Moo & Earn affiliate programme | Mandate lapsed 2 Oct; codes still active; rewards tracked and to be paid if a renewal CIP passes | Share of referred-volume fees; $200M+ referred volume by August | Thread 3605 |
| Core Contributor grants | Exist (Researcher funded Nov 2025, Solver Engineer, UX/UI, Copywriter in earlier years) but no open call; they are sourced by the core team | $2,000 to $3,000 per month historically | Core-Contributor-Grant category |
| Propose & Earn (ideas bounty) | Drafted June 2026, never posted to the forum, pipeline row "0 - Cancelled" | Would have paid 500 xDAI per adopted H2 focus area and 1,000 xDAI per idea that became a funded RFP or grant | Google Doc; weekly update week 24; pipeline |

Nothing else is open. The Optimism Season 8 application (100,000 OP plus 200,000 COW in solver and integration incentives) was submitted in October 2025 and Optimism is not among the chains CoW runs on a year later. The three Playground RFPs, the Value Distribution RFP, BYOS and the localisation RFP are all filled.

## 2. The committee's own pipeline (Notion database, read 19 Oct)

Stage names are the committee's: Ideation, Scoping, Posted, Sourcing, Awarded, In Progress, Complete, Cancelled, Declined.

| Item | Stage | Owner | What it is |
|---|---|---|---|
| Text to Trade | 1 - Ideation | Sov | No document linked; appears from April 2026 onwards as "no material changes" every week |
| Quote API v2 | 1 - Ideation | Sov | Anxo listed it in Feb 2026 as "potentially suitable for a grant", Stephan said it was on the Q2 roadmap. Since then the core team shipped a "Streaming Quote API" to integrators (CIP-79 update, Sept) and the pay-per-quote x402.cow.fi (9 Oct). Probably overtaken by internal work |
| Methane | 1 - Ideation | Sov; author mfw78 | ERC-4337 gas abstraction: pay gas in USDC/COW/DAI, bundler as Shepherd WASM modules, paymasters via CREATE2, CoW swaps the gas token to ETH. "~400 hours (10 weeks FTE)", AGPL-3.0, "NOT third-party audits". Public one-pager. Depends on Shepherd, which is mfw78's own late-running grant |
| CoWPath | 1 - Ideation | Sov; author mfw78 | "Integration wizard and developer guidance system" (week 46). One-pager is private. mfw78's Nov 2025 task list: "Write grant for CoW Protocol integration wizard / support" |
| Automated Fee Consolidation and TWAP | Cancelled (Aug 2026) | mfw78 | Bridging L2 fees to mainnet and automating the weekly COW buyback TWAP via Shepherd modules; "7 weeks to production". Public one-pager. Cancelled after sitting in scoping "for an extended period" |
| Documentation RFC | Cancelled (May 2026) | Sov | Five responses; committee "decided not to advance the work to a formal RFP"; mfw78 questioned "whether an external documentation effort can succeed without structured access to subject matter experts" |
| Back-office Interface (Anxo) | Declined | | Anxo's internal admin and debug panel; "Back office Interface and Trade Settlement Window Metrics will also be handled internally" (week 11) |
| Trade Settlement Window Metrics (Anxo) | Declined | | Prometheus metrics for effective limit price so the team is alerted when an order had a window to settle and did not; handled internally |
| H2 2026 Grant Ideas: Propose & Earn | Cancelled | Sov | See above |
| Community-built Python SDK - Volume Rewards | In Progress | Sov | One-year volume assessment of cow-py ($18M volume, 8,800 orders per bleu) under the volume reward terms |
| Fiberscope; Solver Score Conformance Test Set | Posted | Sov | The two live applications still being discussed |

Everything the committee has itself originated in 2026 came from the core team (BYOS from Felix, Value Distribution from NotSoFormal, localisation from MooKeeper) or from mfw78's own Shepherd stack. The only outsider-originated grant in the whole 2026 pipeline is the $2,000 conformance corpus.

## 3. What the core team asked for in writing (Oct 2025 to Feb 2026) and what happened to each

From the Q4 2025 Action Plan, the Q4 Work Plan, "RFP Ideas for Discussion", the core team's Notion ideas list and the Grants x Core meeting notes.

| Ask | Who | Status a year later |
|---|---|---|
| **Composable CoW Order Decoder Tool**: "TWAP and programmatic orders currently only show appData strings in block explorers, making debugging nearly impossible... CoW's existing appData SDK provides most of the infrastructure needed" | Luis (core) | Listed as "Ready to Launch" RFP in the Q4 2025 Work Plan. Never posted. CIP-82 names "Order Decoder" as a 2026 developer-onboarding priority. bleu's Programmatic Orders API (closed Oct 2026) now indexes conditional orders and their parts, which covers part of the need |
| **Order Execution Troubleshooting Dashboard** ("why my order didn't moo") | Anxo | "Requires infrastructure access with security implications". Built internally: "The 'Was the order correctly created?' debug tool ended up being built internally, as it required defining requirements tightly and providing infrastructure access that made external development impractical" (week 11) |
| **Smart Order UI Features**: stop-loss and composable orders in the main UI, Safe integration | Luis | "Needs dedicated review resources given high UI/UX standards". TWAP for EOAs shipped internally 30 Sept 2026 |
| **SDK warnings and USD estimations**: "We don't have USD estimations, and therefore, we don't include some important warnings... I leave it as a potential idea for grants to migrate warning logic to the SDK... Warnings could be one of the most impactful next thing. It would have avoided the issue AAVE had making a user sign an order at a terrible price, making the user loose $500K" | Anxo, comment on the Action Plan, 17 Oct 2025 | Open. `cow-sdk` issue #309 "Model warnings for quotes" (May 2025) is still open with one comment. The March 2026 $50M slippage trade and the docs RFC's "a partner couldn't determine that the buy amount field requires slippage to be packed in" are the same wound |
| **Integration wizard** ("something like widget.cow.fi but for the SDK") plus "post-mortems with recent failed integrations" | Luis and Anxo in the same comment thread | Became CoWPath (mfw78, private, Ideation for 11 months) |
| **QoS: fewer wrong prices, price caching, missing paths; watch-tower ready for more EOA orders; end-to-end tests and alerts; instrumentation and debugging** | Anxo via Alex Marsh, Oct 2025 | Watch-tower part became Shepherd (mfw78). Rest internal |
| **Verified vs non-verified quotes: visual indication in UI** ("prices too good to be true") | Anxo | No grant; UI is core-owned |
| **Tighter slippage tolerance** ("finish volatility, ideally lower to 0.1 when possible") | Anxo | Internal |
| **"Trigger refund button" in CoW Explorer for expired native-ETH orders** | comment on the Action Plan | No trace of it shipping; small, user-facing, explorer now lives in the cowswap monorepo |
| **Cross-chain order relayer (ERC-7683)** | Sov's ideas doc, "needs more discussion" | Core team shipped Bitcoin cross-chain swaps and swap-and-bridge itself |
| **Batch auction simulator** (educational) | Sov's ideas doc | "uncertain if people would actually use it". Dropped |
| **Automated fee collection via Zodiac roles and bridging scripts** | Discord, Oct 2025 | Became mfw78's Fee Automation one-pager; cancelled Aug 2026 |
| **External grant applications on CoW's behalf** (Optimism etc.), "grantee takes 10% of secured funds" | Sov | Became the CIP-82 5% partnership success fee for committee members |
| **Fund dependencies** (Solidity, ethers.js) with the Ethereum Foundation | Action Plan | No trace |

## 4. Budget: the constraint is not money

From the Q4 2025 Action Plan (Oct 2025): "Only 22% of our 2025 xDAI and 8% of our COW budget has been deployed." Available then: 465K xDAI and 1.24M COW for general grants, 4.75M COW for volume deals. Planned Q4 deployment: about 200K xDAI plus 230K COW (developer RFPs 45K, solver competition 90K, integration partners 150K COW, EF partnership 30K, retro round 40K, Optimism match 80K COW). Meeting note, 20 Oct 2025: "4.5M COW in volume-based incentives remains largely untapped (only 8% utilized to date)."

CIP-82 (Jan 2026) then cut the xDAI request from 600K to 500K and moved to quarterly releases with up to 75% of idle assets returnable to the treasury. KPK's H1 2026 review shows about 140K DAI leaving under CIP-82 in six months. The committee holds roughly 300K xDAI (Q3 2025 review) and spends well under half of what it is allowed to.

What limits spending is stated repeatedly in the council's own notes: core-team review bandwidth ("Technical review has historically been a deficiency", H1 2025; "whether an external documentation effort can succeed without structured access to subject matter experts and a commitment to timely review cycles from the core team", mfw78, April 2026; "External PRs are reviewed on a best-effort basis and may sit for several weeks", services), and alignment ("The Council is holding new grant sourcing until roadmap priorities are set with the Core team", Aug 2026; "Felix and Anxo exchanged detailed feedback on documentation improvements. Discussion inconclusive - requires action plan from core team before grants can develop RFP", Nov 2025).

So an outsider is not competing for scarce money. They are competing for scarce reviewer attention, and the committee's stated north star is "Make it easier to build on and integrate with CoW Protocol, expanding DAO capacity to deliver beyond core team priorities. Success is measured by external contributions to and integration-driven volume."

## 5. How the council works internally, as it affects an applicant

- Weekly council sync (Mondays); the Grants x Core twice-monthly sync was cancelled in Feb 2026 and folded into Sov's weekly. Sov attends the core team's Monday 15:00 UTC call. Updates are drafted from public sources first ("Draft: This update was assembled from public sources. Sov has not yet provided raw inputs", week 42), so what you post in the forum is literally what the council reads.
- "An initial evaluation has been produced for committee review" on every new application within the week it is posted (weeks 37, 42). Rejections follow one to eight days later.
- The pipeline records a Steward (Sov, Chim) and a Reviewer (mfw for technical, Anxo, Haris, Chen, NotSoFormal for domain). An application with no plausible reviewer does not move: "If no Reviewer is assigned, the proposal is unlikely to pass."
- Division of labour agreed with the core team (Oct 2025): "The Grants Committee owns fiscal responsibility and ROI assessment. Core team provides technical review only (not budget decisions)... We seek alignment on priorities, not approval on individual grants." In practice every 2026 award had a core reviewer named before Snapshot.
- Outreach happens: in Nov 2025 Sov contacted Scopelift, Woof, Mevlog and Tanto about RFPs; in Jan 2026 c3rnst's successors nudged bleu toward the ethers RFP. Known builders get pinged; unknown ones must show up.
- The committee tracks "Next Action" dates and flags stale items; CoWPath and Methane have been "no material changes" for most of 2026 without being cancelled, because the author is the technical lead.

## 6. What this changes about where to aim

1. The two asks the core team wrote down and nobody delivered are the **Order Decoder** (named in CIP-82, "Ready to Launch" in Oct 2025, never posted) and **SDK-level warnings with USD estimates** (Anxo's own words, open `cow-sdk` issue #309). Both are developer-onboarding items, both have a named internal requester, and both are small enough to prototype before asking.
2. Methane, CoWPath and Fee Automation are mfw78's. Do not pitch into them; if anything, ask in the Shepherd thread whether Methane needs a hand once Shepherd's 7-day run and extension (due 23 Oct) land.
3. Propose & Earn is dead on the pipeline, but a well-argued "H2 focus area" post costs nothing and the council has publicly said it wants community input on where money would do the most good.
4. Anything that needs infrastructure access (dashboards, debuggers, metrics) will be built internally; the council has said so three times.
5. Volume deals pay far more than grants ($50K per integration at the Q4 2025 structure) but only to someone who brings a wallet or protocol with users.
