# CoW DAO Grants Program: rules, numbers, and how the committee actually decides

Source: 24 forum threads (templates, process guide, agreement terms, committee reviews, retro round, RFPs), fetched 2026-10-19. Thread ids in brackets; https://forum.cow.fi/t/<id> opens each one. Where a digest is truncated (the Grant Agreement body [2752], the H1 review after section 5 [3115], the Q3 review after "Process Improvements" [3208]) this is noted; nothing is inferred beyond what the digests contain.

---

## 1. Application template and process rules

### 1.1 Template fields (verbatim headings) [2768]
Posted by @c3rnst 2025-01-20 ("Template: Grant Application"). Headings, in order:

1. **Grant Title** - "Grant Application - [+Title]" ... "using a new thread"
2. **Author(s)** - "names, usernames or GitHub usernames of the author(s) or main point of contact"
3. **Experiences and qualifications: (optional or keep it short)** - "Feel free to include prior team work/ projects that you did as the applying team."
4. **Grant Description:** - "purpose, objectives, and intended outcomes; you can cover the grant category ... potential impact it will have on the CoW Protocol ecosystem"
5. **Type of Grant:** - "Is this a milestones based or a time-based grant. If it does not fit into either category, specify the hybrid or precisely other type."
6. **Milestones:** - table with columns `Milestones | Title | Due date (*) | Funding request`; "(*) Or e.g. weeks after acceptance; or a meaningful and concrete specification". Then **Specifics: Milestone 1** ("Please break down the funding request by milestone.")
7. **Scope of Work (for time-based)** - units of Hours / Days / Months; "include a meaningful and concrete funding request, which includes rough monthly estimates based on expected time spent (side note: this is relevant for the accounting)."
8. **Length** - "A grant should not exceed 6 months (and needs to be renewed with a new application). You may apply for a length exception with reason." Commencement date defaults to "the successful passing of the proposal on Snapshot".
9. **Funding Request:** - "amounts in xDAI and COW tokens, if applicable". For time-based: "(i) indicate an estimate ... + (ii) indicate a total CAP (max. funding that will be requested as part of this grant, so that the Committee does not sign a 'blank cheque')".
10. **Gnosis Chain Address (to receive the grant)** - "one Gnosis Chain wallet address ... ideally the same as the Snapshot submission account".
11. **Other Information (optional or keep it short)**
12. **Terms and Conditions** - mandatory line: "By submitting this grant application, I acknowledge and agree to be bound by the CoW DAO Participation Agreement and the CoW DAO Grant Agreement Terms."
13. **INCLUDE NOTE TO COMMITTEE:** "Please notify the Grantee of their reviewer and their steward in the thread and latest upon successful approval of the Grant on Snapshot."

