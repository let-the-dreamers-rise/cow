# Rejected ledger, 2024 to October 2026

Every rejected, cancelled or silently dead grant thread from 2024 onwards, with the sentence that killed it. Quotes are verbatim from the thread; the thread id opens at `https://forum.cow.fi/t/<id>`. The 2026 queue is covered separately in `05-live-queue-oct-2026.md`.

## The kill sentences, by cause

### "No measurable impact on protocol usage" (marketing, education, community, events)

| Thread | What | Who killed it | Sentence |
|---|---|---|---|
| 3283 Drive CoW Awareness and Adoption (SI<3>) | regional education programs | Sov, same day | "Our program is currently focused on initiatives with direct impact on CoW Protocol usage. This includes things like developer tooling, integrations that drive trading volume, solver ecosystem improvements, and technical infrastructure. General awareness and marketing campaigns, even well-executed ones, don't fit our current funding priorities." |
| 3298 Boring Security class, second attempt with 100 students taught | security class with CoW Swap content | Sov, same day | "Without tracking mechanisms to measure student-to-user conversion, we can't justify funding education initiatives at this time. If you're able to add UTM tracking and share data on how many graduates actually start using CoW Swap, we'd be interested in revisiting." |
| 3075 Boring Security, first attempt | | Sov, 8 days | "our current grant priorities focus on initiatives that demonstrate a direct, measurable impact on CoW Protocol metrics, such as trading volume, user acquisition, or technical infrastructure development." |
| 2860 Hispanic community (content creator) | | mfw78, next day | "there is no clear, measurable method that can be assessed as to the impact of the grant." Then: "for engaged-based grants, such as marketing etc, I would only favour those on a conversion basis... UTM codes for referrals to CoW Swap's front-end are already logged... I don't support clicks, views, etc" |
| 2852 Brand in India, memes | $7,200 / 5 months | mfw78, 4 days | same sentence as 2860; "after internal discussion, Grants Committee is not willing to entertain this grant." |
| 2745 CowPioneers local communities | five tiers of KPIs | netrunner, mfw78, Chim9 over 3 weeks | mfw78: "It seems odd to engage a variety of audiences in different languages when the core method of using the application if via an interface that is only in English." (This remark became the i18n RFP four months later.) |
| 2962 CowCheck governance-to-social content | | middleway, Kowrigan, mfw78 | mfw78: "bridging social media with governance lacks clear tangible benefits." |
| 2523 Ethereum Mexico sponsorship | | Chim9, 9 days | "events sponsorships are rather out of scope for the Grants DAO" |
| 3221 Alphaday community hub | | Sov, same day | "I checked in with the marketing team on this side and we don't feel this proposal is something that makes sense for us to pursue." |
| 2951 Winks.fun (swap inside Twitter) | $8,000 in COW | nobody | zero replies in 18 months |

### "Core team owns this" or "already exists"

