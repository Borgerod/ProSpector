from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
# ___ local imports ___
import SQL.db as db


def getSession():
    # Create new Session
    Session = sessionmaker(bind = db.engine)
    # session = Session()
    return Session()
# # Create new Session
# Session = sessionmaker(bind = db.engine)
# session = Session()

class Insert:
    
    def toGulesider(self, data:list):
        '''
        takes a list of data from page, splits it, then inserts it into db
        '''
        tlfErrorCounter = 0000
        orgNumErrorCounter = 0000
        session = getSession()
        # data['name']
        # data['organisationNumber']
        # data['hitType']
        # data['phones']

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

    def toCategories(self, dataset):
        '''
        takes a list of data from page, splits it, then inserts it into db
        '''
        session = getSession()
        for data in dataset:
            row = db.Categories(
                data,
            )
            session.add(row) 
        try:
            session.commit()
        except exc.IntegrityError:
            session.rollback()  
    
    def to1881Industries(self, dataset):
        '''
        takes a list of data from page, splits it, then inserts it into db
        '''
        session = getSession()
        for industry in dataset:
            row = db.Industry1881(
                industry,
            )
            session.add(row) 
            try:
                session.commit()
            except exc.IntegrityError:
                session.rollback()  


    def toProffIndustries(self, data):
        '''
        takes a list of data from page, splits it, then inserts it into db
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


    def toProff(self, org_num, navn):
            '''
            takes a list of data from page, splits it, then inserts it into db
            '''
            session = getSession()
            row = db.Proff(
                org_num,
                navn,
            )
            #! keep just in case
            try:
                session.add(row) 
                session.commit()
            except exc.IntegrityError:
                session.rollback()
    
    
    def to1881(self, org_num, navn):
        '''
        takes a list of data from page, splits it, then inserts it into db
        '''
        session = getSession()
        row = db._1881(
            org_num,
            navn,
        )
        #! keep just in case
        try:
            session.add(row) 
            session.commit()
        except exc.IntegrityError:
            session.rollback()        




# def insertDataToGulesider():
#     '''
#     takes a list of data from page, splits it, then inserts it into db
#     '''
#     for data in dataset:
#         if data['customer']:
#             org_num = data['organisationNumber']
#             navn = data['name']
#             tlf = data['phones'][0]['number']
#             row = db.Gulesider(
#                 org_num,
#                 navn,
#                 tlf,
#             )
#             session.add(row) 
#     session.commit()

# def insertDataToCategories():
#     '''
#     takes a list of data from page, splits it, then inserts it into db
#     '''
#     for data in dataset:
#         if data['customer']:
#             org_num = data['organisationNumber']
#             navn = data['name']
#             tlf = data['phones'][0]['number']
#             row = db.Gulesider(
#                 org_num,
#                 navn,
#                 tlf,
#             )
#             session.add(row) 
#     session.commit()


