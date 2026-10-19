# State of CoW Protocol and CoW DAO, October 2026

What the protocol, the core team, the solvers and the treasury are doing right now, from the DAO's own threads (monthly recaps, CIPs, technical posts, treasury reports), the public GitHub repos and the docs. Thread ids open at `https://forum.cow.fi/t/<id>`. Read this before judging any idea: most ideas die on something in here.

## Numbers

| | July 2026 | Aug 2026 | Sept 2026 |
|---|---|---|---|
| Monthly volume | $2.5B | $2.88B | $3.5B |
| Monthly trades | 691,978 | 353,601 | 612,679 |
| Active wallets | 111.5k | 70.6k | 110.2k |
| Aggregator market share (all supported chains) | 14.5% | 15.1% | 16.1%, #3 |
| Cumulative volume | $208.5B | $211.6B | $216.4B |

Source: recaps 3527, 3550, 3610. Note the trade count halved in August and recovered in September. A trading-bot operator ("Chase", thread 3577, 27 Sept) says their bots were "a little over 24% of all trades on CowSwap in the past 30 days" and are migrating away because of protocol fees. Small-order economics are a live problem (see solver section).

Revenue since 2024: "$41.9M across products like CoW Swap and MEV Blocker" (core team, 3454, May 2026). Treasury under KPK management: $22.0M actively managed at end-June 2026, $26.5M in scope, mandate targets two years of operating runway in stablecoins (3533). 2026 outflows include CIP-82 grants (about 140k DAI in H1), CIP-79 dev services (6.3M USDC), CIP-83 core team COW replenishment (25M COW), CIP-86 DNS-hijack reimbursements.

## What shipped in 2026