| Thread | What | Sentence |
|---|---|---|
| 3301 swap.cow.fi prerender HTML (crutch12) | | mfw78: "the Grants Committee would be unwilling at the current quoted price in that it would make more sense for this to be done by the internal team as opposed to an external contributor." |
| 3267 PostHog telemetry in the TS SDK | | Sov: "we already track SDK errors in our front-end, and we don't believe this would provide sufficient additional value to offset the ongoing maintenance costs." |
| 3049 Backend Alloy migration (mfw78's own company) | | no reply; services did the migration in-house, which later killed 3330 too |
| 3190 AzothBalancer RPC load balancer for solvers | v0.3.0 live | mfw78: "much of this work is already done for CoW Protocol's infrastructure"; then "the impact of providing RPC tooling around this is relatively low... Many SDKs, such as alloy and ethers-js allow for providers that facilitate fallback". solver_cow: "after inquiring with the solvers, it appears that there doesn't seem to be too much demand for this service specifically." |
| 2245 Halborn infrastructure security assessment | | middleway: "the team has had discussions with Halborn in the past for a security review, but this hasn't eventually worked out mainly due to the high cost. At this moment in time there's no appetite to reconsider this." |
| 3211 Zokyo security partnership | | Sov: "We have had other service providers approach us with similar partnership ideas and, for the moment, this is just not something we are interested in pursuing." |
| 2448 POMA engage-to-earn for developers | | mfw78: "given that we have a perpetual running grants program, there is ample opportunity for developers to pitch an idea and get funded, so there is no need for this kind of program." |

### "Not open source", "not sustainable", or "too expensive for what it is"

| Thread | What | Sentence |
|---|---|---|
| 2551 and 2660 Curia Lab governance analytics ($20k) | | sohkai: "funding this type of dashboard (solely governance analytics) and the amount requested ($20k) can be justified given they aren't directly able to contribute towards moving the needle on any core protocol metrics." c3rnst: "not in the spirit of being open source and sustainable vs. quite pricey." Became an RFP that bleu won on Dune. |
| 2654 TogetherCrew governance dashboard | | c3rnst: "the deciding factors to explore another proposal was the longevity of not having to handle another front-end long-term as well as price." |
| 2400 Solver analytics dashboard (bharath) | | mfw78: "Will the Rest API's source code and front-end be open sourced?" Then silence. |
| 3233 Playground block explorer (0xmitch) | RFP response | mfw78: "Issues that were highlighted included the rolling of a complete block explorer, additional dependencies in the chain (next js), and overall fragility of the implementation. The decision to not proceed with this Grant Application is final." |
| 3220 Arcadia Finance integration + audit | BUSL contracts | mfw78: "the remit of the CoW DAO Grants Committee is limited to GPL / MIT"; offered 50/50 audit split plus volume milestones (5,000 COW at $1M, 30,000 at $25M, 75,000 at +$100M); when Arcadia asked for prior dev costs: "if we entertain post-facto accounting... this sets / establishes precedence that allows for projects to pitch grants and point to previous development costs"; marked rejected for "lack of discussion" |
| 1840 Milkman 2.0 | $70k over two years incl. support | netrunner: "the ongoing support costs will surpass the total grant value after 11 months" |

### "Solvers must integrate it, and they won't"

| Thread | What | Sentence |
|---|---|---|
| 2632 Concentrated-liquidity CoW AMM + rehypothecation | | mfw78: "Solver support is very, very difficult. Even with adaptors, getting solvers to support these kinds of instruments is very difficult and represents a high degree of risk that this project itself, while perhaps getting built, may remain very ineffective"; then "Given that these features would also require integration by solvers, the inertia for adoption of such a feature is quite high" |
| 2895 PolySwap v1 | | mfw78: "Getting any solver support is a very, very difficult undertaking, especially if it requires any nuanced handling." (v2 was funded after the solver dependency was designed out) |
| 3467 Polytope pre-flight SMT verification | PoC claimed | Sov: "we'd need to see solver express interest in something like this before exploring further. If a solver team confirms they'd integrate this, we're open to revisiting." |
| 3566 TDA MEV detection research | pilot with results | Sov: "The committee asked for a view from the solver side on whether this research would be useful and non-duplicative, and that interest hasn't materialised" |

### "Another SDK / another language / another bot framework"

| Thread | What | Sentence |
|---|---|---|
| 3281 R SDK | CRAN author | Sov: "DeFi tooling has largely consolidated around Python, TypeScript, and Rust... Each additional SDK also adds an ongoing maintenance burden that we need to weigh against expected usage and potential volume." mfw78 then pointed at UTM attribution in the SDK "so volume can then be attributed." |
| 3333 Hummingbot connector (retro) | | mfw78: "The mechanism and API within CoW Protocol is not designed for high frequency trading, with some endpoints being extremely costly... I would not be in favour of this grant in any form without validation of other HFT and backend API changes" |
| 3226 CCXT connector | | paid 6k of 15k; "We don't see sufficient value in pursuing alternative deliverables (e.g. publishing as a standalone npm package) to justify further funding." |
| 2789 and 2778 Ethers v6 upgrade (two individuals) | RFP responses | anxolin: "there's a very manageable number of uses of the ethers library. 64 in CoW Swap and 22 in the SDK... the migration 5 to 6 shouldn't be that hard"; bleu got it |
| 3019, 3023, 3074 i18n setup (BootNode, Protofire, bleu) | RFP responses | "No discernable differentiation between Grant proposers" (Q3 review); paused for months; BootNode built anyway and got 60% |

### "Not relevant", "misconstrues events", or plain no

| Thread | Sentence |
|---|---|
| 3394 Aegis SDK (after the $50M slippage trade) | mfw78: "CoW Swap already has this functionality... I'm closing this application as it is not relevant, and seeks to misconstrue recent events." |
| 3325 Transaction monitoring and alerts | Sov: "I don't think this is at all something we would be interested in pursuing." |
| 3434 Quantir risk layer ($35k) | Sov: "We have reviewed this internally and, at this time, we're not interested in moving forward." |
| 2956 SafeBlock cross-chain aggregator | mfw78: "we are signalling that we do not wish to entertain this grant." |
| 3106 BuildUnion grant tracking platform | Sov: "I have seen this same post pop up in a number of gov forums over the last few days, it seems you are making the rounds" |
| 3201 Helva conversational AI agent | Sov: "better suited for our Retro Round than a milestone grant... You can build, launch, track usage metrics, then apply with traction." The retro application (3210) then got no reply at all. |
| 3330 ethcontract-rs to Alloy | mfw78: "The CoW Protocol services is currently being migrated to alloy, at which point ethcontract-rs will be deprecated" |

### Approved, then cancelled or terminated

| Thread | What happened |
|---|---|
| 3224 Rust SDK (pstylez78), 8,500 xDAI | Approved Nov 2025. Jan: "Can you please provide an update". Feb: "we may have to commence action to start to cancel". April: "Despite approval over five months ago, no public repository or deliverable has been produced... No funds have been disbursed." Replaced by the collective cow-rs grant. |
| 2510 MEV Blocker verification tool (april) | 11 working days estimated, approved July 2024. Feb 2025 middleway: "The lack of communication was the main driver for the termination, together with initial assessments that were not so positive." May 2025 fleupold found the script "does not seem to find any violations" on a block with a known violation. Terminated. |
| 2843 Tycho | 50% paid after 19 months; "there's no transaction or usage evidence that it was met." |

## Counts

Of roughly 70 rejected or dead threads since 2024 (about 40 in the Rejected category plus around 30 untagged or rejected in the root category):

- Marketing, education, events, community, content: about 20. Zero funded, ever, except the 2023 Covariance widget campaign.
- Analytics dashboards and monitoring: about 10. One funded (bleu, on Dune, via RFP). Everything with its own front end lost.
- SDKs, integrations, bot frameworks without volume evidence: about 10. Zero funded except through RFPs or the committee's own collective repo.
- Security vendors and audits as a service: 4. Zero.
- Research without a solver or core sponsor: 4. Zero since 2024 (research grants were funded in 2023 when the committee was larger).
- Consumer apps built first, asked later: about 8. Zero.

Recurring phrases: "direct, measurable impact on CoW Protocol usage", "who would use it", "solver express interest", "maintenance burden", "would make more sense for this to be done by the internal team", "not something we are interested in pursuing", "please kindly open another topic". Rejections are two or three sentences, arrive within one to eight days, and are never reversed except when a core developer intervenes (crutch12, 3315).