### 1.2 Process Guide (Feb 2025) rules [2830]
- **Milestones**: "Measurable goals with clear deadlines (milestones must be delivered in order)." "Each milestone is funded separately. Even if the final milestone is not reached, completed milestones can be paid." "If project completion is critical, allocate more funding to the final milestone or add 'completion funding.'"
- **Duration**: "Grants should not exceed six months unless justified and explicitly highlighted."
- **Budget/payment timing**: "Payments are typically post-milestone unless justified for upfront funding (and explicitly highlighted)."
- **Team Background**: "Relevant experience and expertise (exclude referrals)."
- **Review period**: "The Grants Committee reviews applications (typically within two weeks). Lack of response signals disinterest, but ideally, a committee member responds within two weeks."
- **Steward/Reviewer**: Committee assigns a Steward (committee member) who validates milestones/funding "obtaining expert input from the Reviewer" and must "Assign a Reviewer before Snapshot voting". **"If no Reviewer is assigned, the proposal is unlikely to pass."**
- **Discussion period / Snapshot**: "There is no required forum review period, but proposals should allow time for feedback." Snapshot is "the only official Grants DAO governance response mechanism". Spam protection: 0.0005 xDAI on Gnosis Chain. "Snapshot Voting Period: Three days (avoid weekends or holidays)". Snapshot proposal must contain: IPFS link to the Grant Agreement ("serves as signing equivalent"), final application text, forum link. Best practice: mark forum post "Moved to Snapshot".
- **Deliverable review & payment**: "Milestones must be reviewed before payouts." Grantees request reviews/payments in the forum thread tagging Steward/Reviewer. "Once approved, the milestone is included in the next end-of-month payout cycle (typically by the 15th of the next month)." "The Grants Committee has a 30-day payment term". "Payments are in xDAI or COW tokens (converted if needed) and only on Gnosis Chain." "GRANTEES MAY SUBMIT AN INVOICE (new from April 2025)". Time-based grants "Paid based on worked hours ... subject to Reviewer approval".
- **Communication**: "Official communication must be in the forum thread of the original application."
- **Scope changes**: Minor (no vote): "Small deadline extensions, budget shifts within milestones, minor deliverable clarifications, and partial payouts". Major (Snapshot vote): "Budget increases, significant scope changes, extensions beyond six months, changes to payment structure, or grantee reassignment". "New milestones or continuations, renewals or similar shall always be seen as a stand-alone new grant application".
- **Termination**: by grantee, 30-day forum notice; by committee via Snapshot, "typically 30-day notice, but immediate in urgent cases"; immediate reasons include "Misuse of funds, harmful actions agai[nst...]" (digest truncated).
- **KYC**: not mentioned in template or guide. The only evidence is Aragon's later remark that "KYC and signing requirements ... took 1 week longer than expected ... a vote would go up after then followed by contract and legal document agreements" [3328]. So KYC/contract signing does happen post-Snapshot for larger RFP engagements.
- **Payment currency drift**: 2025 guide says xDAI/COW on Gnosis only [2830]; by 2026 RFPs say "Payments are made in stablecoins (USDC, DAI, or USDS) on Ethereum mainnet" [3328, 3481], and translation payouts were "in DAI ... on Ethereum mainnet" [3481]. Chainza gave an "Ethereum mainnet only" address in June 2026 [3469].

### 1.3 What the committee calls good/bad
- Good (RFP template "Values", see §2) plus selection language: "The committee will consider the above values, cost, timing, quality, and scope" [2816, 3217-3219]. Translation RFP: "Best value wins, not lowest cost." [3481]
- Bad: H1 denials were for applications that "either didn't meet quality standards or failed to meet eligibility criteria" [3115]. i18n RFP paused for "No discernable differentiation between Grant proposers" [3208]. Retro guidance explicitly excludes "marketing materials" [3128].
- "Currently, there are no official rejection criteria. If the forum discussion does not provide a clear outcome, an applicant can post their proposal to the Grants DAO Snapshot space and request a committee vote if needed." [2816, 2993, 3217-3219]

---

## 2. Grants DAO Values (verbatim) [2816; repeated in 3217, 3218, 3219]
"These values may evolve and are listed in no particular order:
- **Open Source**: Integrations should be open source.
- **Milestones**: Milestones should be attainable and well-defined to ensure easy verification of completion.
- **Price Transparency**: Pricing should be broken down into optional and core metrics/deliverables to allow selective implementation.
- **Sustainability**: Address the sustainability of deliverables (e.g., who will manage, maintain, and for how long, including associated costs).
- **Simplicity**: Aim for simplicity. Completion is often more valuable than striving for perfection—except for critical components, which must meet the highest standards.
- **Documentation**: Provide solid documentation to ensure that others can build on your work smoothly, where applicable.
- **Flexibility**: We recognize that some processes require flexibility ... Open communication is encouraged to adapt to these changes. Scope extensions and pricing changes typically require a committee vote."

RFP template also says: "Note: Funding is left open on purpose, to avoid anchoring a proposal." and "The selection will be made by the Grants DAO committee at their discretion ... Committee members may ask questions or make a decision independently. The committee can also decide to close or extend the timeline or go with none of the submitted proposals." [2816]

---

