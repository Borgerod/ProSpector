# ProSpector
Lead generation software, commissioned by Mediavest AS. <br />
data source:  brreg.no  &nbsp;|&nbsp; extraction targets:  gulesider.no, 1881.no, proff.no and gooogle.com  <br />


## Rundown:
#### [ENG] The software's tasks:
So what we want to achieve is that you can retrieve lists of companies that have both paid advertisements in the catalogs and have a vacant, deficient or no profile on Google.
- Step 1: Gulesider 1881, or proff.no after --> Companies with paid paid
- Step 2: Scrape google maps for --> Which does not have an owner confirmed (Listed as "do you own this business")
- Step 2 addition: Must also scrape for companies that have an "insufficient profile" (has confirmed the owner without content)

#### [NO] Programvarens oppgaver:
Så det vi vil få til er at man kan hente ut lister over bedrifter som har både betalt annonsering hos katalogene og har ledig, mangelfull eller ingen profil på Google.
-  Steg 1: Gulesider 1881, eller proff.no etter --> Bedrifter med betalt oppføring
-  Steg 2: Skrape google maps etter --> Som ikke har en eier bekreftet (Står oppført som "eier du denne bedriften")
-  Steg 2 tillegg: Skal også skrape etter bedrifter som har "mangelfull profil" ( har bekreftet eier men ingen innhold) 




## TODO
#### UI:
   - [X] BIG ISSUE: CallListWidget{} when changing to darkmode/lightmode the "Ringestatus" checkboxes resets. 
   - [ ] Fix darkmode Issue on app Startup 
   - [X] Make notes-state presistant [note: a small bug with loading]
   - [ ] Complete translation to Norwegian 
   - [ ] Write instructions 
   - [ ] Add: "press enter" function to LoginWidget{}
   - [ ] Finish "remember me" knapp 
   - [ ] Increase min.windowsize 
   - [ ] Change fontweight for bodytext in "renew list"   
   - [ ] [ Low Prio ] Make "Instructions from Supervisor" section in "Instructions"
   		- [ ] Add section editable for supervisors & other privilages
   		- [ ] Add Column "supervisor" in user-db 
   - [ ] [ Low Prio ] Clean up files (but first verify functionality, then backup)
   - [ ] [ Low Prio ] Maybe add splash screen / loading screen
   - [ ] [ Low Prio ] Make instructions look Nicer 

##### UI (small bugs):
   - [ ] Loading issue with presistant satates [notes_page.dart]
   - [ ] Laggy transition of light/darkmode    [menu_widget.dart]
   - [ ] Acryllic allways opens in darkmode    [menu_widget.dart]
   - [ ] Maximize window, often needs 2 clicks [window_title_bar.dart] (I think)
   - [ ] Overflow in About in smallwindow      [about_widget.dart / main.dart]
   - [ ] ... [  ]


#### API:
   - [x] Make api server
   - [ ] Finish change-password api
   - [ ] Finish/fix "view call list" / "renew list" button. 
   - [ ] ...


#### Extractor:
   - [x] Finish brreg
   - [x] Finsih proff
   - [x] Finish 1881
   - [x] Finish gulesider
   - [x] Finish google
   - [ ] ...

#### Backend:
   - [x] Overview: manage user progress (call list)
   - [x] Manage user login 
   - [x] Password hasher 
   - [ ] ...

#### AWS:
   - [ ] uplaod db to aws 
   - [ ] upload code to aws (if possible)



## Notes from Client:
	Det eneste vi ser etter i et prospekt er om de har:
	-  Betalt oppføring på: Proff, 1881 eller Gulesider
	-  Ingen, ikke-bekreftet eller mangelfull Google-profil 
		
	"De andre kriteriene er ikke viktig for da det tyder på at de har behov for markedsføring da de har kjøpt oppføring hos katalogene."

	utelukke:
	- mediebyråer & reklamebyråer
	•	Mediebyråer , Markedsføringskonsulenter  , Medie- og kommunikasjonsrådgivning , Internettdesign og programmering , Reklamebyrå

