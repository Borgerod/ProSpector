# ProSpector
SaaS Lead generation software, commissioned by Mediavest AS. <br />
data source:  brreg.no  &nbsp;|&nbsp; extraction targets:  gulesider.no, 1881.no, proff.no and gooogle.com  <br />

## Copyright Stamement
Please note that this repository is temporarly set to public due to job-applications, 
this is a private source-code to a product for sale. You do not have premission to use this code for private use or financial gain.
As defined by the Copyright act 1968; no content from this repository may be reproduced, transmitted or copied without the ecpress written permission of A.Borgerød.
Application made by Aleksander Borgerød, all rights reserved to (C) 2022 A.Borgerød ENK. 


## Summary
Job Completed: October 2022 [renovated; november 2022]
Job type: B2B SaaS development
Job categogy: Data Extraction, Lead Generation, Database server, Cloud Computing, API integration
Language: Python, Dart
Style: OOP


## Rundown:
#### [ENG] The software's tasks:
So what we want to achieve is that you can retrieve lists of companies that have both paid advertisements in the catalogs and have a vacant, deficient or no profile on Google.
- Step 1: Gulesider 1881, or proff.no after --> Companies with paid paid
- Step 2: Scrape google maps for --> Which does not have an owner confirmed (Listed as "do you own this business")
- Step 2 addition: Must also scrape for companies that have an "insufficient profile" (has confirmed the owner without content)

   ##### The software structure, simply explained:
      The shop             : App (frontend)  : /App
      The back-office      : App (backend)   : /fast_api_server/*
      The delivery truck   : Api             : /fast_api_server/main.py
      The Warehouse        : Cloud storage   : [AWS](https://aws.amazon.com/)
      The Manifacturer     : Data Extractor  : /backend

#### [NO] Programvarens oppgaver:
Så det vi vil få til er at man kan hente ut lister over bedrifter som har både betalt annonsering hos katalogene og har ledig, mangelfull eller ingen profil på Google.
-  Steg 1: Gulesider 1881, eller proff.no etter --> Bedrifter med betalt oppføring
-  Steg 2: Skrape google maps etter --> Som ikke har en eier bekreftet (Står oppført som "eier du denne bedriften")
-  Steg 2 tillegg: Skal også skrape etter bedrifter som har "mangelfull profil" ( har bekreftet eier men ingen innhold) 

   ##### The software structure, simply explained:
      Butikken    : App (frontend)  : /App
      Bakrommet   : App (backend)   : /fast_api_server/*
      varebil     : Api             : /fast_api_server/main.py
      Lageret     : Cloud storage   : [AWS](https://aws.amazon.com/)
      Fabrikken   : Data Extractor  : /backend


## PreView
![splash](https://user-images.githubusercontent.com/97392841/196432180-2d0efdcc-454c-4e0d-9cf7-bf4a69deff40.JPG)
![login](https://user-images.githubusercontent.com/97392841/196432256-8e8a61f5-e17e-441d-a379-459c75cd80ba.JPG)
![home_dark](https://user-images.githubusercontent.com/97392841/196432172-647b9794-2bb8-4eac-9def-712fde47d625.JPG)
![home_light](https://user-images.githubusercontent.com/97392841/196432176-0f9200b6-9bed-486f-acb0-d437c7657047.JPG)
![call_list](https://user-images.githubusercontent.com/97392841/196432170-9e15c096-1b69-4e22-b15a-2886a6755434.JPG)
![about](https://user-images.githubusercontent.com/97392841/196432168-89580045-b235-4ffe-80a5-54caaa37da55.JPG)


# GLOSSARY
| **Term** |      **Definition**      |
|:--------:|:------------------------:|
| 2C4E     | Too crude for Efficiency |
|          |                          |
|          |                          |

# TODO
<br>


### CURRENT PROGRESS for todo tasks: 
NOTE: This todo-list is NOT up to date [28.11.2022]
------------------------------------------------------------------------

   **Task 1. Address-Implemention for GoogleExtractor**

   | No. | Progress                                                       
   |:---:|:----------------------------:|
   | 1   | added addresses to brreg_table 
   <!-- | 2   | added addresses to input_table -->
   <!-- | 3   | Optimize SQL functions in postgres.py   -->
   <!-- | 4   | add address implementation to Google Extractor  -->
   <!-- | 5   | remove unnessasary code from search tree      -->


------------------------------------------------------------------------

<br><br><br>



### POST CLIENT-MEETING TODO:
------------------------------------------------------------------------
   ### Overall: 
   - [x] rename /Mediavest_Scraper_bot/ to /ProSpector/ 
   - [ ] Reform / reorganize directory; \n NOTE: every path-reference is relative to (root) /prospector/ so: "./" means "/prospector/"
         - 
         - move fast_api_server to /prospector/ or ./backend/
         - move or remove ./phone_verification.py
         - 
         - remove all README.md except for ./README.md
         - remove ./release (is old)
         - remove ./fast_api_server (is old)
         - remove ./sql_app (is old)
         - remove all unnessasary (fake) files and folders from ./App/../release/
         - 
         - create shortcut for ./App/../release/
         - create shortcut for ./App/../app_version_check/installers/
   - [ ] Fix the .env concept for ./App/../fast_api_server/ & ./backend/ [CURRENTLY-IN-PROGRESS]
         - (MAYBE) remove ./App/../release/..fast_api_server/backend/.env
         - (MAYBE) remove ./App/../release/env/
         - (MAYBE) remove ./env/
         - implement proper .env functionality in code 
         - make instructions for setup.exe to add enviorment variables. 
   - [ ] Change Password for Postgres (and maybe AWS) [CURRENTLY-IN-PROGRESS]
   - [ ] update .gitignore

   ### UPDATE FROM TEST:
   - [ ] Fix gmail account -- error messages (fortell google at det er en bot og det IKKE er suspisios activity)
   - [ ] Til google extractor --> legg til adresse og poststed i google søket istedenfor maps. 
   - [ ] Fjerne utlandske bedrifter
   - [ ] Mål oppdatere listen annen hver uke (helst hver uke) (optimaliser listen)
   - [ ] VIL ikke oppdatere listen 
        - får også melding om godkjent, listebytte når den ikke skal det.
   - [ ] Mulig feil med data extraction, mulig noen av dem ikke har google profil. (eller har hatt når der ble scrapet) eks. odds medsbu dødsbo  

   ### Database:
   - [ ] Remove prospects in "call_list" that has [true, true, true]
   - [ ] Reset liste_id 
   - [ ] add phone_numbers to your user database

   ### Backend-Extractor:
   - [x] Investigate "wrong org_num"-bug for some of the prospects, see bugs[1]
      - [ ] add tag on input_list from BRREG: "if Organisasjonsform == "Norskregistrert utenlandsk foretak": check & confirm org_num"
   - [x] Add function that detects googles "search-suggestion", parse & extract
   - [ ] replace "replace if row exsist" function with an update function
   - [x] make phone_verification-backend 
   - [x] integrate phone_verification-backend to fast-api-server
   - [x] make sure if you need an if statement to restrict to one account pr phone number 
   - [ ] add daily quotas
   - [ ] implement adresses to input_table & brreg_table to be used by GoogleExtractor [see CURRENT PROGRESS (1)]
   - [ ] Reform SQL structure in postgres.py --> Status Quo: 2C4E (too crude for efficiancy)

     ### Extractor Optimization:
      ''' Use practises from "clean code" to optimize and objectify the code
       - [x] Refine Extractor in Google.py
       - [ ] Refine Extractor in gulesider.py
       - [ ] Refine Extractor in proff.py
       - [ ] Refine Extractor in 1881.py
   
   ### Backend-Server:
   - [ ] add Exeption handling for more precise exceptions, irt. signup-errors (all types of signup-errors are returned as 500 "Internal server error" )
   - [ ] reorganize fast_api_server; remove all the unnessasary folders. 
   - [x] re-Enable send EMAIL functionality
   - [ ] Consider merging ./backend/SQL/ & ./fast_api_server/  ==> Will merge? [ ] yes or [ ] no
    

   ### Frontend:
   - [?] Add copy function to the call list table 
   - [x] add phone_verification to your app 
   - [ ] Implement the specific Exception handling from "todo: Backend-Server"

   ### bugs:
   - [1] : 
   - [2] : 
<br>
------------------------------------------------------------------------
<br><br><br>

### BEFORE DEMO RELEASE:
------------------------------------------------------------------------
''' Todo list of bugs that occored upon compiling '''
   - [ ] add to .bat add uvicorn to path
   - [ ] add a python checker in setup.exe
   - [ ] Make gtihub repo private and give installer access key (or something like that)
   - [x] Fix Login button error [high prio] (ROOT BUG)
   - [x] Fix loading screen bug [low prio] (Unknown)
   - [x] fix Expanded - Stack bug [high prio] (ROOT BUG)
   - [x] fix plain_background error [medium prio] (RESIDUAL BUG)
   - [x] Add installer
   - [x] Implement update-function
   - [x] Add function that starts fastAPI server upon app-launch 
   - [x] change update function to change "current version" to 1.X+1 after the installation was sucsessfull. 
   - [x] make sure that server-terminal opens either in background / minimized or behind UI   
   - [ ] ...

### UI:
   - [x] BIG ISSUE: CallListWidget{} when changing to darkmode/lightmode the "Ringestatus" checkboxes resets. 
   - [x] Fix darkmode Issue on app Startup [note: see small bugs]
   - [x] Make notes-state presistant [note: a small bug with loading]
   - [x] Complete translation to Norwegian 
   - [x] Write instructions 
   - [x] Add: "press enter" function to LoginWidget{}
   - [x] Finish "remember me" knapp 
   - [x] fix text borders in instructions
   - [x] [ Low Prio ] Fix border Issue with popups
   - [x] [ Low Prio ] Increase min.windowsize 
   - [x] [ Low Prio ] Change fontweight for bodytext in "renew list"   
   - [ ] [ Low Prio ] Make "Instructions from Supervisor" section in "Instructions"
   		- [ ] Add section editable for supervisors & other privilages
   		- [ ] Add Column "supervisor" in user-db 
   - [x] [ Low Prio ] Clean up files (but first verify functionality, then backup)
   - [x] [ Low Prio ] Maybe add splash screen / loading screen
   - [x] [ Low Prio ] Make instructions look Nicer 
   - [ ] ...

### UI (small bugs):
   - [x] Loading issue with presistant state   [notes_page.dart]
   - [x] Laggy transition of light/darkmode    [menu_widget.dart]
   - [x] Acryllic allways opens in darkmode    [menu_widget.dart]
   - [x] Maximize window, often needs 2 clicks [window_title_bar.dart] (I think)
   - [x] Overflow in About in smallwindow      [about_widget.dart / main.dart]
   - [ ] ...


### API:
   - [x] Make api server
   - [x] Finish change-password api
   - [x] Finish/fix "view call list" / "renew list" button. 
   - [ ] ...


### Extractor:
   - [x] Finish brreg
   - [x] Finsih proff
   - [x] Finish 1881
   - [x] Finish gulesider
   - [x] Finish google
   - [ ] ...

### Backend:
   - [x] Overview: manage user progress (call list)
   - [x] Manage user login 
   - [x] Password hasher 
   - [ ] ...

### AWS:
   - [x] uplaod db to aws 
   - [ ] upload code to aws (if possible)
   - [x] Test if RDS works without postgres. 



## Notes from Client:
	Det eneste vi ser etter i et prospekt er om de har:
	-  Betalt oppføring på: Proff, 1881 eller Gulesider
	-  Ingen, ikke-bekreftet eller mangelfull Google-profil 
		
	"De andre kriteriene er ikke viktig for da det tyder på at de har behov for markedsføring da de har kjøpt oppføring hos katalogene."

	utelukke:
	- mediebyråer & reklamebyråer
	•	Mediebyråer , Markedsføringskonsulenter  , Medie- og kommunikasjonsrådgivning , Internettdesign og programmering , Reklamebyrå

