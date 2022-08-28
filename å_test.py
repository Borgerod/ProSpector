import time; start = time.perf_counter() #Since it also takes time to Import libs, I allways start the timer asap. 
import pandas as pd 
import requests 
from bs4 import BeautifulSoup
import numpy as np
import json
import gzip
import ast
import psycopg2
from psycopg2.extras import Json
from sqlalchemy import create_engine
import concurrent.futures
from tqdm import tqdm
import datetime as dt

# ___ local imports __________
from config import payload, tablenames, settings
from postgres import databaseManager, cleanUp, fetchData, checkForTable, postLastUpdate, deleteData, replacetData
from file_manager import *

# verify= '''Se bilder
# Se utsiden
# Finn Brynildsrud & Sønner AS
# Nettsted
# Veibeskrivelse
# Lagre
# 5,0
# 1 Google-anmeldelse
# Verktøyprodusent i Moss
# Adresse: Kallumveien 28, 1524 Moss
# Åpningstider:
# Stengt ⋅ Åpner kl. 08 man.
# Telefonnummer: 69 25 36 17
# Foreslå en endring
# · Eier du denne bedriften?
# Spørsmål og svar
# Still et spørsmål
# Vær først ute med å stille et spørsmål
# Vurderinger fra nettet
# 3/5Facebook · 1 stemme
# Anmeldelser
# Skriv en anmeldelse
# Legg til et bilde
# 1 Google-anmeldelse
# Anmeldelsene er ikke bekreftet
# Fra Finn Brynildsrud & Sønner AS
# "Finmekanisk verksted i Moss.Mekanisk bearbeiding av metall og plast.Formverktøy for plastproduksjon.Fresing, Dreiing, Rundsliping, Plansliping, Honing, Gnisterosjon.Reparasjon av gamle bildeler, fjerning av fastrustede eller brukne bolter."
# '''

# search_term = 'FINN BRYNILDSRUD & SØNNER AS'

# import re
# # for ch in [' AS',' ASA', ' AB']
# # search_term.replace(' AS')


# for ch in [' AS',' ASA', ' AB']:
#     if ch in search_term:
#         search_term = search_term.replace(ch,"")
# # rx = re.compile('([ASASA AB])')
# # text = rx.sub('', search_term)
# # print(search_term)

# # if re.search(search_term, verify, re.IGNORECASE):
# # 	print("YES")

# # import re
# # # re = re.escape(r'\ a.*$')
# # print(re.escape(r'\ a.*$'))
# # # re = re.escape('www.stackoverflow.com')
# # print(re.escape('www.stackoverflow.com'))
# reg = 'www.stackoverflow.  com'
# # pat = re.compile(r'reg')
# # reg = re.escape(reg)
# # pat = re.compile(reg)

# print(re.sub('[^A-Za-z0-9]', '', reg))
# alt_search_term = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in search_term.split("\n")][0]
# print(cleanString)
# # sea
# print()



