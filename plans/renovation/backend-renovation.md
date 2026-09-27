# Backend Renovation

## Summary

Make the API boot, log in and serve the call list, then rebuild the scraper side around the one source that still works (brreg). Written from `analysis/findings/backend-verdict.md`. Every item cites a finding.

Eight phases after a setup step (phase 0), ordered by dependency. Phases 1–5 get the app working again. Phases 6–7 bring the scraper side back. Phase 8 is cleanup.

| Phase | What | Unblocks | Runs as |
|-------|------|----------|---------|
| 0 | Branch and baseline | everything | main chat |
| 1 | Reproducible install | 2 | main chat |
| 2 | Env-based config | 3 | main chat |
| 3 | Local Postgres and driver | 4 | main chat |
| 4 | Password hashing | 5 | main chat |
| 5 | Route smoke tests | frontend plan | main chat |
| 6 | One shared schema | 7 | main chat |
| 7 | Scrapers | fresh leads | main chat, one source at a time |
| 8 | Repo hygiene | — | main chat |

All phases run in the main chat. No workers.

---

## Method

### Scope fence

- Fix what the verdict names. No new features, no redesign, no renaming for taste.
- A bug found outside the listed items goes into the **Found while renovating** table at the bottom, not into the code. It gets fixed only if a phase's verify step fails because of it.
- If an item needs more files than it lists, stop and ask.

### Proof per item

Each item ends with a **Verify** command. An item is done only when that command passes. Paste the shortest decisive line of its output into the phase's commit body.

### Git

- Branch `renovate/backend` from `main`.
- One commit per phase, via the `commit` skill. Types: `fix` for repairs, `chore` for deps and hygiene, `test` for new tests.
- No squash of phases into one commit — each phase must be revertable on its own.

### Environment

- Python 3.12 (installed; verified during analysis).
- Postgres runs in Docker (`docker` is on PATH; verified). Decision: Docker over the local PostgreSQL 17 install, because a compose file makes the setup reproducible from the repo alone. The image tag is `postgres:17`, matching the major version already installed on this machine.
- The app calls `127.0.0.1:8000` (found in `App/prospector_app/lib`). Keep port 8000.

---

## Phase 0 — Branch and baseline

1. `git switch -c renovate/backend`
2. Record the analysis state as the baseline: `plans/analysis/findings/phase1-backend.md` is the "before".

**Verify**: `git branch --show-current` prints `renovate/backend`.

---

## Phase 1 — Reproducible install

Finding: every requirement is unpinned; several are unused (phase 3 dependency table).

Files: `backend/user_backend/fast_api_server/requirements.txt`, new `requirements-dev.txt` beside it.

| Change | Finding |
|--------|---------|
| Pin every kept dep to the version tested in phase 3 | phase 3 "Proposed pin" column |
| Drop `jinja2`, `aiofiles`, `seedir`, `aiosqlite`, `chromedriver-binary`, `psycopg2` | phase 3: no imports / replaced |
| Add `psycopg[binary]==3.3.6`, `pydantic-settings` (pin to the version pip resolves) | phase 1 unblock 2; phase 2 of this plan |
| Temporarily pin `bcrypt==4.0.1` | phase 3: bcrypt 5 breaks passlib (removed again in phase 4) |
| Move `pytest`, `pre-commit` to `requirements-dev.txt` | phase 3: dev tools |

**Verify** (fresh venv outside the repo):
```bash
python -m venv /tmp/pv && /tmp/pv/Scripts/pip install -r requirements.txt -r requirements-dev.txt && /tmp/pv/Scripts/pip check
```
Exit 0, and `pip check` prints `No broken requirements found.`

---

## Phase 2 — Env-based config

Finding: boot fails on `ModuleNotFoundError: No module named 'virtual_env'`; `Settings` lacks `PROJECT_VERSION` and `SECRET_KEY` (phase 1 unblock log).

Files: `core/config.py`, `apis/version1/send_email.py`, `apis/version1/send_sms.py`, new `backend/.env.example`.

- Replace `virtual_env.config.Config` with one `pydantic-settings` `Settings` class that reads env vars and `backend/.env`.
- Add `PROJECT_VERSION` and `SECRET_KEY`. Missing required values must fail at startup with the variable's name — no default secrets, no empty fallbacks.
- `send_email.py` and `send_sms.py` read from the same `Settings`.
- `.env.example` lists every variable with a placeholder. `.env` is already gitignored (verified in `.gitignore`).
- `backend/.env` already exists, recovered from the private repo's `virtual_env/setEnv.bat` (last commit 2022-12-01). Gitignored (verified with `git check-ignore`). Adjust it for local use:
  - Postgres values point at an old AWS RDS host. Replace them with the local Docker values from phase 3.
  - `SECRET_KEY` was the placeholder `NO_SECRET_KEY`. Replace with a fresh value from `python -c "import secrets; print(secrets.token_urlsafe(32))"`.
  - Add `PROJECT_VERSION`.
  - Mail and Twilio values are kept as recovered. They were stored in plain text in git history, so the user rotates (replaces) the Gmail app password and Twilio token before the first live send.

