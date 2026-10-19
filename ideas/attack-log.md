# CoW Grants: candidate ideas and the attack log

Method: for each idea, state what it is, who would use it, what it would cost the DAO, then attack it the way the people who actually decide would. The attackers are real and quoted: Sov's "who would use it" (3612, 3619), mfw78's "a day or two of dedicated, effective time" (3569) and "golden vectors written by the core team is significantly more appropriate than having 3rd party assembled work" (3612, 3620), the services maintainers' "core team only unless labelled", and the delegates who vote on CIPs. Keep only what survives, and say what it is worth in money and in hours.

Three facts frame everything, all from October 2026:

1. The committee told a prospective applicant on 2 Oct: "the committee isn't publishing new problem areas or RFPs right now, so there isn't a specific area we can point you to... we wouldn't recommend investing in a research sprint in the expectation of a grant" (Sov, 3606).
2. On 1 Oct a brand-new account was nonetheless approved for $2,000 (satya_98402, 3569) after six weeks of visible unpaid work on exactly the thing mfw78 pointed at.
3. Thirteen other new accounts applied between May and 18 Oct. None was funded. Six were rejected within 48 hours.

So the base rate for a cold application is zero, the base rate for a six-week courtship on a maintainer-chosen target is one for one, and the prize at the end of the courtship is about $2,000.

## Scoreboard

