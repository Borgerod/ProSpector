




______________________________ TEST 1 _____________________________________________________________
'https://www.google.com/search?q=S%20THORSTENSEN%20AS%20maps'
'https://www.google.com/search?q=TAKSTPLAN%20AS%20maps'
'https://www.google.com/search?q=VOLDENTOLLEFSEN%20AS%20maps'
'https://www.google.com/search?q=ANTI%20AS%20maps'
'https://www.google.com/search?q=SJÅSUND%20MARINE%20AS%20maps'
'https://www.google.com/search?q=NORSK%20TAKSERING%20AS%20maps'
'https://www.google.com/search?q=TERAX%20TRANSPORTSERVICE%20AS%20maps'
'https://www.google.com/search?q=A%20VÅGE%20AS%20maps'
'https://www.google.com/search?q=THERESE%20GIVING%20maps'
'https://www.google.com/search?q=LATOR%20SKILTFABRIKK%20AS%20maps'
'https://www.google.com/search?q=ANNE%20MARTHE%20KALDESTAD%20HANSTVEIT%20maps'
'https://www.google.com/search?q=BAUNEN%20FISK%20OG%20VILT%20AS%20maps'
'https://www.google.com/search?q=ANNE%20KARI%20ØDEGÅRD%20maps'
'https://www.google.com/search?q=FYSIOTERAPI%20RENATE%20MEIJER%20maps'
'https://www.google.com/search?q=VARMEISOLERING%20AS%20maps'

OUTPUT:
	org_num                             navn  google_profil      eier_erklært     komplett_profil
0   816744342                 S THORSTENSEN AS         False [x]         False [x]           False [x]
1   816762022                     TAKSTPLAN AS          True [x]          True [x]           False [x]
2   816795842               VOLDENTOLLEFSEN AS          True [x]          True [x]            True [x]
3   816809932                          ANTI AS          True [x]          True [x]            True [x]
4   816810132                SJÅSUND MARINE AS          True [x]         False [x]            True [x]
5   814319962               NORSK TAKSERING AS          True [x]         False [x]           False [x]
6   814391132            LATOR SKILTFABRIKK AS          True [x]          True [x]            True [x]
7   814398072                VARMEISOLERING AS          True [x]          True [x]            True [x]
8   814454932        TERAX TRANSPORTSERVICE AS          True [x]          True [x]            True [x]
9   814478912                   THERESE GIVING         False [x]         False [x]           False [x]
10  999654126                        A VÅGE AS      Usikkert [-]          True [x]            True [x]   #! Feil skyldes "." i "A. Våge AS"
11  999662757  ANNE MARTHE KALDESTAD HANSTVEIT      Usikkert [x]          True [x]           False [x]
12  999665497                ANNE KARI ØDEGÅRD          True [x]         False [x]           False [x]
13  999665896           BAUNEN FISK OG VILT AS          True [x]         False [x]           False [x]
14  999666612        FYSIOTERAPI RENATE MEIJER         False [x]         False [x]           False [x]




FASIT:
	org_num                             navn google_profil  eier_erklært  komplett_profil
0   816744342                 S THORSTENSEN AS         False         False            False
1   816762022                     TAKSTPLAN AS         True          True             False 			
2   816795842               VOLDENTOLLEFSEN AS         True          True             True  
3   816809932                          ANTI AS         True          True             True  
4   816810132                SJÅSUND MARINE AS         True          False            True 
5   814319962               NORSK TAKSERING AS         True          False            False 
6   814391132            LATOR SKILTFABRIKK AS         True          True             True 
7   814398072                VARMEISOLERING AS         True          True             True 
8   814454932        TERAX TRANSPORTSERVICE AS         True          True             True 
9   814478912                   THERESE GIVING         False         False            False 
10  999654126                        A VÅGE AS         True          True             True 
11  999662757  ANNE MARTHE KALDESTAD HANSTVEIT         Usikkert      True             False 
12  999665497                ANNE KARI ØDEGÅRD         True          False            False
13  999665896           BAUNEN FISK OG VILT AS         True          False            False 
14  999666612        FYSIOTERAPI RENATE MEIJER         False         False            False


