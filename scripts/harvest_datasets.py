"""Find candidate datasets for each problem area through public catalog APIs, and write
data/candidate_datasets.csv for review. Nothing here is added to datasets.csv automatically:
promote rows by hand once a dataset checks out.

Sources (official APIs only; no page scraping):
  - Hugging Face Hub   https://huggingface.co/api/datasets?search=...
  - HDX (UN OCHA)      https://data.humdata.org/api/3/action/package_search?q=...   (CKAN)
  - Google Earth Engine public STAC catalog (weather, climate, land, buildings)
  - NASA Earthdata (CMR)  https://cmr.earthdata.nasa.gov/search/collections.json?keyword=...
  - NOAA NCEI            https://www.ncei.noaa.gov/access/services/search/v1/datasets?text=...
  - OpenAlex (papers, CC0) -> data/candidate_research.csv: most-cited open-access papers per area

Usage: python3 scripts/harvest_datasets.py        (stdlib only; needs internet)
Existing rows keep their status; new finds come in as status=candidate.
"""
import csv, json, sys, time, urllib.parse, urllib.request
from pathlib import Path

OUT = Path(__file__).parent.parent / "data" / "candidate_datasets.csv"
HEADER = ["area", "source", "source_id", "title", "url", "query", "license", "popularity", "status"]
UA = {"User-Agent": "ai-fixable-problems-db harvester (github.com/rheasrepos/ai-fixable-problems-db)"}

# area -> search terms. Areas are problem_ids, or new areas not yet written up as problems.
QUERIES = {
    "food-waste": ["food waste", "food loss", "food rescue", "food prices", "food security"],
    "dangerous-climate-conditions": ["flood", "heat wave", "extreme weather", "precipitation", "drought"],
    "shelter-scarcity": ["homelessness", "housing", "eviction", "informal settlements", "building footprints"],
    "living-wage-gap": ["wages", "salary", "cost of living", "job postings", "minimum wage"],
    "culture-and-language-preservation": ["endangered languages", "low-resource languages", "indigenous languages",
                                          "oral history", "cultural heritage", "flores"],
}
EE_KEYWORDS = {  # Earth Engine is searched by keyword match on title/keywords/description
    "dangerous-climate-conditions": ["temperature", "precipitation", "flood", "drought", "reanalysis", "era5"],
    "shelter-scarcity": ["building", "settlement", "population", "urban"],
    "food-waste": ["crop", "cropland", "agricultur"],
}
EARTH_QUERIES = {  # NASA and NOAA hold physical-world data, so only the areas where that fits
    "dangerous-climate-conditions": ["heat wave", "extreme temperature", "flood", "drought", "precipitation", "land surface temperature"],
    "food-waste": ["crop yield", "cropland", "food security", "agricultural drought"],
    "shelter-scarcity": ["population density", "human settlements", "urban extent"],
}
RESEARCH_QUERIES = {
    "food-waste": ["food waste", "food loss and waste"],
    "dangerous-climate-conditions": ["urban heat island", "flood early warning", "heat-related mortality"],
    "shelter-scarcity": ["homelessness", "eviction", "informal settlements"],
    "living-wage-gap": ["living wage", "minimum wage employment"],
    "raising-kids-in-a-digital-world": ["adolescent social media mental health", "cyberbullying", "AI companions adolescents"],
    "culture-and-language-preservation": ["endangered languages", "low-resource languages machine translation"],
}
RESEARCH_OUT = Path(__file__).parent.parent / "data" / "candidate_research.csv"
RESEARCH_HEADER = ["area", "openalex_id", "title", "url", "year", "cited_by", "query", "status"]
PER_QUERY = 15

def get(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))

def huggingface(area, q):
    url = "https://huggingface.co/api/datasets?" + urllib.parse.urlencode(
        {"search": q, "limit": PER_QUERY, "sort": "downloads", "direction": -1})
    for d in get(url):
        lic = next((t.split(":", 1)[1] for t in d.get("tags", []) if t.startswith("license:")), "")
        yield {"area": area, "source": "huggingface", "source_id": d["id"], "title": d["id"],
               "url": f"https://huggingface.co/datasets/{d['id']}", "query": q, "license": lic,
               "popularity": f"{d.get('downloads', 0)} downloads"}

def hdx(area, q):
    url = "https://data.humdata.org/api/3/action/package_search?" + urllib.parse.urlencode({"q": q, "rows": PER_QUERY})
    for d in get(url)["result"]["results"]:
        yield {"area": area, "source": "hdx", "source_id": d["name"], "title": d.get("title", d["name"]),
               "url": f"https://data.humdata.org/dataset/{d['name']}", "query": q,
               "license": d.get("license_title", ""), "popularity": (d.get("organization") or {}).get("title", "")}

def nasa_cmr(area, q):
    url = "https://cmr.earthdata.nasa.gov/search/collections.json?" + urllib.parse.urlencode({"keyword": q, "page_size": PER_QUERY})
    for d in get(url)["feed"]["entry"]:
        yield {"area": area, "source": "nasa_cmr", "source_id": d["id"], "title": d.get("title", d.get("short_name", d["id"])),
               "url": f"https://search.earthdata.nasa.gov/search?q={urllib.parse.quote(d.get('short_name', d['id']))}",
               "query": q, "license": "", "popularity": d.get("data_center", "")}

def noaa_ncei(area, q):
    url = "https://www.ncei.noaa.gov/access/services/search/v1/datasets?" + urllib.parse.urlencode({"text": q, "limit": PER_QUERY})
    for d in get(url).get("results", []):
        yield {"area": area, "source": "noaa_ncei", "source_id": d["id"], "title": d.get("name", d["id"]),
               "url": next((l.get("url") for l in (d.get("links") or {}).get("other", []) if isinstance(l, dict) and l.get("url")),
                           f"https://www.ncei.noaa.gov/access/search/dataset-search?text={urllib.parse.quote(d['id'])}"),
               "query": q, "license": "", "popularity": "NOAA NCEI"}

