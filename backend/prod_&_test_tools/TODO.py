
''' * DAGENS TODO's  - DAG 1 [04.09.22]
	
	> Main Goals:
	- [ ] Integrer callList-display, updateCallList-api, & innloggings-api til appen.
	- [ ] Rett opp i APP utseende.
	- [ ] Integrere db, api-server, extractor, --> AWS 
	
	TODO's etter prioritering:  -> TODO [check] (hh:mm)
	
	0. ___ PREP ___
		TODO [X] (00:10) Gjør deg klar 													| start: (??:??) - finish: (??:??)
		TODO [X] (00:15) Lag "DAGENS TODO's" 											| start: (??:??) - finish: (11:12)
	  	TODO [X] (00:10) orienter deg selv												| start: (11:12) - finish: (11:20)
	  	TODO [X] (00:05) åpne opp alle programmer, etc. 								| start: (11:12) - finish: (11:20)
	  TOT.TIME = (00:25)
	  ACT.TIME = (xx:xx)

	1. ___ API  ___
		TODO [X] (00:30) Fix GetOverview												| start: (11:12) - finish: (??:??)
		TODO [X] (01:00) getCallList API må ta hensyn: kunden's hist + kollegaer Lister | start: (??:??) - finish: (??:??)				
		TODO [X] (01:00) oppdaget or reparerte feil i getCallList					 	| start: (??:??) - finish: (20:00)				
		# TODO [ ] (00:00) Lag API calls for [1] google-extractor, [2] full-update 		| start: (00:00) - finish: (00:00)
	  TOT.TIME = (02:15)
	  ACT.TIME = (xx:xx)


	2. ___ APP ___
		TODO [ ] (00:30) Integrer callList-display --> App. 							| start: (08:20) - finish: (00:00)
		TODO [ ] (00:45) Integrer updateCallList-api --> App.							| start: (00:00) - finish: (00:00)
		TODO [ ] (01:00) Integrer innloggings-api --> App.								| start: (00:00) - finish: (00:00)
		TODO [ ] (00:00) Rett opp i APP utseende.										| start: (00:00) - finish: (00:00)
		TODO [ ] (00:00) Skriv ferdig instruksjoner										| start: (00:00) - finish: (00:00)	
		# TODO [ ] (00:00) 																| start: (00:00) - finish: (00:00)	
	  TOT.TIME = (02:15)
	  ACT.TIME = (xx:xx)

	3. ___ AWS ___
		TODO [ ] (00:00) Finn ut hvordan å integrere pythonkoder til AWS 				| start: (00:00) - finish: (00:00)
		TODO [ ] (00:00) Integrere db --> AWS 											| start: (00:00) - finish: (00:00)
		# TODO [ ] (00:00) 																| start: (00:00) - finish: (00:00)	
	  TOT.TIME = (02:15)
	  ACT.TIME = (xx:xx)


	4. ___ EXTRACTOR ___
		TODO [ ] (00:00) Skrap ferdig google-table 										| start: (00:00) - finish: (00:00)
		# TODO [ ] (00:00) 																| start: (00:00) - finish: (00:00)	
	  TOT.TIME = (02:15)
	  ACT.TIME = (xx:xx)

  > OPPSUMMERING: 
	  TOTAL TID BRUKT:
	  	start (11:12) - finish (20:00) => ca 08:48:00 h 
	  
	  MENGDE ARBEID GJENNOMFØRT inkl. prep.: 
		originale arb.oppg: 6/13 => 46 % 
		m/ ekstra arb.oppg: 7/14 => 50 % 
	 
	  KOMMENTAR:
	  	- Repareringen av API'ene tok mye av arbeidskraften
	  	- Prøve å inplementere "relative overview table generator" relativt til bedriftskundene, så hver bedrift fikk sin egen overview table,
	  	  men det viste seg å være veldig vanskelig og problemet har blitt utsatt til post-release. 

'''

