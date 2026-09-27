# Phase 3 — Rate the rot

Evidence sources: phase 1 and 2 findings, the scratch venv (`C:\Users\borge\scratch_venv_prospector`, all latest versions as of 2026-09-27), `pip index versions`, Context7 docs, and live HTTP probes run on 2026-09-27.

Labels: `dead` · `breaking` · `fine` · `unknown`.

## Dependencies — API (`backend/user_backend/fast_api_server/requirements.txt`)

Every line in the file is unpinned, so a fresh install takes the latest release.

| Dep | Latest | Label | Evidence | Proposed pin |
|-----|--------|-------|----------|--------------|
| `fastapi` | 0.141.1 | fine | Installs. `@app.on_event("startup")` still runs (scratch test). | `fastapi==0.141.1` |
| `uvicorn` | 0.54.0 | fine | Installs and starts; failures were in app code. | `uvicorn==0.54.0` |
| `pydantic[email]` | 2.13.5 | fine | `class Config: orm_mode = True` only raises a `UserWarning`. A FastAPI `response_model` still serialises a plain ORM-like object (scratch test, HTTP 200). Context7: `orm_mode` renamed `from_attributes`, `class Config` deprecated. | `pydantic[email]==2.13.5` |
| `sqlalchemy` | 2.1.1 | breaking | A plain `postgresql://` URL now needs the psycopg v3 driver (`ModuleNotFoundError: No module named 'psycopg'`, phase 1 unblock 2). `db.query(...)` legacy API and `sqlalchemy.ext.declarative.declarative_base` still import. | `sqlalchemy==2.1.1` with `psycopg[binary]` |
| `psycopg2` | 2.9.13 | breaking | Installed fine on Windows, but SQLAlchemy 2.1 no longer picks it for `postgresql://`. Only use left: `from psycopg2 import IntegrityError` in `db/repository/users.py:1`. | drop; use `psycopg[binary]==3.3.6` |
| `passlib[bcrypt]` + `bcrypt` | 1.7.4 + 5.0.0 | dead | Any hash fails: `ValueError: password cannot be longer than 72 bytes`. passlib 1.7.4 is the last release. With `bcrypt==4.0.1` hash and verify both work (scratch test). | `bcrypt==4.0.1` short term; replace passlib later |
| `python-jose` | 3.5.0 | fine | `jwt.encode` works (scratch test). Maintenance concern from the plan not verified. | `python-jose==3.5.0` |
| `databases` | 0.9.0 | fine | Imports with SQLAlchemy 2.1.1. Only used for a `SELECT 1` health check (`db/utils.py:8`). | `databases==0.9.0` |
| `asyncpg` | 0.31.0 | fine | Driver for `databases` on Postgres. | `asyncpg==0.31.0` |
| `aiosqlite` | 0.22.1 | dead | No import anywhere. SQLite path in `db/session.py:9-10` is broken (uses a Postgres URL). | drop |
| `fastapi-mail` | 1.6.8 | unknown | Installs. Send path not reached. `send_email.py` holds both old and new config keys. | `fastapi-mail==1.6.8` |
| `twilio` | 9.11.1 | unknown | Installs. `client.verify.services(...)` calls not run (no credentials). | `twilio==9.11.1` |
| `phonenumbers` | 9.0.40 | fine | Only `phonenumbers.parse`; stable API. Not run. | `phonenumbers==9.0.40` |
| `python-multipart` | 0.0.32 | fine | Needed for the login form. Installs. | `python-multipart==0.0.32` |
| `python-dotenv` | 1.2.3 | fine | Used only by `dev_backend/SQL/config.py`. | `python-dotenv==1.2.3` |
| `jinja2` | 3.1.6 | dead | No import anywhere in `backend/`. | drop |
| `aiofiles` | 25.1.0 | dead | No import anywhere in `backend/`. | drop |
| `seedir` | 0.5.1 | dead | No import anywhere in `backend/`. | drop |
| `pre-commit` | 4.6.2 | fine | Dev tool; no config file tracked. | move to dev deps |
| `pytest` | 9.1.1 | fine | Installs. The only tests fail on a syntax error (phase 1). | `pytest==9.1.1` |
| `requests` | 2.34.2 | fine | Installs. | `requests==2.34.2` |
| `chromedriver-binary` | 156.0.8075.0.0 | dead | Not imported by the API. Scrapers import it only in a comment (`google.py:57`); they use a committed `utilities/chromedriver.exe`. | drop |

