## DB Layer Analysis

### Models Table

**User Backend (Active)** — `backend/user_backend/fast_api_server/db/models/`:
| Table | Columns |
|-------|---------|
| **User** | id (PK), username, email, hashed_password, is_active, is_superuser, org, phone_number |
| **CallList** | org_num (PK), name, google_profil, eier_bekreftet, komplett_profil, ringe_status, liste_id, link_til_profil |
| **CallListOverview** | liste_id (PK), liste_start, liste_limit, kunde_id, er_ledig, er_ferdig |

**Dev Backend (Leftover)** — `backend/dev_backend/SQL/`:
| Table | Purpose |
|-------|---------|
| CallList, CallListTest | Same as user backend (duplicated) |
| Gulesider, Proff, 1881, Google, InputTable | Data extraction/scraping models |
| 6× industry tables | Categorical data from external sources |

---

### DB Engine Targeting

**User Backend:**
- **Primary target:** PostgreSQL
- **Fallback (broken):** SQLite—condition inverted + malformed string
- **File:** `backend/user_backend/fast_api_server/db/session.py:9-10` — reads `USE_SQLITE_DB == "True"` but returns PostgreSQL string

**Dev Backend:**
- **Target:** PostgreSQL only  
- **File:** `backend/dev_backend/SQL/config.py:64` — `create_engine(settings.DATABASE_URL)` where DATABASE_URL is always Postgres

---

### Live vs. Leftover

**User Backend is LIVE** ✅
- `backend/user_backend/fast_api_server/main.py:8,10` imports `db.session` and `db.repository`; creates tables; serves /callList, /overView, /ShowUser endpoints
- Actively used by the FastAPI server

**Dev Backend is LEFTOVER** ❌
- `backend/dev_backend/main.py:139` wraps extraction logic in `if __name__ == '__main__':`—lines 147–179 are commented out
- It's a standalone data-scraping script, not integrated into the live app

---

### Schema (PostgreSQL in both)

**Actual schema** is declared via SQLAlchemy ORM; tables auto-created on startup:
- User backend: 3 tables  
- Dev backend: 11+ tables (mostly extraction intermediates)

Both point to the same PostgreSQL instance based on `DATABASE_URL` config, but only user backend is active.
