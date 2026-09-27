# Renovation

Plans that **change code**. One per verdict, written only after that verdict exists.

`analysis/` decides what is wrong. `renovation/` fixes it. Nothing here starts before the matching verdict file is written.

| Plan | Written from | Status |
|------|--------------|--------|
| [`backend-renovation.md`](backend-renovation.md) | `analysis/findings/backend-verdict.md` | phases 0–8 done; scraper rewrites deferred |
| `frontend-renovation.md` | `analysis/findings/frontend-verdict.md` | not written |

## Rules

- One renovation plan per subsystem. No plans about plans.
- Every item traces to a finding. No item without a verdict line behind it.
- Ordered by dependency, not by ease.
- Each item is independently verifiable — a command or test that proves it landed.
