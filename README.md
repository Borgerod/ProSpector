# Mediavest_Scraper_bot
Leads scraper (gule sider + google) for Mediavest AS


## framework:
Oppgaven til programmet
Så det vi vil få til er at man kan hente ut lister over bedrifter som har både betalt annonsering hos katalogene og har ledig, mangelfull eller ingen profil på Google.
-  Steg 1: Gulesider 1881, eller proff.no etter --> Bedrifter med betalt oppføring
-  Steg 2: Skrape google maps etter --> Som ikke har en eier bekreftet (Står oppført som "eier du denne bedriften")
-  Steg 2 tillegg: Skal også skrape etter bedrifter som har "mangelfull profil" ( har bekreftet eier men ingen innhold) 


## TODO
UI:
 - [ ] BIG ISSUE: CallListWidget{} when changing to darkmode/lightmode the "Ringestatus" checkboxes resets. 
 - [ ] fix darkmode Issue on app Startup 
 - [ ] make notes-state presistant  
 - [ ] complete translation to Norwegian 
 - [ ] write instructions 
 - [ ] add: "press enter" function to LoginWidget{}

API:
- [ ] finish change-password api
- [ ] finish/fix "view call list" / "renew list" button. 
- [ ] 
<!-- - [x] make api server -->


extractor:
- [ ]
<!-- - [x] finish brreg
- [x] finsih proff
- [x] finish 1881
- [x] finish gulesider
- [x] finish google -->

backend:
- [ ]
<!-- - [x] Overview: manage user progress (call list)
- [x] manage user login 
- [x] password hasher  -->


AWS:
- [ ] uplaod db to aws 
- [ ] upload code to aws (if possible)



Notes from Client:
	Det eneste vi ser etter i et prospekt er om de har:
	-  Betalt oppføring på: Proff, 1881 eller Gulesider
	-  Ingen, ikke-bekreftet eller mangelfull Google-profil 

De andre kriteriene er ikke viktig for oss da det tyder på at de har behov for markedsføring da de har kjøpt oppføring hos katalogene.

	utelukke:
	- mediebyråer & reklamebyråer
	•	Mediebyråer , Markedsføringskonsulenter  , Medie- og kommunikasjonsrådgivning , Internettdesign og programmering , Reklamebyrå


HIGHLIGT syntax
# TODO Highlighted as a TODO
# - This will also be highlighted as a TODO (Prefixed with a -)
# This will be an unhighlighted comment
# * This will be an highlighted (UNDEFINED) comment
# ! This is another comment
# - and again, continued highlighting
# ? question
# FIXME fixme comment
# // undefined comment
# # # hidden (Deprecated) comment 
# # # hidden (Deprecated) comment 
### comment

# rgba(235, 64, 52, 0.8)
# rgba(235, 255, 145, 0.8)