#* konklusjon: Alt Stemmer Utenom én liten punktum feil. 



______________________________ TEST 2 _____________________________________________________________
'https://www.google.com/search?q=NAMDAL%20GLASSERVICE%20AS%20maps'
'https://www.google.com/search?q=TELEMIX%20AS%20maps'
'https://www.google.com/search?q=PER%20MULVIK%20AS%20maps'
'https://www.google.com/search?q=ENGØ%20GÅRD%20AS%20maps'
'https://www.google.com/search?q=SHG%20TRANSPORT%20AS%20maps'
'https://www.google.com/search?q=AKTIV%20EIENDOMSMEGLING%20AS%20maps'
'https://www.google.com/search?q=DAVID%20LANDSVERK%20maps'
'https://www.google.com/search?q=BUYPASS%20AS%20maps'
'https://www.google.com/search?q=ARNULF%20LARSSEN%20AS%20maps'

OUTPUT:
	org_num                             navn  google_profil      eier_erklært     komplett_profil
0  941881459  PETROLEUMSERVICE Robert Jacobsen      Usikkert [x]        False [x]           False [x]
1  941883680             NAMDAL GLASSERVICE AS          True [x]         True [x]            True [x]
2  941921280                        TELEMIX AS          True [x]         True [x]            True [x]
3  941987516                     PER MULVIK AS          True [x]         True [x]            True [x]
4  941988954                      ENGØ GÅRD AS          True [x]        False [x]            True [x]
5  983152465                  SHG TRANSPORT AS          True [x]        False [x]           False [x]
6  983154980          AKTIV EIENDOMSMEGLING AS         False [x]        False [x]           False [x]
7  983155499                   DAVID LANDSVERK      Usikkert [-]        False [x]           False [x]	#! Feil skyldes; navn stemmer ikke med ad men er tydelig en annen person.  
8  983163327                        BUYPASS AS         False [x]        False [x]           False [x]
9  983164994                 ARNULF LARSSEN AS         False [x]        False [x]           False [x]

FASIT:
	org_num                             navn google_profil  eier_erklært  komplett_profil
# 0  941881459  PETROLEUMSERVICE Robert Jacobsen         Usikkert      False            False 
# 1  941883680             NAMDAL GLASSERVICE AS         True          True             True
# 2  941921280                        TELEMIX AS         True          True             True
# 3  941987516                     PER MULVIK AS         True          True             True
# 4  941988954                      ENGØ GÅRD AS         True          False             True
# 5  983152465                  SHG TRANSPORT AS         True          False            False
# 6  983154980          AKTIV EIENDOMSMEGLING AS         False         False            False
# 7  983155499                   DAVID LANDSVERK         False         False            False
# 8  983163327                        BUYPASS AS         False         False            False
# 9  983164994                 ARNULF LARSSEN AS         False         False            False

#* konklusjon: Alt Stemmer Utenom én liten usikkerhets (som tilgis). 






	org_num                                               navn google_profil  eier_erklært  komplett_profil███████████████████████████████████████████████████████████████████████████████████████████    | 49/50 [00:16<00:00,  5.03it/s]