def checkGoogleAlarmTrigger():
    html = '''
         html dir="LTR"><head><meta http-equiv="content-type" content="text/html; charset=utf-8"><meta name="viewport" content="initial-scale=1"><title>https://www.google.com/search?q=UNNS%20NEGLDESIGN%20UNN%20K%20SIGVARTSEN%20maps</title></head>
        <body style="font-family: arial, sans-serif; background-color: #fff; color: #000; padding:20px; font-size:18px;" onload="e=document.getElementById('captcha');if(e){e.focus();} if(solveSimpleChallenge) {solveSimpleChallenge(,);}">
        <div style="max-width:400px;">
        <hr noshade="" size="1" style="color:#ccc; background-color:#ccc;"><br>
        <form id="captcha-form" action="index" method="post">
        <noscript>
        <div style="font-size:13px;">
        For å fortsette, slå på JavaScript i nettleseren.
        </div>
        </noscript>
        <script type="text/javascript" async="" src="https://www.gstatic.com/recaptcha/releases/3TZgZIog-UsaFDv31vC4L9R_/recaptcha__no.js" crossorigin="anonymous" integrity="sha384-vI9Fjl9JEacT4Tak+zC0gGZuKofOUf+FRnq6j1GJKqyvhyGyu8/GtFkXgI28In+W"></script><script src="https://www.google.com/recaptcha/api.js" async="" defer=""></script>
        <script>var submitCallback = function(response) {document.getElementById('captcha-form').submit();};</script>
        <div id="recaptcha" class="g-recaptcha" data-sitekey="6LfwuyUTAAAAAOAmoS0fdqijC2PbbdH4kjq62Y1b" data-callback="submitCallback" data-s="LbCG7RWUtWOoTtqaPUZwvHdb79Is92JbdY5nl57MslVUSqEIO5B8NmPhya0t67p0SJMwAj7rPJ5VCgQGBPzOAcMMP8P_l3qQsfO0YvxrXXQD80t1Mc_VaqOChYHT1jJL4Jw9zysyfWou3QW6kSyTtaQmx9MpcE-Ap3C1m9NUloeCCzzw7PKuu_Yf8I95vcMd1Bc88r6I3JUZuNeY5GTh7Qdd0Kn64BqnSw_e2Bc"><div style="width: 304px; height: 78px;"><div><iframe title="reCAPTCHA" src="https://www.google.com/recaptcha/api2/anchor?ar=1&amp;k=6LfwuyUTAAAAAOAmoS0fdqijC2PbbdH4kjq62Y1b&amp;co=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbTo0NDM.&amp;hl=no&amp;v=3TZgZIog-UsaFDv31vC4L9R_&amp;size=normal&amp;s=LbCG7RWUtWOoTtqaPUZwvHdb79Is92JbdY5nl57MslVUSqEIO5B8NmPhya0t67p0SJMwAj7rPJ5VCgQGBPzOAcMMP8P_l3qQsfO0YvxrXXQD80t1Mc_VaqOChYHT1jJL4Jw9zysyfWou3QW6kSyTtaQmx9MpcE-Ap3C1m9NUloeCCzzw7PKuu_Yf8I95vcMd1Bc88r6I3JUZuNeY5GTh7Qdd0Kn64BqnSw_e2Bc&amp;cb=zd121mdilitc" width="304" height="78" role="presentation" name="a-yavsy3t54432" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox"></iframe></div><textarea id="g-recaptcha-response" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;"></iframe></div>

        <input type="hidden" name="q" value="EgRYWNaPGNObqJgGIhA9mqnfzszBOtbCGw3K63ewMgFy"><input type="hidden" name="continue" value="https://www.google.com/search?q=UNNS%20NEGLDESIGN%20UNN%20K%20SIGVARTSEN%20maps">
        </form>
        <hr noshade="" size="1" style="color:#ccc; background-color:#ccc;">
        <div style="font-size:13px;">
        <b>Om denne siden</b><br><br>

        Systemene våre har oppdaget uvanlig trafikk fra ditt datanettverk. Denne siden kontrollerer om det faktisk er du som sender forespørslene, og ikke en maskin. <a href="#" onclick="document.getElementById('infoDiv').style.display='block';">Why did this happen?</a><br><br>

        <div id="infoDiv" style="display:none; background-color:#eee; padding:10px; margin:0 0 15px 0; line-height:1.4em;">
        Denne siden vises når Google automatisk fanger opp forespørsler fra ditt datanettverk som ser ut til å bryte med våre <a href="//www.google.com/policies/terms/">vilkår for bruk</a>. Denne blokken utløper kort tid etter at disse forespørslene stopper. I mellomtiden vil du kunne fortsette å bruke våre tjenester ved å skrive inn kontrollordet over.<br><br>Det kan hende at trafikken har blitt sendt av skadelig programvare, et programtillegg for nettleseren eller et skript som sender automatiserte forespørsler. Hvis du deler nettverkstilkobling, kan du be din administrator om hjelp – det kan hende at en annen datamaskin som benytter samme IP-adresse står bak. <a href="//support.google.com/websearch/answer/86640">Les mer</a><br><br>Dersom du bruker avanserte termer som ofte benyttes av maskiner, eller sender forespørsler veldig raskt, kan det hende at du noen ganger blir bedt om å skrive inn et kontrollord.

        </div><br>
        IP adresse: 88.88.214.143<br>Tidspunkt: 2022-08-27T12:28:04Z<br>Nettadresse: https://www.google.com/search?q=UNNS%20NEGLDESIGN%20UNN%20K%20SIGVARTSEN%20maps<br>
        </div></div>


        <div style="background-color: rgb(255, 255, 255); border: 1px solid rgb(204, 204, 204); box-shadow: rgba(0, 0, 0, 0.2) 2px 2px 3px; position: absolute; transition: visibility 0s linear 0.3s, opacity 0.3s linear 0s; opacity: 0; visibility: hidden; z-index: 2000000000; left: 0px; top: -10000px;"><div style="width: 100%; height: 100%; position: fixed; top: 0px; left: 0px; z-index: 2000000000; background-color: rgb(255, 255, 255); opacity: 0.05;"></div><div class="g-recaptcha-bubble-arrow" style="border: 11px solid transparent; width: 0px; height: 0px; position: absolute; pointer-events: none; margin-top: -11px; z-index: 2000000000;"></div><div class="g-recaptcha-bubble-arrow" style="border: 10px solid transparent; width: 0px; height: 0px; position: absolute; pointer-events: none; margin-top: -10px; z-index: 2000000000;"></div><div style="z-index: 2000000000; position: relative;"><iframe title="reCAPTCHA-utfordringen utløper om to minutter" src="https://www.google.com/recaptcha/api2/bframe?hl=no&amp;v=3TZgZIog-UsaFDv31vC4L9R_&amp;k=6LfwuyUTAAAAAOAmoS0fdqijC2PbbdH4kjq62Y1b" name="c-yavsy3t54432" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox" style="width: 100%; height: 100%;"></iframe></div></div></body></html>   
    '''
    return ('Systemene våre har oppdaget uvanlig trafikk' or 'unnusual traffic') in html


if checkGoogleAlarmTrigger(driver):
    print(True)
else:
    print(False)

# rch_term='FINN BRYNILDSRUD & SØNNER AS'
# if search_term.lower() in verify.lower():
# 	print("YES")


# if not (x or y):
# 	print("x and y is both false")

'''
1069577
'''
# print(m)