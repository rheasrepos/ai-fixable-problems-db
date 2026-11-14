"""Pull approved write-in answers from the site's poll and add them to data/candidate_issues.csv.

Only rows you've approved in Supabase are readable with the public key, so nothing unreviewed
gets in. Reads PUBLIC_SUPABASE_URL / PUBLIC_SUPABASE_ANON_KEY from the environment, or from
~/code/raddotcom/.env (override with RADDOTCOM).
Usage: python3 scripts/import_visitor_answers.py
"""
import csv, json, os, urllib.request
from pathlib import Path

SITE = "https://rheamad.vercel.app/ai-problems"
OUT = Path(__file__).parent.parent / "data" / "candidate_issues.csv"

def env():
    vals = {k: os.environ.get(k, "") for k in ("PUBLIC_SUPABASE_URL", "PUBLIC_SUPABASE_ANON_KEY")}
    dotenv = Path(os.environ.get("RADDOTCOM", Path.home() / "code" / "raddotcom")) / ".env"
    if not all(vals.values()) and dotenv.exists():
        for line in dotenv.read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                if k.strip() in vals and not vals[k.strip()]: vals[k.strip()] = v.strip().strip('"')
    return vals["PUBLIC_SUPABASE_URL"], vals["PUBLIC_SUPABASE_ANON_KEY"]

def main():
    url, key = env()
    if not (url and key): raise SystemExit("Set PUBLIC_SUPABASE_URL and PUBLIC_SUPABASE_ANON_KEY (or put them in raddotcom/.env).")
    req = urllib.request.Request(f"{url}/rest/v1/problem_vote_writeins?select=*", headers={"apikey": key})
    writeins = json.loads(urllib.request.urlopen(req, timeout=30).read())
    rows = list(csv.DictReader(open(OUT, encoding="utf-8")))
    have = {(r["issue"].lower(), r["source"]) for r in rows}
    new = 0
    for w in writeins:
        issue = w["problem"].strip()
        if issue and (issue.lower(), "Visitors") not in have:
            rows.append({"issue": issue, "source": "Visitors", "url": SITE, "status": "candidate", "problem_id": ""}); new += 1
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=["issue", "source", "url", "status", "problem_id"]); wr.writeheader(); wr.writerows(rows)
    print(f"added {new} visitor answers to {OUT}")

if __name__ == "__main__":
    main()
