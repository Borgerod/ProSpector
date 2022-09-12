'''

    GOAL DESCRIPTION & REPLATIONSHIP BETWEEN; "OverView" & "CallList"

    1. user presses renew call list for the first time. 
    2. program first checks local_state (presistant) if user has a previous call list
        if so, it will update the overview (& calllist)
    # 3. then checks the users history. 
    4. then checks checks Ovewview for the users & coworkers history
    5. filters out callList based on occopied & finished List_IDs
    6. returns the first available list. 
    7. updates said List_ID in Overview as occopied 
    8. displays callList for the user 
        CallList is presistent 
'''





'''
sammenlign CallList og Overview:

calllist:
    schemas - None
    db.models - [X]
    db.repository - [X] 
    api-route - None
    webbapp-route - None

overview:
    db.models: [X]
    db.repository: [X]

calllist-overview forskjeller: 
    db.models: overall - None
    - calllist har index=True på alle. 

    db.repository:
    - calllist har start + limit params 
    - calllist return har offset + limit 


OverView Checklist:
    db.models:
    - [X] class har (Base)
    - [X] riktig tablename 
    - [X] primary key
    - [X] riktig column-names 
    - [ ] riktig datatype
    - [ ] alle er index=True

    - [ ] sjekk session
    - [ ] sjekk base_class "Base"
            må Base inkludere overview?
    - [ ] sjekk utils 


    db.repository:
    - [ ] db: Session
    - [ ] Må Session inkludere overview?
    - [ ] getOverView caller query riktig 
'''

#_______ CHECK LISTS __________________________________

'''
        db.models checklist:

                CallList CHECK:
                    [X] org_num
                    [X] navn
                    [-] google_profil
                    [X] eier_erklært
                    [X] komplett_profil
                    [X] ringe_status
                    [X] primary_key 
                    [-] pgAdmin primary_key 


                CallListOverview CHECK:
                    [X] liste_id
                    [X] liste_start
                    [X] liste_limit
                    [X] kunde_id
                    [X] er_ledig
                    [X] er_ferdig
                    [X] primary_key 
                    [-] pgAdmin primary_key 
'''

'''
        base_class CheckList:

            [X] Overview's tablename har Stor bokstav i seg, kanskje det er hvorfor. 
                NB: Did Make A Difference: from response -> [Null] to response -> []
                    # #to generate tablename from classname
                    # --> return cls.__name__.lower()
            [ ] Hva er cls??  
'''

'''     ! NB: IMPORTANT TODO HERE
        Session CheckList:
            [X] Riktig Session 
                # - bruker feil DATABASE_URL:     "postgresql+psycopg2://sql_app.db"
                # - burde være:                   "postgresql+psycopg2://backend.db" 
                ! SOM BURDE ENDRES TILBAKE TIL sql_app NÅR DU ER FERDIG !!!
'''

'''
        Utils CheckList:
            sjekker bare om db er connected eller ikke, urelatert til tables. 
            [X] er Utils Urelatert til tables?
'''
'''
{
  "brukernavn": "Admin",
  "epost": "borgerod@hotmail.com",
  "passord": "Password123",
  "organisasjon": "a.borgerod"
}
'''