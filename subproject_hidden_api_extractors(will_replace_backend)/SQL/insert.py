from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
# ___ local imports ___
import SQL.db as db

# Create new Session
Session = sessionmaker(bind = db.engine)
session = Session()

class Insert:
    
    def toGulesider(self, data:list):
        '''
        takes a list of data from page, splits it, then inserts it into db
        '''
        tlfErrorCounter = 0000
        orgNumErrorCounter = 0000
        try:
            org_num = data['organisationNumber']
        except KeyError:
            orgNumErrorCounter+=1
            org_num = 404000+tlfErrorCounter
        navn = data['name']
        try:
            tlf = data['phones'][0]['number']            
        except KeyError:
            tlfErrorCounter+=1
            tlf = 404000+tlfErrorCounter
        row = db.Gulesider(
            org_num,
            navn,
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
        for data in dataset:
            row = db.Categories(
                data,
            )
            session.add(row) 
        try:
            session.commit()
        except exc.IntegrityError:
            session.rollback()  


    def toIndustries(self, data):
        '''
        takes a list of data from page, splits it, then inserts it into db
        '''
        row = db.Industry(
            data,
        )
        session.add(row) 
        try:
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


