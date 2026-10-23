# Contributing

Adding a problem touches several files. Do it in one pull request:

1. `problems.csv`: one row. Pick the primary `sdg_goal` and any `sdg_targets` (https://sdgs.un.org/goals).
2. `risks.csv`: one row with **ethics**, **morality**, and **devils_advocate** filled in (definitions in SCHEMA.md). Required.
3. `datasets.csv` + `problem_datasets.csv`: each dataset that exists (reuse an existing `dataset_id` if it's already listed), and a `role` saying how it helps.
4. `existing_work.csv` and `data_gaps.csv`: as many rows as apply. Zero is fine, but say so in the PR.
5. Run `python scripts/validate.py` (no installs needed). CI runs the same check.

Set `contributor` to your GitHub handle and `date_added` to today.
