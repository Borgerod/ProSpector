from sqlalchemy.orm import Session
from db.models.call_list import CallList, CallListOverview

def getRowsBetween(db: Session, start: int, limit: int):
    return db.query(CallList).offset(start).limit(limit).all()


def getCurrentCallList(db, user):
    current_list_info = getCurrentCallListInfo(db, user.id)
    return db.query(CallList)[current_list_info.liste_start:current_list_info.liste_limit]


def getOverview(db: Session, user: int):
    ''' todo [] consider renaming getOverview to something more descriptive?
        Used to aquire a new call list.
            Checks if the current list is completed,
            if so; it updates the current list status to finished,
            finally returns renewCallList()
            if not; returns error message.
    '''
    if checkIfCurrentLists(db, user.id):
        if checkCurrentListStatus(db, kunde_id = user.id):
            return "Error, Please finish the current Call list before requesting a new one."
        updateCurrentListStatus(db, user.id)
    return renewCallList(db, user)
    # overview = db.query(CallListOverview).filter_by(er_ledig = True, er_ferdig = False).first()
    # overview.er_ledig = False
    # overview.kunde_id = user.id 
    # db.commit()
    # return db.query(CallList)[overview.liste_start:overview.liste_limit]

def renewCallList(db: Session, user: int):
    '''
        Returns the first available & unfinished list from overview. 
    '''
    overview = db.query(CallListOverview).filter_by(er_ledig = True, er_ferdig = False).first()
    overview.er_ledig = False
    overview.kunde_id = user.id 
    db.commit()
    return db.query(CallList)[overview.liste_start:overview.liste_limit]



def updateCurrentListStatus(db: Session, kunde_id: int):
    '''
        updates users overview-status for current list 
    '''
    overview = db.query(CallListOverview).filter_by(kunde_id = str(kunde_id), er_ferdig=False).first()
    overview.er_ledig = True
    overview.er_ferdig = True
    db.commit()

def checkIfCurrentLists(db: Session, kunde_id: int):
    ''' todo [] rename to something more descriptive 
    '''
    return db.query(CallListOverview).filter_by(kunde_id = str(kunde_id), er_ferdig = False).scalar()

def checkCurrentListStatus(db: Session, kunde_id: int ):
    '''
        checks if all the prospects have been called 
    '''
    current_list_info = getCurrentCallListInfo(db, kunde_id)
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
    callStatus = db.query(CallList).filter_by(org_num = str(org_num)).first()
    if callStatus.ringe_status:
         callStatus.ringe_status = False
    else:
        callStatus.ringe_status = True
    db.commit()