**Verify**:
```bash
cd backend/user_backend/fast_api_server && python -c "import core.config"
```
With `.env` filled: exit 0. With `SECRET_KEY` removed: a validation error naming `SECRET_KEY`.

---

## Phase 3 — Local Postgres and driver

Findings: SQLAlchemy 2.1 needs psycopg v3 for `postgresql://`; the SQLite switch is broken (`db/session.py:9-10`); `psycopg2` is still imported for `IntegrityError` (`db/repository/users.py:1`).

Files: new `backend/docker-compose.yml`, `db/session.py`, `db/repository/users.py`, `db/utils.py`.

- Compose file: one `postgres:17` service, port 5432, credentials from `backend/.env`.
- Build the URL as `postgresql+psycopg://…` for SQLAlchemy.
- Remove the SQLite branch. Decision: drop rather than fix — nothing uses it (phase 3: `aiosqlite` never imported).
- `IntegrityError` from `sqlalchemy.exc` instead of `psycopg2`.
- `db/utils.py` health check: keep `databases` + `asyncpg`, and give it the plain `postgresql://` URL (asyncpg does not accept the `+psycopg` suffix — **not verified**; check during this phase).

**Verify**:
```bash
docker compose -f backend/docker-compose.yml up -d
cd backend/user_backend/fast_api_server && uvicorn main:app --port 8000 &
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000/docs
```
Prints `200`, and the log shows `Database is connected`.

---

## Phase 4 — Password hashing

Finding: passlib 1.7.4 + bcrypt 5 fails every hash (phase 3). passlib has had no release since 1.7.4.

Files: `core/hashing.py`, `requirements.txt`.

- Decision: replace passlib with the `bcrypt` package directly. Existing hashes are bcrypt, so stored passwords keep working.
- Keep the `Hasher` interface (`verify_password`, `get_password_hash`) so callers do not change.
- Remove the temporary `bcrypt==4.0.1` pin; pin `bcrypt==5.0.0`. Drop `passlib`.
- Passwords over 72 bytes: reject with a clear error at user creation. Do not truncate silently.

**Verify**: new `tests/test_hashing.py` — hash then verify returns `True`; wrong password returns `False`; a hash made by passlib 1.7.4 + bcrypt 4.0.1 (captured once as a string fixture) still verifies.

---

## Phase 5 — Route smoke tests

Finding: no API tests exist (phase 1: the only tests live in `dev_backend`). The app depends on the routes listed in the verdict "Order" section.

Files: new `backend/user_backend/fast_api_server/tests/` (conftest + one file per router).

- Tests run against the Docker Postgres with a throwaway database.
- Cover the routes the app calls: `/login/token`, `/users/`, `/currentcallList`, `/callList/ringe_status`, `/ResetPassword*`.
- Twilio and email calls are replaced with test doubles at the `Verification` / `send_email_async` boundary. Real sends need credentials — see **Open decisions**.
- A failing test that points to a route bug: fix that bug in this phase, log it in **Found while renovating**. One bug is already known: `create_user` calls the async `send_otp_code_async` without `await` (`route_users.py:23`).

**Verify**: `pytest backend/user_backend/fast_api_server/tests` — all pass.

**After this phase, the frontend plan can start.**

---

## Phase 6 — One shared schema

> **Outcome (2026-09-27):** done together with phase 7. `dev_backend` turned out far more broken than planned (imports of modules that never existed, such as `SQL.models.insert` and `core.base`), so the user chose a minimal rebuild over an in-place repair. The old `dev_backend/SQL/` layer is deleted; the scraper side now imports the API's models and settings directly. The committed `VERIFY_SID` went with it.

Finding: both layers declare `call_list` (`dev_backend/SQL/call_list.py:17`, `fast_api_server/db/models/call_list.py:6`). The scrapers write it; the API reads it (verdict, DB section).

Files: `dev_backend/SQL/call_list.py`, `dev_backend/SQL/config.py`.

- Scraper side imports the API's `CallList` model instead of declaring its own.
- `dev_backend/SQL/config.py` reads the same `backend/.env` through the phase 2 `Settings`.
- Move the committed Twilio `VERIFY_SID` (`dev_backend/SQL/config.py:53`, `:96`) to env.

**Verify**:
```bash
git grep -n "__tablename__ = .call_list.$" backend
```
Exactly one hit, in `fast_api_server/db/models/call_list.py`. And `git grep VA0af259` returns nothing.

---

## Phase 7 — Scrapers