'''	* DAGENS TODO's  - DAG 2 [05.09.22]

	0. ___ PREP ___
		TODO [ ] (00:45) Gjør deg klar; 				 								| start: (08:20) - finish: (09:00)
						 update todos, åpne opp alle programmer, orienter deg selv, finn research, etc.
	2. ___ APP ___
		TODO [ ] (00:30) Integrer callList-display --> App. 							| start: (09:00) - finish: (00:00)	
		TODO [ ] (00:45) Integrer updateCallList-api --> App.							| start: (00:00) - finish: (00:00)
		TODO [ ] (01:00) Integrer innloggings-api --> App.								| start: (00:00) - finish: (00:00)
		TODO [ ] (00:00) Rett opp i APP utseende.										| start: (00:00) - finish: (00:00)
		TODO [ ] (00:00) Skriv ferdig instruksjoner										| start: (00:00) - finish: (00:00)	


  > OPPSUMMERING: 
	  TOTAL TID BRUKT:
	  	start (xx:xx) - finish (xx:xx) => ca xx:xx:xx h 
	  
	  MENGDE ARBEID GJENNOMFØRT inkl. prep.: 
		originale arb.oppg: x/xx => xx % 
		m/ ekstra arb.oppg: x/xx => xx % 
	 
	  KOMMENTAR:
	    - Har satt meg mer realistiske mål denne gangen 
	    -
'''




'''
	THE OVERALL TODO FILE 
	used instead of readme.md due to preference reasons 
'''
''' ! ISSUES:
		! [1] Issue with onbe of the extractors where one of them is raising an error. 
		! [2] Issue with Feedback function for the app; Email-API not working.  
		! [3] ISSUE request.connection error in gulesider.py
			  requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
			  might have something to do with internet connnection
		! [4] ISSUE Input_table getds bigger
		! [5] There is a posibility that output_table is getting smaller, 
			todo [ ] WIll look into it
			print output_table [24.08 - 16:54]: 1374 rows
			print output_table [24.08 - 16:55]: 1432 rows 
			print output_table [24.08 - 17:13]: 2369 rows 
			print output_table [25.08 - 10:17]: 2457 rows

			print gulesider_output_table [25.08 - 10:17]: 383 rows

			print I88I_output_table [25.08 - 10:17]: 4537 rows
		! [6] raised error in I88I.py:
			sqlalchemy.exc.IntegrityError: (psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "pg_type_typname_nsp_index"
				DETAIL:  Key (typname, typnamespace)=(output_table, 2200) already exists.

				[SQL:
				CREATE TABLE output_table (
				        org_num BIGINT,
				        navn TEXT
				)

				]
				(Background on this error at: https://sqlalche.me/e/14/gkpj)
		! [ ] Raised error in gulesider.py: requests.exceptions.ReadTimeout: None: None
		! [ ] Ser ut som I88I.py ikke filtrerer ut bedrifter uten markedsføring riktig. 
		  Ser ut som den glemmer å parse over til den 
		  nye siden hvis siden er en liste
'''