0   810182482                       FAGMØBLER HERMAN ANDERSEN AS      Usikkert         False             True
1   810392312                                        METALLCO AS          True         False             True
2   810574232               AS TROMSØ AUTOMOBILCOMPANI - AS TACO          True          True             True
3   810876832                       FINN BRYNILDSRUD & SØNNER AS          True          True             True
4   811548022                                     FRØY REDERI AS          True         False            False
5   811563552                           STANDART BYGG & PLATT AB          True         False            False
6   811608602                               UNDERSTELLSERVICE AS          True          True            False
7   811616362                                    VEST MARKISE AS          True          True             True
8   811662712                       WALTER HEIDKAMP MÅL & MENING         False         False            False
9   811669512                                  NILSEN TV-SERVICE          True          True            False
10  811683922                               SOUMAH RENHOLD SEKOU      Usikkert          True             True
11  811702552                 NØTTERØY KONSULENTTJENESTER DØRDAL      Usikkert         False            False
12  811717142                             OLSEN AUTO JESSHEIM AS          True          True             True
13  811723622                               TORNADO TRANSPORT AB          True         False            False
14  811751502                              MALERMESTER BRAUTE AS          True          True            False
15  811770892                            ET HÅRSTUDIO EIDSVÅG AS          True          True             True
16  811799572                                  BJØRN HÅGENSEN AS         False         False            False
17  811890332                             NORMANN COPENHAGEN APS      Usikkert          True             True
18  812045482                            OTTESTAD BILVERKSTED AS          True         False             True
19  812055372                                         KB BYGG AS          True          True             True
20  812077872                                 VERGE TELEMARK LTD      Usikkert          True             True
21  812126032                                     VRT HOLDING AS          True         False            False
22  812181912                                  VINDUSPUSSEREN AS          True          True             True
23  812187082                                TELLUS LOGISTICS AS          True          True             True
24  812269232                              SIA PEARL BALTIC LABS         False         False            False
25  812297732                              SANDEFJORD MARITIM AS          True          True             True
26  812303902                                      TST MASKIN AS          True          True             True
27  812330152                        TAKTEKKERMESTER BJØRSVIK AS          True          True             True
28  812338862                                         SAVAL B.V.      Usikkert          True             True
29  812372262                                    OMV PETROM S.A.         False         False            False
30  812398652                                       HÅRSTRÅET AS          True          True             True
31  812409832                                      SAFETYRESPECT          True          True             True
32  812417312                                  HARALDSEN AUTO AS          True         False             True
33  812441752                                            VUVI AS          True          True             True
34  812450212                               LYD & TELE LARVIK AS         False         False            False
35  812479792            WORKFORCE INTERNATIONAL CONTRACTORS LTD      Usikkert         False             True
36  812481312                                        VEAS RØR AS          True          True            False
37  812512862                                      RØRLEGGER1 AS      Usikkert          True             True
38  812518372                           STALBUD TARNOW SP.Z.O.O.      Usikkert         False            False
39  812541692                               SKAGERAK REGNSKAP AS          True          True             True
40  812548212                                STENSVOLD ANLEGG AS          True          True            False
41  812644912                 TD RAIL & INDUSTRY - CONSULTING AB         False         False            False
42  812651722                                    WO INTERIOR A/S          True         False            False
43  812668412                          EKER DAMPSAG & HØVLERI AS      Usikkert         False             True
44  812702742                             NEXT ONE TECHNOLOGY AS         False         False            False
45  812752642                                         SON VVS AS          True          True             True
46  812801562                                    VERA GRØNNEBERG         False         False            False
47  812849832  SAMVIRKEFORETAKET NAKKEN, ØGLAND, BRÅTHEN OG K...         False         False            False
48  812859412                               HUSFLIDEN ÅLESUND AS          True          True             True
49  812862782                                     SHAHZAD QAISER         False         False            False







	org_num                                               navn  google_profil  eier_erklært  komplett_profil
