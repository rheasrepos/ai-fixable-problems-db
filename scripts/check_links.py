#!/usr/bin/env python3
"""Open every link in data/*.csv and report which ones no longer work.

    python3 scripts/check_links.py            # run on your own computer (needs internet); takes a few minutes
    python3 scripts/check_links.py --table datasets

Writes build/link_report.csv: table, row id, column, url, status, final url, note.
  ok        the page answered normally
  moved     it answered, but at a different address (check the row still points at the right thing)
  blocked   the site refused an automated visit (401/402/403/429, a reset connection, or a certificate Python can't check): open it by hand, it is probably fine
  broken    404/410, a server error, or no answer at all
Nothing in data/ is changed. Standard library only.
"""
import csv, os, re, sys, time, urllib.request, urllib.error, urllib.parse, ssl, concurrent.futures as cf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ONLY = sys.argv[sys.argv.index("--table") + 1] if "--table" in sys.argv else None
UA = {"User-Agent": "Mozilla/5.0 (link check for github.com/rheasrepos/ai-fixable-problems-db)", "Accept": "*/*"}
IDCOL = {"datasets": "dataset_id", "tools": "tool_id", "interventions": "intervention_id", "existing_work": "work_id", "problems": "problem_id"}

def links():
    for f in sorted(os.listdir(os.path.join(ROOT, "data"))):
        table = f[:-4]
        if not f.endswith(".csv") or table.startswith("candidate_") or (ONLY and table != ONLY): continue
        for r in csv.DictReader(open(os.path.join(ROOT, "data", f), encoding="utf-8")):
            rid = r.get(IDCOL.get(table, ""), "") or r.get("problem_id", "")
            for k, v in r.items():
                if v and re.match(r"https?://", v): yield table, rid, k, v.strip()

def check(url, depth=0):
    target = url.split("#")[0]
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(target, headers=UA, method=method)
            with urllib.request.urlopen(req, timeout=25, context=ssl.create_default_context()) as res:
                final = res.geturl()
                same = urllib.parse.urlsplit(final).netloc.replace("www.", "") == urllib.parse.urlsplit(target).netloc.replace("www.", "") and \
                       urllib.parse.urlsplit(final).path.rstrip("/") == urllib.parse.urlsplit(target).path.rstrip("/")
                return ("ok" if same else "moved"), final, str(res.status)
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (400, 403, 405, 406, 501): continue      # some sites refuse HEAD; try GET
            if e.code in (301, 302, 303, 307, 308) and e.headers.get("Location"):   # redirects urllib does not follow by itself
                nxt = urllib.parse.urljoin(target, e.headers["Location"])
                if nxt != target and depth < 4:
                    s2, f2, n2 = check(nxt, depth + 1)
                    return ("moved" if s2 in ("ok", "moved") else s2), (f2 or nxt), n2
            if e.code in (401, 402, 403, 429): return "blocked", "", str(e.code)
            return "broken", "", str(e.code)
        except Exception as e:
            if method == "HEAD": continue
            msg = type(e).__name__ + ": " + str(e)[:80]
            # a refused connection or a certificate Python can't check is usually the site rejecting scripts, not a dead page
            if "ConnectionReset" in msg or "CERTIFICATE_VERIFY_FAILED" in msg: return "blocked", "", msg
            return "broken", "", msg
    return "broken", "", "no answer"

def main():
    rows = list(links()); uniq = sorted({u for *_, u in rows})
    print(f"{len(rows)} links, {len(uniq)} distinct. Checking…")
    res = {}
    with cf.ThreadPoolExecutor(8) as ex:
        for n, (u, out) in enumerate(zip(uniq, ex.map(check, uniq)), 1):
            res[u] = out
            if out[0] != "ok": print(f"  {out[0]:8} {out[2]:>5}  {u}")
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    path = os.path.join(ROOT, "build", "link_report.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["table", "row", "column", "url", "status", "final_url", "note", "checked"])
        for t, rid, k, u in rows: w.writerow([t, rid, k, u, *res[u], time.strftime("%Y-%m-%d")])
    tally = {}
    for s, *_ in res.values(): tally[s] = tally.get(s, 0) + 1
    print("done:", ", ".join(f"{v} {k}" for k, v in sorted(tally.items())), "->", os.path.relpath(path, ROOT))

if __name__ == "__main__":
    main()