'''
	* ESTRACTORS CURRENT PROGRESS & STATUS LOG:
		 _________________________
		| Status Check [25.08.22] |	
		|-------------------------|
		|		brreg:	OK		  |
		|	gulesider:	error 	  |
		|	   	 I88I:	error 	  |
		|		proff:	OK		  |
		|	   google:	-		  |
		|_________________________|

	* Find_rate:
		proff: 		0.00254 => 0.26%									| Estimated total finds: 2794
		gulesider: 	0.00559 => 0.56% 									| Estimated total finds: 6149
		I88I: 		0.0438  => 4.38% [HAS X AMOUNT OF WRONG OUTPUTS]	| Estimated total finds: 48180 (more likely; 4471 (0.41%))

	* PROGRESS SO FAR:
		brreg:	    | 100% |
		proff:	    | 100% |
		gulesider:  |   7% | 137/1951 [1:41:41<22:26:34, 44.54s/it] ---> Input_array position: 137 * 500 =   68.500
		I88I:	    |  11% | 207/1951 [3:04:45<25:56:38, 53.55s/it] ---> Input_array position: 207 * 500 =  103.500
		google:     |   0% |

	* RAISESD ERRORS:
		gulesider:
			! [ ] requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
				
				? PROBABLE CAUSES: 
					- [ ] 
					- [ ] 		

				todo POSSIBLE SOLUTIONS:
					- [ ] 
					- [ ] 

				TEMP - WHOLE ERROR:
				  	multiprocessing.pool.RemoteTraceback:
				  	"""
					  	Traceback (most recent call last):
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/urllib3/connectionpool.py", line 703, in urlopen
						    httplib_response = self._make_request(
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/urllib3/connectionpool.py", line 449, in _make_request
						    six.raise_from(e, None)
						  File "<string>", line 3, in raise_from
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/urllib3/connectionpool.py", line 444, in _make_request
						    httplib_response = conn.getresponse()
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/http/client.py", line 1374, in getresponse
						    response.begin()
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/http/client.py", line 318, in begin
						    version, status, reason = self._read_status()
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/http/client.py", line 287, in _read_status
						    raise RemoteDisconnected("Remote end closed connection without"
						http.client.RemoteDisconnected: Remote end closed connection without response

						During handling of the above exception, another exception occurred:

						Traceback (most recent call last):
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/requests/adapters.py", line 440, in send
						    resp = conn.urlopen(
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/urllib3/connectionpool.py", line 785, in urlopen
						    retries = retries.increment(
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/urllib3/util/retry.py", line 550, in increment
						    raise six.reraise(type(error), error, _stacktrace)
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/urllib3/packages/six.py", line 769, in reraise
						    raise value.with_traceback(tb)
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/urllib3/connectionpool.py", line 703, in urlopen
						    httplib_response = self._make_request(
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/urllib3/connectionpool.py", line 449, in _make_request
						    six.raise_from(e, None)
						  File "<string>", line 3, in raise_from
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/urllib3/connectionpool.py", line 444, in _make_request
						    httplib_response = conn.getresponse()
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/http/client.py", line 1374, in getresponse
						    response.begin()
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/http/client.py", line 318, in begin
						    version, status, reason = self._read_status()
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/http/client.py", line 287, in _read_status
						    raise RemoteDisconnected("Remote end closed connection without"
						urllib3.exceptions.ProtocolError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

						During handling of the above exception, another exception occurred:

						Traceback (most recent call last):
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/multiprocessing/pool.py", line 125, in worker
						    result = (True, func(*args, **kwds))
						  File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/gulesider.py", line 289, in extractionManager
						    soup = pullRequest(new_link, source, org_num, search_term)
						*  File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/base_extractor.py", line 24, in pullRequest 	<------------------------ WHERE 
						*   r = requests.get(url, timeout = 10) <-- THE CAUSE 
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/requests/api.py", line 75, in get
						    return request('get', url, params=params, **kwargs)
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/requests/api.py", line 61, in request
						    return session.request(method=method, url=url, **kwargs)
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/requests/sessions.py", line 529, in request
						    resp = self.send(prep, **send_kwargs)
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/requests/sessions.py", line 645, in send
						    r = adapter.send(request, **kwargs)
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/requests/adapters.py", line 501, in send
						    raise ConnectionError(err, request=request)
				    TEMP  requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response')) <- ERROR RAISED 
					"""

					The above exception was the direct cause of the following exception:

					Traceback (most recent call last):
					  File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/gulesider.py", line 372, in <module>
					    gulesiderExtractor(testmode = False)
					* File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/gulesider.py", line 356, in gulesiderExtractor 	<---------------------------- WHERE 
					*   results = list(tqdm(pool.imap_unordered(extractionManager, input_array), total = len(input_array)))  		 	<------------ ORIGIN OF ERROR RAISE 
					  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/tqdm/std.py", line 1195, in __iter__
					    for obj in iterable:
					  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/multiprocessing/pool.py", line 870, in next
					    raise value
				  TEMP  requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response')) <----- ERROR RAISED 
		
			! [ ] requests.exceptions.ReadTimeout: None: None
				
				? PROBABLE CAUSES: 
					- [ ] 
					- [ ] 		

				TODO POSSIBLE SOLUTIONS:
					- [ ] 
					- [ ] 

				TEMP - WHOLE ERROR:
					[...]

			! [ ] requests.exceptions.HTTPError: 504 Server Error: Gateway Timeout for url: https://www.gulesider.no/971366796/bedrifter
			  TEMP - WHOLE ERROR:
				multiprocessing.pool.RemoteTraceback:
					"""
					Traceback (most recent call last):
					  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/multiprocessing/pool.py", line 125, in worker
					    result = (True, func(*args, **kwds))
					  File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/gulesider.py", line 286, in extractionManager
					    soup = pullRequest(url, source, org_num, search_term)
					  File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/base_extractor.py", line 25, in pullRequest
					    r.raise_for_status() #? a bit unsure why i have this here
					  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/requests/models.py", line 960, in raise_for_status
					    raise HTTPError(http_error_msg, response=self)
					requests.exceptions.HTTPError: 504 Server Error: Gateway Timeout for url: https://www.gulesider.no/971366796/bedrifter
					"""

					The above exception was the direct cause of the following exception:

					Traceback (most recent call last):
					  File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/gulesider.py", line 377, in <module>
					    gulesiderExtractor(testmode = True)
					  File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/gulesider.py", line 362, in gulesiderExtractor
					    results = list(tqdm(pool.imap_unordered(extractionManager, input_array), total = len(input_array)))
					  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/tqdm/std.py", line 1195, in __iter__
					    for obj in iterable:
					  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/multiprocessing/pool.py", line 870, in next
					    raise value
				 TEMP requests.exceptions.HTTPError: 504 Server Error: Gateway Timeout for url: https://www.gulesider.no/971366796/bedrifter	

		I88I:
			! [ ] requests.exceptions.TooManyRedirects: Exceeded 30 redirects.
				? PROBABLE CAUSES: 
					? [1] Apparently the website (Amazon in solution case) does this based on the User-Agent header
							source: https://stackoverflow.com/questions/23651947/python-requests-requests-exceptions-toomanyredirects-exceeded-30-redirects
					? [2] 		

				§ POSSIBLE SOLUTIONS:
					todo [ ] (CAUSE [1]) Change header to Stop redirects
						
						s = requests.Session()
						s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
						r = s.get(url)

						This created a session (for ease of re-use and for cookie persistence), and a copy of the Chrome user agent string. The request succeeds (returns a 200 response).
						source: https://stackoverflow.com/questions/23651947/python-requests-requests-exceptions-toomanyredirects-exceeded-30-redirects

					todo [ ] (CAUSE [1]) Increase max_redirects:

						session = requests.Session()
						session.max_redirects = 60
						session.get('http://www.amazon.com')
						
						Increase of max_redirect is possible by explicitly specifying the count.
						source: https://stackoverflow.com/questions/23651947/python-requests-requests-exceptions-toomanyredirects-exceeded-30-redirects
					todo [ ] (CAUSE [1]) enable allow_redirects:  
						r = requests.get(url, allow_redirects=True)


				TEMP - WHOLE ERROR:
					multiprocessing.pool.RemoteTraceback:
					"""
						Traceback (most recent call last):
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/multiprocessing/pool.py", line 125, in worker
						    result = (True, func(*args, **kwds))
						  File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/I88I.py", line 150, in extractionManager
						    req = getRequest(url)
						  File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/I88I.py", line 100, in getRequest
						    return requests.get(url, cookies=cookies, verify=True) #* -> req
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/requests/api.py", line 75, in get
						    return request('get', url, params=params, **kwargs)
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/requests/api.py", line 61, in request
						    return session.request(method=method, url=url, **kwargs)
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/requests/sessions.py", line 529, in request
						    resp = self.send(prep, **send_kwargs)
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/requests/sessions.py", line 667, in send
						    history = [resp for resp in gen]
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/requests/sessions.py", line 667, in <listcomp>
						    history = [resp for resp in gen]
						  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/requests/sessions.py", line 166, in resolve_redirects
						    raise TooManyRedirects('Exceeded {} redirects.'.format(self.max_redirects), response=resp)
					>  requests.exceptions.TooManyRedirects: Exceeded 30 redirects.												 <-------------------------------- ERROR RAISED 
					"""

					The above exception was the direct cause of the following exception:

					Traceback (most recent call last):
					  File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/I88I.py", line 245, in <module>
					    opplysningenExtractor(testmode = False)
					* File "C:/Users/Big Daddy B/OneDrive/GitHub/Mediavest_Scraper_bot/I88I.py", line 220, in opplysningenExtractor 	<------------------------------------ WHERE 
					*   results = list(tqdm(pool.imap_unordered(extractionManager, input_array), total = len(input_array)))  		 	<-------------------- ORIGIN OF ERROR RAISE 
					  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/site-packages/tqdm/std.py", line 1195, in __iter__
					    for obj in iterable:
					  File "C:/Users/Big Daddy B/AppData/Local/Programs/Python/Python310/lib/multiprocessing/pool.py", line 870, in next
					    raise value
				    >  requests.exceptions.TooManyRedirects: Exceeded 30 redirects.												      <--------------------------- ERROR RAISED 

			! [ ] Infinite loop in getRequest() [I88I.py, line 76]
				  the code in getRequest() creates a bug when I88I reaches a webpage that simply won't cooperate (maybe it'a a bad request, etc.)
				  and since the while-try-loop won't stop trying untill a succsessfull request has been made, then it get's stuck and stops working.
				  snippet from output: 
				  		100%|████████████████████████████████████████████████████████████████████████████▊| 499/500 [00:45<00:00,  2.54it/s]

				? PROBABLE CAUSES: 
					? [ ] while-try-loop won't stop trying on bad requests
							The exception causing the Issue: 
								> requests.exceptions.TooManyRedirects: Exceeded 30 redirects.
					? [ ] 		

				todo POSSIBLE SOLUTIONS:
					§ [ ] create a list if specific exceptions + print the faulty link / company 
					§ [ ] create a try limit + print the faulty link / company 


				fixme WHOLE ERROR: 
				  			next_result = 0
				  	>	while next_result == 0:																							  <--------------------------- ERROR RAISED 
					  			try:
					  				r = s.get(url, cookies=cookies, verify=True)
					  				next_result = 1
					  				return r
					  			except:
					  				# print(f"ERROR CAUGHT in getRequest():")
					  				time.sleep(5)
					  				continue
					  			break
					
			! [ ] 

'''




