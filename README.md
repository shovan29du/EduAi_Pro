# EduAi_Pro — All-Ages Learning Platform

EduAi_Pro is a learning platform that scales from early childhood through graduate school and adult professional development. It started as a children's education app and every child-safety default from that era is still in place; on top of it sits a full academic ladder (Grades 1–10, College C1–C2, Undergraduate UG1–UG4, Master's M1–M2) and a suite of adult-oriented resource centres — sports, world cuisine, a virtual art museum, and a general-purpose AI tutor — with no login required. Five profiles are switchable from the header: **Aliza** and **Saifan** (school-age learners), **Parent** (curation/oversight), and **Shovan** and **Bely** (full adult/college/university learner access plus curation).

A rule that holds across the entire codebase: **nothing is fabricated**. Every linked resource is a real, live URL to a genuine source; every biographical fact, historical claim, and quiz answer is something a human author is confident is true; and where no honest free source exists for a given resource type, the field is left empty rather than guessed at. Where content can't be individually verified in this environment (e.g. a specific video ID), it's shipped as a plain search-results link and explicitly marked unverified rather than presented as vetted.

## Feature tour

### Dashboard & core learning
- **Dashboard** — study timer, Fact of the Day, History of the Day, and Art of the Day (with a real image resolved live from Wikipedia), plus continue-learning and recommended-next-action widgets.
- **Subjects** — a persistent, explainable per-learner concept mastery map. Practice answers and lesson mini-checks update a Bayesian-style mastery estimate, schedule spaced reviews, track misconceptions, pick an adaptive difficulty, and recommend the next lesson with a visible reason.
- **Academic levels** — Grades 1–10 plus C1, C2 (college), UG1–UG4 (undergraduate), and M1, M2 (master's), each with its own curriculum minimum (20 lessons at Levels 1–3 up to 120 at M1–M2) and its own safety profile — genuinely harmful content is always blocked at every level, while child-only topic restrictions relax for college/university/adult levels.
- **Professional workspace** (adult/college/university) — research projects with local-document import and ranked search, bibliography/BibTeX export, configurable assessments, assignments, portfolios, career pathways, cohorts, discussions, and SCORM/xAPI/LTI export for institutional deployments.
- **Ark AI Tutor** — calls the Anthropic API directly (not a claude.ai consumer session); supports direct, Socratic, worked-example, and competing-perspectives modes, grounds answers in curriculum resources with citations, and ships a 367-prompt skill library, a 68-model catalogue, and 61 tools. Nine LLM providers beyond Claude (OpenAI, Gemini, Grok, Groq, Mistral, Together AI, Perplexity, Fireworks, DeepSeek, OpenRouter) can be configured from **Appearance → Ark AI Connection**, with automatic fallback to Claude if the chosen provider's call fails.

### Resource centres
- **Cuisine & Food Resource Centre** — the adult edition of the app, framed with no content restrictions beyond one dietary rule: every recipe is pork-free, with beef, lamb, mutton, or duck substituted where a dish is traditionally made with pork (noted transparently for well-known swaps like Carbonara or char siu). It covers:
  - **Cuisines** — 45 world cuisines with real history, geography, famous dishes, key ingredients, cooking techniques, cultural notes, and a quiz each.
  - **Recipes** — 1,900+ real, named dishes across 50 cuisines, filterable by cuisine, category (curry, soup, bread, rice, noodles, pasta, dumplings, grilled, dessert, ice cream, hot drinks, and more), protein (including a distinct Fish/Seafood/Duck split), and free-text ingredient search — each card links to a real thumbnail, a YouTube search, an image search, and a text guide.
  - **Cooking Techniques** — a glossary spanning dry-heat, moist-heat, preservation, general prep, and a dedicated knife-skills category (julienne, brunoise, chiffonade, tourné, and more), each with a picture, video link, text guide, and real recipes from the collection that use it.
  - **Food History**, **Herbs & Spices** (38 entries with live photos, uses, and substitutions), **Ingredient Alternatives** (including a dedicated halal-substitute list for haram ingredients like bacon, lard, and gelatin), **Cooking Problems & Fixes**, and **Measurement Equivalents**.
- **Virtual Museum** — 8,704 real, open-access objects across 23 galleries, presented in a Google Arts & Culture-style photo-tile layout with a day-rotating "Featured Today" spotlight and a virtual-tour link out to Google Arts & Culture per object. The largest gallery is built from the Cleveland Museum of Art's open-access catalogue by `backend/scripts/add_top_2000_museum_missing.py`, which is deterministic and idempotent — re-run it after raising its target count to pull in more of the bundled source list.
- **Sports Centre** — sports overviews, tournament histories (football, cricket, tennis World Cups and top leagues), and real player biographies.
- **Game Centre** — 50+ browser games (memory match, pattern recall, math sprints, word games, Sudoku, reaction games, and more) across several categories, with a day-rotating Daily Challenge, per-game difficulty tiers, cross-sibling leaderboards, and spaced-repetition-style scoring.
- **Practical Skills** — 30+ pathways spanning cooking, first aid, financial literacy, coding (Scratch and Python), typing, drawing, photography (including a 50-lesson Vivo X200 Pro mobile-photography pathway), public speaking, study/research skills, gardening, chess, fitness/martial arts (judo, boxing, taekwondo, Muay Thai, and more), and critical thinking.
- **Music & Instruments** — theory, singing, rhythm/ear training, world and classical music, and lessons for 11 instruments (piano, guitar, violin, drums, flute, saxophone, tabla, sitar, harmonium, keyboard, voice).
- **Other Subjects** — Environmental Science, World Politics, World Religions, Health, Business Studies, and Civics, grouped under one tab.
- **World Cinema** and **Song Centre** — the BFI *Sight and Sound* top-200 films with locally generated catalogue thumbnails and multi-platform discovery links, and a 500-song batch sourced from Kworb's all-time YouTube chart data (each retaining its rank, exact view count, and check date).
- **Countries**, **World Literature**, **Biographies**, **Survival Skills**, **STEM Lab**, **Non-Fiction**, **Languages**, **Grammar**, **Vocabulary**, **Assessment**, **Colouring**, **Code Editor**, **Chess**, **Study Coach**, **Karaoke**, and a cross-subject **Resource Tab** / open-courses library (MIT OpenCourseWare, Harvard Online Learning, edX, Coursera, Udemy, OpenLearn, Saylor Academy, Khan Academy) with a local owned-content scanner for a parent's own books, video, and audio.

### Safety, curation, and content standards
- **Restricted Mode** hides anything not explicitly marked `safe: true`, enforced both client-side (`frontend/src/utils/safetyFilter.js`) and server-side (`backend/app/safety.py`), which also sanitizes blocked words before content reaches the client. This is independent of profile choice — it's a per-session toggle from the 🔒 header icon.
- **Parent-only live web search**: the **Parent** profile's Curate tab is the only place the app touches the open internet (via the Brave Search API). Results are shown for human review only; nothing is auto-saved or shown to children until a parent explicitly approves it, at which point it passes through the safety filter before being written into the syllabus.
- **Provider-connected accounts are never fabricated.** External-course and streaming links (Udemy, Coursera, Netflix, JustWatch, Pinterest, and similar) are plain, unauthenticated search or catalogue pages generated by scripts in `backend/scripts/` — this project does not, and cannot, embed a specific paid account's licensed catalogue without that provider's real API credentials.

## Architecture

- **Backend**: FastAPI (`backend/app/main.py`), SQLAlchemy with PostgreSQL in production (SQLite fallback for local dev at `backend/data/eduai_pro.db`), Alembic migrations, and a large `backend/data/` and `backend/syllabus/` tree of authored/generated JSON that seeds the database.
- **Frontend**: React + Vite + Tailwind, code-split per tab via `React.lazy`, with a service worker (`vite-plugin-pwa`) for offline/installable use.
- **Data generation**: most large datasets (the museum's CMA gallery, the recipe collection, movie thumbnails, chart-verified songs) are built by deterministic, idempotent scripts in `backend/scripts/`, not hand-authored JSON — re-running a script reproduces the same output plus any newly available source records.

## Running locally

### One-command install

```bash
python3 full_install.py
```

Creates the backend virtualenv, installs dependencies, applies database migrations, imports legacy curriculum, runs `npm install` for the frontend, writes a launcher script (`start_EduAi_Pro.sh`/`.bat`), and creates an **EduAi_Pro** desktop shortcut (with a real generated icon) on both the normal Desktop and every configured OneDrive Desktop. Safe to re-run.

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export BRAVE_SEARCH_API_KEY=your-key-here  # optional, enables Parent web search
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The dev server proxies `/api/*` to `http://localhost:8000` (`vite.config.js`).

### Production stack (Docker Compose)

```bash
cp .env.example .env
docker compose up --build
```

Starts PostgreSQL, Redis, the API, and the frontend; the API container applies Alembic migrations on startup. Set `DATABASE_URL` for production Postgres and `AI_MONTHLY_BUDGET_USD` to cap AI spend. For an existing install, import legacy JSON once (idempotent):

```bash
cd backend
python -m alembic upgrade head
python -m scripts.migrate_json_to_db
```

`vercel.json` and `render.yaml` provide deploy configs for hosting the frontend on Vercel and the backend on Render.

## Tests

```bash
# backend
cd backend && .venv/bin/python -m pytest

# frontend
cd frontend && npm test
```

`.github/workflows/ci.yml` runs both suites plus a frontend production build on every push/PR.

## Parental Control Panel

The 🔒 header icon toggles **Restricted Mode**, independent of which profile is selected. Per-child progress, scores, and badges live server-side (`backend/data/progress_<Child>.json`, gitignored, generated at runtime) via `/api/progress/{child}`; the Parent profile has no progress record since it isn't a learner account.

## Adding new resources

1. **Manually**: edit the relevant `backend/syllabus/grade<N>.json` (or the equivalent `backend/data/*` file for a resource centre). Every resource needs `"safe": true` to be visible in Restricted Mode.
2. **Via Parent curation**: switch to the Parent profile, search the live web, review results, and click "Add to syllabus" — this runs the safety filter and writes `safe: true` automatically.

Approved video channels live in `backend/safe/safe_channels.json` — only add channels genuinely appropriate for children.

## Contributing

Keep additions scoped, cite real sources, and verify URLs point to genuinely free, public resources before adding them. Don't fabricate links, ratings, view counts, or biographical facts — where no honest source exists for something, leave it out rather than guess.
