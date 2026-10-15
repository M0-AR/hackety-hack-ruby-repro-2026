# From _why to 2026: Reproducibly Benchmarking Hackety Hack, Ruby and the Beginner-Programming Ecology

**A from-scratch, live-data-verified replication + extension study — no local code reused.**

> `hackety-hack-ruby-repro-2026/` — experiments, Docker reproduction, and a publishable paper draft
> for Rauf (2015) *Getting to Know Hackety Hack* (Rosen, Code Power series, Grades 5–8).

## Abstract

We revisit a 2015 teen-programmer book centred on **Hackety Hack + Ruby + Shoes** and ask what
still holds in October 2026. Combining (i) headless re-execution of the book's core code claims,
(ii) live public-API measurements (RubyGems, GitHub, StackExchange, 2026-10-15 UTC), (iii) current
TIOBE / vendor data, and (iv) two 2026 systematic reviews + three meta-analyses of block-based
pedagogy, we benchmark six beginner ecologies the book introduces:
**Hackety Hack/Shoes, Scratch, Alice, Arduino, Lego Mindstorms, TryRuby/KidsRuby**.

**Verified findings (all scripts pass, live snapshots in `data/`):**

| Claim (book, ch.) | 2026 verdict | Evidence |
|---|---|---|
| `Turtle.draw` square: `forward 50` + `turnright 90` ×4; `4.times` ≡ unrolled (Ch.3) | ✅ **PASS** closure err `0.0`, generalises to n-gons | `01_turtle_geometry.py` |
| Ruby `print "Hello, world!"` (1 line) vs Java 5-line boilerplate (p.12) | ✅ **PASS** 11.5× token ratio | `02_verbosity_benchmark.py` |
| "Many companies use Rails" (Twitter/Hulu era examples, Ch.2) | ✅ **PASS, updated** — Rails 8.1.4, **801 M** downloads; GitHub/Shopify/GitLab still on Rails per 2026-09 vendor audits | `03`, `04` live; Monterail/LlamaPress Sep-2026 |
| Ruby joyful/beginner-suitable (Matz/MINSWAN, Ch.2) | ✅ **PASS pedagogically, FAIL by search-share** — TIOBE Oct-2026 Ruby **0.53 % (#28)** vs Python **19.23 % (#1)** | TIOBE + `05` (SO: py 2.2 M vs rb 229 k) |
| Hackety Hack runs today (Ch.3–5) | ⚠️ **PARTIAL** — original idle since ~2019; **revival real**: Scarpe 253★ pushed 2026-10-01, v0.5.0 Dec-2025; clogs 0.1.0 Aug-2026 boots Hackety Hack headless | `04` live + Largo/hacketyhack + scarpe-team/scarpe |

**Three pre-registered hidden patterns (3/3 PASS, `07_hidden_patterns.py`):**

1. **H1 Joy-vs-scale paradox** — best first language ≠ most-searched language (36× Python/Ruby TIOBE gap while Hackety scores ease 5/5, transfer 5/5).
2. **H2 Physicality premium** — Arduino/Lego mean 3.33 > screen-only mean 2.90, matching meta-analytic `g≈0.72` (physicality) > `g≈0.44` (visualisation); the book under-weights the two pages on Arduino/Lego vs evidence.
3. **H3 Revival decoupling** — Scarpe/clogs activity is genuinely recent yet 2 orders below Rails (232× star gap): revival ≠ popularity reversal.

## 1. Why this study (and why from scratch)

The user brief required: *no local-repo reuse; build new; README must read as a publishable paper;
benchmark SOTA; surface a hidden pattern for a future PhD; verify against live/public data with
2026–27 best practices; one-at-a-time web search with backoff; Docker-Compose reproduction.*

We therefore created this folder empty and grounded every number either in executed code or in a
dated public source (§6). Search was sequential (websearch → DuckDuckGo → OpenResearch →
paper-search → agent-reach → wiki → GSD/HN/SO → Kaggle → GitMCP) to respect 429 limits.

## 2. What the book actually claims (paraphrase, not quotation)

- **Ch.1 (_why / Gillette):** "Little Coder's Predicament" (2009 Art&&Code): 1980s BASIC machines (C64/Atari-800) gave instant `one line → visible result`; modern consoles/phones do not; fix = ship an easy language with devices. Action: *(Poignant) Guide to Ruby* (2004, comics + foxes) then Hackety Hack IDE (2005 conf) teaching Ruby ground-up, zero prerequisites.
- **Ch.2 (Ruby):** Matz 1993–95 (Perl/Smalltalk/Eiffel/Ada/Lisp synthesis), OOP vs procedural, Japan-only until v1.3/1999, RoR 2006 (Hansson/Basecamp) scaffolding + form-input idiom; MINSWAN ethos; Redmond (NYPL/Guggenheim/Brooklyn Museum) case: scaffolding → Fahrenheit→Celsius tool; "learn A+B ⇒ infer C".
- **Ch.3 (Start hacking):** Hackety Mouse icon → turtle + `Editor → Turtle.draw` → `background maroon` → `pencolor honeydew; forward 50` → square via `turnright 90` → `4.times` refactor → `alert "Hello, world!"` → `ask` quiz + too-high/too-low → knock-knock → Shoes stacks (vertical) / flows (horizontal) + `Shoes.rb` manual.
- **Ch.4 (What I made):** Pong/Space-Invaders/Connect-Four/Birthday/Devin-smelly; TryRuby (`6*4 ⇒ 24`, `"David".reverse ⇒ divaD`, `[12,47,35].max/.sort`, toast→honeydew poem); KidsRuby/Ruby4Kids Falling-Blocks + Gosu callbacks/main-loop; Scratch (MIT Media Lab 2007, 800 k users/1 M projects then) drag-drop blocks; Alice (Pausch, drag-drop + Sims-2, Alice 3.0 ↔ Java); Arduino (~$30, sensors, tweeting oven, e-dice, Puff dragon); Lego Mindstorms (MIT Media Lab, Java/Lua escape hatch).
- **Ch.5 (Further):** Automator/AutoHotkey birthdays; HTML (20-min) + CSS → JavaScript (Greasemonkey) → PHP/Python/Perl/Webmonkey; Pash MixTape.me (RoR + Prototype + Flash MP3); App-Store gold-rush (900 k apps/50 B downloads then); critics box: 4 lessons, no error messages, crashy (CommonSenseMedia).
- **Back-matter:** Glossary (OOP, open-source, loop/stack…), AITP/CATA/NAP/TryComputing, 20+ further-reading titles, 20+ bibliography URLs (retrieved Oct-2013).

We test the *falsifiable* subset; historical anecdotes are treated as context, not claims.

## 3. Method (reproducible by design)

```
python 01 (geometry) → 02 (verbosity) → 03 (RubyGems LIVE) → 04 (GitHub LIVE)
→ 05 (StackExchange LIVE) → 06 (pedagogy matrix + sensitivity) → 07 (H1-H3)
bash run_all.sh  ==  docker compose up research   # pinned images below
```

- **Headless > GUI** for CI: turtle is simulated (heading integration); Shoes DSL asserted by LOC/token + optional `lacci` load in `verify_book_claims.rb` (Ruby 3.3 container).
- **Live > scraped:** RubyGems `/api/v1/gems/{rails,scarpe,lacci,shoes}.json`; GitHub `/repos/{rails/rails,scarpe-team/scarpe,shoes/shoes4,hacketyhack/hacketyhack}`; StackExchange `/2.3/tags/{ruby,python,scratch,alice}/info`. Snapshots timestamped in `data/live_*.json`; offline fallback *skips* rather than fakes.
- **Matrix > vibes:** 5 dimensions × 0–5 rubric (PAPER.md §3.4), weights `ease .25, oop .20, phys .20, transfer .20, community .15`; sensitivity = 60 single-cell ±1 perturbations, require ≥80 % top-rank stability (achieved 100 %).
- **Pre-registration:** H1–H3 thresholds fixed in `07` before live pulls (repo history shows code before `data/`).

## 4. Results (live numbers, 2026-10-15)

### 4.1 Code claims hold exactly

- Square closure `0.000000000000`; n ∈ {3,4,5,6,8} all `<1e-9`; P=200 A=2500 for 50 px square.
- Ruby 1 LOC / 2 toks; Java 5 LOC / 23 toks (11.5×); Shoes-min 3 LOC — "joyful terseness" is measurable.

### 4.2 Production Ruby is alive, beginner Ruby is niche — both true at once

- **RubyGems (live):** rails 8.1.4 — 801,345,835 total; scarpe 0.5.0 — 6,244; lacci — 4,556; shoes 3.0.1 — 75,246. Rails/scarpe ≈ **128,339×**.
- **GitHub (live):** rails/rails 58,838★ (pushed today); scarpe-team/scarpe 253★ (pushed 2026-10-01); shoes/shoes4 1,608★ (stalled 2023-11); hacketyhack/hacketyhack 456★ (touched 2026-07). Rails/scarpe ≈ **233×**.
- **StackOverflow tags (live):** python 2,204,234 > ruby 229,116 > scratch 299 > alice 24.
- **TIOBE Oct-2026 (tiobe.com + TechRepublic 2026-10-13):** Python 19.23 %, Ruby 0.53 % (#28), Scratch 1.27 % (#12 in Jul-2026), Rust #10, Julia re-enters #18. Ruby was #30 Mar-2025 ("no need for Ruby anymore" — Jansen) then #16 Aug-2026 (+10 YoY): volatile tail, stable story = Python dominance.
- **Vendor cross-check Sep-2026:** GitHub, Shopify, GitLab, Basecamp/HEY, Doximity still on Rails (engineering blogs + Rails Foundation cases, read 2026-09-04); 48-company list (GitHub/Shopify/Airbnb/Twitch/Tesla…) — book's *examples* aged (Twitter/Hulu) but *thesis* ("Rails runs real companies") verifies stronger.

### 4.3 Revival is real and inspectable

- Scarpe (Italian for shoes): Lacci DSL + swappable display (Webview default, native Rust painter, WASM); requires Ruby ≥3.2; `scarpe 0.5.0` Dec-2025; native backend "feature complete with Shoes" per maintainers; Ruby Weekly #819 (2026-10-01) + #788 feature it.
- clogs (Aug-2026, MIT, `Largo/hacketyhack`): Shoes-on-libui on plain CRuby, no JVM/browser; boots `ruby hacketyhack.rb` (splash/tabs/Home render; 11/12 Shoes samples unmodified); editor "takes text but unfinished; online features point at dead server" — matches book's critic box, 11 years later.
- shoes4 (JRuby/SWT) stalled; original Hackety Hack OpenHub: 5,424 LOC, 0 active contributors, last meaningful push ~2019 — preservation, not development, until Scarpe/clogs.

### 4.4 Pedagogy benchmark (see `results/pedagogy_matrix.csv`)

Ranked weighted: Arduino 3.45 > Lego 3.20 > Hackety/Shoes 3.00 = Scratch 3.00 > TryRuby 2.90 > Alice 2.70.
Grounded in: Sun et al. 2026 JCAL (46-study PRISMA: task/social/tech approaches; age/gender/difficulty moderators; "unstructured interface + abstract-CT + trial-and-error" challenges); Hu et al. block-meta `g=0.47`; Costa & Miranda Alice meta `d=0.54 [0.34,0.74]`; Xu et al. block-vs-text; 2020 programming-intervention meta (`g=0.81` per se; physicality `0.72` > visualisation `0.44`; Scratch visualisation esp. effective).

## 5. Hidden patterns → PhD seeds (all PASS, `results/hidden_patterns.md`)

**H1 Joy-vs-scale paradox (36.3×).** TIOBE counts *tutorial-search volume*, not learning joy or retention. Ruby can be the better *first* language (1-line hello, `learn A+B⇒C`, MINSWAN help) while Python wins *search-share* (AI/data/jobs). *Seed:* longitudinal joy-retention vs search-share dissociation (n≈300, novices randomised to Ruby-via-Hackety/Scarpe vs Python, 12-week retention + transfer test).

**H2 Physicality premium (+0.43).** The book's Ch.5 buries Arduino/Lego yet evidence says physicality beats pure visualisation. *Seed:* RCT physical (Arduino/Lego) vs screen (Scratch/Hackety) with identical CT targets + delayed transfer to text Ruby/Python.

**H3 Revival decoupling (233×, pushed 2 weeks ago).** OSS revivals can be technically complete and culturally alive (Discord, Ruby Weekly, WASM demos) without reversing popularity. *Seed:* ethnography of Shoes→Shoes4→Scarpe→clogs: why _why's 2007 DSL keeps being resurrected (whimsy + "few lines → window" + packaging pain).

## 6. Sources (dated; full URLs in PAPER.md)

TIOBE Oct/Aug/Jul-2026 + methodology (Mandarin terms added Oct-2026); InfoWorld 2026-03-10 (Ruby #30); Rollbar Jun-2026 (Ruby #20 mid-year, >1 M GitHub Rubyists); TechRepublic 2026-10-13; idogawa clogs 2026-09-29; Largo/hacketyhack (created 2026-08-09); scarpe-team/scarpe (224★, Ruby ≥3.2, FOR_AGENTS.md); RubyGems scarpe 0.5.0 Dec-2025; shoes4 #1586 ("Is Shoes dead?"); OpenHub HacketyHack (535 commits/32 contributors, 0 in last 12 mo); Monterail/LlamaPress/TechVinta/Arc Sep-2026 Rails employer audits; Sun et al. JCAL 2026-03-11; SAGE/Hu, BJET/Costa, CSE/Xu metas; Wikipedia Hackety Hack / _why; HN "Teaching a 10-year-old"; SO Shoes threads; Kaggle (null — no Ruby beginner datasets, itself a finding).

## 7. Reproduce (Docker, 2 commands)

```bash
# local (Python 3.12, no keys)
pip install -r requirements.txt
bash run_all.sh   # writes data/live_*.json + results/

# docker (pinned)
docker compose config          # validates
docker compose up research     # python:3.12-slim, runs full suite
docker compose run ruby ruby experiments/verify_book_claims.rb  # ruby:3.3-slim
docker compose --profile notebook up notebook  # Jupyter on :8888
```

Images: `python:3.12-slim`, `ruby:3.3-slim`, `jupyter/minimal-notebook:python-3.12`.
Network needed only for Exps 03–05; offline they skip (never fake) and 01/02/06/07-stale still pass.

## 8. Limitations & threats

- TIOBE = search interest, not code-in-prod (we triangulate with downloads/stars/tags).
- GitHub stars/downloads are popularity, not quality; SO counts conflate novices + pros.
- Pedagogy scores are expert-curated from reviews, not a new RCT — sensitivity-tested but still prior-dependent; weights are stated so others can re-weight (`06` is 60 lines).
- Scarpe/clogs move weekly; pin your re-run date (ours: 2026-10-15) and re-pull `data/`.
- Book OCR supplied by user; we paraphrase, never republish — fair-use scholarship.

## 9. What to cite / reuse

- `PAPER.md` — full publishable draft (IMRaD + rubrics + threats + PhD roadmap).
- `experiments/01–07` + `verify_book_claims.rb` — copy-paste runnable claims.
- `results/pedagogy_matrix.csv`, `rubygems_downloads.csv`, `hidden_patterns.md`.
- `CITATION.cff` — cite this repro, not the 2015 book, for numbers.

## 10. Future (your PhD on-ramp)

1. Run the H1 RCT (preregister joy + retention + transfer; use TryRuby + Scarpe-native + Scratch arms).
2. Instrument `ask/alert` micro-quiz from Ch.3 as a validated CT item bank.
3. Package a one-click Scarpe-native Hackety Hack for classrooms (fix editor + local-first programs, per clogs TODO) and measure vs Scratch on the same tasks.

---
*Built from zero, verified live, shared publicly. No local repo was read or reused. AI-use disclosure:
LLM assisted boilerplate + prose; all numbers are executed or dated-fetched, re-runnable via `run_all.sh`.*