> **Outcome (2026-09-27):** minimal rebuild, chosen by the user.
> - `extractors/brreg.py` rewritten: streams the brreg CSV download, skips bankrupt and dissolving companies, and bulk-loads `call_list` plus `call_list_overview_mediavest` in lists of 40 (the API's default `/callList` page size). Live run: 1,163,572 companies in 82 s. The API serves them from `/callList`.
> - Deleted: every other extractor, the old SQL layer, `utilities/` (including `chromedriver.exe` and the unused reCAPTCHA solver). Restore from commit `402f752` when the Gulesider / Proff rewrites start.
> - 7.2–7.6 (Gulesider, Proff, Google, regnskapstall) are deferred to their own later step.
> - Tests: `backend/dev_backend/tests`, 3 passed.

Findings: phase 3 scraper probes; verdict per-source table. One source per commit.

First, make `dev_backend` importable:
- New `backend/dev_backend/requirements.txt` with pins for `requests`, `beautifulsoup4`, `pandas`, `numpy`, `tqdm`, `selenium` (phase 3: no requirements file exists).
- Fix the `IndentationError` in `SQL/query_test.py:93` (phase 1).
- Fix the broken import path `backend.dev_backend.SQL.models.insert` (`main.py:8`, `extractors/brreg.py:25`) — `SQL/models/` does not exist; the file is `SQL/insert.py`. Found while planning.

**Verify**: `python -m compileall backend/dev_backend -x notes_and_outputs` exits 0, and `pytest backend/dev_backend/SQL` collects.

Then, per source:

| Order | Source | Action | Verify |
|-------|--------|--------|--------|
| 7.1 | brreg | Revive. Download, filter, write into `call_list`. This is the seed data for the app. | Live run fills `call_list`; row count > 0 |
| 7.2 | Gulesider company search | Rewrite parser for the new page format (`self.__next_f` payload). | Parser test on a saved HTML fixture + one live page |
| 7.3 | Proff search | Rewrite parser for the new layout. | Same |
| 7.4 | Proff industry list | Rewrite for `/bransjer`. | Same |
| 7.5 | Google | Probe first in a real browser with Selenium Manager. Revive only if the claimed/unclaimed markers still exist; else drop. | Probe result recorded before any code |
| 7.6 | regnskapstall | Probe a profile page first. Same rule as 7.5. | Same |
| 7.7 | Drop | Delete `_1881.py`, `industries_1881.py`, `industries_gulesider.py`, `utilities/recaptcha_solver.py`, `utilities/chromedriver.exe`. | `git grep` finds no imports of them |

Rewrites 7.2–7.4 each get a saved HTML fixture under `dev_backend/tests/fixtures/`, so the parser test does not hit the live site.

---

## Phase 8 — Repo hygiene

- Remove `utilities/enheter_alle.json.gz` from tracking; brreg downloads it fresh (phase 3: endpoint live). Add to `.gitignore`.
- Delete the `TEST BLOCK — DELETE ME` section from `plans/README.md`.

Not in scope: `setup.exe` (97 MB) stays. Removing it from history needs a history rewrite, which is destructive and a separate user decision.

**Verify**: `git ls-files | grep -E "enheter_alle|chromedriver.exe"` prints nothing.

---

## Open decisions

These need the user before the named phase. Everything else above is decided.

| Decision | Needed by | Why it cannot be decided here |
|----------|-----------|-------------------------------|
| Rotate Gmail app password and Twilio token, then allow one live test send | Phase 5 live check | Recovered values are in `backend/.env` but not validated, and were exposed in git history. Rotation and live sends reach outside accounts. |
| Revive or drop Google and regnskapstall | Phase 7.5, 7.6 | Depends on probe results not yet run |
| Scraping terms of use for Gulesider and Proff | Phase 7.2–7.4 | Legal question, not a code question |

## Found while renovating

| Where | What | Fixed in |
|-------|------|----------|
| `route_users.py:23` | `send_otp_code_async` called without `await`, so signup never sent the SMS | Phase 5 (test failed; fixed) |
| `main.py` `GET /ResetPassword` | Changes any user's password from just an email address, with no login or code check | Not fixed — security, needs a user decision |
| `main.py` `GET /ShowUser` | Returns the full user row, including `hashed_password` | Not fixed — security, needs a user decision |
| `main.py` `/callList`, `/callList/ringe_status` | No login required | Not fixed — needs a user decision |
| `send_sms.py` `requestVerification` | Creates a new Twilio Verify service on every request instead of using `VERIFY_SID` | Not fixed |
| Windows machine env vars | 18 `POSTGRES_*` / `MAIL_*` / `TWILIO_*` / `SECRET_KEY` vars set machine-wide by the 2022 `setEnv.bat`, pointing at AWS RDS. They override `backend/.env`. Tests load `.env` over them; running uvicorn needs them unset. | Not fixed — machine config, needs the user |
| `main.py:8`, `extractors/brreg.py:25` | Import path `SQL.models.insert` does not exist | Phase 7 (files rebuilt) |
| brreg CSV | The register now includes `telefon`, `mobil`, `epostadresse` and `hjemmeside`, but `call_list` has no column for them | Added `telefon` and `mobil` (user approved, 2026-09-27) |

## Done when

- API boots on a fresh clone with `.env` + `docker compose up` + `uvicorn`.
- All tests in `fast_api_server/tests` pass.
- `call_list` holds brreg data and the app's routes return it.
- Each scraper is either working with a fixture test or deleted.
- No secrets or generated data tracked in git.
