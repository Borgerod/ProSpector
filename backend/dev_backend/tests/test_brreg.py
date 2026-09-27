import csv
import gzip

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from db.models.call_list import CallList, CallListOverview
from extractors import brreg

FIELDS = ["organisasjonsnummer", "navn", "telefon", "mobil", "konkurs", "underAvvikling", "underTvangsavviklingEllerTvangsopplosning"]


def write_fixture(path, rows):
    with gzip.open(path, "wt", encoding = "utf-8", newline = "") as f:
        writer = csv.DictWriter(f, fieldnames = FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def company(org_num, name, telefon = "", mobil = "", konkurs = "false", avvikling = "false", tvang = "false"):
    return dict(zip(FIELDS, [str(org_num), name, telefon, mobil, konkurs, avvikling, tvang]))


def test_inactive_companies_are_skipped(tmp_path):
    path = tmp_path / "enheter.csv.gz"
    write_fixture(path, [
        company(810000001, "Aktiv AS", telefon = "51 68 57 00"),
        company(810000002, "Konkurs AS", konkurs = "true"),
        company(810000003, "Avvikling AS", avvikling = "true"),
        company(810000004, "Tvang AS", tvang = "true"),
    ])
    assert list(brreg.read_active_companies(brreg.read_csv_gz(path))) == [(810000001, "Aktiv AS", "51 68 57 00", None)]


def test_load_splits_into_lists(db_engine):
    companies = [(900000000 + i, f"Firma {i}", None, None) for i in range(brreg.LIST_SIZE + 1)]
    assert brreg.load(db_engine, companies) == brreg.LIST_SIZE + 1
    with Session(db_engine) as session:
        assert session.scalar(select(func.count()).select_from(CallList)) == brreg.LIST_SIZE + 1
        overviews = session.scalars(select(CallListOverview).order_by(CallListOverview.liste_id)).all()
        assert [(o.liste_id, o.liste_start, o.liste_limit) for o in overviews] == [
            (1, 0, brreg.LIST_SIZE), (2, brreg.LIST_SIZE, brreg.LIST_SIZE + 1)]
        assert session.get(CallList, 900000000 + brreg.LIST_SIZE).liste_id == 2


def test_load_replaces_previous_data(db_engine):
    brreg.load(db_engine, [(111111111, "Old AS", None, None)])
    brreg.load(db_engine, [(222222222, "New AS", "22 22 22 22", "999 99 999")])
    with Session(db_engine) as session:
        rows = session.scalars(select(CallList)).all()
        assert [(r.org_num, r.telefon, r.mobil) for r in rows] == [(222222222, "22 22 22 22", "999 99 999")]
