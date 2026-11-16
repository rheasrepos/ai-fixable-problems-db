# Research notes behind `data/tools.csv`

Raw notes from the 2026-11-16 research on which open AI tools are used and which are not.
`UNUSED_TOOLS_REPORT.md` (repo root) is the summary; these four files hold more tools than its tables do.

| File | Covers |
|---|---|
| `child_safety.md` | child online safety tools (about 30 rows) |
| `climate_food.md` | dangerous climate conditions, food waste |
| `shelter_wage_language.md` | shelter scarcity, living wage, languages (about 45 rows) |
| `evidence_and_trackers.md` | measured non-use rates, existing trackers, proposed status tiers |

Every claim in the notes carries a label: **verified** (read in a fetched page or cloned repo), **snippet only**,
or **UNVERIFIED** (background knowledge, a lead and not a fact). Do not promote an UNVERIFIED line into
`tools.csv` without opening its source. Fetched pages were read through an automated extraction, so re-check
any quotation before printing it as verbatim.

## Open items (as of 2026-11-16)

Checked against the source on 2026-11-16:

- **18,244 vs 18,247 scientific repositories.** Not an error. The SciCat dataset has 18,247 repositories; the
  inactivity count (11,631 with no commit in six months, about 64%) is out of the 18,244 in the paper's model
  ([arXiv 2504.18971](https://arxiv.org/pdf/2504.18971)). The 64% is derived from those two counts, not stated in the paper.
- **ECMWF real-time data is no longer a paid license.** On 1 October 2025 ECMWF opened its entire real-time
  catalogue under CC BY 4.0 with no data charges ([ECMWF](https://www.ecmwf.int/node/29497)). Limits: delivery of
  the full high-volume data may still carry service charges, and the free online subset is at 25 km, with 9 km
  forecasts (2-hour latency) announced for later in 2026. The digital-twin lineage doc in the Claude project
  still says the feed is paid; a correction note sits next to it.

Decisions for Rhea:

- **PAN12 grooming-chat corpus.** Left off the public datasets tab. It is openly downloadable on Zenodo but
  states no license, and it contains real predator chats.
- **`models.csv` in ai-progress-open-dataset.** Whether it gets openness and use-status columns
  (see that repo's RELATED_WORK.md).

Not re-checked:

- The verification labels on the 54 rows in `tools.csv` are the original researchers' labels. Only the
  Al-Nabki et al. row was checked a second time, against the journal paper.
- GitHub's website was blocked during the research, so no archived flags or star counts were read directly.

Not researched at all (names only, nothing known):

- Child safety: cyberbullying classifiers and datasets, open age-estimation models, NSFW proxy classifiers.
- Climate: FuXi, FengWu, NeuralGCM, ClimaX, Prithvi WxC, ClimateBench, WeatherBench 2, ClimateLearn.
- Food: FAO Food Loss and Waste database as a tool, WRAP tools, cold-chain digital twins, Winnow, Leanpath, Too Good To Go.
- Shelter and wage: Open Buildings and Overture, slum-mapping models, DataKind projects, JobBERT, ESCOXLM-R, Fairwork, Turkopticon, labor-market ABMs.
- Languages: ELAR, PARADISEC, AILLA, Universal Dependencies, FLORES, Aya, Living Tongues.

Three measurements nobody has published, from the report's conclusion: the current share of Hugging Face models
with zero downloads; a survival analysis of AI-for-good fellowship project repositories; how many
community-language speech models on the Hub have any downloads.
