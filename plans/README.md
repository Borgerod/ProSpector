# ProSpector Revival Plan

## Goal

ProSpector has not been touched since May 2024. It does not build. This plan finds out how bad it is, then decides per subsystem whether to repair or rewrite.

Order: **backend first, frontend second.** The app is a client of the backend. Fixing the client against a broken or changed API means doing the work twice.

| Step | File                                                   | Output                                                    |
| ---- | ------------------------------------------------------ | --------------------------------------------------------- |
| 1    | [analysis/backend-plan.md](analysis/backend-plan.md)   | Dependency labels, scraper status, repair/rewrite verdict |
| 2    | [analysis/frontend-plan.md](analysis/frontend-plan.md) | Same, for the app. Template only until step 1 is done.    |
| 3    | [renovation/](renovation/README.md)                    | The actual fixes, written from the verdicts               |

## Two folders

| Folder        | Does                                         | Touches code                                    |
| ------------- | -------------------------------------------- | ----------------------------------------------- |
| `analysis/`   | Finds out what is broken. Ends in a verdict. | No — see the unblock budget in the backend plan |
| `renovation/` | Fixes it. One plan per verdict.              | Yes                                             |

Analysis never repairs. Renovation never investigates. Keeping them apart is what stops a scan turning into an unplanned refactor.

## Scope

| Part                                   | Stack                                         | Files   |
| -------------------------------------- | --------------------------------------------- | ------- |
| `backend/user_backend/fast_api_server` | FastAPI, SQLAlchemy, JWT                      | 22      |
| `backend/dev_backend`                  | Scrapers (1881, gulesider, proff, brreg), SQL | 23      |
| `App/prospector_app`                   | Flutter, Firebase                             | 43 dart |

## Rules

- Each analysis plan ends with a written verdict, not a half-finished migration.
- No fixing forward past a phase that failed. Record the error, move on.
- Repair-vs-rewrite is the user's call. Analysis produces evidence, not decisions.
- Three files per subsystem, maximum: a plan, its findings, its renovation plan. No more layers.

## Known already

- `requirements.txt` has **zero version pins**. Any install is a lottery.
- `pubspec.yaml` pins Dart SDK `>=2.19.0 <3.0.0` — pre-Dart 3. Installed Flutter is Dart 3.x.
- No CI, no lockfiles committed, no `.github/`.
- 97 MB `setup.exe` committed at repo root.

## How the model map is enforced

Cheap phases are written as `claude -p --model X --effort Y` commands inside the plan. Each runs in its own process with its model fixed on the command line, so the map is obeyed without changing session settings between phases.

Judgement phases run in the main chat, because a fresh process cannot carry the conversation.

## TEST BLOCK — DELETE ME

This block exists only to test how file changes show up in the chat.
Line two of the test block.
Line three of the test block.
Line four of the test block.
Line five of the test block.
Line six of the test block.
Line seven of the test block.
Line eight of the test block.
Line nine of the test block.
Line ten of the test block.
Line eleven of the test block.
Line twelve of the test block.
Line thirteen of the test block.
Line fourteen of the test block.
Line fifteen of the test block.
Line sixteen of the test block.
Line seventeen of the test block.
Line eighteen of the test block.
Line nineteen of the test block.
Line twenty of the test block.