''' TODO __________________________
? ASK DANIEL:
	todo [ ] how they would prefer the app:
			 built for administration 
			         or 
			 built for employees


! FUNCTIONAL:
	todo [X] rename 1881.py to I88I.py (atten_åtti_en) (BACKEND)

	todo [X] fix DataFrame error with brreg.py (BACKEND)
			 AttributeError: 
			 	'DataFrame' object has no attribute 'company_name'	
	
	todo [ ] Fix Issue [1] (BACKEND)

	todo [ ] Find out if you can diplay PANDAS in flutter, (APP)
			 if you have to build the dataframe manually. 
			 (steal from InvesteringsKalkulator)

	
* OPTINMAL:
	todo [?] Remove feature "deleteData()" from extractors regarding "input_table" (BACKEND)
			 reason being even though a company has "unpayed entry" for one website, 
			 doesn't mean it's like that for the other sites. 

	todo [?] In regards to brreg updating or resetting the input_table, (BACKEND)
	 		 Add a code that removes all previously confirmed companies 
	 		 (the ones in output_table or google_table) from input_table.

	todo [ ] Add de option to download dataframe as a CSV / EXCEL file (APP)(BACKEND) 
	
	todo [ ] Finish Documentation for: (BACKEND)
			 1.  [ ] brreg.py
			 2.  [ ] I88I.py
			 3.  [ ] gulesider.py
			 4.  [ ] input_table.py
			 5.  [ ] base_extraction.py
			 6.  [ ] config.py
			 7.  [ ] file_manager.py
			 8.  [ ] main.py
			 9.  [ ] output_table.py
			 10. [ ] proff.py (could steal stuff from old_proff.py)
			 11. [ ] error_save.py
		  Update:
			 1.  [ ] postgres.py (check if update is needed)
			 2.  [ ] google.py (check if update is needed)

	todo [ ] Finish FeedBack, see Issue [2] (APP)(BACKEND)
		 	 Either:
			 	 - Fix issues with API
			 	  			or
			 	 - Create your own way of sending the email

	todo [ ] Organize theme and Finish "LightMode" (APP)

	todo [ ] make / update a specific CleanUp code for Brreg_table:
			 where it removes companies that are e.g.: 
			 "konkurs == True"
			 "under_avvikling == True"
			 "under_tvangsavvikling_eller_oppløsning == True"

	todo [ ] Check if it's possible to upload backend to AWS (CLOUD)
			 so the users can control the updating of the database themselves 
			 by making API calls. 

	todo [ ] make a file that combines all output tables. 
	
* FINAL:
	todo [ ] Clean Files (BACKEND)
			 Save backup of "dirty" files as 
			 "BACKUP_pre_code_cleanup_[date]" 

	todo [ ] Create API's for: (APP)(BACKEND)
				1. get Dataframe
				2. update DataBase 
				3. delete Company (for confirmed sales)

	todo [ ] Create an overall "Instructions manual" (BACKEND)
'''


