'''
____ BRREG DATAFRAME OUTPUT ________________________________________________________

	Untouched dataframe output from brreg, columns will be removed & names changed

'''
organisasjonsnummer                                                        922924368
navn                                         - A THOUSAND WORDS - ØDEGÅRDEN GJERR...
registreringsdatoEnhetsregisteret                                         2019-06-19
registrertIMvaregisteret                                                        True
antallAnsatte                                                                      0
registrertIForetaksregisteret                                                  False
registrertIStiftelsesregisteret                                                False
registrertIFrivillighetsregisteret                                             False
konkurs                                                                        False
underAvvikling                                                                 False
underTvangsavviklingEllerTvangsopplosning                                      False
maalform                                                                      Bokmål
links                                                                             []
organisasjonsform.kode                                                           ENK
organisasjonsform.beskrivelse                                    Enkeltpersonforetak
organisasjonsform.links                                                           []
naeringskode1.beskrivelse                          Oversettelses- og tolkevirksomhet
naeringskode1.kode                                                            74.300
forretningsadresse.land                                                        Norge
forretningsadresse.landkode                                                       NO
forretningsadresse.postnummer                                                   3060
forretningsadresse.poststed                                                  SVELVIK
forretningsadresse.adresse                                           [Storgaten 120]
forretningsadresse.kommune                                                   DRAMMEN
forretningsadresse.kommunenummer                                                3005
institusjonellSektorkode.kode                                                   8200
institusjonellSektorkode.beskrivelse                       Personlig næringsdrivende
hjemmeside                                                                       NaN
stiftelsesdato                                                                   NaN
sisteInnsendteAarsregnskap                                                       NaN
postadresse.land                                                                 NaN
postadresse.landkode                                                             NaN
postadresse.postnummer                                                           NaN
postadresse.poststed                                                             NaN
postadresse.adresse                                                              NaN
postadresse.kommune                                                              NaN
postadresse.kommunenummer                                                        NaN
naeringskode2.beskrivelse                                                        NaN
naeringskode2.kode                                                               NaN
naeringskode2.hjelpeenhetskode                                                   NaN
frivilligMvaRegistrertBeskrivelser                                               NaN
overordnetEnhet                                                                  NaN
naeringskode1.hjelpeenhetskode                                                   NaN
naeringskode3.beskrivelse                                                        NaN
naeringskode3.kode                                                               NaN
naeringskode3.hjelpeenhetskode                                                   NaN
Name: 0, dtype: object



'''
____ BRREG DATAFRAME OUTPUT --> MARKED _____________________________________________
 
	everything marked with "#" are columns that will NOT be included in the database

'''
organisasjonsnummer                                                        922924368
navn                                         - A THOUSAND WORDS - ØDEGÅRDEN GJERR...
registreringsdatoEnhetsregisteret                                         2019-06-19
registrertIMvaregisteret                                                        True
antallAnsatte                                                                      0
registrertIForetaksregisteret                                                  False
registrertIStiftelsesregisteret                                                False
registrertIFrivillighetsregisteret                                             False
konkurs                                                                        False
underAvvikling                                                                 False
under_tvangsavvikling_eller_oppløsning                                      False
# maalform                                                                      Bokmål
# links                                                                             []
organisasjonsform.kode                                                           ENK
organisasjonsform.beskrivelse                                    Enkeltpersonforetak
# organisasjonsform.links                                                           []
naeringskode1.beskrivelse                          Oversettelses- og tolkevirksomhet
naeringskode1.kode                                                            74.300
forretningsadresse.land                                                        Norge
forretningsadresse.landkode                                                       NO
forretningsadresse.postnummer                                                   3060
forretningsadresse.poststed                                                  SVELVIK
forretningsadresse.adresse                                           [Storgaten 120]
forretningsadresse.kommune                                                   DRAMMEN
forretningsadresse.kommunenummer                                                3005
institusjonellSektorkode.kode                                                   8200
institusjonellSektorkode.beskrivelse                       Personlig næringsdrivende
hjemmeside                                                                       NaN
stiftelsesdato                                                                   NaN
sisteInnsendteAarsregnskap                                                       NaN
# postadresse.land                                                                 NaN
# postadresse.landkode                                                             NaN
# postadresse.postnummer                                                           NaN
# postadresse.poststed                                                             NaN
# postadresse.adresse                                                              NaN
# postadresse.kommune                                                              NaN
# postadresse.kommunenummer                                                        NaN
# naeringskode2.beskrivelse                                                        NaN
# naeringskode2.kode                                                               NaN
# naeringskode2.hjelpeenhetskode                                                   NaN
# frivilligMvaRegistrertBeskrivelser                                               NaN
overordnetEnhet                                                                  NaN
# naeringskode1.hjelpeenhetskode                                                   NaN
# naeringskode3.beskrivelse                                                        NaN
# naeringskode3.kode                                                               NaN
# naeringskode3.hjelpeenhetskode                                                   NaN




'''
____ BRREG DATAFRAME --> NEW COLUMN NAMES __________________________________________
 
	Column from output with unnececary columns dropped and names changed. 

'''
'org_num',
'navn',
'registreringsdato',
'mva_registrert',
'antall_ansatte',
'foretaks_registeret',
'stiftelses_registeret',
'frivillighets_registeret',
'konkurs',
'under_avvikling',
'under_tvangsavvikling_eller_oppløsning',
'organisasjonsform_kode',
'organisasjonsform_beskrivelse',
'naeringskode1_beskrivelse',
'naeringskode1_kode',
'land',
'landkode',
'postnummer',
'poststed',
'adresse',
'kommune',
'kommunenummer',
'sektorkode_kode',
'sektorkode_beskrivelse',
'hjemmeside',
'stiftelsesdato',
'siste_innsendt_årsregnskap',
'overordnet_enhet',

org_num
navn
registreringsdato
mva_registrert
antall_ansatte
foretaks_registeret
stiftelses_registeret
frivillighets_registeret
konkurs
under_avvikling
under_tvangsavvikling_eller_oppløsning
organisasjonsform_kode
organisasjonsform_beskrivelse
naeringskode1_beskrivelse
naeringskode1_kode
land
landkode
postnummer
poststed
adresse
kommune
kommunenummer
sektorkode_kode
sektorkode_beskrivelse
hjemmeside
stiftelsesdato
siste_innsendt_årsregnskap
overordnet_enhet



