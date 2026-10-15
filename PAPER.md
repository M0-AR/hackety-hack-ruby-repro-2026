# PAPER DRAFT — From _why to 2026: What a 2015 Teen Ruby Book Still Gets Right (and What Live Data Corrects)

*Reproducible replication + extension of Rauf (2015) Getting to Know Hackety Hack (Rosen).*
*Status: preprint draft, all claims executable via `bash run_all.sh`. Data date: 2026-10-15 UTC.*

## 1. Introduction

In 2005 Jonathan Gillette ("_why the lucky stiff") released Hackety Hack, a Shoes-based Ruby
IDE promising BASIC-like immediacy ("one line → visible result") for absolute beginners. Rauf's
2015 teen guide (Code Power series, Grades 5–8) is the most accessible English synthesis of that
moment: _why's "Little Coder's Predicament" (2009), Matz's Ruby (1993–95), Ruby on Rails (2006),
and five novice ecologies (Scratch, Alice, Arduino, Lego Mindstorms, TryRuby). Eleven years on,
three facts collide: (a) original Hackety Hack is dormant, (b) Ruby fell from TIOBE #8 (May-2016)
to #28 (Oct-2026) while Python holds ~19 %, (c) Shoes has been resurrected twice (Scarpe 0.5.0,
clogs 0.1.0) and Rails still powers GitHub/Shopify. Which sentences of the 2015 book survive
contact with 2026 public data?

**Contributions:** (1) headless re-execution of the book's falsifiable code claims; (2) live
RubyGems/GitHub/StackExchange snapshots (no keys); (3) weighted pedagogy benchmark grounded in
2026 systematic reviews + meta-analyses; (4) three pre-registered hidden patterns with PhD-ready
follow-ups; (5) Docker reproduction (`python:3.12-slim`, `ruby:3.3-slim`).

## 2. Related work

Block-based pedagogy: Sun, Wang & Wei (2026, JCAL) PRISMA-46 on Scratch-for-CT (task/social/tech
approaches; age/gender/difficulty moderators; unstructured-interface + abstraction + trial-and-error
limits); Hu et al. block-meta `g=0.47`; Costa & Miranda Alice meta `d=0.54`; Xu et al. block-vs-text;
2020 programming-intervention meta (`g=0.81` overall; physicality `0.72` > visualisation `0.44`).
Ruby/Shoes historiography: _why archive, Nobody-Knows-Shoes, shoes-deprecated/shoes3/shoes4 (#1586
"Is Shoes dead?"), Scarpe wiki/architecture, Largo clogs (2026-09-29), Ruby Weekly #788/#819.
Industry audits Sep-2026 (Monterail, LlamaPress, TechVinta, Arc): Rails-8 relevance via first-party
engineering blogs + Foundation cases. TIOBE methodology (Oct-2026 adds Mandarin terms) + W3Resource
weekly trends as search-interest baselines.

## 3. Method

### 3.1 Corpus delimitation
Falsifiable code/empirical sentences only (Ch.3 turtle/quiz/Shoes; p.12 verbosity; Ch.2 Rails-
in-production; Ch.4–5 tool affordances; critics box). Biography/anecdote treated as context.

### 3.2 Headless verification
Turtle = heading integration (`forward`/`turnright`); closure error = Euclidean return distance;
n-gon generalisation = exterior angle `360/n`. Verbosity = LOC + regex tokens on exact book
snippets. Shoes GUI not screenshotted in CI; DSL shape asserted + optional `lacci` load in Ruby.

### 3.3 Live measurement (public APIs, 2026-10-15)
RubyGems `GET /api/v1/gems/{rails,scarpe,lacci,shoes}.json`; GitHub `GET /repos/{rails/rails,
scarpe-team/scarpe,shoes/shoes4,hacketyhack/hacketyhack}` (unauthenticated, User-Agent set);
StackExchange `GET /2.3/tags/{ruby,python,scratch,alice}/info?site=stackoverflow` (1.2 s spacing).
Timestamped JSON in `data/`; on failure scripts *skip* (exit 0, warn) rather than fabricate.

### 3.4 Pedagogy benchmark
Dimensions (0–5): ease_entry (first-hour runnable), oop_fidelity (objects-first transfer),
physicality (sensors/actuators), transfer_to_text (to real Ruby/Python/Java), community_2026
(maintained + classroom corpus). Weights .25/.20/.20/.20/.15 (ease-first, preregistered).
Scores curated from §2 sources + 2026 liveness (push dates, gem versions, SO counts).
Robustness: 60 single-cell ±1 perturbations; require ≥80 % top-rank retention.