## 3. Grant Agreement key terms [2752]
Version "Last Updated: February 2025 (Version passed with CIP-63)"; passed via Snapshot CIP, pinned to IPFS 2025-02-21 (bafkreifcftgale...). The digest truncates the body at the definitions, so the following is what is in the digest:
- **Who signs**: "By submitting a Grant Proposal to Snapshot, the Grant Recipient acknowledges and agrees to be bound by this Agreement, and additionally by the CoW DAO Participation Agreement." CoW DAO is represented by Gnosis Chain address 0xcA771eda...; grants paid from Grants Program safe 0xCA1F000D520c21C47E6c634DD31b92b91A6338bD. Hierarchy: Participation Agreement > Snapshot-approved grant > this Agreement ("the terms of the Snapshot-approved grant will prevail").
- **Proposal minimum content**: authors/project/objectives, grant type, milestones+timelines (milestone grants) or scope/time (time-based), budget split by milestone, Gnosis Chain address matching Snapshot signer.
- **Duration (11.1)**: "Except where otherwise specified, a Grant Period should never exceed six (6) months which, if needed, is to be actively renewed". Kowrigan proposed an up-to-1-year clause for "(i) Integration Grants based on volume ... (ii) ... critical infrastructure ... (iii) any other Grant ... in the Grants Committee's sole discretion"; then concluded "Except where otherwise specified" already gives the latitude.
- **IP / open source (para 8)**: "Software or copyrightable work developed as part of a project conducted under a Milestone-Based Grant must be licensed under GNU LESSER GENERAL PUBLIC LICENSE Version 3 (or later), MIT LAB/Apache 2.0 Licenses, or another suitable open-source license approved by CoW DAO". c3rnst asked whether the committee can override the licence; Kowrigan: "With the current wording, no. The license is in the hands of CoW DAO"; c3rnst: "I think it's good to keep it only it the hands of CoW DAO". Confidential Information clause defined.
- **Termination (11.3 / mutual)**: "a Grant can always be terminated early by mutual agreement. For such termination, the Grant Recipient must submit a Snapshot vote detailing the Termination suggestion (termination date, final payment requested), subject to successful approval by the Grant Committee."
- **Eligibility (sanctions / US persons)**: recipients must declare they "Are not a United States citizen, permanent resident alien, entity organized under United States law, or any person in the United States" and are not sanctioned. netrunner.eth challenged; Kowrigan: sanctions clause stays ("would do more harm to the DAO than the missed opportunity"); the US clause "is historical" and "could allow to delete".
- **Payment terms** (as restated in 2026 RFPs [3328, 3481]): "Payments are made in stablecoins (USDC, DAI, or USDS) on Ethereum mainnet"; "Grant recipients are independent of CoW DAO (not employees, agents, or partners)"; "All deliverables must be open source under approved licenses"; "Standard payment terms are 30 days after milestone completion".
- **Clawback / taxes**: not present in the digest text. Practical clawback behaviour is evidenced instead by the CCXT case: grant value reduced and remainder "terminated" while prior payment "stands" [3226].

---

## 4. H1 2025 and Q3 2025 reviews

### 4.1 H1 2025 Review (written by @mfw78, posted by @Sov 2025-07-23) [3115]
Numbers (committee says "Application numbers to be confirmed"):
- "~22 applications received in H1"
- "~6 applications denied - either didn't meet quality standards or failed to meet eligibility criteria for funding"
- "~7 in active evaluation"
- "~6 progressed to funding"
- "~4 applications stalled since April - identified bottleneck requiring process improvement"
- Committee: 3 of 8 left (sohkai, netrunner.eth, fairlight "Removed during committee renewal"). 6 applicants for 2 seats, 4 interviewed (@Sov selected; @MasterMojo, @shivani, @sharkonomics "Strong candidate, not selected"). "Made strategic decision to fill only 1 position, maintaining high standards".
- Committee after H1: @mfw78 (Technical lead), @Chim9 (steward, payments), @middleway.eth, @Kubesqrt, @Master_CoW (Core Team, strategic alignment), @Sov (retro framework lead). @c3rnst = non-committee core team support.
- Safe: 4/6 multisig at 0xCA1F000D...; "Some transactions taking 7+ days for sufficient signatures".
Named grants: "CoW SDK Upgrade - Bleu selected as implementer"; "Data Pipeline for Solver Team"; "CoWAMM Trade Envy Analysis - Completed by tommel"; "ZeroMEV Infrastructure Maintenance - Ongoing support"; "Dune Governance Dashboard"; "Manipulation-Resilient Price Oracle".
Stated lessons/deficiencies: "Technical review has historically been a deficiency"; "Grant Termination Process: Need for clearer framework on ending non-performing grants"; "Communication Gaps: Need for improved SLAs on application processing"; "Ad-hoc external reviews without standardized framework". Priorities for H2: Discord/Discourse automation, "Technical Review Framework", "Improving Intake Process", "Establishing Retro-funding Model", KPI framework. No dollar budget figures appear in the H1 digest.

