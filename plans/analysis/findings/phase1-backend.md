# Phase 1 — Install and run

Scratch venv: `C:\Users\borge\scratch_venv_prospector` (Python 3.12.3), outside repo. No repo source files touched.

| # | Command | Exit code | Shortest decisive error line |
|---|---------|-----------|-------------------------------|
| 1 | `pip install -r backend/user_backend/fast_api_server/requirements.txt` | 0 | (none — install succeeded) |
| 2 | `python -m compileall backend` | 1 | `*** Sorry: IndentationError: expected an indented block after 'else' statement on line 87 (query_test.py, line 93)` |
| 2b | (second failure, same run) | 1 | `SyntaxError: invalid character '\u2212' (U+2212)` in `backend\dev_backend\extractors\notes_and_outputs\proff\links.py`, line 58 |
| 3 | `uvicorn main:app` (boot only, cwd `backend/user_backend/fast_api_server`) | 1 | `ModuleNotFoundError: No module named 'virtual_env'` (from `apis/version1/send_email.py:4`, `from virtual_env.config import Config`) |
| 4 | `pytest backend/dev_backend/SQL/query_test.py backend/dev_backend/SQL/slots_test.py` | 2 | `IndentationError: expected an indented block after 'else' statement on line 87` (query_test.py, line 93) — collection aborted, slots_test.py never reached |

## Unblock log

None attempted. `virtual_env` module is not in requirements.txt, not present anywhere in the repo, and not on PyPI under that name — it is a local config module (likely holding secrets, given the import is `virtual_env.config.Config`) that must exist outside version control on the original dev machine. No safe guess of its contents is possible without changing behavior, so it was left as a recorded blocker rather than unblocked.

## Gate note

Per plan gate: `pip install` completed without needing any unblock attempt, so the phase 1 gate condition (3 failed unblock attempts on pip install) was not triggered. The two compileall syntax errors are both in `dev_backend` (scrapers/SQL), not in `fast_api_server`. The API subsystem fails only at runtime boot, on a missing local module.

## Unblock log (main chat, after the phase 1 worker)

Blocked step: `uvicorn main:app` boot. Budget used: 2 of 3 attempts, 1 of 10 pins, 0 repo files.

| # | Blocker (quoted) | Unblock | Result |
|---|------------------|---------|--------|
| 1 | `ModuleNotFoundError: No module named 'virtual_env'` | Stub `virtual_env/config.py` with dummy values in the session scratchpad, put on `PYTHONPATH`. Outside the repo. | Next error: `ModuleNotFoundError: No module named 'psycopg'` from `db/session.py:17` |
| 2 | `ModuleNotFoundError: No module named 'psycopg'` (SQLAlchemy 2.1.1 maps a plain `postgresql://` URL to the psycopg v3 driver) | Pin `psycopg[binary]==3.3.6` in `findings/requirements.pinned.txt`, install into scratch venv | Next error: `AttributeError: 'Settings' object has no attribute 'PROJECT_VERSION'` (`main.py:26`) |
| — | `PROJECT_VERSION` missing from `core/config.py` | Stopped. Only fix is a repo source edit; budget allows 0. | Boot not reached |

Known later blockers, found by reading, not by running: `core/config.py` has no `SECRET_KEY` (used by `core/security.py:16`, so login fails), and `main.py:28` `create_tables()` needs a live Postgres at import time.
