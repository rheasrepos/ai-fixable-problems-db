# AI-Fixable Problems Database

A database of problems in the world that could be addressed with AI, given the large datasets that already exist.

## Status

v0 scaffold (2026-10-23): schema, validator, JSON export, and CI are in place. The SDG goals are prefilled; the other tables have headers only.

```
data/*.csv                 linked tables (see SCHEMA.md)
scripts/schema.py          table definitions (source of truth)
scripts/validate.py        checks every PR (stdlib only)
scripts/export_json.py     joins everything into build/problems.json for the raddotcom page
scripts/sync_merge.py      copies it into raddotcom, keeping the site's LLM-written marks
UNUSED_TOOLS_REPORT.md     research behind data/tools.csv: which open tools are used, and why not
research_notes/            raw notes behind the report, plus the open items list
```

Design: linked tables (problems ↔ datasets); UN SDG taxonomy; solution kind (digital / physical / hybrid); required risk section with ethics, morality, and devil's advocate; CSVs in GitHub, browsed on raddotcom.

## Next

- [ ] Add the first 3–5 problems by hand to test the schema.
- [x] raddotcom page: `/ai-problems` route in the raddotcom repo reads `static/ai-problems.json`. Run `sync-to-raddotcom.command` after editing data, then commit and push raddotcom.

## Origin note

> "make a database of all the problems we can fix in the world using AI given the massive datasets we do havev….."

Margin note, NYU AI Safety Association reading, week of Oct 2026.

## Passage it responds to

The note sits beside Buchanan's section on data, the second leg of the "AI triad" (algorithms, data, compute). He argues that data is often how ML systems learn about the world, so a fact missing from the data won't be learned. He adds that larger, more representative datasets make systems more capable, and that unrepresentative data lets bias creep in.

## Open questions

- [ ] (none recorded yet)

## How to cite this database

Madhogarhia, Rhea. *AI-Fixable Problems Database*. 2026. https://rheamad.vercel.app/ai-problems (data: https://github.com/rheasrepos/ai-fixable-problems-db). Data licensed CC BY 4.0; code MIT. Many descriptions were drafted with an LLM (rows marked `claude-draft`) and are being checked against their sources.

## Citation (the passage this responds to)

Buchanan, Ben. "The AI Triad and What It Means for National Security Strategy." Center for Security and Emerging Technology (CSET), Georgetown University. https://cset.georgetown.edu/wp-content/uploads/CSET-AI-Triad-Report.pdf