## Dependencies — scrapers (`backend/dev_backend`)

No requirements file exists for `dev_backend`. Imports found: `selenium`, `bs4`, `pandas`, `numpy`, `tqdm`, `sqlalchemy`, `fastapi_mail`, `dotenv`.

| Dep | Label | Evidence | Proposed pin |
|-----|-------|----------|--------------|
| `selenium` | breaking | Not in any requirements file (`ModuleNotFoundError` in scratch venv). `google.py:71` passes `executable_path=` to `webdriver.Chrome`; Context7 Selenium 4 docs say to use a `Service` object or Selenium Manager. Removal of the argument is not verified. | `selenium==4.49.0` |
| `bs4`, `pandas`, `numpy`, `tqdm` | unknown | Not listed anywhere; not installed or run. | add a requirements file |

## Code state

| Item | Label | Evidence |
|------|-------|----------|
| API boot | dead | Needs untracked `virtual_env.config` (gitignored), then `Settings.PROJECT_VERSION` is missing (`main.py:26`). See phase 1 unblock log. |
| API login | dead | `Settings` has no `SECRET_KEY` (`core/security.py:16`), and bcrypt 5 breaks hashing. |
| API DB | breaking | Postgres only. SQLite switch broken (`db/session.py:9-10`). Tables are created at import, so boot needs a live DB. |
| `dev_backend` tests | dead | `SQL/query_test.py:93` `IndentationError`; pytest collection aborts. |
| `notes_and_outputs/proff/links.py` | dead | `SyntaxError: invalid character '\u2212'`. Notes file, not runtime code. |

## Scrapers — live probes (2026-09-27)

One request per target, desktop Chrome user agent, `curl`.

| Scraper | Target probed | Result | Label |
|---------|---------------|--------|-------|
| `brreg.py` | `data.brreg.no/enhetsregisteret/api/enheter/lastned` | HTTP 200, `enheter_alle.json.gz`, 210 MB | fine |
| `gulesider.py` (company search) | `gulesider.no/rørlegger/bedrifter/1` | HTTP 200, but no `__NEXT_DATA__` script; page uses `self.__next_f` (newer Next.js format). Code reads `__NEXT_DATA__` (`gulesider.py:98`). | dead |
| `industries_gulesider.py` | `gulesider.no/bedriftsregister/kategorier-a` | HTTP 403, Cloudflare "Just a moment..." challenge | dead |
| `industries_1881.py` | `1881.no/sitemap/industries-a` | Redirects to `/Error/PageNotFound` (404) | dead |
| `_1881.py` (profiles) | Listing page format not probed; its industry input list (above) is 404 | Plan rule: assume dead until proven | dead (assumed) |
| `_1881.py` phone lookup via `regnskapstall.no` | Home page HTTP 200; profile page format not probed | | unknown |
| `industries_proff.py` | `proff.no/industry/select?beginLetter=A` | Redirects to `/bransjer`; expected `ul.three-aligned-columns clear` absent | dead |
| `proff.py` | `proff.no/bransjesøk?q=Rørleggere` | HTTP 200. Company-name link class still present, but `search-container-wrap`, `org-number` and the next-page arrow are absent. Code needs all three (`proff.py:68,82,90`). | dead |
| `google.py` | `google.com/search?q=...` | HTTP 200 without JavaScript; claimed/unclaimed class names `cQhrTd` / `ndJ4N` absent. Scraper uses a real browser, which was not run. | unknown |
| `utilities/recaptcha_solver.py` | — | Not called by any extractor (phase 2) | dead |