def openalex(area, q):
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode({
        "filter": f"title_and_abstract.search:{q},is_oa:true", "sort": "cited_by_count:desc", "per_page": PER_QUERY,
        "select": "id,display_name,publication_year,cited_by_count,open_access,doi"})
    for w in get(url)["results"]:
        link = (w.get("open_access") or {}).get("oa_url") or w.get("doi") or w["id"]
        yield {"area": area, "openalex_id": w["id"].rsplit("/", 1)[-1], "title": w.get("display_name") or "",
               "url": link, "year": w.get("publication_year") or "", "cited_by": w.get("cited_by_count") or 0, "query": q}

def harvest_research():
    old = {}
    if RESEARCH_OUT.exists():
        for r in csv.DictReader(open(RESEARCH_OUT, encoding="utf-8")): old[(r["area"], r["openalex_id"])] = r
    found = dict(old)
    for area, qs in RESEARCH_QUERIES.items():
        for q in qs:
            try:
                n = 0
                for row in openalex(area, q):
                    key = (row["area"], row["openalex_id"])
                    if key not in found and row["title"] and str(row["url"]).startswith("http"):
                        found[key] = {**row, "status": "candidate"}; n += 1
                print(f"{'openalex':12} {area:36} {q!r}: +{n}")
            except Exception as e:
                print(f"{'openalex':12} {q!r}: FAILED {e}")
            time.sleep(0.3)
    with open(RESEARCH_OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=RESEARCH_HEADER); w.writeheader()
        for r in sorted(found.values(), key=lambda r: (r["area"], -int(r["cited_by"] or 0))):
            w.writerow({k: str(r.get(k, "")).replace("\n", " ") for k in RESEARCH_HEADER})
    print(f"wrote {len(found)} research candidates to {RESEARCH_OUT} ({len(found) - len(old)} new)")

def earth_engine():
    roots = ["https://storage.googleapis.com/earthengine-stac/catalog/catalog.json",
             "https://earthengine-stac.storage.googleapis.com/catalog/catalog.json"]
    root = None
    for r in roots:
        try: root = get(r); base = r.rsplit("/", 1)[0]; break
        except Exception as e: print(f"  earth engine: {r} failed ({e})")
    if not root: return
    def walk(node, base, depth=0):
        for link in node.get("links", []):
            if link.get("rel") != "child" or depth > 3: continue
            href = urllib.parse.urljoin(base + "/", link["href"])
            try: child = get(href)
            except Exception: continue
            if child.get("type") == "Collection" or "extent" in child:
                yield child
            else:
                yield from walk(child, href.rsplit("/", 1)[0], depth + 1)
            time.sleep(0.05)
    for c in walk(root, base):
        hay = " ".join([c.get("title", ""), c.get("description", "")[:500], " ".join(c.get("keywords", []))]).lower()
        for area, kws in EE_KEYWORDS.items():
            hit = next((k for k in kws if k in hay), None)
            if hit:
                yield {"area": area, "source": "earth_engine", "source_id": c["id"], "title": c.get("title", c["id"]),
                       "url": f"https://developers.google.com/earth-engine/datasets/catalog/{c['id'].replace('/', '_')}",
                       "query": hit, "license": c.get("license", ""), "popularity": ""}

def main():
    old = {}
    if OUT.exists():
        for r in csv.DictReader(open(OUT, encoding="utf-8")):
            old[(r["area"], r["source"], r["source_id"])] = r
    found, errors = dict(old), []
    for area, qs in QUERIES.items():
        for q in qs:
            for name, fn in (("huggingface", huggingface), ("hdx", hdx)):
                try:
                    n = 0
                    for row in fn(area, q):
                        key = (row["area"], row["source"], row["source_id"])
                        if key not in found: found[key] = {**row, "status": "candidate"}; n += 1
                    print(f"{name:12} {area:36} {q!r}: +{n}")
                except Exception as e:
                    errors.append(f"{name} {q!r}: {e}"); print(f"{name:12} {q!r}: FAILED {e}")
                time.sleep(0.3)
    for area, qs in EARTH_QUERIES.items():
        for q in qs:
            for name, fn in (("nasa_cmr", nasa_cmr), ("noaa_ncei", noaa_ncei)):
                try:
                    n = 0
                    for row in fn(area, q):
                        key = (row["area"], row["source"], row["source_id"])
                        if key not in found: found[key] = {**row, "status": "candidate"}; n += 1
                    print(f"{name:12} {area:36} {q!r}: +{n}")
                except Exception as e:
                    errors.append(f"{name} {q!r}: {e}"); print(f"{name:12} {q!r}: FAILED {e}")
                time.sleep(0.3)
    print("earth engine catalog (takes a few minutes)...")
    try:
        n = 0
        for row in earth_engine():
            key = (row["area"], row["source"], row["source_id"])
            if key not in found: found[key] = {**row, "status": "candidate"}; n += 1
        print(f"earth_engine: +{n}")
    except Exception as e:
        errors.append(f"earth_engine: {e}")
    rows = sorted(found.values(), key=lambda r: (r["area"], r["source"], r["source_id"]))
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADER); w.writeheader()
        for r in rows: w.writerow({k: (r.get(k) or "").replace("\n", " ") for k in HEADER})
    print(f"\nwrote {len(rows)} candidates to {OUT} ({len(rows) - len(old)} new)")
    if errors: print("errors:", *errors, sep="\n  ")

if __name__ == "__main__":
    main()
    harvest_research()
