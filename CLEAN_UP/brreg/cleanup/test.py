import pandas as pd 
import pprint
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', 40)		# Columns  (column display border)
# pd.set_option('display.width', 2000)
# data_snippet = {'organisasjonsnummer': '922924368', 'navn': '- A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLATIONS', 'organisasjonsform': {'kode': 'ENK', 'beskrivelse': 'Enkeltpersonforetak', 'links': []}, 'registreringsdatoEnhetsregisteret': '2019-06-19', 'registrertIMvaregisteret': True, 'naeringskode1': {'beskrivelse': 'Oversettelses- og tolkevirksomhet', 'kode': '74.300'}, 'antallAnsatte': 0, 'forretningsadresse': {'land': 'Norge', 'landkode': 'NO', 'postnummer': '3060', 'poststed': 'SVELVIK', 'adresse': ['Storgaten 120'], 'kommune': 'DRAMMEN', 'kommunenummer': '3005'}, 'institusjonellSektorkode': {'kode': '8200', 'beskrivelse': 'Personlig næringsdrivende'}, 'registrertIForetaksregisteret': False, 'registrertIStiftelsesregisteret': False, 'registrertIFrivillighetsregisteret': False, 'konkurs': False, 'underAvvikling': False, 'underTvangsavviklingEllerTvangsopplosning': False, 'maalform': 'Bokmål', 'links': []}
data_snippet = {	'Organisasjonsnummer': '922924368',
					'Navn': '- A THOUSAND WORDS - ØDEGÅRDEN GJERRUD TRANSLATIONS',
					'Organisasjonsform.kode': 'ENK',
					'Organisasjonsform.beskrivelse': 'Enkeltpersonforetak',
					'Naeringskode 1.kode': '74.300',
					'Naeringskode 1.beskrivelse': 'Oversettelses- og tolkevirksomhet',
					'Naeringskode 1.hjelpeenhetskode':'',
					'Naeringskode 2.kode': '',
					'Naeringskode 2.hjelpeenhetskode':'',
					'Naeringskode 2.beskrivelse': '',
					'Naeringskode 3.kode': '',
					'Naeringskode 3.beskrivelse': '',
					'Naeringskode 3.hjelpeenhetskode':'',
					'Hjelpeenhetskode': '',
					'Hjelpeenhetskode.beskrivelse': '',
					'Antall ansatte': '0',
					'Hjemmeside': '',
					'Postadresse.adresse': '',
					'Postadresse.poststed': '',
					'Postadresse.postnummer': '',
					'Postadresse.kommune': '',
					'Postadresse.kommunenummer': '',
					'Postadresse.land': '',
					'Postadresse.landkode': '',
					'Forretningsadresse.adresse': 'Storgaten 120',
					'Forretningsadresse.poststed': 'SVELVIK',
					'Forretningsadresse.postnummer': '3060',
					'Forretningsadresse.kommune': 'DRAMMEN',
					'Forretningsadresse.kommunenummer': '3005',
					'Forretningsadresse.land': 'Norge',
					'Forretningsadresse.landkode': 'NO',
					'Institusjonell sektorkode': '8200',
					'Institusjonell sektorkode.beskrivelse': 'Personlig næringsdrivende',
					'Siste innsendte årsregnskap': '',
					'Registreringsdato i Enhetsregisteret': '2019-06-19',
					'Stiftelsesdato': '',
					'FrivilligRegistrertIMvaregisteret': '',
					'Registrert i MVA-registeret': 'JA',
					'Registrert i Frivillighetsregisteret': 'NEI',
					'Registrert i Foretaksregisteret': 'NEI',
					'Registrert i Stiftelsesregisteret': 'NEI',
					'Konkurs': 'NEI',
					'Under avvikling': 'NEI',
					'Under tvangsavvikling eller tvangsoppløsning': 'NEI',
					'Overordnet enhet i offentlig sektor': '',
					'Maalform': 'Bokmål',}
# print(len(data_snippet.keys()))
df = pd.json_normalize(data_snippet)
print(df.T)
print(len(df.T))

# # df = pd.DataFrame.from_dict(data_snippet, orient = 'index')

# # pprint.pprint(df.to_dict(orient='records')[0])
# # print(len(df.to_dict(orient='records')[0]))
# # new_dict = df.to_dict(orient='records')[0]


# # df = pd.DataFrame.from_dict(new_dict, orient = 'index')
# # print(df)
# # print(len(df))
# print(df)
# df.drop(['Maalform'], axis=1, inplace=True)
# print(df)


df  = df.drop([
	'Maalform', 
	'Postadresse.land', 
	'Postadresse.landkode',
	'Postadresse.postnummer',
	'Postadresse.poststed',
	'Postadresse.adresse',
	'Postadresse.kommune',
	'Postadresse.kommunenummer',
	'Naeringskode 2.beskrivelse',
	'Naeringskode 2.kode',
	'Naeringskode 2.hjelpeenhetskode',
	'FrivilligRegistrertIMvaregisteret',
	'Naeringskode 1.hjelpeenhetskode',
	'Naeringskode 3.beskrivelse',
	'Naeringskode 3.kode',
	'Naeringskode 3.hjelpeenhetskode', 
			# ], axis = 0, inplace = True)
			], axis = 1)
print(df.T)
print(len(df.T))




# df.drop([
# 	'Målform', 
# 	'Postadresse.land', 
# 	'Postadresse.landkode',
# 	'Postadresse.postnummer',
# 	'Postadresse.poststed',
# 	'Postadresse.adresse',
# 	'Postadresse.kommune',
# 	'Postadresse.kommunenummer',
# 	'Næringskode 2.beskrivelse',
# 	'Næringskode 2.kode',
# 	'Næringskode 2.hjelpeenhetskode',
# 	'FrivilligMvaRegistrertBeskrivelser',
# 	'Næringskode 1.hjelpeenhetskode',
# 	'Næringskode 3.beskrivelse',
# 	'Næringskode 3.kode',
# 	'Næringskode 3.hjelpeenhetskode', 
# 	'Organisasjonsform.links',      
# 			# ], axis = 0, inplace = True)
# 			], axis = 1)
# print(df.T)
# print(len(df.T))