0   870016972                   UNNS NEGLDESIGN UNN K SIGVARTSEN          False         False            False
1   870051662                       SEE TRANS STEIN ERIK ERIKSEN          False         False            False
2   870157592                  SKREIA TETT-TV Hans Petter Ulsrud          False         False            False
3   870179782                             SANDEID SAMFUNDSHUS SA          False         False            False
4   870193602                              NORGES URMAKERFORBUND          False         False            False
5   870229062                                         WEUM TROND          False         False            False
6   870238312              RYGGE BLIKKENSLAGERVERKSTED Pettersen          False         False            False
7   870244762                         VETERINÆR FREDDIE HELGESEN          False         False            False
8   870274572                                      OLE J MARKENG          False         False            False
9   870305362                       NORRA DALS BRUNNSBORRNING AB          False         False            False
10  870311702                                   ODDLEIV GRØNNING          False         False            False
11  870312792                              SKJELBRED TRULS HÅKON          False         False            False
12  870329652                           NORGES STYRKELØFTFORBUND          False         False            False
13  870338392                                    VESTERBUKT RUNE          False         False            False
14  870346492                                         TOR MELING          False         False            False
15  870378262      TRANSPORT OG SVEISESERVICE Torbjørn K Lægreid          False         False            False
16  870386192                               HELLE FOLKE SØLVSMED          False         False            False
17  870418582                                  MURER VIGGO BALLO          False         False            False
18  870418892                           REGNSKAP & KONTORSERVICE          False         False            False
19  870432232                  SMIETORGET MARKEDSFØRINGSFORENING          False         False            False
20  870445652                                        OALAND KÅRE          False         False            False
21  870464622                                         NYLEND DAG          False         False            False
22  870479972                            STEINAR HAGEN TRANSPORT          False         False            False
23  870538332                                       TROND LANDRØ          False         False            False
24  870547072                                     ODDBJØRG HOLME          False         False            False
25  870896972                                  OLE-JACOB SOLBERG          False         False            False
26  870914482                            THERMO-TRANSIT NORGE AS          False         False            False
27  870922752                            SARTOR BILOPPRETTING AS          False         False            False
28  870952252                                     VÅGAN SIGBJØRN          False         False            False
29  870963882      GLÅMDAL INTERKOMMUNALE RENOVASJONSSELSKAP IKS          False         False            False
30  870966962                                           NORE OLA          False         False            False
31  870984812                               WAAL DRAMMEN OLJE AS          False         False            False
32  870986572                           TO KOKKER SELSKAPSMAT AS          False         False            False
33  871034982                                    SANDNES HAVN KF          False         False            False
34  871035032                                           IVAR IKS          False         False            False
35  871055912                                        IL TAKST AS          False         False            False
36  871085552                          MÅLØY FARGE & INTERIØR AS          False         False            False
37  871143412             TOM GRAN KOBBER OG BLIKKENSLAGERMESTER          False         False            False
38  871143722                    ASKILSRUD PER ENGEBRETH ADVOKAT          False         False            False
39  871146802                                     NYQUIST FRISØR          False         False            False
40  871177392                               RALLY BILVERKSTED AS          False         False            False
41  871211132                                TREND SKO LARVIK AS          False         False            False
42  871231362                             ØKONOMIHUSET FAUSKE AS          False         False            False
43  871248532                              TORIL SØRBØ HALVORSEN          False         False            False
44  871295182                         TANNLEGE VIRGIL RUNDBERGET          False         False            False
45  871317062  OPPLÆRINGSKONTORET FOR INDUSTRIFAG OKI VESTFOL...          False         False            False
46  871321752             EL & IT FORBUNDET VESTFOLD OG TELEMARK          False         False            False
47  871324352                                   SILJAN NORMISJON          False         False            False
48  871361592                OPPLÆRINGSKONTORET FOR NORDHORDLAND          False         False            False
49  871365652                          SOGN & FJORDANE FISKARLAG          False         False            False



______________________________ TEST 3 _____________________________________________________________
'https://www.google.com/search?q=UNNS%20NEGLDESIGN%20UNN%20K%20SIGVARTSEN%20maps'
'https://www.google.com/search?q=SEE%20TRANS%20STEIN%20ERIK%20ERIKSEN%20maps'
'https://www.google.com/search?q=SKREIA%20TETT-TV%20Hans%20Petter%20Ulsrud%20maps'
'https://www.google.com/search?q=SANDEID%20SAMFUNDSHUS%20SA%20maps'
'https://www.google.com/search?q=NORGES%20URMAKERFORBUND%20maps'
'https://www.google.com/search?q=WEUM%20TROND%20maps'
'https://www.google.com/search?q=RYGGE%20BLIKKENSLAGERVERKSTED%20Pettersen%20maps'
'https://www.google.com/search?q=ODDLEIV%20GRØNNING%20maps'
'https://www.google.com/search?q=OLE%20J%20MARKENG%20maps'
'https://www.google.com/search?q=VETERINÆR%20FREDDIE%20HELGESEN%20maps'
'https://www.google.com/search?q=NORRA%20DALS%20BRUNNSBORRNING%20AB%20maps'

OLD OUTPUT:
	org_num                                               navn    google_profil    eier_erklært     komplett_profil		TRIGGER
