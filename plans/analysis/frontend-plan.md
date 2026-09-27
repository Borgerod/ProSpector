# Frontend Plan

> **Template — not filled in yet.**
> Write this after `plans/analysis/findings/backend-verdict.md` exists. The API contract decides most of the work here.

## Summary

_TBD._

| Phase | What | Runs as | Model | Effort |
|-------|------|---------|-------|--------|
| 1 | | command | | |
| 2 | | command | | |
| 3 | | main chat | opus | high |
| 4 | | main chat | opus | high |

---

## Method

Same as the backend plan — see [backend-plan.md](backend-plan.md#method).

Cheap phases are written as `claude -p --model X --effort Y` commands so the model map is enforced by the command line, not by memory. Judgement phases run in the main chat.

---

## Phase 1 — _name_

_TBD._

**Output**: `plans/analysis/findings/phase1-frontend.md`

---

## Phase 2 — _name_

_TBD._

**Output**: `plans/analysis/findings/phase2-frontend.md`

---

## Phase 3 — _name_

_TBD._

**Output**: `plans/analysis/findings/phase3-frontend.md`

---

## Phase 4 — Verdict

_TBD._

**Output**: `plans/analysis/findings/frontend-verdict.md`

---

## Done when

_TBD._

---

## Parked notes

Collected while scanning the backend. Not verified. Do not treat as findings.

| Note                                                                                                      |
| --------------------------------------------------------------------------------------------------------- |
| `pubspec.yaml` pins Dart SDK `>=2.19.0 <3.0.0`. Installed Flutter is Dart 3.x — app cannot compile as-is. |
| `flutter_neumorphic` and `flutter_acrylic 1.0.0+2` look unmaintained.                                     |
| `firebase_core 1.19.1` / `firebase_auth 3.4.1` are several majors behind.                                 |
| `flutter_facebook_auth` is pinned to a git fork at a loose commit.                                        |
| `flutter_secure_storage` is commented out with a TODO about a build error.                                |
| 43 dart files, no lockfile committed.                                                                     |
