''' TODO __________________________

	todo [X] check that database is fine
			- [X] run CleanUp on brreg_table
			- [C] repair extra index issue in brreg_table

	todo [ ] run a full test of backend to check for errors.

	todo [X] remove "test_env" from database and config. 

	todo [ ] Reorganize tablenames in database (and extractors)
			 status quo is confusing. 

	todo [X] I88I.py does not have a progressbar for chunks 
	
	todo [ ] rename google_output_table to call_list 

	todo [ ] fix request.connection error in gulesider.py
			 error persisted after try: except solution in base_extractor.py
			 requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
			todo [ ] new Solution; try divide gulesider into chunks like I88I and proff
			! Update: Error also showed up in I88I.py 
	possible solution:
	import socket
	from urllib3.connection import HTTPConnection

	HTTPConnection.default_socket_options = (
	    HTTPConnection.default_socket_options + [
	        (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
	        (socket.SOL_TCP, socket.TCP_KEEPIDLE, 45),
	        (socket.SOL_TCP, socket.TCP_KEEPINTVL, 10),
	        (socket.SOL_TCP, socket.TCP_KEEPCNT, 6)
	    ]
	)

	todo [ ] fix request.connection error in gulesider.py
! ISSUE request.connection error in gulesider.py
	requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))


! ISSUE Input_table getds bigger


! There is a posibility that output_table is getting smaller, 
	todo [ ] WIll look into it
	print output_table [16:54]: 1374 rows
	print output_table [16:55]: 1432 rows 
	print output_table [17:13]: 2369 rows 
'''

'''
____NOTES: DATABASE CHECKUP____
	
	brreg_table has an extra index column (might be resedue from a previous faulty code, run cleanup and check again.)
'''



'''
____OTHER NOTES____
	Ant selskapet i brreg_table som er;
		- konkurs: 									  2709 rows
		- under_avvikling:							  5672 rows
		- under_tvangsavvikling_eller_oppløsning:	  645 rows
												    = 9026 rows 
		- siste_insendte_årsregnskap.isnull(): 	   679 351 rows 
		- siste_insendte_årsregnskap has value:    399 515 rows 


9026 / 600 = 15.04 runs to scrape


google: 	(600) 165.02 sec --(pr.enh)--> 0.275 sec
gulesider: 	(500)  18.25 sec --(pr.enh)--> 0.037 sec
1881: 		(600)  54.14 sec --(pr.enh)--> 0.090 sec
proff: 	   (1000)  26.50 sec --(pr.enh)--> 0.027 sec
whole run: 							   ==> 0.429 sec

google: 	(600) 165.02 sec --(pr.sec)-->  3.6 enh/s
gulesider: 	(500)  18.25 sec --(pr.sec)--> 27.4 enh/s
1881: 		(600)  54.14 sec --(pr.sec)--> 11.1 enh/s
proff: 	   (1000)  26.50 sec --(pr.sec)--> 37.7 enh/s
whole run: 							   ==> 79.8 enh/s

time it would take to scrape all unnessasary companies in brreg_table:
	3872 sec ==> 01:04 hours

'''



'''! Errors caught during "Full Test":


! Error in gulesider.py:
	- [ gulesider.py reached input_table row nr. 11662 before error]
	multiprocessing.pool.RemoteTraceback:
		"""
		Traceback (most recent call last):
		  File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
		    httplib_response = self._make_request(
		  File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 449, in _make_request
		    six.raise_from(e, None)
		  File "<string>", line 3, in raise_from
		  File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 444, in _make_request
		    httplib_response = conn.getresponse()
		  File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1374, in getresponse
		    response.begin()
		  File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 318, in begin
		    version, status, reason = self._read_status()
		  File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 287, in _read_status
		    raise RemoteDisconnected("Remote end closed connection without"
		http.client.RemoteDisconnected: Remote end closed connection without response

		During handling of the above exception, another exception occurred:

		Traceback (most recent call last):
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 440, in send
		    resp = conn.urlopen(
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 785, in urlopen
		    retries = retries.increment(
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 550, in increment
		    raise six.reraise(type(error), error, _stacktrace)
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\packages\six.py", line 769, in reraise
		    raise value.with_traceback(tb)
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
		    httplib_response = self._make_request(
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 449, in _make_request
		    six.raise_from(e, None)
		  File "<string>", line 3, in raise_from
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 444, in _make_request
		    httplib_response = conn.getresponse()
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1374, in getresponse
		    response.begin()
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 318, in begin
		    version, status, reason = self._read_status()
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 287, in _read_status
		    raise RemoteDisconnected("Remote end closed connection without"
		urllib3.exceptions.ProtocolError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

		During handling of the above exception, another exception occurred:

		Traceback (most recent call last):
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\multiprocessing\pool.py", line 125, in worker
		    result = (True, func(*args, **kwds))
		  # File "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\gulesider.py", line 274, in extractionManager
		    soup = pullRequest(url, source, org_num, search_term)
		  # File "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\base_extractor.py", line 24, in pullRequest
		    r = requests.get(url, timeout = 10)
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 75, in get
		    return request('get', url, params=params, **kwargs)
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 61, in request
		    return session.request(method=method, url=url, **kwargs)
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 529, in request
		    resp = self.send(prep, **send_kwargs)
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 645, in send
		    r = adapter.send(request, **kwargs)
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 501, in send
		    raise ConnectionError(err, request=request)
		requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
		"""

		The above exception was the direct cause of the following exception:

		Traceback (most recent call last):
		  # File "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\gulesider.py", line 345, in <module>
		    gulesiderExtractor(testmode = False)
		  # File "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\gulesider.py", line 329, in gulesiderExtractor
		    for result in results:
		  # File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\multiprocessing\pool.py", line 870, in next
		    raise value
		requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))




! Error in I88I.py:
	- [ I88I.py reached input_table row nr. 11662 before error]
	- I88I.py continued by itsself after the error was fixed 
		IndentationError: unexpected indent
		Traceback (most recent call last):
		  File "<string>", line 1, in <module>
		  File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\multiprocessing\spawn.py", line 116, in spawn_main
		    exitcode = _main(fd, parent_sentinel)
		  File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\multiprocessing\spawn.py", line 125, in _main
		    prepare(preparation_data)
		  File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\multiprocessing\spawn.py", line 236, in prepare
		    _fixup_main_from_path(data['init_main_from_path'])
		  File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\multiprocessing\spawn.py", line 287, in _fixup_main_from_path
		    main_content = runpy.run_path(main_path,
		  File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\runpy.py", line 269, in run_path
		    return _run_module_code(code, init_globals, run_name,
		  File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\runpy.py", line 96, in _run_module_code
		    _run_code(code, mod_globals, init_globals,
		  File "C:\Users\Big Daddy B\AppData\Local\Programs\Python\Python310\lib\runpy.py", line 86, in _run_code
		    exec(code, run_globals)
		  File "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\proff.py", line 32, in <module>
		    from base_extractor import genSearchTerm, pullRequest
		  File "C:\Users\Big Daddy B\OneDrive\GitHub\Mediavest_Scraper_bot\base_extractor.py", line 89
		    next_result = 0
		IndentationError: unexpected indent


'''