### 4.2 Q3 2025 Review (@mfw78, 2025-10-03) [3208]
- Kubesqrt stepped down 2025-08-05; committee = mfw78, Chim9, middleway.eth, Master_CoW, Sov. @NotSoFormal = core-team liaison. Safe 4/6 -> 3/5 (2025-09-16) "significantly reducing signing burden".
- **Python SDK (cow-py) - COMPLETED**: "Bleu ($6K), 8baller ($2K), bh2smith ($1K review)"; "Final allocation of $9K (increased from initial $5K due to scope expansion)"; "First community-built SDK with minimal grants committee oversight"; "Already generating significant order flow volume".
- **Framework Agnostic SDK - COMPLETED** (Bleu): xDAI + COW vesting paid Sept 2025; "now actively integrated and used within CoW Swap itself".
- **Data Pipeline for CoWAMM Pools - COMPLETED** (Tommel), paid July 2025.
- **ZeroMEV Infrastructure Maintenance - CONCLUDED**: last monthly payment August 2025; "Some remaining vested COW tokens still pending".
- **i18n RFP - PAUSED**: "Three submissions (Bootnode, Protofire, Bleu)"; "Key issues: No discernable differentiation between Grant proposers"; "Process paused for 1-2 months pending improved submissions"; "Bootnode proceeded with work at their own risk despite no committee approval".
- Finances: "Safe Holdings: Approximately 300K xDAI"; monthly payments = committee stipend + grants (July: ZeroMEV, data pipeline, Python SDK; Aug: final ZeroMEV; Sept: Framework-agnostic SDK). "Budget Efficiency: Maintained disciplined approach to grant allocation".
- Priorities / RFP pipeline: Governance Dashboard Enhancement (Dune, time-based selectors), CoW Playground Formalization, Backend Diagnostics Tools ("Under evaluation due to security considerations"). "@Sov and @NotSoFormal leading RFP ideation with input from core team priorities". Retro philosophy: "demonstrated impact rather than upfront promises".
- Reply to @vegayp asking for project links: Sov: "All of them have submitted proposals and are tracked here in the forum under the grants section."

### 4.3 Fund more / fund less (across both)
- More: core-team-sourced RFPs, SDKs/dev tooling that is "used within CoW Swap itself", retro rewards for shipped work [3208, 3128].
- Less: undifferentiated competing proposals (i18n paused) [3208]; "Not marketing materials" [3128]; later, nothing at all: "the committee isn't publishing new problem areas or RFPs right now" (Oct 2026) [3606].

---

## 5. Retro round

### 5.1 Rules [3128, 3164]
- Proposed 2025-07-30 by @Sov; opened 2025-08-18. Build period Aug-Nov 2025 (later "Now through the end of the year"), evaluation "January 2026". Five focus areas: Solver Infrastructure ("rather than specific solver implementations"), Developer Tools, MEV Protection Research, AI Agent Infrastructure (MCP servers, bot frameworks), User Experience & Education ("Not marketing materials").
- "Awards start at a minimum of 5,000 xDAI plus 5,000 vested COW tokens for approved contributions, scaling up based on impact and quality." No separate budget: "There is not a separate budget for this program ... we will use the already approved budget for the grants council" (Sov).
- Title "[RETRO ROUND] Your Project Name", standard template, "If you're responding to an existing RFP, → Use the traditional grant process with milestones. If you have an original idea → Submit to the retro round."
- Evidence must be verifiable: "publicly verifiable data sources where possible (GitHub commits, research papers, deployments etc)". External reviewer = an unsuccessful committee applicant "we were impressed by their technical ability" plus core team.
- Candid framing of demand: "our challenge traditionally has not been an abundance of applications but a lack thereof"; "right now more of the worry is driving quality applications". Builders may state "their preferred terms of payment".

