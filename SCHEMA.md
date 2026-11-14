# Schema

Seven linked CSVs in `data/`. `scripts/schema.py` is the source of truth; `scripts/validate.py` enforces it.
Multi-valued cells use `;`. IDs are lowercase-with-hyphens.

```
sdg_goals ──< problems >──< problem_datasets >── datasets
                 │
                 ├──< existing_work
                 ├──< data_gaps
                 └─── risks   (exactly one row per problem)
```

| Table | One row is | Key columns |
|---|---|---|
| sdg_goals | a UN Sustainable Development Goal (1–17, prefilled) | sdg_goal, name |
| candidate_issues | a problem pulled from an outside list, not yet written up | issue, source, url, status (candidate / promoted / out_of_scope), problem_id |
| problems | a problem AI could help fix | problem_id, name, description, sdg_goal (primary), sdg_targets (any goal, e.g. `12.3;2.1`), solution_kind (digital / physical / hybrid), solution_summary, maturity (idea / research / pilot / deployed) |
| datasets | an existing dataset | dataset_id, name, url, access (open / gated / proprietary / unknown), license, size (with units), modality |
| problem_datasets | how one dataset serves one problem | problem_id, dataset_id, role |
| existing_work | a paper, project, product or policy already working on it | work_id, problem_id, title, url, kind, year, maturity |
| interventions | anything tried against a problem | intervention_id, problem_id, name, organization, kind (ai / other_tech / policy / funding / market / community / human_connection / open_data), year_started, url, scale, effect, evidence (rct / quasi_experimental / self_reported / none), effect_source, featured (well-known; shown first) |
| data_gaps | data that's missing for a problem | problem_id, gap, why_it_matters, how_to_close |
| risks | the risk case for a problem | who_could_be_harmed, dual_use, bias_and_representation, **ethics**, **morality**, **devils_advocate** (bold = required) |

## solution_kind

- **digital**: the AI's output is information (a forecast, a diagnosis, a translation).
- **physical**: the AI acts in or changes the physical world (robots, drones, control of a grid or a lab).
- **hybrid**: digital output that directly drives a physical intervention (e.g. a forecast that triggers food delivery).

## The three required risk sections

- **ethics**: duties and process. Consent, privacy, accountability, who decides, and who is answerable when it fails.
- **morality**: whether it is right to do at all. Whose values are encoded, what is lost even when it works, and whether AI should be the one doing it.
- **devils_advocate**: the strongest case *against* pursuing this, written as if you believed it. Not a rebuttal.

A problem can't be merged without all three.