| # | Idea | Would they pay? | Would I pay? | Verdict |
|---|---|---|---|---|
| C1 | cow-py conformance corpus and reproducible E2E (the satya shape, in Python) | Yes, about $1,500 to $2,500, after a discovery thread | Only if a real discrepancy is found first | **Survives. Do the discovery first.** |
| C2 | TWAP-for-EOAs execution quality study with open dataset | Only if anxolin or the CoW Swap product lead says so in-thread | Yes, as a product team | Runner-up, contingent |
| C3 | Merged PRs on open issues, then retro | Yes, $80 to $100 per merged PR | Yes | **Do regardless; it is the entry fee** |
| C4 | EBBO self-certificate CLI for users | No (competition-adjacent, duplicates private `ebbo`) | Maybe as a user | Killed |
| C5 | Moo & Earn affiliate program independent evaluation | No (marketing, core-owned) | As a delegate, yes; as the grants committee, no | Killed as a grant; possible as an unpaid governance post |
| C6 | Solana: SVM solver readiness, auction-data publication, SDK tooling | Not yet ("still marked experimental", no auction data) | Not yet | Killed until Q1 2027 |
| C7 | Small-order flight analysis (the 24%-of-trades bot leaving) | No (competition economics are core-only) | Yes, as the core team | Killed |
| C8 | Docs-versus-chain conformance audit of competition rules across ten chains | No as a grant; yes as issues and PRs | Yes | Folded into C3 |
| C9 | BYOS sub-solver with a strategy | Not via grants; rewards come from the auction | No, no edge | Killed |
| C10 | Hooks or CoW Shed tooling (the empty lane) | Only with a sponsor and a volume story | No | Killed |
| C11 | Agent-wallet spending policy for CoW trades (user's own `rein` / `clawshield` lineage) | No ("would need adoption", as CoW Skills) | Not without users | Killed |
| C12 | Dune-replacement public data pipeline | No; Fiberscope is ahead with a solver endorsement | No | Killed |
| C13 | Safe EIP-1271 watch tower, or any programmatic-order consumer | No sponsor; bleu's own version got silence | No | Killed |
| C14 | Any consumer app or integration without existing users | No; zero funded in two years | No | Killed |
| C15 | A second application in the solver-testing lane (conformance vectors, readiness, parity) | No; three are already queued and the doctrine is set | No | Killed |

Expected money from the surviving path over the next three months: $0 to about $2,500, for 40 to 80 hours, with the $2,000 outcome requiring a maintainer to say yes in public. The relationship is worth more than the cheque: every repeat grantee's second grant was bigger and faster than their first.

## C1. cow-py conformance corpus and reproducible E2E (survives)

**What.** A fixture corpus generated from `cowprotocol/services` (order digests, UIDs, EIP-712 signing across recovery ids, appData hashing, quote-to-order field mapping) consumed by `cowdao-grants/cow-py` tests, plus closing mfw78's own open issue #27 ("adjust E2E test to be reproducible by external contributors") and issue #75 ("ensure test for default app code"). The Python twin of the cow-rs corpus the committee approved on 1 Oct.

**Who would use it.** cow-py has 27,000+ PyPI downloads, "$18M+ in volume from 8,800 orders across six chains" (bleu, 3637). Its maintainers (bleu, 8ball030) are the reviewers. mfw78 told satya: "the services is the 'source of truth', and cow-rs would be tested against properties / invariants etc derived from services. This would be the path that I would recommend in order to arrive at a grant that is soundly scoped (and useful)" (3546).

**Attack: "The corpus already exists for cow-rs; copying it to Python is a day of work."**
True if the cow-rs fixtures are language-neutral JSON. Then the grant is not "build a corpus" but "wire cow-py to the same corpus and fix what breaks". Price that honestly at one to two days: $1,000 to $2,000. Do not pad it. mfw78 cut satya from $5,500 to $2,000 and said why.

**Attack: "Who asked for this?"**
Nobody yet. That is the whole question. The answer is a discovery thread, not an application: post in 3406 or a new technical thread what cow-py does differently from services for one concrete case, with the failing test. satya's credibility came from finding a CIP-87 text-versus-code discrepancy and reporting it before asking for money. If two weeks of checking finds no discrepancy, the honest result is "cow-py matches; here are the tests that prove it", which is a PR, not a grant.

**Attack: "cow-py is a grants-org repo maintained by bleu; the committee just paid bleu for cow-rs and told them to finish existing grants first."**
That cuts both ways. bleu is busy (BYOS, Programmatic Orders maintenance, cow-rs phase 2) and a 2-day parity job is beneath their rate. Ask bleu in the thread whether they'd review. If they say yes, the committee's usual "no reviewer, no grant" objection is gone.

**Attack: "The CloudFront WAF issue (#78) says cow-py's httpx requests get 403s; the E2E tests may not even run."**
Then issue #27 and #78 are the first two things to fix, and both are visible, mergeable work with no grant needed. Fixing them is the audition.

**Attack: "Reads as AI generated."**
mfw78's one capitals rejection was for non-idiomatic Rust submitted as a PR. The defence is the same as satya's: a failing test with a line number, self-corrections in public, a price cut without argument.

**Verdict.** Survives as the cheapest possible entry: two weeks of discovery and PRs, then, only if a discrepancy or a maintainer pull exists, a $1,000 to $2,000 proposal in the committee's template with services pinned at a commit, no cross-repo dependency, mainnet payout address, Snapshot not over a weekend.

## C2. TWAP-for-EOAs execution quality study (runner-up, contingent)

**What.** TWAP for EOAs launched 30 Sept via EIP-7702. Nobody has published what the parts actually fill at. Pull every TWAP part since launch (bleu's Programmatic Orders API indexes them; settlements are public), compute fill price versus a benchmark (time-weighted mid over the part's window, from onchain Uniswap state), part failure and expiry rates, delegation adoption by wallet, and compare EOA versus Safe TWAPs. Publish dataset, code, and a short report. Cost: 3,000 to 4,000 xDAI, four weeks.

**Who would use it.** The CoW Swap product team that just shipped it; marketing (they publish monthly numbers); bleu, whose indexer the study exercises; mfw78, whose Shepherd just posted its first 28-part TWAP from a 7702 account (3288).

**Attack: "Research that may not translate into numbers."**
CIP-82 says exactly that research "may not translate into immediate numbers" and the committee has funded zero unsponsored research since 2023. The TDA study (3566) had a pilot result and died in three weeks of silence from the solver side.

**Attack: "Who asked?"**
Nobody. anxolin volunteered as reviewer for the Programmatic Orders API because the frontend needed it. He has not said he needs a quality study. Without his or a product lead's sentence in the thread this is C15 with a different noun.

**Attack: "Dune is paid-only now; what does the pipeline cost?"**
Nothing if built on public RPC and the S3 auction bucket. That is a strength: it is reproducible by the committee, which is how Tycho's and PolySwap's reviews ended.

**Attack: "If the result is bad for TWAP, will they want it published?"**
The DAO's own pattern says yes (Mr_Robot's negative ring result got thanks and data pointers), but the grants committee funds things that help the product ship, not things that audit it. Pre-register it anyway; the honest version is the only one worth paying for.