### 5.2 Applicants and outcomes
- **Bleu - Solver Infrastructure Onboarding** [3197]: Python solver template + Python Baseline. mfw78 (8 days later): "at the moment CoW Protocol leads the pack in terms of number of solvers, and the auction performance appears to be relatively robust ... there is some impact, though it is likely to be low and not necessarily easily measurable." Steered toward liquidity abstraction for solvers. Bleu declined that pivot ("struggling to see how this would differentiate from what Tycho has already built"), delivered PR #37 on 2025-12-15. As of 2026-04-03 mfw78 was still asking core devs (@felixhenneke/@harisang/@solver_cow) for a review "as to what the efficacy is like". **No payment recorded in digest.**
- **Helva conversational AI agent** [3210] (@gicappaemme): asked for "marketing and business development" support and co-marketing. **No committee reply in the digest.** Not tagged grant-funded.
- **CCXT connector** [3128 post 9, 3226] (@tantodefi, @bhavya_gor): asked 15,000 xDAI + 15,000 vested COW. Passed Snapshot (tag 'grant-funded'). Dec 2025 requested per-milestone payment of 10,000 xDAI + 5,000 COW; mfw78 required a reviewable repo "with specific review instructions on how to run tests / prove out code coverage ... verify against CoW Protocol's openapi.yaml". mfw78 on an off-forum update: "Please post this to the forum as an external link can be changed post-facto and we don't have records." Feb 2026 decision: "The total value of the grant shall be reduced so as to be $12,000 + 15000 COW. To make payment in light of the current work completed of $6,000. The remaining $6,000 in stablecoins + 15000 COW is conditional upon upstreamining into the CCXT repository." After CCXT maintainer demanded $40k: "the committee has decided to close this grant as partially completed, with the remainder terminated ... The initial $6,000 payment for completed work stands ... We don't see sufficient value in pursuing alternative deliverables (e.g. publishing as a standalone npm package) to justify further funding." Lesson: "when a deliverable hinges on a third party merging a PR, we need to either flag that as a significant risk upfront or define an alternative completion path".
- **Hummingbot Gateway connector** [3333] (same team, 10,000 xDAI + 20,000 COW): refused. mfw78: "I don't think the value proposition for a HummingBot integration is well defined. The mechanism and API within CoW Protocol is not designed for high frequency trading, with some endpoints being extremely costly. Given the previous CCXT connector integration (which has stalled in upstream), and the lack of any validation for a net benefit to CoW Protocol from such a trading integration, I signal that I would not be in favour of this grant in any form without validation of other HFT and backend API changes that would facilitate such." Applicant withdrew the same day.

---

## 6. Scope Check [3606] and Contributor Introduction [3609] (Oct 2026)
**@naina asked** (2026-10-02), after a rejected Solana client-tooling idea, whether to self-fund a research sprint under CIP-82 priorities (developer onboarding, strategic ecosystem alignment, novel applications, integrations with measurable usage), and specifically: which 1-2 areas need external problem discovery; whether unsolicited applications are still welcome or builders should wait for RFPs; whether the Volume-Based Integration Program is open; whether next step should be RFC/prototype/application; any no-go areas.

**@Sov answered the same day, in full:** "Hi @naina, thanks for checking. The Volume-Based Integration RFP closed to applications on 30 September 2025 (RFP: Volume-Based Integration), and the committee isn't publishing new problem areas or RFPs right now, so there isn't a specific area we can point you to. CIP-82 and the application template remain the public reference for anything submitted, but we wouldn't recommend investing in a research sprint in the expectation of a grant."

