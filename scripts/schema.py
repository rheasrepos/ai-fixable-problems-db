"""Tables and columns for the AI-Fixable Problems DB. validate.py and SCHEMA.md follow this file.
Each table: columns [(name, kind, required, allowed)], primary key, foreign keys {col: (table, col)}."""

LIST_SEP = ";"
MATURITY = {"idea", "research", "pilot", "deployed"}

TABLES = {
    "candidate_issues": {  # raw list of problems pulled from outside sources, not yet written up
        "columns": [
            ("issue",      "str",  True,  None),
            ("source",     "str",  True,  None),
            ("url",        "url",  True,  None),
            ("status",     "enum", True,  {"candidate", "promoted", "out_of_scope"}),
            ("problem_id", "slug", False, None),  # set when promoted
        ],
        "pk": ("issue", "source"), "fk": {},
    },
    "candidate_datasets": {  # found by scripts/harvest_datasets.py; reviewed by hand before promotion
        "columns": [
            ("area",       "slug", True,  None),   # a problem_id, or a new area not yet written up
            ("source",     "enum", True,  {"huggingface", "hdx", "earth_engine", "nasa_cmr", "noaa_ncei", "manual"}),
            ("source_id",  "str",  True,  None),
            ("title",      "str",  True,  None),
            ("url",        "url",  True,  None),
            ("query",      "str",  False, None),
            ("license",    "str",  False, None),
            ("popularity", "str",  False, None),
            ("status",     "enum", True,  {"candidate", "promoted", "rejected"}),
        ],
        "pk": ("area", "source", "source_id"), "fk": {},
    },
    "candidate_research": {  # open-access papers found via OpenAlex; promote good ones to existing_work
        "columns": [
            ("area",       "slug", True,  None),
            ("openalex_id","str",  True,  None),
            ("title",      "str",  True,  None),
            ("url",        "url",  True,  None),
            ("year",       "int",  False, None),
            ("cited_by",   "int",  False, None),
            ("query",      "str",  False, None),
            ("status",     "enum", True,  {"candidate", "promoted", "rejected"}),
        ],
        "pk": ("area", "openalex_id"), "fk": {},
    },
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
            ("scale",       "enum", False, {"local", "regional", "country", "not-place-based"}),  # smallest area the data resolves: places within a city/county; states, provinces or coarse grid cells; one figure per country; or not tied to places
            ("language",    "str",  False, None),  # for data not tied to a place: which languages it covers, as its own card or paper states it
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
    "interventions": {  # anything tried against a problem: AI, other tech, policy, money, markets, people
        "columns": [
            ("intervention_id", "slug", True,  None),
            ("problem_id",      "slug", True,  None),
            ("name",            "str",  True,  None),
            ("organization",    "str",  False, None),
            ("kind",            "enum", True,  {"ai", "other_tech", "policy", "funding", "market",
                                                 "community", "human_connection", "open_data"}),
            ("year_started",    "int",  False, None),
            ("url",             "url",  True,  None),
            ("scale",           "str",  False, None),  # reach, in the source's words
            ("effect",          "str",  False, None),  # measured outcome, in the problem's units
            ("evidence",        "enum", True,  {"rct", "quasi_experimental", "self_reported", "none"}),
            ("effect_source",   "url",  False, None),
            ("featured",        "enum", True,  {"true", "false"}),  # well-known; shown first
            ("notes",           "str",  False, None),
        ],
        "pk": ("intervention_id",), "fk": {"problem_id": ("problems", "problem_id")},
    },
    "tools": {  # an AI tool, model or dataset built for a problem: how open it is, and whether anyone uses it
        "columns": [
            ("tool_id",       "slug", True,  None),
            ("problem_id",    "slug", True,  None),
            ("name",          "str",  True,  None),
            ("organization",  "str",  False, None),
            ("url",           "url",  True,  None),   # the source the row rests on
            ("url_2",         "url",  False, None),
            ("openness",      "enum", True,  {"open", "open_restricted", "open_code_closed_data", "gated",
                                               "closed", "not_open_by_choice", "not_verified"}),
            ("license",       "str",  False, None),
            ("released",      "str",  False, None),   # what was released: code, weights, data, paper only
            ("use_status",    "enum", True,  {"deployed", "deployment_ended", "creator_only", "research_only",
                                               "no_evidence_found", "not_verified"}),
            ("deployment_evidence", "str", False, None),  # who uses it, in the source's terms
            ("maintenance",   "str",  False, None),
            ("barrier",       "str",  False, None),   # documented reason it is not used more
            ("verification",  "enum", True,  {"verified", "partly_verified", "snippet_only", "unverified"}),
            ("verification_note", "str", False, None),
            ("contributor",   "str",  True,  None),
            ("date_added",    "date", True,  None),   # also the date the row was checked
        ],
        "pk": ("tool_id",), "fk": {"problem_id": ("problems", "problem_id")},
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
