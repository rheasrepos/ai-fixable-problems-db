"""Join all tables into one JSON file (one object per problem) for the raddotcom page.
Usage: python scripts/export_json.py [out.json]   (default: build/problems.json)"""
import csv, json, sys
from pathlib import Path

D = Path(__file__).parent.parent / "data"
def rows(t): return list(csv.DictReader(open(D / f"{t}.csv", encoding="utf-8")))

def main(out="build/problems.json"):
    goals = {g["sdg_goal"]: g["name"] for g in rows("sdg_goals")}
    datasets = {d["dataset_id"]: d for d in rows("datasets")}
    links, work, gaps = rows("problem_datasets"), rows("existing_work"), rows("data_gaps")
    risks = {r["problem_id"]: r for r in rows("risks")}
    result = []
    for p in rows("problems"):
        pid = p["problem_id"]
        result.append({**p,
            "sdg_name": goals.get(p["sdg_goal"], ""),
            "datasets": [{**datasets[l["dataset_id"]], "role": l["role"]} for l in links if l["problem_id"] == pid and l["dataset_id"] in datasets],
            "existing_work": [w for w in work if w["problem_id"] == pid],
            "data_gaps": [g for g in gaps if g["problem_id"] == pid],
            "risks": risks.get(pid, {}),
        })
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {len(result)} problems to {out}")

if __name__ == "__main__":
    main(*sys.argv[1:])
