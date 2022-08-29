from sqlalchemy import create_engine
import pandas as pd 

payload = { 'dbname'   : 'media_vest',
			'host'     : 'localhost',
			'user'     : 'postgres',
			'password' : 'Orikkel1991',
			'tablename': 'brreg_table',  }

dbname = payload['dbname']
host = payload['host']
user = payload['user']
password = payload['password']
tablename = payload['tablename'] 


my_list = [*range(27)]

df = pd.DataFrame([my_list], columns = ['organisasjonsnummer',
'navn',
'registreringsdatoEnhetsregisteret',
'registrertIMvaregisteret',
'antallAnsatte',
'registrertIForetaksregisteret',
'registrertIStiftelsesregisteret',
'registrertIFrivillighetsregisteret',
'konkurs',
'underAvvikling',
'underTvangsavviklingEllerTvangsopplosning',
'organisasjonsform.kode',
'organisasjonsform.beskrivelse',
'naeringskode1.beskrivelse',
'naeringskode1.kode',
'forretningsadresse.land',
'forretningsadresse.landkode',
'forretningsadresse.postnummer',
'forretningsadresse.poststed',
'forretningsadresse.adresse',
'forretningsadresse.kommune',
'forretningsadresse.kommunenummer',
'institusjonellSektorkode.kode',
'institusjonellSektorkode.beskrivelse',
'hjemmeside',
'stiftelsesdato',
'sisteInnsendteAarsregnskap'])


engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}')
df.to_sql(f'{tablename}', engine, index = False)



# [
# 'organisasjonsnummer',
# 'navn',
# 'registreringsdatoEnhetsregisteret',
# 'registrertIMvaregisteret',
# 'antallAnsatte',
# 'registrertIForetaksregisteret',
# 'registrertIStiftelsesregisteret',
# 'registrertIFrivillighetsregisteret',
# 'konkurs',
# 'underAvvikling',
# 'underTvangsavviklingEllerTvangsopplosning',
# # 'maalform',
# 'organisasjonsform.kode',
# 'organisasjonsform.beskrivelse',
# 'organisasjonsform._links.self.href',
# 'naeringskode1.beskrivelse',
# 'naeringskode1.kode',
# 'forretningsadresse.land',
# 'forretningsadresse.landkode',
# 'forretningsadresse.postnummer',
# 'forretningsadresse.poststed',
# 'forretningsadresse.adresse',
# 'forretningsadresse.kommune',
# 'forretningsadresse.kommunenummer',
# 'institusjonellSektorkode.kode',
# 'institusjonellSektorkode.beskrivelse',
# '_links.self.href',
# 'hjemmeside',
# 'stiftelsesdato',
# 'postadresse.land',
# 'postadresse.landkode',
# 'postadresse.postnummer',
# 'postadresse.poststed',
# 'postadresse.adresse',
# 'postadresse.kommune',
# 'postadresse.kommunenummer',
# 'sisteInnsendteAarsregnskap',
# 'naeringskode2.beskrivelse',
# 'naeringskode2.kode',
# 'naeringskode2.hjelpeenhetskode'
# ]



# 'organisasjonsnummer',
# 'navn',
# 'registreringsdatoEnhetsregisteret',
# 'registrertIMvaregisteret',
# 'antallAnsatte',
# 'registrertIForetaksregisteret',
# 'registrertIStiftelsesregisteret',
# 'registrertIFrivillighetsregisteret',
# 'konkurs',
# 'underAvvikling',
# 'underTvangsavviklingEllerTvangsopplosning',
# 'organisasjonsform.kode',
# 'organisasjonsform.beskrivelse',
# 'naeringskode1.beskrivelse',
# 'naeringskode1.kode',
# 'forretningsadresse.land',
# 'forretningsadresse.landkode',
# 'forretningsadresse.postnummer',
# 'forretningsadresse.poststed',
# 'forretningsadresse.adresse',
# 'forretningsadresse.kommune',
# 'forretningsadresse.kommunenummer',
# 'institusjonellSektorkode.kode',
# 'institusjonellSektorkode.beskrivelse',
# 'hjemmeside',
# 'stiftelsesdato',
# 'sisteInnsendteAarsregnskap'

# organisasjonsnummer VARCHAR PRIMARY KEY,
# navn VARCHAR,
# registreringsdatoEnhetsregisteret VARCHAR,
# registrertIMvaregisteret VARCHAR,
# antallAnsatte VARCHAR,
# registrertIForetaksregisteret VARCHAR,
# registrertIStiftelsesregisteret VARCHAR,
# registrertIFrivillighetsregisteret VARCHAR,
# konkurs VARCHAR,
# underAvvikling VARCHAR,
# underTvangsavviklingEllerTvangsopplosning VARCHAR,
# organisasjonsform.kode VARCHAR,
# organisasjonsform.beskrivelse VARCHAR,
# naeringskode1.beskrivelse VARCHAR,
# naeringskode1.kode VARCHAR,
# forretningsadresse.land VARCHAR,
# forretningsadresse.landkode VARCHAR,
# forretningsadresse.postnummer VARCHAR,
# forretningsadresse.poststed VARCHAR,
# forretningsadresse.adresse VARCHAR,
# forretningsadresse.kommune VARCHAR,
# forretningsadresse.kommunenummer VARCHAR,
# institusjonellSektorkode.kode VARCHAR,
# institusjonellSektorkode.beskrivelse VARCHAR,
# hjemmeside VARCHAR,
# stiftelsesdato VARCHAR,
# sisteInnsendteAarsregnskap VARCHAR,