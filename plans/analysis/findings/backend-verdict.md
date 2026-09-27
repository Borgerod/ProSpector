# Backend verdict

Evidence: `phase1-backend.md`, `phase2-*.md`, `phase3-backend.md`. Sizes are rough and not measured.

## Summary

- **API: repair.** The code shape is small and still fits current FastAPI. It fails on missing config and a handful of dependency breaks, not on design.
- **Scrapers: mostly replace.** Only the brreg download still works. Every HTML scraper broke because its target site changed.
- **DB: keep one shared Postgres schema**, owned by one place.

## API — repair

Why repair, not rewrite: 14 routes, 3 tables, about 20 Python files. FastAPI, Pydantic 2 and SQLAlchemy 2.1 still accept the code with warnings (phase 3 scratch tests). Every blocker found is config or a pin.

| Must fix, in order | Evidence |
|--------------------|----------|
| Replace the untracked `virtual_env.config` with env-based settings | phase 1: boot fails on `ModuleNotFoundError` |
| Add the missing `PROJECT_VERSION` and `SECRET_KEY` settings | phase 1 unblock log; `core/security.py:16` |
| Switch the Postgres driver to psycopg v3 | phase 1 unblock 2 |
| Pin `bcrypt==4.0.1`, then replace passlib | phase 3: bcrypt 5 breaks every hash |
| Pin every requirement; drop the dead ones | phase 3 dependency table |

- **Rough size:** small. One focused change set in `fast_api_server`.
- **If skipped:** the API cannot boot, so no login and no call list for the app.
- **Depends on it:** the Flutter app. It calls `/login/token`, `/users/`, the phone verification routes, `/currentcallList`, `/callList/ringe_status` and `/ResetPassword*` on `127.0.0.1:8000`.

## Scrapers — per source

| Source | Verdict | Why |
|--------|---------|-----|
| brreg (`brreg.py`) | revive | Download endpoint is live (HTTP 200, 210 MB gzip). Official open API. |
| Gulesider company search | replace | Page loads, but the data moved out of `__NEXT_DATA__`. Parser must be rewritten. |
| Gulesider industry list | drop | Cloudflare challenge (HTTP 403). |
| 1881 industry list and profiles | drop | Industry sitemap is 404. Profiles assumed dead per plan rule. |
| Proff search | replace | Page loads; the parsed containers are gone. Parser must be rewritten. |
| Proff industry list | replace | URL redirects to `/bransjer` with a new layout. |
| regnskapstall phone lookup | unknown | Site up; profile format not probed. |
| Google (`google.py`) | unknown | Needs a real browser run. Also needs `selenium` added and the `executable_path` call updated. |
| `recaptcha_solver.py` | drop | Not called anywhere. |

- **Rough size:** medium to large. Each "replace" is a new parser against a new page format. Scraping sites with bot protection may break again.
- **If skipped:** no new leads reach `call_list`. The API still runs on whatever data is already in the DB.
- **Depends on it:** the `call_list` table the API serves.

## DB — which layer survives

Correction to phase 2: it calls `dev_backend/SQL` "leftover". It is not. Both layers declare the same `call_list` table (`dev_backend/SQL/call_list.py:17`, `fast_api_server/db/models/call_list.py:6`). The scrapers write it; the API reads it. Both target Postgres.

Verdict: keep Postgres and the API's models as the one schema. Point the scraper side at those models instead of its own copy. The SQLite switch is broken (`db/session.py:9-10`); drop it or fix it, but do not keep it half-working.

## Secrets

- No passwords, API keys, private keys or DB URLs with credentials found in any tracked file or in git history (pattern scan, 3 commits).
- Committed: Twilio Verify service SID `VA0af2…` in `dev_backend/SQL/config.py:53` and `:96`. It is an identifier, not a credential, but it is tied to a real account. Move it to env.
- Large binaries tracked: `setup.exe` (97 MB, repo root), `utilities/chromedriver.exe`, `utilities/enheter_alle.json.gz`. Not secrets; repo weight.
- The real secrets lived in the gitignored `virtual_env/` and `.env`. They are not in the repo, so the original values are lost unless a local copy exists.

## Order — what the frontend plan needs first

1. API boots with env-based config and a local Postgres.
2. Login works (settings fix plus bcrypt pin).
3. Call-list routes return data, seeded from brreg.
4. Phone verification and email reset, once Twilio and mail credentials exist.
5. Scraper replacements, last. The app does not need them to run.