- TWAP orders for EOAs (30 Sept), via EIP-7702 delegation; discovery layer is bleu's grant-funded Programmatic Orders API (3346, 3637). Partial approvals on every order type. Telegram trade notifications.
- Cross-chain swaps to and from Bitcoin (July). Safe{Mobile} via WalletConnect. PQ1 hardware wallet clear-signing.
- Integrations: Aave asset and position swaps on Plasma; Gate Web3 swap; RealityFi rTokens (1,700+ tokenized equities) on Bitget Wallet; Jumper Advanced limit orders; RHEA cross-chain DEX; MetaMask Agent Wallet execution; Lido NEST buybacks; Lido Fast Swaps.
- Chains: mainnet, Gnosis, Arbitrum, Base, Polygon, BNB, Avalanche, Linea, Ink, Plasma (kaisersolver's list, 3511). Solana: core team proposal 8 Sept (3557) to launch at 0 bps volume fee for 12 months; "public launch / demo of a MVP by October", "no plan to launch an explicit solver incentive". The Solana SDK is "still marked experimental" (Sov, 3603).
- Moo & Earn affiliate program (CIP-84, April to 2 Oct): "$200M+ in total referred volume, with over 1,000 affiliates". Mandate expired 2 Oct; rewards being tracked but not paid pending a renewal CIP (3605). The core team is "reviewing the program's results to decide whether to propose an extension".
- Pay-per-quote API x402.cow.fi launched in October at $0.001 per quote (per application 3642). Returns 404 to a plain fetch; it is a new, core-owned service.
- Governance: CIP-85 performance and consistency rewards (Feb); CIP-86 DNS-hijack victim grants (April, done); CIP-87 penalty caps as % of order volume (25 Aug); CIP-88 quote competition redesign, quote reward budget at 10% of protocol revenue with the core team mandated to design the mechanism (Sept); CIP-89 Balancer unwind (Sept); CIP-Draft Fee Policy Iteration giving the core team a standing mandate on fee policy within ranges (14 Oct, 3627); CIP-Draft bonding pool simplification (May, 3455).
- Value distribution: Aragon RFP delivered (3328); core team framework 15 May (3454): enforce the solver HODL rule, a 1:1 burn trial from the DAO Safe (60 to 85M COW), flexible buyback mandate. Buybacks since April 2024: 78.6M COW bought vs 66.6M solver emissions.

## Solver competition: the open problems

Everything here is owned by the core solver team (harisang, felixhenneke, fleupold, arcsh7, Nikita) and the committee's technical lead has said twice in one day (3612, 3620, 13 Oct) that third-party reference tooling for it is unwelcome unless requested by that team. Listed so you know what not to pitch, and what the team is busy with.

1. **Small orders lost money for solvers after CIP-74** (3317, Fractal's tokenwood, Dec 2025): with the reward cap tied to the protocol fee, "solvers expected profits are now NEGATIVE for trades below $10k" (74% of batches); rewards concentrated in the top solver (72 of 93 ETH in a fortnight). marco_at_quasi: possibly intended, "a kodak moment". harisang took it to a single thread. CIP-85 and CIP-87 followed.
2. **Quote competition is weaker than solve competition** (3560): solvers underquote by ~4.8 bps volume-weighted; only 0.05% of quotes get rewarded. CIP-88 passed; mechanism design is now a core mandate. An outside analysis of CIP-88 (3620) was rejected the day after it was posted.
3. **Consistency metric v2.1** (3577): in-market orders only; marco_at_quasi asked how out-of-market failures count; harisang: edge cases "negligible".
4. **Readiness before production** (3572): no shadow competition except Arbitrum and mainnet; "the criteria for that evaluation are not published". kaisersolver's cow-backtester (3529) replays archived auctions from the public S3 bucket (`solver-instances.s3.eu-central-1.amazonaws.com`, ~30 days retention) against any /solve endpoint. ZeroNine found Plasma's settlement deadline is 10 to 11 blocks in the data, not the 5 in the docs; nobody from core has answered in a month.
5. **Rings and direct CoWs barely exist** (3511, Mr_Robot, July): of detected crossings on mainnet, 85 of 100 were zombies (no balance or allowance, cancelled, expired); 0 of 14 feasible rings cleared gas. kaisersolver confirmed from production: "Rings: zero a day." A would-be solver should not expect to win on matching.
6. **Solver onboarding is a Telegram queue** (3628): a new solver engine asked for staging access on 15 Oct, got flagged by the spam bot, re-posted three times, no reply by 18 Oct. The forum's "feed access" question (3401) was answered by marketing with a docs link.
7. **EBBO violation claims** (3274): a user must show better onchain routing on every block between auction start and settlement; felixhenneke did that investigation by hand and found no violation. CoW keeps a private `cowprotocol/ebbo` repo (Python).
8. **Services issues the core team has opened for itself** (Sept to Oct 2026): settlement end racing ahead of start (#5031), Solana driver assumes 400 ms slots (#5018), reorg invalidations leaving stale Cancelled events (#5032), EIP-7702 delegation in settlement (#4997), /trades endpoint detoasting 137 MB per request (#4949), parallel e2e tests (#4894, which the committee refused to fund in 3575: "if it lands as help wanted the repo's own reward program covers it").

## Developer surface

- Repos: 138 in `cowprotocol`. Active: services (Rust, 318 stars, 19 open issues, 39 open PRs), cowswap (144 open issues), cow-sdk (TypeScript, 12 open issues, 23 open PRs), contracts, composable-cow, hooks-trampoline, watch-tower, solver-rewards (Python, 2 open PRs), dune-sync, dune-queries, docs (49 open issues, several from 2024 marketing nits), bff, token-lists, trading-bot.
- Archived in 2026: ethcontract-rs, explorer, cow-amm, arak, conditional-smart-orders, solver-template-py. CoW AMM "has been deprecated" (mfw78, 3559).
- Grants org `cowdao-grants`: cow-py (Python SDK, GPL-3, 18 stars, 7 open issues incl. mfw78's own "adjust E2E test to be reproducible by external contributors", CloudFront WAF blocking httpx), cow-rs (default branch is a bare LICENSE; the crate `cowprotocol` is published as alpha from bleu's branches; 6 issues, 3 PRs), cow-shed, offline-mode, services-performance, cow-fee, polyswap, milkman, weiroll, zeromev-core.
- Contribution rules (services CONTRIBUTING.md): "For merged PRs that close an issue labeled `help wanted`, we offer 100 DAI". Exactly one open `help wanted` issue exists in services (#2394, "Remove feature gates for verified quotes", open since Feb 2024, 9 comments). "External PRs are reviewed on a best-effort basis and may sit for several weeks." "Treat unlabeled issues as if they were `core team only`." PRs over 200 lines of production code need prior agreement in an issue.
- Docs: 120 pages; tutorials for solvers (onboard, local test, optimal bidding, routes, flashloans, 7702 delegate), programmatic orders, hooks, widget. Docs issues #653 (Ink baseline undefined in competition rules) and #654 (grants pages cited CIP-63) were filed in August by an outsider; the grants pages now cite CIP-82, so the easy one was done internally.
- Data: Dune switched to paid-only query refresh in September 2026 (per Fiberscope, 3619); CoW's own dune-sync, dune-queries and solver-rewards pipelines depend on Dune. Public auction bodies live in the S3 instance bucket; competition records at `api/v2/solver_competition/by_tx_hash/{tx}`.

## Who is who (as it matters for a grant)

- Grants committee: mfw78 (technical lead; former core contributor; runs Nexum Labs / nullislabs and holds the Shepherd grant; prices work by "days of dedicated, effective time"; polices AI slop in capitals), Sov (steward; writes nearly every rejection; two to three sentences, one to eight days), Chim9 (payments and close-outs), Master_CoW (core team seat; never posts in grant threads). c3rnst was support staff in 2024 to 2025. middleway.eth left in March 2026.
- Core team voices that decide outcomes when they speak: anxolin (CoW Swap / programmatic orders; vouched for bleu's API and reviewed it), shoom3301 and le_zhy (frontend; rescued crutch12, estimated the ethers migration), harisang and felixhenneke (solver team; reviewers for BYOS, trade envy, solver data pipelines; were asked and did not answer on TDA research), fleupold (CTO; reviewed the MEV Blocker tool to its death, uses ZeroMEV daily), notsoformal (ops; posts fee and Solana proposals), moo_keeper (marketing; answers technical threads with docs links), solver_cow (solver team; polled solvers on the RPC balancer and found no demand).
- Incumbent grantee: bleu (10+ grants, three years, five grants in 2026, publishes its own retrospective). Live solver operators who post well: kaisersolver (Fiftysix LLC; cow-backtester, cow-certify, docs PR #652 merged), ZeroNine (Plasma), gabari (Nexroute, Base/BNB), tokenwood (Fractal), marco_at_quasi (Quasilabs).
