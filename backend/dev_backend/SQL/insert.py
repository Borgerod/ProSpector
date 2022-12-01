from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
import pandas as pd 
import numpy as np 
# ___ local imports ___
import SQL.db as db


def getSession() -> None:
    # Create new Session
    Session = sessionmaker(bind = db.engine)
    # session = Session()
    return Session()
# # Create new Session
# Session = sessionmaker(bind = db.engine)
# session = Session()

# class Insert:
class Insert:
    
    def toGulesider(self, data:list) -> None:
        '''
        takes a list of data from page, splits it, then inserts it into db
        '''
        tlfErrorCounter = 0000
        orgNumErrorCounter = 0000
        session = getSession()

        try:
            org_num = data['organisationNumber']
        except KeyError:
            orgNumErrorCounter+=1
            org_num = 404000+orgNumErrorCounter
        navn = data['name']
        try:
            tlf = data['phones'][0]['number']            
        except KeyError:
            tlfErrorCounter+=1
            tlf = 404000+tlfErrorCounter
        is_premium = False
        if data['hitType'] == 'premium':
            is_premium = True
        row = db.Gulesider(
            org_num,
            navn,
            is_premium,
            tlf,
        )
        try:
            session.add(row) 
            session.commit()
        except exc.IntegrityError:
            session.rollback()

    def toCategories(self, data:str) -> None:
        '''
        takes a list of data from page, splits it, then inserts it into db
        '''
        session = getSession()
        row = db.Categories(
            data,
        )
        session.add(row) 
        try:
            session.commit()
        except exc.IntegrityError:
            session.rollback()  
    
    def to1881Industries(self, data:str) -> None:
        '''
        takes a list of data from page, splits it, then inserts it into db
        '''
        session = getSession()
        row = db.Industry1881(
            data,
        )
        session.add(row) 
        try:
            session.commit()
        except exc.IntegrityError:
            session.rollback()  

    def toProffIndustries(self, data:str) -> None:
        '''
        takes data from page, splits it, then inserts it into db
        '''
        session = getSession()
        row = db.IndustryProff(
            data,
        )
        session.add(row) 
        try:
            session.commit()
        except exc.IntegrityError:
            session.rollback()  

    def toProff(self, org_num, navn, tlf) -> None:
            '''
            takes a list of data from page, splits it, then inserts it into db
            '''
            session = getSession()
            row = db.Proff(
                org_num,
                navn,
                tlf
            )
            #! keep just in case
            try:
                session.add(row) 
                session.commit()
            except exc.IntegrityError:
                session.rollback()
      
    def to1881(self, org_num, navn, tlf) -> None:
        '''
        takes a list of data from page, splits it, then inserts it into db
        '''
        session = getSession()
        row = db._1881(
            org_num,
            navn,
            tlf
        )
        #! keep just in case
        try:
            session.add(row) 
            session.commit()
        except exc.IntegrityError:
            session.rollback()        

    def toGoogle(self, array:np.ndarray) -> None:
        '''
        inserts generated list and inserts it into googleInputTable
        '''
        session = getSession()
        for data in array:
            row = db.Google(
            data[0], #org_num   
            data[1], #name
            data[2], #loc        
            )
            session.add(row) 
        try:
            session.commit()
        except exc.IntegrityError:
            session.rollback()  


# TODO: [x] implement Phone numbers and add to Call List.
    def toCallList( self, org_num:int, navn:str, tlf:str,
                    google_profil:str, eier_bekreftet:bool, komplett_profil:bool, 
                    ringe_status:bool, link_til_profil:str,
                    ) -> None:
        '''
        Used by google.py inserts output into AWS db
        '''
        session = getSession()
        row = db.CallList(
            org_num,
            navn,
            google_profil,
            eier_bekreftet,
            komplett_profil,
            ringe_status,
            link_til_profil,
        )
        try:
            session.add(row) 
            session.commit()
        except exc.IntegrityError:
            session.rollback()

