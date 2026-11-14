"""Validate every CSV in data/. Stdlib only.  Usage: python scripts/validate.py [data_dir]"""
import csv, re, sys, datetime
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from schema import TABLES, LIST_SEP, header

SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TARGET = re.compile(r"^\d{1,2}\.[0-9a-z]+$")

def check(kind, allowed, v):
    if kind == "slug": return bool(SLUG.match(v)) or "must be lowercase-with-hyphens"
    if kind == "int":  return v.isdigit() or "must be a whole number"
    if kind == "date":
        try: datetime.date.fromisoformat(v); return True
        except ValueError: return "must be YYYY-MM-DD"
    if kind == "enum": return v in allowed or f"must be one of {sorted(allowed)}"
    if kind == "url":  return v.startswith(("http://", "https://")) or "must start with http(s)://"
    if kind == "list": return all(p.strip() for p in v.split(LIST_SEP)) or f"empty item in '{LIST_SEP}' list"
    return True

def main(data_dir="data"):
    d, errors, data = Path(data_dir), [], {}
    for t, spec in TABLES.items():
        p = d / f"{t}.csv"
        if not p.exists(): errors.append(f"missing {p}"); data[t] = []; continue
        r = csv.DictReader(open(p, newline="", encoding="utf-8"))
        if r.fieldnames != header(t):
            errors.append(f"{t}.csv: header must be exactly {header(t)}"); data[t] = []; continue
        rows = data[t] = list(r)
        seen = {}
        for i, row in enumerate(rows, start=2):
            for name, kind, req, allowed in spec["columns"]:
                v = (row[name] or "").strip()
                if not v:
                    if req: errors.append(f"{t}.csv:{i} {name} is required")
                    continue
                ok = check(kind, allowed, v)
                if ok is not True: errors.append(f"{t}.csv:{i} {name}={v!r} {ok}")
            key = tuple(row[k] for k in spec["pk"])
            if key in seen: errors.append(f"{t}.csv:{i} duplicate {spec['pk']} (first on line {seen[key]})")
            seen.setdefault(key, i)

    for t, spec in TABLES.items():
        for col, (rt, rc) in spec["fk"].items():
            valid = {r[rc] for r in data[rt]}
            for i, row in enumerate(data[t], start=2):
                if row[col] and row[col] not in valid:
                    errors.append(f"{t}.csv:{i} {col}={row[col]!r} not found in {rt}.csv")

    # cross-table rules
    risk_ids = {r["problem_id"] for r in data["risks"]}
    for i, p in enumerate(data["problems"], start=2):
        if p["problem_id"] not in risk_ids:
            errors.append(f"problems.csv:{i} {p['problem_id']} has no row in risks.csv (ethics, morality, devils_advocate are required)")
        for tg in filter(None, (s.strip() for s in p["sdg_targets"].split(LIST_SEP))):
            if not TARGET.match(tg) or not 1 <= int(tg.split(".")[0]) <= 17:
                errors.append(f"problems.csv:{i} sdg_target {tg!r} should look like <goal 1-17>.<target>")

    for m in errors[:200]: print("ERROR", m)
    print(", ".join(f"{len(v)} {k}" for k, v in data.items()), f"| {len(errors)} errors")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
