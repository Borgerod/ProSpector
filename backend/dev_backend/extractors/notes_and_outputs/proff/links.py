f"https://route.enirocdn.com/route/route.json?pref={n}&lang={i}&instr=true&res=611&api=trueo&waypoints={t[1]},{t[0]};{e[1]},{e[0]}"


f"https://mapsearch.eniro.com/search/geo/suggest?country={i}&q={t}"

i = location
t = searchterm




f"https://www.proff.no/laglister/{nextUrl.href}/?view=json"

'https://www.proff.no/laglister?ef=1&et=28037&i=p296&i=p16684&phone=false&email=false&address=false&view=json'
'https://proff.no/laglister?pf=-8346702&pt=956235841&view=json'

'https://www.proff.no/laglister/YLoFmCo_zvNZxJID58xbvPRqRxqIbXMs7BCyqkVCzBjO4NYWIKrSWsh83eNLR2sE1NVoBLJf99asLxyKGXnTlC1tmKlJ-Hv01wCGwqiyDTCJxtXEpHrAG6zbML3mGiPpeKV0446tt8_uHmx5RNwKHb0V5Ac9c5yZWF_kVuNDECXKywIgBOMRokCVs3PmUtKDXnlX_1z7FO08lf41lVh8bQ/?view=json'


https://www.proff.no/bransjesøk?q=925476633
'''
    parameters:
    ef = ansatte (min)
    et = ansatte (max)
    i = bedrift (pCode) 
    phone = false
    email = false
    address = false
    view = json
    rf = driftsinntekt (min)
    rt = driftsinntekt (max)
    pf = driftsresultat (min)
    pt = driftsresultat (min)
    c = selskapsform 
    l = lokalisering
'''


class proff:
    def __init__(self) -> None:
        self.ef = ef 
        self.et = et 
        self.i = i 
        self.phone = phone
        self.email = email
        self.address = address
        self.view = view
        self.rf = rf 
        self.rt = rt 
        self.pf = pf 
        self.pt = pt 
        self.c = c
        self.l = l  
    
    def __init__(self) -> None:
        self.pf = 0
        self.pt = pt 
        self.rf = −8346702
        self.rt = 956235841
        self.ef = 1
        self.et = 31068 
        self.c = c
        self.l = l
        self.i = i 
        self.phone = phone
        self.email = email
        self.address = address
        self.view = "json"