''' ? FOR CONCIDERATION ________________
? [ ] Changing architechture to run all extractors once for each company.(BACKEND) 
	  most of the extractors are quite similar so it could be efficiant, but it will loose "momentum" in regards to Concurency;
	  -> 4 extractors running sequentially doing 1000 companies concurrently, 
	     seems faster than 4 extractors running concurrently doing 1000 companies sequentlially. 
	  todo [ ] I would have to weigh the pros and cons (synergy VS momentum)
	
	IDEA_1: (LEAST SYNNERGY) (basicly sequential)
		instead of passing when a company has unpayed_entry==True, it will instead call the next extractor that will check the other website.

	IDEA_2: (MOST SYNNERGY, HARD TO PULL OF)
		all extractors starrts at the same time, and the first that finds "unpayed_entry==False" 
		will insert data into output list and delete it from input_list, then it wiill "somehow.."
		run a command that stops the other extractors from working on that company and move on to the next company. 

	IDEA_3: (GOOD SYNNERGY, EASY TO PULL OF)
		all extractors runs paralell at the same time, and the first that finds "unpayed_entry==False" 
		will insert data into output list and delete it from input_list, all extractors has a check-function that checks if input_table or output_table has or doesn't have that company.
		if so, they will abort and move on to the next. 
		Since one of them is significantly faster than the rest, it should be way ahead after a while and the other ones should work like IDEA_2 once it gains momentum.
		that way, the total length of extraction time would at maximum be the extraction time of the slowest extractor working with a full input_table.
		ät best it total extraction time would be the slowest extractor working with the input_table - yield from the other extractors, +momentum buildup 
	! Warning: I might have to again change the archiutechture of the scraper due to CPU-overload; sindce each scraper maximizes the CPU usage, i might have to revert them back to regular multithreading. 

? [ ] Combining the Extractors to one file (BACKEND)
	  				or 
	  atleast the ones using requests-beautifulsoup

'''




