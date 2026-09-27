# Backend Plan

## Summary

Four phases. Get it installed, see what it is, see what rotted, decide.

Phases 1 and 2 are **runnable commands** — model and effort are set on the command line, so no session settings change by hand. Phases 3 and 4 run in the main chat, because judgement needs the conversation.

| Phase | What | Runs as | Model | Effort |
|-------|------|---------|-------|--------|
| 1 | Install and run | command | sonnet | low |
| 2 | Map the code | command ×3 | haiku | low |
| 3 | Rate the rot | main chat | opus | high |
| 4 | Verdict | main chat | opus | high |

Two subsystems, judged separately:

| Subsystem | Path | Risk |
|-----------|------|------|
| API | `backend/user_backend/fast_api_server` | Medium — deps moved, code shape probably fine |
| Scrapers | `backend/dev_backend` | High — target sites change; likely all dead |

---

## Method

### Why commands instead of settings

Each phase command spawns its own `claude -p` process with `--model` and `--effort` on the line. The model map is enforced by the command, not remembered by me. Output goes straight to a findings file, so file dumps never enter the main conversation.

Run them from the repo root. Each writes one file under `plans/analysis/findings/`.

### Evidence before opinion

Phases 3 and 4 may only cite what phases 1 and 2 wrote down. No conclusion from memory about how a library behaves — check it.

### Read-only, with one narrow exception

This plan produces a verdict, not a fix. The only writes are under `plans/analysis/findings/`.

The exception is **unblocking**: if analysis genuinely cannot proceed, a minimal change is allowed to get past it. Fenced hard, because allowing edits is a slippery slope into an unplanned refactor.

**Rules — all apply:**

| Rule | |
|------|--|
| Prove it | Name the blocked step and quote the error before editing |
| Scratch first | Pin in `findings/requirements.pinned.txt`, never in the repo file |
| Runnable, not better | Only make code import or start. No bug fixes, no tidying |
| Log it | Every unblock gets a row in the findings file |
| One at a time | Unblock, re-run, record. Never batch |

**Budget — passing any of these stops the work and becomes a user decision:**

| Limit | |
|-------|--|
| Repo source files touched | **0** |
| Dependency pins in scratch file | **10** |
| Unblock attempts per phase | **3** |
| Behavior change | **never** |

Running out of budget is not a setback — it *is* the verdict. Report it and move on.

---

## Phase 1 — Install and run

Find out if it starts. Facts only, no fixes.

```bash
claude -p --model sonnet --effort low --permission-mode auto \
  "Read plans/analysis/backend-plan.md phase 1 and its Method section, then do it.
   Make a scratch venv on Python 3.12 outside the repo.
   Run, in order, recording command + exit code + shortest decisive error line for each:
     pip install -r backend/user_backend/fast_api_server/requirements.txt
     python -m compileall backend
     uvicorn main:app  (from backend/user_backend/fast_api_server, boot only)
     pytest on the two existing test files
   Obey the unblock budget. Touch no repo source file.
   Write a table to plans/analysis/findings/phase1-backend.md. No opinions, no fixes."
```

**Gate**: if `pip install` cannot complete inside 3 unblock attempts, stop — an uninstallable dependency tree is itself the phase 3 answer.

---

## Phase 2 — Map the code

Three commands, read-only. Run in parallel. File:line only, no suggestions.

```bash
# A — API surface
claude -p --model haiku --effort low --restricted \
  "Read backend/user_backend/fast_api_server/{apis,core,schemas}.
   Return three tables: routes (method, path, handler file:line);
   auth flow steps; every config or secret read (file:line, env var name).
   No fixes, no opinions." > plans/analysis/findings/phase2-api.md

# B — Data layer
claude -p --model haiku --effort low --restricted \
  "Read backend/user_backend/fast_api_server/db and backend/dev_backend/SQL.
   Return: models table; the actual schema; which DB engine each layer targets.
   Two DB layers exist - say plainly whether both are live or one is leftover, with file:line proof.
   No fixes." > plans/analysis/findings/phase2-db.md

# C — Scrapers
claude -p --model haiku --effort low --restricted \
  "Read backend/dev_backend/extractors and backend/dev_backend/utilities.
   One row per scraper: file, target URL, method (HTML parse / API / Selenium), any captcha handling.
   No fixes, no live requests." > plans/analysis/findings/phase2-scrapers.md
```

---

## Phase 3 — Rate the rot

Main chat, opus, high effort. Use Context7 for current versions — never guess from memory.

Labels: `dead` · `breaking` · `fine` · `unknown`

Check closely:

| Dep | Why |
|-----|-----|
| `pydantic` | v1→v2 rewrote validators; FastAPI code may not survive |
| `sqlalchemy` | 1.x→2.0 changed the query API |
| `python-jose` | Largely unmaintained |
| `chromedriver-binary` | Abandoned; Selenium Manager replaces it |
| `psycopg2` | Needs build tools; `-binary` or psycopg3 instead |
| `databases` + `asyncpg` + `aiosqlite` | Three overlapping DB layers; probably one is used |

Scrapers: live-probe each target. Dead if the target no longer returns the expected shape. 1881 and gulesider had captcha workarounds — assume dead until proven.

**Output**: `findings/phase3-backend.md` — one table, one label per row.

---

## Phase 4 — Verdict

Main chat, opus, high effort. Repair or rewrite, per subsystem. Evidence from phases 1–3 only.

Each verdict states rough size, what breaks if skipped, what depends on it.

**Output**: `findings/backend-verdict.md`

| Section | Contents |
|---------|----------|
| API | Repair or rewrite + why |
| Scrapers | Per source: revive, replace, drop |
| DB | Which layer survives |
| Secrets | Anything committed that should not be |
| Order | What the frontend plan needs first |

---

## Done when

- Every dependency has a label and a proposed pin.
- Every scraper is marked live or dead, with evidence.
- API either boots in the scratch venv, or the reason it cannot is written down.
- Verdict file exists.
- `git status` on `backend/` is clean.

Not in scope: new features, deployment, CI, and any repair. Repairs get their own plan under `plans/renovation/`, written from the verdict.
