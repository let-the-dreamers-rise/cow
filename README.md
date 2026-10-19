# CoW Grants Program: research and attack log, 19 October 2026

Everything an applicant should know before posting in https://forum.cow.fi/c/cow-grants-program/10, and a brutal pass over fifteen candidate ideas.

Sources, all public and all fetched on 19 October 2026: the 240 threads in the grants category and its four sub-categories (funded, rejected, core contributor, retro round), 86 governance, technical, treasury and announcement threads from July 2025 onwards, the 98 proposals in the `cowgrants.eth` Snapshot space, docs.cow.fi, the `cowprotocol` and `cowdao-grants` GitHub organisations, forum profile data for the 2026 applicants, the council's public Notion hub (49 weekly updates and the pipeline database), the core team's public Notion ideas list, seven public Google Docs linked from those updates, and mfw78's HackMD one-pagers.

## The short version

- **No RFP is open, but applications are.** On 2 October 2026 the steward wrote: "the committee isn't publishing new problem areas or RFPs right now, so there isn't a specific area we can point you to... we wouldn't recommend investing in a research sprint in the expectation of a grant." The committee's own planning site (a public Notion hub with weekly council updates and a pipeline database) says "inbound applications remain open" while "new grant sourcing is paused". Docs, localisation, education, Solana tooling, second interfaces over Explorer data, RWA layers and CoW AMM are each named-closed in a 2026 thread.
- **Money is not the constraint.** The council's Q4 2025 plan says only 22% of its xDAI and 8% of its COW budget was deployed in 2025. What is scarce is a core-team reviewer and a named internal requester. Two core-team asks from October 2025 were never delivered and are still cited: a Composable CoW Order Decoder (in CIP-82's priority list, drafted as an RFP, never posted) and SDK-level quote warnings with USD estimates (Anxo: "would have avoided the issue AAVE had... $500K"; `cow-sdk` issue #309 still open).
- **Money in 2026 went to bleu (five grants), Aragon (RFP), the committee's own technical lead (Shepherd), four translators (RFP), and one newcomer: $2,000 for an EIP-712 conformance corpus, after six weeks of unpaid work on the one target the technical lead pointed at.** Thirteen other new accounts applied since May. None was funded. Six were rejected within 48 hours.
- **Three filters kill almost everything.** "Who would use it?" (a solver team or core dev must say so in the thread). "Does it touch the solver competition?" (then it is core-only, stated twice on 13 October). "Can it be measured in volume?" (marketing, education and consumer apps have been zero for two years).
- **The committee sets the price.** "A day or two of dedicated, effective time" was $2,000. Seventy-five hours was 3,750 xDAI. Every 2026 ask that was not an RFP bid got cut.
- **C1 discovery done (19 Oct):** cow-py matches services on hashing, UID and EIP-712 signing for all 19 vectors and fails all 19 on ETHSIGN signing, because it signs the unprefixed digest. Fix, failing-then-passing test and patch are in this repo; see `research/08`. That is the "real divergence" the attack log said C1 needed before any proposal.
- **What survives:** the Order Decoder and the SDK warnings (both with a written internal request; each gated on one public yes from a core developer), a Python-side conformance corpus for cow-py (about $1,500 to $2,500, after a discovery thread), merged PRs then a retro claim (about $80 per PR, 100 DAI for a `help wanted` issue), and, contingent on a core dev saying yes, a TWAP-for-EOAs execution quality study. Everything else on the board, including the committee's own ideation items (Methane, CoWPath, Quote API v2, Text to Trade) and the never-launched Propose & Earn bounty, is killed with the committee's own words.

## Files

| File | What it is |
|---|---|
| `research/01-program-rules-and-how-they-decide.md` | Template fields verbatim, process guide, agreement terms, Grants DAO values, the H1 and Q3 2025 reviews, the retro round, every RFP and who won it, and twelve evidenced patterns in how the committee decides. |
| `research/03-funded-ledger-2024-2026.md` | Every Snapshot-approved grant since 2024 with amount, path, outcome, and the five newcomers who got paid in 2026. |
| `research/04-rejected-ledger-2024-2026.md` | About seventy rejections with the exact sentence that killed each, grouped by cause. |
| `research/05-live-queue-oct-2026.md` | The 33 live or recently decided 2026 applications, thread by thread, with every committee reply quoted, applicant account ages, crowded and empty lanes, and the archetypes that fail and work. |
| `research/06-protocol-state-oct-2026.md` | Volume and wallet numbers, what shipped in 2026, the solver competition's open problems, the developer surface, and who decides what. |
| `research/07-what-is-actually-open-oct-2026.md` | The seven channels through which money can reach an outsider today, the committee's own pipeline (Notion), every core-team ask from Oct 2025 to Feb 2026 and what became of it, and the budget underspend. |
| `ideas/attack-log.md` | Fifteen candidate ideas, each attacked with the committee's own objections, a scoreboard, and the exact sequence if you still want to apply. |
| `research/08-cow-py-ethsign-divergence.md` | The discovery result for idea C1: cow-py's ETHSIGN signatures fail all 19 services-generated vectors; cause, impact, fix, test runs. |
| `patches/0001-*.patch` | The cow-py fix and conformance test as a git patch (apply on `cowdao-grants/cow-py` main `f4c95a2` with `git am`). |
| `tools/cowpy_conformance_check.py` | Harness that runs an installed cow-py against `tools/conformance_vectors.v1.json` and prints the per-vector table. |
| `drafts/forum-post-cowpy-ethsign.md`, `drafts/pr-description-cowpy.md` | Ready-to-paste text for the Technical-category post and the pull request. Nothing has been posted. |

## Caveats

- Forum first posts over about 6,000 characters were truncated in the fetch; where an amount or milestone was cut off the ledgers say "not visible".
- Hidden (trust level 0) profiles do not expose creation dates; ages for those accounts are interpolated from neighbouring user ids.
- Two threads carry a `grant-funded` tag but were rejected in-thread (Quantir 3434, ethcontract-rs 3330). The tags are treated as noise.
- Nothing here is advice to post. The attack log's own conclusion is that the expected grant income from the surviving path is $0 to about $2,500 for 40 to 80 hours, and that the relationship, not the cheque, is the asset.
