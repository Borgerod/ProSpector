from typing import Any

from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: Any
    __name__: str

    #? burde kanskje fjerne dette ?
    # to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    #* new
    # SIMPLIFIED VERSION WITHOUT mumbo jumbo
    @declared_attr
    def __tablename__(cls) -> str:
        return declarative_base()

