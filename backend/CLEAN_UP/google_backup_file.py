
#* BACKUPS WORKS REALLY WELL; [MAP] googleExtractor(), [OLD]googleExtractor(), extractionManager() 

def googleExtractor(**kwargs):
	'''
		sets up all nessasary functions, 
		then gets list of company names, 
		then iterates through the list via multithreading: claimedStatus().
	'''
	introPrint()
	testmode_kwarg = kwargs.get('testmode', None)
	file_name, chunksize, mode, tablename, start_limit, end_limit, input_array, long_break, short_break = getSettings(testmode_kwarg)
	nested_input_array = makeChunks(input_array, chunksize)
	infoPrint(nested_input_array, testmode_kwarg)
	
	'''! [tqdm ALT 1]'''
	with tqdm(total = len(nested_input_array)) as pbar: 

		'''! [tqdm ALT 1]'''
		with tqdm(total = len(input_array)) as pbar:
			total_error_count = 0
			for chunk in nested_input_array:
				with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor:  
					futures = list(tqdm(executor.map(extractionManager, chunk), total = len(chunk)))
					result_list = []
					error_count = []
					for result in futures:
						# ''' Error handling '''
						# if result != "CaptchaTriggered":
						if "CaptchaTriggered" not in result:
							(error_count.append(result) if None in result else result_list.append(result))
						else:
							executor.shutdown(wait=False)
							print("\n\n ERROR: shutdown was triggered!")
							error_count.append(result)
							for f in futures:
								if not f.done():
									f.cancel()
							break

					df = makeDataframe(result_list)
					print(df)
					databaseManager(df, tablename)
					
					'''! [tqdm ALT 1]'''
					pbar.update(1) 

					'''! [tqdm ALT 2]'''
					pbar.update(chunksize) 

					total_error_count += len(error_count)
					if len(pbar) != len(input_array):
						time.sleep(long_break)
				
		print(f"error count: {total_error_count}")
		outroPrint()





def googleExtractor(**kwargs):
	'''
		sets up all nessasary functions, 
		then gets list of company names, 
		then iterates through the list via multithreading: claimedStatus().
	'''
	introPrint()
	testmode_kwarg = kwargs.get('testmode', None)
	file_name, chunksize, mode, tablename, start_limit, end_limit, input_array, long_break, short_break = getSettings(testmode_kwarg)
	nested_input_array = makeChunks(input_array, chunksize)
	infoPrint(nested_input_array, testmode_kwarg)
	
	'''! [tqdm ALT 1]'''
	# with tqdm(total = len(nested_input_array)) as pbar: 

	'''! [tqdm ALT 1]'''
	with tqdm(total = len(input_array)) as pbar:

		total_error_count = 0
		for chunk in nested_input_array:
			with concurrent.futures.ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor:		
				results = list(tqdm(executor.map(extractionManager, chunk), total = len(chunk)))
				status_list = [status for status in results if status is not None]
				error_count = [status for status in results if status is 	 None]
				df = makeDataframe(status_list)
				print(df)
				databaseManager(df, tablename)
				
				'''! [tqdm ALT 1]'''
				# pbar.update(1) 

				'''! [tqdm ALT 2]'''
				pbar.update(chunksize) 

				total_error_count += len(error_count)
				if len(pbar) != len(input_array):
					time.sleep(long_break)
			
	print(f"error count: {total_error_count}")
	outroPrint()



def extractionManager(input_array):
	''' 
		import list 
		NB: remember to make sure it gets imported correctly 
		chunk = [] # consists of 500-1000 company names.
	'''
	org_num = input_array[0]
	search_term = input_array[1]

	base_url = "https://www.google.com/search?q=" 
	# print(f"{linkBuilder(base_url, search_term)}\n")
	driver = getDriver()
	driver.get(linkBuilder(base_url, search_term))
	mainWin = driver.current_window_handle  #* CATCHPA SOLVER
	

	try:	
		if driver.find_element(By.CLASS_NAME, "osrp-blk"):
			verify = driver.find_element(By.CLASS_NAME, "osrp-blk").text
			alt_search_term = search_term
			for ch in [' AS',' ASA', ' AB']:
				if ch in search_term:
					alt_search_term = search_term.replace(ch,"")
			alt_verify = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in verify.split("\n")][0]
			if re.search(search_term, verify, re.IGNORECASE):
				is_reqistered = True
			elif re.search(alt_search_term, verify, re.IGNORECASE):
				is_reqistered = True
			elif re.search(search_term, alt_verify, re.IGNORECASE) or re.search(alt_search_term, alt_verify, re.IGNORECASE):
				is_reqistered = True
			else:
				is_reqistered = 'Usikkert'
			try:
				check = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div')
				check_info = check.text
				if 'Add missing information' in check_info:
							has_info = False
				elif 'Legg til manglende informasjon' in check_info:
					has_info = False
				else:
					if is_reqistered:
						has_info = True
					else:
						has_info = False
				check_claimed = check.get_attribute('innerHTML')
				if 'cQhrTd' in check_claimed:
					is_claimed = True
				elif 'ndJ4N' in check_claimed:
					is_claimed = False
				else:
					if is_reqistered == False:
						is_claimed = False
					else:
						is_claimed = True

			except NoSuchElementException:
				has_info = True
				is_claimed = True
	except NoSuchElementException:
		is_reqistered = False
		try:
			check = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[5]/div/div/div')
			check_info = check.text
			if 'Add missing information' in check_info:
						has_info = False
			elif 'Legg til manglende informasjon' in check_info:
				has_info = False
			else:
				if is_reqistered:
					has_info = True
				else:
					has_info = False
			check_claimed = check.get_attribute('innerHTML')
			if 'cQhrTd' in check_claimed:
				is_claimed = True
			elif 'ndJ4N' in check_claimed:
				is_claimed = False
			else:
				if is_reqistered == False:
					is_claimed = False
				else:
					is_claimed = True
		except NoSuchElementException:
			has_info = False
			is_claimed = False
			
	return np.array((org_num, search_term, is_reqistered, is_claimed, has_info), dtype = object)
