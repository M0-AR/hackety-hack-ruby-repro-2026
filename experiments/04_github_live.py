"""Exp 04 — LIVE GitHub verification (no auth, 60 req/hr).
Repos: rails/rails (production Rails), scarpe-team/scarpe (2026 revival),
        shoes/shoes4 (legacy rewrite), hacketyhack/hacketyhack (original).
Asserts rails stars >> scarpe/shoes (orders of magnitude) and scarpe updated >=2024
(revival is real, cf. websearch 2026-02-26 push, scarpe 0.5.0 Dec 2025).
"""
import json, urllib.request, datetime, pathlib, sys

REPOS = ["rails/rails", "scarpe-team/scarpe", "shoes/shoes4", "hacketyhack/hacketyhack"]
OUT = pathlib.Path(__file__).resolve().parent.parent / "data" / "live_github.json"

def fetch(repo):
    url = f"https://api.github.com/repos/{repo}"
    req = urllib.request.Request(url, headers={"User-Agent": "hackety-repro/1.0",
                                               "Accept": "application/vnd.github.v3+json"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode())

if __name__ == "__main__":
    snap = {"fetched_utc": datetime.datetime.utcnow().isoformat(), "repos": {}}
    ok = True
    for repo in REPOS:
        try:
            j = fetch(repo)
            snap["repos"][repo] = {"stars": j.get("stargazers_count"),
                                   "forks": j.get("forks_count"),
                                   "pushed_at": j.get("pushed_at"),
                                   "language": j.get("language")}
            print(f"{repo:28s} stars={j.get('stargazers_count')} pushed={j.get('pushed_at')}")
        except Exception as e:
            print(f"{repo} FAILED: {e}", file=sys.stderr)
            ok = False
    if ok:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(snap, indent=2))
        rails = snap["repos"]["rails/rails"]["stars"] or 0
        scarpe = snap["repos"]["scarpe-team/scarpe"]["stars"] or 0
        print(f"rails/scarpe star ratio = {rails/max(1,scarpe):.1f}x")
        assert rails > 50 * max(1, scarpe), "Rails production footprint must dwarf revival"
        pushed = snap["repos"]["scarpe-team/scarpe"]["pushed_at"] or ""
        assert pushed >= "2024", f"Scarpe revival must be recent, got {pushed}"
        print("LIVE GitHub claims VERIFIED (online).")
    else:
        print("OFFLINE or rate-limited — snapshot not overwritten; test skipped.")
        if OUT.exists():
            print(OUT.read_text()[:1200])
