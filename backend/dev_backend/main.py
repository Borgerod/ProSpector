''' Fills call_list from the brreg register.

Run from backend/dev_backend:  python main.py
Uses the API's models and database settings (backend/.env), so both
sides share one schema.
'''
import sys
from pathlib import Path

# The API's db and core packages live in fast_api_server
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "user_backend" / "fast_api_server"))

from db.base import Base  # noqa: E402
from db.session import engine  # noqa: E402
from extractors import brreg  # noqa: E402


if __name__ == "__main__":
    Base.metadata.create_all(bind = engine)
    count = brreg.run(engine)
    print(f"brreg: loaded {count} companies into call_list")