No reply from mfw78, Chim9 or Master_CoW in either thread. [3609] (2026-10-05, "not requesting funding", asking for a maintainer-selected task in cloud ops/security/testing/monitoring) has **zero replies** in the digest.

---

## 7. RFPs: ask, budget, status, winner, quality comments
| RFP | Ask | Budget | Status / winner | Committee comments |
|---|---|---|---|---|
| Committee selection [2849] (Chim9, 2025-02-21) | up to 2 members; 500-word app; interviews; Snapshot | CIP-63 stipends | Complete. 6 applied, 4 interviewed, 1 hired (@Sov) | "Made strategic decision to fill only 1 position, maintaining high standards" [3115] |
| Volume-Based Integration [2993/2992] (Chim9, 2025-05-05) | integrations driving volume; appID required; new integrators only | 5k COW @ $1M; 30k @ $25M; 75k @ +$100M; 150k @ +$250M; 12-mo vesting; stablecoin/ETH-ETH/BTC-BTC swaps excluded | Closed 2025-09-30 [3606]. No winners named in digests | notsoformal vs "incentives quite low": "still significant in USD terms"; partner fees on top |
| Playground Block Explorer [3217] (mfw78, 2025-10-20) | local explorer, verification, debugging; deadline 2025-11-17 | open | Filled: CoBuilders Otterscan grant "approved by the CoW grants committee" 2025-12-05, M3 done 2026-02-28 [3360] | "Thanks to all that applied ... anticipated responses by 28th of November" |
| Playground Performance Testing [3218] | load generation, Prometheus/Grafana | open | Bleu applied; outcome not in digest | same |
| Playground Offline Mode [3219] | self-contained chain, DEX liquidity | open | RomThpt (M1 alone $20,000) and Bleu applied; outcome not in digest | same |
| Value Distribution Mechanism [3328] (Chim9, 2026-01-06) | research report 40% / design 50% / comms 10%; >=10 benchmarks; Notion form | open; stablecoins on mainnet | Complete. 6 applications, 3 interviewed, **Aragon** selected 2026-02-20; Snapshot 03-02; delivered 05-05; final payment 05-11 | "Aragon's ability to carry this work from design through to implementation ... transparent about tradeoffs ... committed to open-sourcing all deliverables." Applications list published "to maintain complete transparency" |
| Integration Documentation RFC [3360] (Sov, 2026-02-05) | Track A (RAG/AI) or Track B (long-form), order creation/approvals/errors/endpoint selection | open | **Closed, no grant** (Chim9 2026-05-25): "decided not to move forward with an external grant for this RFC". Applicants: mig (live RAG MVP), Woof, BootNode, CoBuilders, Bleu (live Mintlify rebuild, self-paid $250/mo) | "We were impressed by the caliber of the submissions ... The Core Team will be taking these insights and incorporating them directly into their internal roadmap" |
| Bring Your Own Solver [3469] (Chim9, 2026-06-10) | bonded meta-solver, Trampoline, escrow, proposal API; grantee operates it after | open | **Bleu** won 2026-07-02 over Chainza; Snapshot passed 2026-07-13 | "Thank you to both @chainza and @bleu for your excellent submissions ... it was a very strong application, and we hope to see you apply for future grants!" |
| UI Translation [3481] (Sov, 2026-07-01) | ES/PT-BR/RU/FR, ~8,800 words/~1,500 strings, Crowdin, maintenance | per-language; bids 748-1,500 USD; "Best value wins, not lowest cost" | **Complete**: @aspnxdd123 (ES, 900 USDC, applied one day late), @flaviampsilva (PT-BR, 1,000), @just2102 (RU, had already PR'd a RU locale fix), @armand (FR, 950). Bleu lost PT-BR. Paid in DAI on mainnet 2026-10-07 | "We received so many excellent submissions that making the final selection was difficult"; Greek applicant thanked but out of scope |

---

## 8. How the committee actually decides (evidenced patterns)
1. **RFP responses dominate funding; unsolicited ideas rarely get paid.** Every 2026 grant evidenced as paid came from an RFP (Aragon [3328], Bleu BYOS [3469], four translators [3481], CoBuilders explorer [3217->3360]). Unsolicited retro submissions were steered (Bleu solver [3197]), ignored (Helva [3210]), or refused (Hummingbot [3333]). Sov to a prospective applicant: "we wouldn't recommend investing in a research sprint in the expectation of a grant" [3606].
2. **Known contributors win.** Bleu: "more than a dozen grants with CoW over the past three years" [3360], won BYOS [3469], SDK work [3208]. 8baller/bh2smith paid on cow-py [3208]. just2102 won RU having already submitted a frontend PR [3481]. Counter-example: Bleu lost PT-BR to a professional translator, so track record is not decisive when the RFP has a native-speaker reviewer scoring samples [3481].
3. **Impact must be measurable and protocol-relevant; marketing asks are a red flag.** Retro: "Not marketing materials" [3128]; Helva's request for co-marketing got no reply [3210]; mfw78 on solver onboarding: "likely to be low and not necessarily easily measurable" [3197]; on Hummingbot: "lack of any validation for a net benefit to CoW Protocol" [3333].
4. **Technical lead (mfw78) gates payment and can veto in one post.** He demands runnable review instructions and openapi compatibility before paying [3128], reduces grants on reviewer concerns [3226], and his "I signal that I would not be in favour of this grant in any form" ended Hummingbot [3333]. Process guide: "If no Reviewer is assigned, the proposal is unlikely to pass" [2830].
5. **Core team alignment is decisive.** The docs RFC was closed despite "caliber" submissions because the Core Team absorbed it [3360]; RFPs are generated "based on Core Team feedback" via @NotSoFormal [3208]; Aragon's work was gated on "members of the CoW Swap team" review [3328].
6. **Size sweet spot: small.** cow-py $5K->$9K [3208]; CCXT cut from $15K to $12K [3226]; translations ~$900-1,000 per language [3481]; retro floor 5,000 xDAI + 5,000 COW [3128]; a $20K single milestone (RomThpt) has no recorded follow-up [3219]. Safe was ~300K xDAI [3208]. Value-distribution and BYOS amounts are not disclosed in digests.
7. **Dependency on third parties is now treated as a risk to be flagged upfront** [3226]. Open-source only; licence not negotiable by committee [2752].
8. **Timelines.** Forum reply target "within two weeks" [2830]; RFP decisions ~2-6 weeks after close (BYOS: close 06-26 -> decision 07-02 [3469]; VDM: 01-20 -> 02-20 [3328]; translation: 07-15 -> 07-28 [3481]; docs RFC: 03-13 last app -> 05-25 closure [3360]). Payments lag: translation approval 09-29 -> paid 10-07 "We apologize for the delay" [3481]; retro reviews can sit 3+ months (Bleu PR Dec 2025, still unreviewed Apr 2026 [3197]).
9. **Who replies first.** Process/announcement and RFP close-outs: Chim9 or Sov [3469, 3481, 3360, 3328, 3606]. Technical judgment, payment conditions, rejections: mfw78 [3197, 3226, 3333, 3128]. Master_CoW and middleway.eth do not post in any digest except middleway on the T&Cs [2752].
10. **Typical rejection wording** is polite, final, and offers no appeal: "the committee has decided to move forward with @bleu ... we hope to see you apply for future grants!" [3469]; "has decided not to move forward with an external grant for this RFC and will be closing the initiative" [3360]; "close this grant as partially completed, with the remainder terminated ... The blocker here is entirely external and not a reflection on the quality of work" [3226]; "there isn't a specific area we can point you to" [3606]. Silence is also a formal answer: "Lack of response signals disinterest" [2830].
11. **Procedural hard rules**: everything official in the forum thread, not external links ("an external link can be changed post-facto and we don't have records" [3226]); Snapshot vote required for any award, scope increase or termination [2830]; one wallet, matching the Snapshot signer [2768]; 6-month cap [2752].
12. **Current stance (Oct 2026)**: no open RFPs, no published priorities, Volume program closed; "CIP-82 and the application template remain the public reference" [3606]. Community-offered free contributions [3609] got no response.