**Verdict.** Runner-up. Worth a one-paragraph question to anxolin in the Programmatic Orders thread ("would a fill-quality report on EOA TWAP parts be useful to you, and would you review it?"). If the answer is yes, this is the best $3k idea on the board. If silence, drop it.

## C3. Merged PRs on open issues, then retro (do regardless)

**What.** Pick from: cow-py #27, #75, #78; docs issues that are factual, not stylistic (Ink baseline #653 needs core to state the list, so comment and wait; the "Flow of an order" page is outdated, #605; hooks rules in solver docs, #530); the one `help wanted` in services (#2394, remove feature gates for verified quotes, 100 DAI, open since 2024 with 9 comments: read them before touching it); kaisersolver's finding that Plasma's settlement deadline in the data is 10 to 11 blocks against 5 in the docs (ask the solver team to confirm, then PR the docs). Then, after five or more merges, a retro application like dinesh's.

**Who pays.** 100 DAI per merged help-wanted PR (CONTRIBUTING.md); about $80 per merged PR under retro (3321, 15 PRs for 1,200 xDAI, approved within a week).

**Attack: "That is not a grant idea."**
Correct. It is the only thing that has worked for every funded newcomer: dinesh (PRs first), crutch12 (a PR and a core dev's word), CoBuilders (a working demo in the first post), kaisersolver (docs PR #652 merged before asking for anything), satya (a failing test before a proposal).

**Attack: "External PRs may sit for several weeks."**
Yes. Budget for it and ping once a week at most, as the rules say.

**Verdict.** Do it. Thirty hours, $0 to $500, and the account history that every 2026 rejection letter was implicitly about.

## C4. EBBO self-certificate CLI (killed)

**What.** felixhenneke's process for an EBBO claim (3274): the user must show a better onchain route on every block between auction start and settlement. A CLI that takes an order UID and produces that certificate (Uniswap v2/v3, Balancer, Curve quotes per block from an archive node) would save the solver team the hand investigation they did in November and let users file real claims.

**Attack.** It is third-party reference tooling for the competition; mfw78's 13 Oct doctrine applies word for word. CoW already has `cowprotocol/ebbo` (Python) internally. The November claim was not a violation, which suggests the demand is small. Needs an archive node, which the committee has flagged as a cost before. Killed. If it ever exists, it should be a PR to `ebbo`, not a grant.

## C5. Moo & Earn independent evaluation (killed as a grant)

**What.** The affiliate program's mandate expired 2 Oct; the core team is "reviewing the program's results to decide whether to propose an extension"; a delegate (karolak) is already asking to "see the results of the latest 6 months fee execution trial". Affiliate codes are in order appData, which is public, so an outsider can measure referred volume, affiliate concentration, cannibalisation (returning wallets tagged as referred) and cost per incremental dollar.

**Attack.** It is marketing-adjacent and core-owned; the committee has rejected every marketing-analytics ask since 2023 and the marketing team answered Alphaday with "doesn't make sense for us to pursue". The audience that would value it is delegates, who do not control grant money. Killed as a grant. As an unpaid, pre-registered forum post before the renewal CIP, it is the single highest-visibility thing an unknown analyst could publish this quarter, and visibility is what the grants path lacks. Treat as reputation, not revenue.

## C6. Solana (killed until data exists)

The core team's MVP is "by October" with no explicit solver incentives and a solver budget that kaisersolver computed at "$3k to 17k a month... shared across every solver on the chain". The SDK is experimental and the committee "isn't looking to fund wrapper tooling around it at this stage" (3603). There is no published SVM auction data to replay, which is why kaisersolver gated their own Solana readiness item on CoW publishing it (3624). Anything here is premature until Q1 2027. Watch the launch thread; the first useful outside contribution will be measurement once data exists, and the person who already measures Solana transactions is well placed for that, but not yet.

## C7. Small-order flight analysis (killed)

Trade count halved in August; a bot operator claims 24% of trades and is leaving over fees; Fractal showed negative expected profit for solvers under $10k. A public analysis of order-size mix, fee burden and solver margin by bucket would be genuinely useful. It is also exactly the "quote reward dynamics" class that got apsarthsumit's cheap, honest, AI-disclosed proposal killed the day after posting. Killed. The core team has the data and the mandate (CIP-88, fee-policy draft) and has said it does not want outside reference work here.

## C8. Competition-rules docs audit (folded into C3)

kaisersolver found deadline discrepancies; KaiserSnipes found the Ink baseline gap; the "Flow of an order" page is marked outdated. A systematic docs-versus-code-versus-chain pass across ten chains is real work. The committee closed docs to grants in June ("a core-team-owned function", 3464). File issues, submit PRs where the facts are settled, count them toward C3.

## C9. BYOS sub-solver (killed)

The one lane the committee's flagship grant is actively recruiting for (3476: bleu is "prospecting potential subsolvers"). Rewards come from winning auctions, not grants. Mr_Robot and kaisersolver have shown there is no free matching surface; winning needs private liquidity or a routing edge. Without one, a sub-solver is a cost centre. Killed for this applicant.

## C10. Hooks and CoW Shed (killed)

Empty lane, no applications this year, bleu's home turf. A hook dApp needs users to have volume, and the committee funds hooks work when a core dev wants the pattern (anxolin on authenticated hooks, 2408). No sponsor, no volume story, no product. Killed.

## C11. Agent spending policy for CoW trades (killed)

The user's `rein` and `clawshield` repos are agent accounts with spending limits. MetaMask's Agent Wallet already routes through CoW; middleway.eth once asked for "clear sign for CoW Swap orders" and Zodiac-roles delegated trading (2715) but left the committee. CoW Skills, from the incumbent, was refused with "I don't think skills like this would be something we would fund unless it was clear we'd see enough adoption to justify" (3402). Same answer here. Killed, unless an agent product with real trade volume exists first, in which case it is a volume conversation, not a grant.

## C12. Dune replacement (killed)

Fiberscope (3619) has a live product, a solver endorsement within 24 hours, and a 14k ask. The committee's question to them was "who would use it beyond Fibrous". Entering behind them with less is pointless.

## C13 and C14. Programmatic-order consumers and consumer apps (killed)

bleu's PoC-backed Safe watch tower (3383) has had no committee reply in seven months. Consumer apps built first and asked later (33Jane, Quantir, CoW Convert, Polytope, Aegis) are zero for five in 2026; "thanks for building a working demo before applying" precedes the rejection every time.

## C15. Another solver-testing proposal (killed)

Six threads since August; one funded at $2k on the SDK side; three pending; two rejected. The doctrine is now explicit and pasted verbatim into two threads on the same day. Do not be the seventh.

## If you still want the cheque: the exact sequence

1. Week 1 to 2: fix cow-py #27 and #78 (or confirm they are already fixed and say so), run cow-py against the cow-rs corpus, write down one concrete divergence or one concrete "matches". Open a technical thread with the result. Separately, ask anxolin one question in 3346 about C2.
2. Week 3: if a maintainer or bleu replies with interest, post the application in the current template: title "Grant Application - ...", two milestones, $1,000 each, services pinned to a commit, no upstream dependency, LGPL/MIT/GPL, Ethereum mainnet address, the T&C line with links, the "note to committee" line. If nobody replies in two weeks, "lack of response signals disinterest" (process guide) and the work is still a merged PR.
3. Snapshot on a Monday, three-day vote, 0.0005 xDAI on Gnosis for the proposal; expect Sov's onboarding message, a 7-to-14-day review SLA, payment by the 15th of the month after the milestone.
4. Never: an upfront payment ask, a single $20k milestone, a hackmd instead of forum text, a Gnosis address, a weekend vote, a proposal that touches scores, fees, quotes or rewards.
