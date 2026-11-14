# Related work: a meta-analysis

Surveyed 2026-11-13. The question: has anyone built a database of the world's problems that AI could help
with, organized around **the data that exists**, with a **risk case** for each? Each source below is scored on
the same dimensions.

## Sources

| Source | Unit | Taxonomy | Datasets central? | Risks / negatives? | Contribution | Status |
|---|---|---|---|---|---|---|
| [80,000 Hours problem profiles](https://80000hours.org/problem-profiles/) | problem (9 ranked + 6 emerging + 12 others) | own; ranked by scale, neglectedness, solvability | no | implicit in the ranking | none (editorial) | active; updated [2024](https://80000hours.org/2024/10/updates-to-our-problem-rankings-on-factory-farming-climate-change-and-more/), [2025](https://80000hours.org/2025/06/updates-to-our-list-of-the-worlds-most-pressing-problems/) |
| [Oxford AI4SG database](https://philpapers.org/archive/COWADB.pdf) (Cowls, Tsamados, Taddeo, Floridi, *Nature Machine Intelligence*, 2021) | AI project (108) | UN SDGs | no | **excluded** projects with evidence of negative side-effects | survey, Jul 2018 – Nov 2020 | published at aiforsdgs.org/all-projects; page didn't load on 2026-11-13 |
| [IRCAI Global Top 100](https://ircai.org/?p=5475) (UNESCO) | AI project (100) | all 17 SDGs | no | ethics is one selection criterion | open call (2021) | list published |
| [AI for SDGs Think Tank / Observatory](https://ai-for-sdgs.academy/) (Center for Long-term AI, Beijing) | AI project or proposal | all 17 SDGs | no | **yes**: projects with potential negative impact are rated and marked | open submissions | listed as active; no download |
| [McKinsey AI for social good library](https://www.mckinsey.com/ng/our-insights/applying-artificial-intelligence-for-social-good) (2018) | use case (~160) | 10 own domains, also mapped to SDGs | no, but names data access as a main bottleneck | discussed in the paper | none | static; library itself not public |

## What the comparison shows

1. **Everyone catalogs projects, nobody catalogs problems × data.** Every AI-for-SDG source is a list of
   projects that already exist. 80,000 Hours lists problems but has no AI or data angle. The row unit
   "problem, linked to datasets that could address it" doesn't appear anywhere surveyed.
2. **Data is the named bottleneck but never the structure.** McKinsey calls data accessibility one of the most
   significant bottlenecks. None of the databases record which datasets exist, their access level, or what's
   missing. Your `datasets`, `problem_datasets`, and `data_gaps` tables are the gap.
3. **Risk handling is either a filter or a flag.** Oxford excluded harmful projects; IRCAI used ethics as a
   selection criterion; the Beijing observatory flags negative impact. None asks for a written argument
   *against* the work. The required devil's-advocate section is new.
4. **Coverage is lopsided.** In Oxford's database, health (SDG 3) leads, while SDGs 5, 16, and 17 each have
   fewer than five projects. Seeding problems in under-covered SDGs would add the most.
5. **These databases go stale.** Oxford's survey ended in 2020 and its page no longer loads; IRCAI is a 2021
   call; McKinsey is 2018. Plain CSVs on GitHub plus a static page are cheap to keep alive.

## Implications for this repo

- [ ] Seed the first problems from under-covered SDGs (5, 16, 17), not just health and climate.
- [ ] Use existing project lists (IRCAI, the observatory) as sources for `existing_work`, with attribution.
- [ ] Consider adding a `tractability` or `neglectedness` field to borrow 80,000 Hours' framing.
- [ ] Keep the devil's-advocate requirement; it's the clearest difference from prior work.

## Not yet checked

ITU AI for Good, Omdena, Data.org, Project Drawdown, Copenhagen Consensus, Our World in Data, Google AI for Social Good.
The Wayback Machine is blocked for Claude's tools; check aiforsdgs.org there by hand.

## Impact data sources (checked 2026-11-14)

Sources that measure what's been tried against these problems, and whether their data can be pulled in automatically.

| Source | Covers | What's there | Can we pull it automatically? |
|---|---|---|---|
| [ReFED](https://docs.refed.org/methodologies/solutions_database/overview.html) | Food waste (US) | 40+ solutions with tons diverted, net financial benefit, GHG, water, meals, jobs; 700+ solution providers | **No.** [Terms](https://refed.org/terms-of-use) ban automated scraping except through an authorized API. Non-commercial reuse with attribution is allowed, so enter by hand with credit, or ask ReFED for API access. |
| [Project Drawdown](https://www.drawdown.org/explorer/faqs) | Climate | 100+ solutions with effectiveness, adoption, climate impact, cost, speed | **Yes, with credit.** Data per solution under "Methods and Supporting Data"; [methodology on Zenodo](https://zenodo.org/records/18037237) is CC BY 4.0. Drawdown counts policy and funding as "levers", not solutions. |
| [J-PAL evaluations](https://www.povertyactionlab.org/evaluations) | Poverty, labor, housing, etc. | 1,200+ RCT summaries in 99 countries; filters include an AI sector. Replication data on [Dataverse](https://www.povertyactionlab.org/blog/7-12-22/rct-data-survey-instruments-how-find-what-you-need-j-pal-dataverse) | **Not without asking.** No export and no terms page found. Curate by hand or ask J-PAL. |
| [3ie Development Evidence Portal](https://3ieimpact.org/terms-of-use) | Development programs | Impact evaluations and systematic reviews | **Not without asking.** Terms allow personal, non-commercial use and prohibit commercial use; nothing on automated collection. |
| OECD Creditor Reporting System | Funding flows | Project-level aid by sector and purpose code | **Yes.** Bulk download (~1.2 GB) via [oda_reader](https://pypi.org/project/oda_reader/) (MIT, by ONE Campaign). OECD's own data licence not yet confirmed. |
