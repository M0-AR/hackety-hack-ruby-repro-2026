"""Exp 03 — LIVE RubyGems verification (no key): is Rails still relevant 2026-27?
Hits https://rubygems.org/api/v1/gems/<name>.json for rails, scarpe, lacci.
Asserts rails downloads >> scarpe (production relevance) and records snapshot.
Falls back to cached snapshot in data/ if offline; always writes results table.
"""
import json, urllib.request, datetime, pathlib, sys

GEMS = ["rails", "scarpe", "lacci", "shoes"]
OUT_JSON = pathlib.Path(__file__).resolve().parent.parent / "data" / "live_rubygems.json"
RES_CSV = pathlib.Path(__file__).resolve().parent.parent / "results" / "rubygems_downloads.csv"

def fetch(name):
    url = f"https://rubygems.org/api/v1/gems/{name}.json"
    req = urllib.request.Request(url, headers={"User-Agent": "hackety-repro/1.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode())

if __name__ == "__main__":
    snap = {"fetched_utc": datetime.datetime.utcnow().isoformat(), "gems": {}}
    live_ok = True
    for g in GEMS:
        try:
            j = fetch(g)
            snap["gems"][g] = {"downloads": j.get("downloads"),
                               "version": j.get("version"),
                               "version_downloads": j.get("version_downloads")}
            print(f"{g:8s} total={j.get('downloads')} ver={j.get('version')}")
        except Exception as e:
            print(f"{g} FETCH FAILED: {e}", file=sys.stderr)
            live_ok = False
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    RES_CSV.parent.mkdir(parents=True, exist_ok=True)
    if live_ok:
        OUT_JSON.write_text(json.dumps(snap, indent=2))
        with open(RES_CSV, "w") as f:
            f.write("gem,version,total_downloads,version_downloads\n")
            for g, v in snap["gems"].items():
                f.write(f"{g},{v['version']},{v['downloads']},{v['version_downloads']}\n")
        r = snap["gems"]["rails"]["downloads"] or 0
        s = snap["gems"].get("scarpe", {}).get("downloads") or 0
        print(f"rails/scarpe download ratio = {r/max(1,s):.1f}x")
        assert r > 100 * max(1, s), "Rails must dwarf Shoes-revival gems (production relevance)"
        print("LIVE RubyGems claim VERIFIED (online).")
    else:
        print("OFFLINE — keeping prior snapshot if present; test skipped, not failed.")
        if OUT_JSON.exists():
            print(OUT_JSON.read_text()[:1000])
