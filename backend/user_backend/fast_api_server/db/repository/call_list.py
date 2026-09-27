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


def checkIfCurrentLists(db: Session, kunde_id: int ):
    return db.query(CallListOverview).filter_by(kunde_id = str(kunde_id), er_ferdig = False).scalar()


def checkCurrentListStatus(db: Session, kunde_id: int ):
    current_list_info = getCurrentCallListInfo(db, kunde_id)
    overview = db.query(CallListOverview).filter_by(kunde_id = str(kunde_id), er_ferdig = False).first()
    liste_id = overview.liste_id
    current_list = db.query(CallList).filter_by(liste_id = str(liste_id)).all()
    all_unfinished = []
    for i in current_list:
        if i.ringe_status == False:
            all_unfinished.append(i)
    return all_unfinished        

def getCurrentCallListInfo(db: Session, kunde_id: int):
    return db.query(CallListOverview).filter_by(kunde_id = str(kunde_id)).first()

def updateCallListStatus(db: Session, org_num: int, user) -> bool:
    ''' Toggles ringe_status for a row in the user's current list. False if the row is not there. '''
    current_list_info = getCurrentCallListInfo(db, user.id)
    if not current_list_info:
        return False
    callStatus = db.query(CallList).filter_by(org_num = org_num, liste_id = current_list_info.liste_id).first()
    if not callStatus:
        return False
    callStatus.ringe_status = not callStatus.ringe_status
    db.commit()
    return True

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
