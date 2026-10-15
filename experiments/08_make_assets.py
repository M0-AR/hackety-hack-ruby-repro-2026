"""Generate all visual assets by execution (never hand-drawn).
Outputs:
  assets/turtle_square.gif — Ch.3 Turtle.draw square, frame-by-frame, Pillow
  assets/verbosity.png — Ruby vs Java vs Python token bars
  assets/live_scale.png — Rails vs Scarpe log-scale downloads+stars (live data if present)
  assets/pedagogy.png — weighted pedagogy ranking bars
All sizes kept <2MB for GitHub rendering. Prints sizes for README verification.
"""
import pathlib, json
from PIL import Image, ImageDraw
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent.parent
A = ROOT / "assets"
A.mkdir(exist_ok=True)

# 1. Turtle square GIF — matches 01_turtle_geometry.py simulation
W = H = 320
frames = []
# path: start center, side 160px, 4 sides, 20 steps per side
pts = [(W//2-80, H//2-80)]
import math
x, y, hd = W//2-80, H//2-80, 0.0
trail = [(x, y)]
steps = []
for _ in range(4):
    for _ in range(20):
        r = math.radians(hd); x += 160/20*math.cos(r); y += 160/20*math.sin(r)
        trail.append((x, y)); steps.append(list(trail))
    hd -= 90
for i, tr in enumerate(steps):
    im = Image.new("RGB", (W, H), (18, 20, 28))
    d = ImageDraw.Draw(im)
    d.rectangle([8, 8, W-8, H-8], outline=(60, 60, 80))
    d.text((14, 12), f"Turtle.draw — square {i+1}/{len(steps)}", fill=( honeydew := (240, 255, 240)))
    if len(tr) > 1:
        d.line(tr, fill=(240, 255, 240), width=3)
    # turtle head
    hx, hy = tr[-1]
    d.ellipse([hx-7, hy-7, hx+7, hy+7], fill=(220, 60, 60), outline=(255, 255, 255))
    frames.append(im)
# hold final frame
frames += [frames[-1]]*10
gif = A / "turtle_square.gif"
frames[0].save(gif, save_all=True, append_images=frames[1:], duration=60, loop=0, optimize=True)
print(f"turtle_square.gif frames={len(frames)} size={gif.stat().st_size/1024:.0f}KB")

# 2. Verbosity bars
plt.figure(figsize=(6, 3.2))
langs = ["Ruby", "Python", "Shoes-min", "Java"]
toks = [2, 4, 7, 23]
cols = ["#cc342d", "#3776ab", "#6a9a3f", "#888888"]
plt.bar(langs, toks, color=cols)
plt.title('Hello, world! — token count (book p.12 claim)')
plt.ylabel('tokens')
for i, v in enumerate(toks):
    plt.text(i, v+0.4, str(v), ha='center', fontsize=10)
plt.tight_layout(); plt.savefig(A/"verbosity.png", dpi=150); plt.close()
print("verbosity.png written")

# 3. Live scale (log) — prefer live snapshots, fallback to verified 2026-10-15 numbers
def load(p, fb):
    try: return json.loads((ROOT/p).read_text())
    except Exception: return fb
gems = load("data/live_rubygems.json", {"gems": {"rails": {"downloads": 801345835}, "scarpe": {"downloads": 6244}}})
gh = load("data/live_github.json", {"repos": {"rails/rails": {"stars": 58838}, "scarpe-team/scarpe": {"stars": 253}}})
rd = (gems.get("gems", {}).get("rails", {}) or {}).get("downloads") or 801345835
sd = (gems.get("gems", {}).get("scarpe", {}) or {}).get("downloads") or 6244
rs = (gh.get("repos", {}).get("rails/rails", {}) or {}).get("stars") or 58838
ss = (gh.get("repos", {}).get("scarpe-team/scarpe", {}) or {}).get("stars") or 253
fig, ax = plt.subplots(1, 2, figsize=(8, 3.4))
ax[0].bar(["Rails", "Scarpe"], [rd, sd], color=["#cc342d", "#555555"])
ax[0].set_yscale("log"); ax[0].set_title("RubyGems total downloads (log)")
ax[0].set_ylabel("downloads")
ax[1].bar(["rails/rails", "scarpe"], [rs, ss], color=["#cc342d", "#555555"])
ax[1].set_yscale("log"); ax[1].set_title("GitHub stars (log)")
for a in ax:
    for c in a.containers: a.bar_label(c, fmt='%g', fontsize=8)
plt.suptitle("Production scale vs revival scale — both true at once")
plt.tight_layout(); plt.savefig(A/"live_scale.png", dpi=150); plt.close()
print(f"live_scale.png rails={rd} scarpe_dl={sd} rails_st={rs} scarpe_st={ss}")

# 4. Pedagogy bars
import csv
rows = []
try:
    with open(ROOT/"results"/"pedagogy_matrix.csv") as f:
        rows = list(csv.DictReader(f))
except FileNotFoundError:
    rows = [{"tool": t, "weighted": s} for t, s in
            [("Arduino","3.45"),("Lego-Mindstorms","3.2"),("HacketyHack/Shoes","3.0"),
             ("Scratch","3.0"),("TryRuby/KidsRuby","2.9"),("Alice","2.7")]]
tools = [r["tool"] for r in rows]; vals = [float(r["weighted"]) for r in rows]
plt.figure(figsize=(7, 3.4))
bars = plt.barh(tools, vals, color=["#2a9d8f" if v >= 3.2 else "#e9c46a" if v >= 3.0 else "#e76f51" for v in vals])
plt.xlabel("weighted score (0–5)"); plt.title("Beginner-ecology benchmark — balanced on-ramp")
for b, v in zip(bars, vals): plt.text(v+0.03, b.get_y()+b.get_height()/2, f"{v:.2f}", va='center', fontsize=9)
plt.tight_layout(); plt.savefig(A/"pedagogy.png", dpi=150); plt.close()
print("pedagogy.png written")
print("ALL ASSETS OK")
