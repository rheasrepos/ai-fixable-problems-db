"""Tables and columns for the AI-Fixable Problems DB. validate.py and SCHEMA.md follow this file.
Each table: columns [(name, kind, required, allowed)], primary key, foreign keys {col: (table, col)}."""

LIST_SEP = ";"
MATURITY = {"idea", "research", "pilot", "deployed"}

TABLES = {
    "sdg_goals": {
        "columns": [("sdg_goal", "int", True, None), ("name", "str", True, None)],
        "pk": ("sdg_goal",), "fk": {},
    },
    "problems": {
        "columns": [
            ("problem_id",       "slug", True,  None),
            ("name",             "str",  True,  None),
            ("description",      "str",  True,  None),
            ("sdg_goal",         "int",  True,  None),   # 1-17, primary goal
            ("sdg_targets",      "list", False, None),   # e.g. "3.4;3.8"
            ("solution_kind",    "enum", True,  {"digital", "physical", "hybrid"}),
            ("solution_summary", "str",  True,  None),   # what the AI would actually do
            ("maturity",         "enum", True,  MATURITY),  # furthest stage reached by anyone
            ("contributor",      "str",  True,  None),
            ("date_added",       "date", True,  None),
        ],
        "pk": ("problem_id",), "fk": {"sdg_goal": ("sdg_goals", "sdg_goal")},
    },
    "datasets": {
        "columns": [
            ("dataset_id",  "slug", True,  None),
            ("name",        "str",  True,  None),
            ("url",         "url",  True,  None),
            ("access",      "enum", True,  {"open", "gated", "proprietary", "unknown"}),
            ("license",     "str",  False, None),
            ("size",        "str",  False, None),  # free text with units, e.g. "2.1 TB", "40M records"
            ("modality",    "list", False, None),  # e.g. "satellite imagery;tabular"
            ("description", "str",  False, None),
            ("contributor", "str",  True,  None),
            ("date_added",  "date", True,  None),
        ],
        "pk": ("dataset_id",), "fk": {},
    },
    "problem_datasets": {
        "columns": [
            ("problem_id", "slug", True, None),
            ("dataset_id", "slug", True, None),
            ("role",       "str",  True, None),  # how this dataset helps with this problem
        ],
        "pk": ("problem_id", "dataset_id"),
        "fk": {"problem_id": ("problems", "problem_id"), "dataset_id": ("datasets", "dataset_id")},
    },
    "existing_work": {
        "columns": [
            ("work_id",    "slug", True,  None),
            ("problem_id", "slug", True,  None),
            ("title",      "str",  True,  None),
            ("url",        "url",  True,  None),
            ("kind",       "enum", True,  {"paper", "project", "product", "policy"}),
            ("year",       "int",  False, None),
            ("maturity",   "enum", True,  MATURITY),
            ("notes",      "str",  False, None),
        ],
        "pk": ("work_id",), "fk": {"problem_id": ("problems", "problem_id")},
    },
    "data_gaps": {
        "columns": [
            ("problem_id",     "slug", True,  None),
            ("gap",            "str",  True,  None),  # data that's missing
            ("why_it_matters", "str",  True,  None),
            ("how_to_close",   "str",  False, None),
        ],
        "pk": ("problem_id", "gap"), "fk": {"problem_id": ("problems", "problem_id")},
    },
    "risks": {  # exactly one row per problem; ethics, morality, devils_advocate are mandatory
        "columns": [
            ("problem_id",       "slug", True,  None),
            ("who_could_be_harmed", "str", True, None),
            ("dual_use",         "str",  False, None),
            ("bias_and_representation", "str", False, None),
            ("ethics",           "str",  True,  None),
            ("morality",         "str",  True,  None),
            ("devils_advocate",  "str",  True,  None),
        ],
        "pk": ("problem_id",), "fk": {"problem_id": ("problems", "problem_id")},
    },
}

def header(table):
    return [c[0] for c in TABLES[table]["columns"]]
