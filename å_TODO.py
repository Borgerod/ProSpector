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
		print output_table [16:54]: 1374 rows
		print output_table [16:55]: 1432 rows 
		print output_table [17:13]: 2369 rows 
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







# ! JUST SOME NOTES, nvm this
# start: {'tot_time': 0.00,'input_list': 10000, 'output': 0,  'yield': 0%, 'reduction' : 0&,}

# worker_1 : {'speed': "fast",   'time(h)': 0.30, 'input_list': 10000, 'output': 500,  'yield': 20%, 'reduction' : 80&, '*input_list': ('input_list'*'reduction')=9500,}   
# worker_2 : {'speed': "normal", 'time(h)': 1.00, 'input_list': 10000, 'output': 500,  'yield': 20%, 'reduction' : 80&, '*input_list': ('input_list'*'reduction')=9500,}   
# worker_3 : {'speed': "noraml", 'time(h)': 1.30, 'input_list': 10000, 'output': 500,  'yield': 20%, 'reduction' : 80&, '*input_list': ('input_list'*'reduction')=9500,}   
# worker_4 : {'speed': "slow",   'time(h)': 2.30, 'input_list': 10000, 'output': 500,  'yield': 20%, 'reduction' : 80&, '*input_list': ('input_list'*'reduction')=9500,}   



# # UTGANGSPUNKT (uten å ta hensyn til tid)
# run_1 : input_list = 10000 * 80% = 8000, tot_time = 0.00 + 0.30 = 0.30, output = 10000 * 20% = 2000, ==> *input_list = input_list = 8000
# run_2 : input_list =  8000 * 80% = 6400, tot_time = 0.30 + 1.00 = 1.30, output =  8000 * 20% = 1600, ==> *input_list = input_list = 6400
# run_3 : input_list =  6400 * 80% = 5120, tot_time = 1.30 + 1.30 = 3.00, output =  6400 * 20% = 1280, ==> *input_list = input_list = 5120
# run_4 : input_list =  5120 * 80% = 4096, tot_time = 3.00 + 2.30 = 5.30, output =  5120 * 20% = 1024, ==> *input_list = input_list = 4096


# end: {'tot_time': 5.30, 'input_list': 4096, 'output': 5904,  'yield': 59%, 'reduction' : 41%,}
# # note: 5.30h = 330.0min
# ==> yield_rate = 330/5904  = 0.05589 = 5.6%
# ==> yield/min = 5904/330 = 17.89 / min 



# # UTGANGSPUNKT (uten å ta hensyn til tid)
# run_1 : input_list = 10000 * 80% = 8000, output = 10000 - 8000 = 2000, time = 0.30, yield_pr_min = 2000 /  30 = 66.66, yield_rate = 3.30%
# run_2 : input_list = 10000 * 80% = 8000, output = 10000 - 8000 = 2000, time = 1.00, yield_pr_min = 2000 /  60 = 33.33, yield_rate = 1.65&
# run_3 : input_list = 10000 * 80% = 8000, output = 10000 - 8000 = 2000, time = 1.30, yield_pr_min = 2000 /  90 = 22.22, yield_rate = 1.10%
# run_4 : input_list = 10000 * 80% = 8000, output = 10000 - 8000 = 2000, time = 2.30, yield_pr_min = 2000 / 150 = 13.33, yield_rate = 0.65%

# # JUSTERT (med å ta hensyn til tid)
# run_1 : input_list = 10000 * 80% = 8000, output = 10000*0.2 = 2000, yield_pr_min = 66.66, time = 2000/66.66 = 0.30, yield_rate = 3.30%
# run_2 : input_list =  8000 * 80% = 6400, output =  8000*0.2 = 1600, yield_pr_min = 33.33, time = 1600/33.33 = 0.48, yield_rate = 3.30%
# run_3 : input_list =  6400 * 80% = 5120, output =  6400*0.2 = 1280, yield_pr_min = 22.22, time = 1280/22.22 = 0.57, yield_rate = 3.30%
# run_4 : input_list =  5120 * 80% = 4096, output =  5120*0.2 = 1024, yield_pr_min = 13.33, time = 1024/13.33 = 1.16, yield_rate = 3.30%

# end: {'tot_time': 3.50, 'input_list': 4096, 'output': 5904,  'yield': 59%, 'reduction' : 41%,}

