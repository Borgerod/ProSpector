from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded

def getOverview(db: Session, user: int):
    if checkIfCurrentLists(db, user.id):
        if checkCurrentListStatus(db, kunde_id=user.id):
            return "Error, Please finish the current Call list before requesting a new one."
        updateCurrentListStatus(db, user.id)
    overview = db.query(CallListOverview).filter_by(er_ledig=True, er_ferdig=False).first()
    overview.er_ledig = False
    overview.kunde_id = user.id 
    db.commit()
    return db.query(CallList)[overview.liste_start:overview.liste_limit]#.all()

def updateCurrentListStatus(db: Session, kunde_id: int):
    overview = db.query(CallListOverview).filter_by(kunde_id = str(kunde_id), er_ferdig=False).first()
    overview.er_ledig = True
    overview.er_ferdig = True
    db.commit()


def updateCallListStatus(db: Session, org_num: int):
    callStatus = db.query(CallList).filter_by(org_num = str(org_num)).first()
    if callStatus.ringe_status:
         callStatus.ringe_status = False
    else:
        callStatus.ringe_status = True
    db.commit()
     

@app.put("/callList/items")
async def update_item(item_id: str, item: org_num, db: Session = Depends(get_db)):
    return updateCallListStatus(db: Session, org_num: int)




class CallList(Base):
    __tablename__ = "call_list"
    org_num = Column(Integer, unique=True, index=True, primary_key=True)
    navn = Column(String, index=True)
    google_profil = Column(String, index=True)
    eier_bekreftet = Column(Boolean(), index=True)
    komplett_profil = Column(Boolean(), index=True)
    ringe_status = Column(Boolean(), index=True)

class CallListOverview(Base):
    __tablename__ = "call_list_overview_mediavest"
    liste_id = Column(Integer, unique=True, index=True, primary_key=True)
    liste_start = Column(Integer, unique=True, index=True)
    liste_limit = Column(Integer, unique=True, index=True)
    kunde_id = Column(String, unique=True, index=True)
    er_ledig = Column(Boolean(), default=True, index=True)
    er_ferdig = Column(Boolean(), default=False, index=True)



