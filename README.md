# CoW Grants Program: research and attack log, 19 October 2026

Everything an applicant should know before posting in https://forum.cow.fi/c/cow-grants-program/10, and a brutal pass over fifteen candidate ideas.

Sources, all public and all fetched on 19 October 2026: the 240 threads in the grants category and its four sub-categories (funded, rejected, core contributor, retro round), 86 governance, technical, treasury and announcement threads from July 2025 onwards, the 98 proposals in the `cowgrants.eth` Snapshot space, docs.cow.fi, the `cowprotocol` and `cowdao-grants` GitHub organisations, and forum profile data for the 2026 applicants.

## The short version

- **The program is open on paper and closed in practice.** On 2 October 2026 the steward wrote: "the committee isn't publishing new problem areas or RFPs right now, so there isn't a specific area we can point you to... we wouldn't recommend investing in a research sprint in the expectation of a grant." The Volume-Based Integration RFP closed a year ago. Docs, localisation, education, Solana tooling, second interfaces over Explorer data, RWA layers and CoW AMM are each named-closed in a 2026 thread.
- **Money in 2026 went to bleu (five grants), Aragon (RFP), the committee's own technical lead (Shepherd), four translators (RFP), and one newcomer: $2,000 for an EIP-712 conformance corpus, after six weeks of unpaid work on the one target the technical lead pointed at.** Thirteen other new accounts applied since May. None was funded. Six were rejected within 48 hours.
- **Three filters kill almost everything.** "Who would use it?" (a solver team or core dev must say so in the thread). "Does it touch the solver competition?" (then it is core-only, stated twice on 13 October). "Can it be measured in volume?" (marketing, education and consumer apps have been zero for two years).
- **The committee sets the price.** "A day or two of dedicated, effective time" was $2,000. Seventy-five hours was 3,750 xDAI. Every 2026 ask that was not an RFP bid got cut.
- **What survives:** a Python-side conformance corpus for cow-py (about $1,500 to $2,500, only after a discovery thread finds a real divergence or a maintainer asks), merged PRs then a retro claim (about $80 per PR, 100 DAI for a `help wanted` issue), and, contingent on a core dev saying yes in public, a TWAP-for-EOAs execution quality study. Everything else on the board is killed with the committee's own words.

## Files

| File | What it is |
|---|---|
| `research/01-program-rules-and-how-they-decide.md` | Template fields verbatim, process guide, agreement terms, Grants DAO values, the H1 and Q3 2025 reviews, the retro round, every RFP and who won it, and twelve evidenced patterns in how the committee decides. |
| `research/03-funded-ledger-2024-2026.md` | Every Snapshot-approved grant since 2024 with amount, path, outcome, and the five newcomers who got paid in 2026. |
| `research/04-rejected-ledger-2024-2026.md` | About seventy rejections with the exact sentence that killed each, grouped by cause. |
| `research/05-live-queue-oct-2026.md` | The 33 live or recently decided 2026 applications, thread by thread, with every committee reply quoted, applicant account ages, crowded and empty lanes, and the archetypes that fail and work. |
| `research/06-protocol-state-oct-2026.md` | Volume and wallet numbers, what shipped in 2026, the solver competition's open problems, the developer surface, and who decides what. |
| `ideas/attack-log.md` | Fifteen candidate ideas, each attacked with the committee's own objections, a scoreboard, and the exact sequence if you still want to apply. |

## Caveats

- Forum first posts over about 6,000 characters were truncated in the fetch; where an amount or milestone was cut off the ledgers say "not visible".
- Hidden (trust level 0) profiles do not expose creation dates; ages for those accounts are interpolated from neighbouring user ids.
- Two threads carry a `grant-funded` tag but were rejected in-thread (Quantir 3434, ethcontract-rs 3330). The tags are treated as noise.
- Nothing here is advice to post. The attack log's own conclusion is that the expected grant income from the surviving path is $0 to about $2,500 for 40 to 80 hours, and that the relationship, not the cheque, is the asset.
