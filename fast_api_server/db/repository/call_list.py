from sqlalchemy.orm import Session
from db.models.call_list import CallList, CallListOverview

def getRowsBetween(db: Session, start: int, limit: int):
    return db.query(CallList).offset(start).limit(limit).all()

def getCurrentCallList(db, user):    
    current_list_info = getCurrentCallListInfo(db, user.id)
    if current_list_info: 
        return db.query(CallList).filter_by(liste_id = current_list_info.liste_id).all()
    else:
        assignNewList(db, user.id)
        current_list_info = getCurrentCallListInfo(db, user.id)
        return db.query(CallList).filter_by(liste_id = current_list_info.liste_id).all()
        




    # # print(current_list_info.liste_id)
    # # for i in db.query(CallList)[current_list_info.liste_start:current_list_info.liste_limit]:
    # #     print(i.navn)
    # # return db.query(CallList)[current_list_info.liste_start:current_list_info.liste_limit]
    # # return db.query(CallList).filter_by(liste_id = current_list_info.liste_id).all()


def updateCurrentListStatus(db: Session, kunde_id: int):
    overview = db.query(CallListOverview).filter_by(kunde_id = str(kunde_id), er_ferdig = False).first()
    overview.er_ledig = True
    overview.er_ferdig = True
    db.commit()

def assignNewList(db: Session, kunde_id: int):
    newList = db.query(CallListOverview).filter_by(er_ledig = True, er_ferdig = False).first()
    newList.kunde_id = kunde_id
    newList.er_ledig = False
    db.commit() 
    # return newList


def checkIfCurrentLists(db: Session, kunde_id: int ):
    return db.query(CallListOverview).filter_by(kunde_id = str(kunde_id), er_ferdig = False).scalar()


def checkCurrentListStatus(db: Session, kunde_id: int ):
    current_list_info = getCurrentCallListInfo(db, kunde_id)
    overview = db.query(CallListOverview).filter_by(kunde_id = str(kunde_id), er_ferdig = False).first()
    current_list = db.query(CallList)[overview.liste_start:overview.liste_limit]
    # current_list = db.query(CallList).offset(current_list_info.liste_start).limit(current_list_info.liste_limit).all()
    all_unfinished = []
    for i in current_list:
        if i.ringe_status == False:
            all_unfinished.append(i)
    return all_unfinished        

def getCurrentCallListInfo(db: Session, kunde_id: int):
    return db.query(CallListOverview).filter_by(kunde_id = str(kunde_id)).first()

def updateCallListStatus(db: Session, org_num: int):

    callStatus = db.query(CallList).filter_by(org_num = org_num).first()
    if callStatus.ringe_status:
         callStatus.ringe_status = False
    else:
        callStatus.ringe_status = True
    db.commit()

def renewList(db: Session, user: int):
    if checkIfCurrentLists(db, user.id):
        if checkCurrentListStatus(db, kunde_id = user.id):
            return False
        updateCurrentListStatus(db, user.id)
        assignNewList(db, user.id)
        return True
    return "Error, checkIfCurrentLists() failed!"
        # updateCurrentListStatus(db, user.id)




#! [OLD] NOW SURE IF ITS NEEDED ANYMORE
def getOverview(db: Session, user: int):
    if checkIfCurrentLists(db, user.id):
        if checkCurrentListStatus(db, kunde_id = user.id):
            return "Error, Please finish the current Call list before requesting a new one."
        updateCurrentListStatus(db, user.id)
    overview = db.query(CallListOverview).filter_by(er_ledig = True, er_ferdig = False).first()
    overview.er_ledig = False
    overview.kunde_id = user.id 
    db.commit()
    return db.query(CallList)[overview.liste_start:overview.liste_limit]#.all()
