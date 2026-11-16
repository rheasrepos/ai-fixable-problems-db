"""Copy build/problems.json into the raddotcom site, keeping the site file's `ai_written` lists.
Those lists (which cells show the LLM underline) are edited by hand in raddotcom, so a plain copy would erase them.
Rows that are new get no list; the page then marks every free-text cell in them as LLM-written.
Usage: python scripts/sync_merge.py build/problems.json <raddotcom>/static/ai-problems.json"""
import json, sys
from pathlib import Path

KEYS = {"datasets": "dataset_id", "existing_work": "work_id", "interventions": "intervention_id",
        "data_gaps": "gap", "tools": "tool_id"}

def main(src, dst):
    new = json.loads(Path(src).read_text(encoding="utf-8"))
    dst = Path(dst)
    old = {p["problem_id"]: p for p in json.loads(dst.read_text(encoding="utf-8"))} if dst.exists() else {}
    kept = 0
    for p in new:
        o = old.get(p["problem_id"], {})
        if "ai_written" in o: p["ai_written"] = o["ai_written"]
        if "ai_written" in (o.get("risks") or {}) and p.get("risks"): p["risks"]["ai_written"] = o["risks"]["ai_written"]
        for table, key in KEYS.items():
            marks = {r[key]: r["ai_written"] for r in o.get(table, []) if "ai_written" in r}
            for r in p.get(table, []):
                if r[key] in marks: r["ai_written"] = marks[r[key]]; kept += 1
    dst.write_text(json.dumps(new, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {len(new)} problems to {dst} (kept LLM marks on {kept} rows)")

if __name__ == "__main__":
    main(*sys.argv[1:])
