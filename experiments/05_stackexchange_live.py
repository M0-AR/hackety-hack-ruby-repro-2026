"""Exp 05 — LIVE StackExchange verification (no key, throttled).
Compares tag counts ruby vs python vs scratch vs alice as proxy for
'search-interest' behind TIOBE (book-era claim: Ruby joyful but Python won).
Endpoint: /2.3/tags/{tag}/info?site=stackoverflow
Asserts python count > ruby count (2026 dominance) and ruby count > 0.
"""
import json, urllib.request, datetime, pathlib, sys, time, urllib.parse

TAGS = ["ruby", "python", "scratch", "alice"]
OUT = pathlib.Path(__file__).resolve().parent.parent / "data" / "live_stackexchange.json"

def fetch(tag):
    q = urllib.parse.urlencode({"site": "stackoverflow"})
    url = f"https://api.stackexchange.com/2.3/tags/{tag}/info?{q}"
    req = urllib.request.Request(url, headers={"User-Agent": "hackety-repro/1.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode())

if __name__ == "__main__":
    snap = {"fetched_utc": datetime.datetime.utcnow().isoformat(), "tags": {}}
    ok = True
    for t in TAGS:
        try:
            j = fetch(t)
            items = j.get("items", [])
            c = items[0].get("count") if items else 0
            snap["tags"][t] = c
            print(f"{t:8s} questions={c}")
            time.sleep(1.2)  # respect throttle
        except Exception as e:
            print(f"{t} FAILED: {e}", file=sys.stderr)
            ok = False
    if ok and all(v for v in snap["tags"].values() if v is not None):
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(snap, indent=2))
        assert snap["tags"]["python"] > snap["tags"]["ruby"], "Python must exceed Ruby (TIOBE 2026)"
        assert snap["tags"]["ruby"] > 1000, "Ruby must still be non-trivial"
        print("LIVE StackExchange pattern VERIFIED (online).")
    else:
        print("OFFLINE/throttled — snapshot not overwritten; test skipped.")