0   870016972                   UNNS NEGLDESIGN UNN K SIGVARTSEN          False [-]        False [-]           False [x]   	noSuchElement: 'osrp-blk'
1   870051662                       SEE TRANS STEIN ERIK ERIKSEN          False [x]        False [x]           False [x]
2   870157592                  SKREIA TETT-TV Hans Petter Ulsrud          False [-]        False [x]           False [x]
3   870179782                             SANDEID SAMFUNDSHUS SA          False [-]        False [-]           False [-]
4   870193602                              NORGES URMAKERFORBUND          False [-]        False [x]           False [x]
5   870229062                                         WEUM TROND          False [-]        False [-]           False [x]
6   870238312              RYGGE BLIKKENSLAGERVERKSTED Pettersen          False [-]        False [-]           False [x]
7   870244762                         VETERINÆR FREDDIE HELGESEN          False [x]        False [x]           False [x]
8   870274572                                      OLE J MARKENG          False [x]        False [x]           False [x]
9   870305362                       NORRA DALS BRUNNSBORRNING AB          False [-]        False [-]           False [x]
10  870311702                                   ODDLEIV GRØNNING          False [x]        False [x]           False [x]

NEW OUTPUT:
	org_num                                               navn  google_profil  eier_erklært  komplett_profil
	# 0   870016972                   UNNS NEGLDESIGN UNN K SIGVARTSEN          False         False            False
	# 1   870051662                       SEE TRANS STEIN ERIK ERIKSEN          False         False            False
	# 2   870157592                  SKREIA TETT-TV Hans Petter Ulsrud          False         False            False
	# 3   870179782                             SANDEID SAMFUNDSHUS SA          False         False            False
	# 4   870193602                              NORGES URMAKERFORBUND          False         False            False
	# 5   870229062                                         WEUM TROND          False         False            False
	# 6   870238312              RYGGE BLIKKENSLAGERVERKSTED Pettersen          False         False            False
	# 7   870244762                         VETERINÆR FREDDIE HELGESEN          False         False            False
	# 8   870274572                                      OLE J MARKENG          False         False            False
	# 9   870305362                       NORRA DALS BRUNNSBORRNING AB          False         False            False
	# 10  870311702                                   ODDLEIV GRØNNING          False         False            False

FASIT:
	org_num                             					navn google_profil  eier_erklært  komplett_profil
0   870016972                   UNNS NEGLDESIGN UNN K SIGVARTSEN          True          True             False
1   870051662                       SEE TRANS STEIN ERIK ERIKSEN          False         False            False
2   870157592                  SKREIA TETT-TV Hans Petter Ulsrud          True          False            False
3   870179782                             SANDEID SAMFUNDSHUS SA          True          True             True
4   870193602                              NORGES URMAKERFORBUND          True          False            False
5   870229062                                         WEUM TROND          True          True             False
6   870238312              RYGGE BLIKKENSLAGERVERKSTED Pettersen          True          True             False
7   870244762                         VETERINÆR FREDDIE HELGESEN          False         False            False
8   870274572                                      OLE J MARKENG          False         False            False
9   870305362                       NORRA DALS BRUNNSBORRNING AB          True          True             False
10  870311702                                   ODDLEIV GRØNNING          False         False            False




test_array = [ [870016972,'UNNS NEGLDESIGN UNN K SIGVARTSEN',],
		   [870051662,'SEE TRANS STEIN ERIK ERIKSEN',],
		   [870157592,'SKREIA TETT-TV Hans Petter Ulsrud',],
		   [870179782,'SANDEID SAMFUNDSHUS SA',],
		   [870193602,'NORGES URMAKERFORBUND',],
		   [870229062,'WEUM TROND',],
		   [870238312,'RYGGE BLIKKENSLAGERVERKSTED Pettersen',],
		   [870244762,'VETERINÆR FREDDIE HELGESEN',],
		   [870274572,'OLE J MARKENG',],
		   [870305362,'NORRA DALS BRUNNSBORRNING AB',],
		   [870311702,'ODDLEIV GRØNNING',],  ]


