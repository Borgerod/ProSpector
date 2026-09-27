''' Loads active companies from the brreg open register into call_list.

Source: https://data.brreg.no/enhetsregisteret/api/enheter/lastned/csv
(gzipped CSV, one row per company). Free, official, no key needed.
'''
import csv
import gzip
from pathlib import Path
from typing import Iterable, Iterator

import requests
from sqlalchemy import delete
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from db.models.call_list import CallList, CallListOverview

URL = "https://data.brreg.no/enhetsregisteret/api/enheter/lastned/csv"
DOWNLOAD_PATH = Path(__file__).resolve().parents[1] / "downloads" / "enheter.csv.gz"

# Same as the API's default /callList page size (main.py get_limited_call_list)
LIST_SIZE = 40

# Companies in any of these states are not worth calling
INACTIVE_FLAGS = ("konkurs", "underAvvikling", "underTvangsavviklingEllerTvangsopplosning")


def download(path: Path = DOWNLOAD_PATH) -> Path:
    path.parent.mkdir(parents = True, exist_ok = True)
    with requests.get(URL, stream = True, timeout = 60) as response:
        response.raise_for_status()
        with open(path, "wb") as f:
            for chunk in response.iter_content(chunk_size = 1 << 20):  # 1 MiB read buffer
                f.write(chunk)
    return path


def read_active_companies(rows: Iterable[dict]) -> Iterator[tuple[int, str]]:
    ''' Yields (org_num, name) for companies not bankrupt or being dissolved. '''
    for row in rows:
        if any(row[flag] == "true" for flag in INACTIVE_FLAGS):
            continue
        yield int(row["organisasjonsnummer"]), row["navn"]


def read_csv_gz(path: Path) -> Iterator[dict]:
    with gzip.open(path, "rt", encoding = "utf-8", newline = "") as f:
        yield from csv.DictReader(f)


def load(engine: Engine, companies: Iterable[tuple[int, str]]) -> int:
    ''' Replaces call_list and its overview with the given companies,
        split into lists of LIST_SIZE. Returns the number of companies.
        Replacing resets every ringe_status, as the old brreg import did.
    '''
    with Session(engine) as session:
        session.execute(delete(CallList))
        session.execute(delete(CallListOverview))
        session.commit()

    count = 0
    raw = engine.raw_connection()
    try:
        with raw.cursor() as cursor:
            with cursor.copy("COPY call_list (org_num, name, ringe_status, liste_id) FROM STDIN") as copy:
                for org_num, name in companies:
                    copy.write_row((org_num, name, False, count // LIST_SIZE + 1))
                    count += 1
            list_count = -(-count // LIST_SIZE)
            with cursor.copy("COPY call_list_overview_mediavest (liste_id, liste_start, liste_limit, er_ledig, er_ferdig) FROM STDIN") as copy:
                for liste_id in range(1, list_count + 1):
                    start = (liste_id - 1) * LIST_SIZE
                    copy.write_row((liste_id, start, min(start + LIST_SIZE, count), True, False))
        raw.commit()
    finally:
        raw.close()
    return count


def run(engine: Engine) -> int:
    return load(engine, read_active_companies(read_csv_gz(download())))