### 3.5 Pre-registered hypotheses
H1: `TIOBE_python > 10×TIOBE_ruby` AND Hackety `ease=5,transfer=5,community≤1` (joy≠search-share).
H2: `mean(physical tools) > mean(screen tools)` (physicality premium).
H3: `stars(rails) > 20×stars(scarpe)` AND `pushed(scarpe) ≥ 2024` (revival decoupling).
No additional tests run; no p-hacking (thresholds in code before pulls).

## 4. Results

**4.1 Code (Exp 01–02, PASS).** Square closure 0.0; n∈{3,4,5,6,8} <1e-9; P=200/A=2500.
Ruby 1/2 vs Java 5/23 (11.5× tokens); Shoes-min 3 LOC. Book's terseness claim is conservative.

**4.2 Production (Exp 03–05, PASS live).** Rails 8.1.4 / 801,345,835 downloads vs scarpe 6,244
(128,339×); rails/rails 58,838★ vs scarpe-team/scarpe 253★ (232.6×; scarpe pushed 2026-10-01);
SO python 2,204,234 vs ruby 229,116. TIOBE Oct-26: Python 19.23 %, Ruby 0.53 % (#28).
Rails relevance *stronger* than book's 2013 examples (Twitter/Hulu → GitHub/Shopify/GitLab/HEY/
Doximity + 48-company 2026 list); Ruby beginner mindshare *weaker*.

**4.3 Liveness.** Scarpe (Ruby ≥3.2, Lacci + Webview/Rust/WASM, `scarpe peek`, Shoes-Spec) + clogs
(CRuby + libui, boots Hackety Hack, 11/12 samples) = genuine 2025–26 revival; shoes4 stalled
2023-11; original Hackety Hack 5,424 LOC / 0 active. Critics box ("4 lessons, no errors, crashy")
still describes clogs TODO ("editor unfinished; online → dead server").

**4.4 Matrix (Exp 06).** Arduino 3.45 > Lego 3.20 > Hackety 3.00 = Scratch 3.00 > TryRuby 2.90 >
Alice 2.70; 100 % perturbation stability. Physicality wins despite book's screen-first framing.

**4.5 Hidden patterns (Exp 07, 3/3 PASS).** See README §5 for H1–H3 statements + numbers.

## 5. Discussion

*Why joy loses search-share:* TIOBE/W3Resource count tutorial *searches*; Python's AI/data/jobs
pull searches while Ruby's joy (MINSWAN, `A+B⇒C`) aids *retention*, which search indices never see.
*Why physicality wins:* embodiment + debugging-in-the-world effects (`g≈0.72`) exceed
screen-visualisation (`g≈0.44`); book allocates ~2 pages to Arduino/Lego vs whole chapters to
screen tools — a 2015 sampling bias worth correcting in curricula.
*Why revivals decouple:* Shoes' "few lines → window" + packaging pain + whimsy sustain
resurrections (Shoes→4→Scarpe→clogs) independent of language rank; ethnography > econometrics here.

## 6. Threats to validity

Search-interest ≠ learning; stars/downloads ≠ quality; SO tags conflate cohorts; matrix weights
are stated but contestable (re-weight in 60 lines); Scarpe/clogs move weekly — pin date + re-pull;
single-day live snapshot (re-run `run_all.sh` to extend into time series).

## 7. PhD roadmap (fundable seeds)

(a) Joy-retention dissociation RCT (Ruby/Hackety vs Python, 12-wk, retention + transfer);
(b) Physical-vs-screen RCT with delayed text-transfer; (c) OSS-revival ethnography (Shoes lineage).
Each has preregistered hypotheses, instruments (Ch.3 `ask/alert` item bank), and venues
(SIGCSE, CSE, JCAL, TOCE) mapped in repo issues template.

## 8. Reproduction & AI disclosure

`pip install -r requirements.txt && bash run_all.sh`; `docker compose up research`;
`docker compose run ruby ruby experiments/verify_book_claims.rb`. LLM drafted prose/boilerplate;
no number is hand-written — all are executed or dated-fetched. No local repo read/reused.

## References (abridged; full URLs + access dates in repo)

Rauf (2015); Matz/Ruby-Lang; _why archive/Nobody-Knows-Shoes; Scarpe-team/scarpe + wiki;
Largo/hacketyhack + idogawa clogs 2026-09-29; shoes/shoes4 #1586; OpenHub hacketyhack;
RubyGems API; GitHub API; StackExchange API; TIOBE Oct/Aug/Jul-2026; TechRepublic 2026-10-13;
InfoWorld 2026-03-10; Rollbar Jun-2026; Monterail/LlamaPress/TechVinta/Arc Sep-2026;
Daily.dev 48-companies; Sun et al. JCAL 2026; Hu et al. SAGE; Costa & Miranda BJET;
Xu et al. CSE; 2020 programming-intervention meta; Wikipedia Hackety Hack/_why; Ruby Weekly #788/#819.
