from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def extractionManager(driver):
	print(f"processing with duration {driver}")
	time.sleep(driver)
	if checkGoogleAlarmTrigger(driver):
		return "CaptchaTriggered"
		# return None
	else:
		# return np.array((driver, 10, "something"), dtype = object)
		return [driver, 10, "something"]

def checkGoogleAlarmTrigger(driver): #! [CURRENTLY DISABLED]
	return driver == 1
	# 	return "result found"	
	# html = driver.page_source
	# return ('Systemene våre har oppdaget uvanlig trafikk' or 'unnusual traffic') in html

from concurrent.futures import ThreadPoolExecutor, as_completed
from inspect import currentframe, getframeinfo
import os
from tqdm import tqdm
import numpy as np

'''* map'''
# chunk = list(range(80000))
# with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor:     
	# future = list(tqdm(executor.map(process, chunk), total = len(chunk)))
	# result_list = [result for result in future if result is not None]
	# error_count = [result for result in future if result is     None]
	# for result in future:
	# 	# if future.result() == None:
	# 	if future.result() == "result found":
	# 		executor.shutdown(wait=False)
	# 		print("\n\n ERROR: shutdown was triggered!")
	# 		for f in futures:
	# 			if not f.done():
	# 				f.cancel()
	# 		break	
# print("exiting program")


















'''* submit'''
chunk = list(range(3))
print(chunk)
# with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor:  
# 	with tqdm(total = len(chunk)) as pbar:
# 		futures = [executor.submit(extractionManager, i) for i in chunk]
# 		pbar.update(1) 
# 		result_list = []
# 		error_count = []
# 		for future in as_completed(futures):
# 			if future.result() is not "CaptchaTriggered":
# 				result = future.result()
# 				# result_list.append(result)
# 				(error_count.append(result) if result is None else result_list.append(result))
# 				# (error_count.append(result) if not result else result_list.append(result))
# 			else:
# 				executor.shutdown(wait=False)
# 				print("\n\n ERROR: shutdown was triggered!")
# 				for f in futures:
# 					if not f.done():
# 						f.cancel()
# 				break
# 	print(error_count)
# 	print(result_list)
# 	print("exiting program")


with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor: 
	with tqdm(total = len(chunk)) as pbar:
		futures = [executor.submit(extractionManager, i) for i in chunk]
		pbar.update(1)  
		result_list = []
		error_count = []
		for future in as_completed(futures):
			result = future.result()
			if result != "CaptchaTriggered":
				(error_count.append(result) if None in result else result_list.append(result))
			else:
				executor.shutdown(wait=False)
				print("\n\n ERROR: shutdown was triggered!")
				for f in futures:
					if not f.done():
						f.cancel()
				break


		# for result in futures.result():
		# 	# ''' Error handling '''
		# 	if result != "CaptchaTriggered":
		# 	# if "CaptchaTriggered" not in result:
		# 		(error_count.append(result) if None in result else result_list.append(result))
		# 	else:
		# 		executor.shutdown(wait=False)
		# 		print("\n\n ERROR: shutdown was triggered!")
		# 		error_count.append(result)
		# 		for f in futures:
		# 			if not f.done():
		# 				f.cancel()
		# 		break












# '''* Map'''
# nested_input_array = [list(range(10))]
# total_error_count = 0
# for chunk in nested_input_array:
	# with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor:  
	# 	with tqdm(total = len(chunk)) as pbar2:
	# 		futures = executor.map(extractionManager, chunk)
	# 		# futures = list(executor.map(extractionManager, chunk))
	# 		pbar2.update(1) 
	# 		result_list = []
	# 		error_count = []
	# 		for result in futures:
	# 			if result is not "CaptchaTriggered":
	# 				''' without None handling '''
	# 				# result_list.append(result)

	# 				''' with None handling '''
	# 				# [ALT] (error_count.append(result) if result is None else result_list.append(result))
	# 				(error_count.append(result) if not result else result_list.append(result))

	# 			else:
	# 				executor.shutdown(wait=False)
	# 				print("\n\n ERROR: shutdown was triggered!")
	# 				for f in futures:
	# 					if not f.done():
	# 						f.cancel()
	# 				break

	# print(error_count)
	# print(result_list)
	# print("exiting program")

# '''* Map comprehension'''
# nested_input_array = [list(range(3))]
# total_error_count = 0
# for chunk in nested_input_array:
# 	with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor:  
# 		futures = list(tqdm(executor.map(extractionManager, chunk), total = len(chunk)))
# 		# for i in futures:
# 		# 	print(i)
# 		# with tqdm(total = len(chunk)) as pbar2:
# 		# 	futures = executor.map(extractionManager, chunk)
# 		# 	futures = list(executor.map(extractionManager, chunk))
# 		# 	pbar2.update(1)



# 		result_list = []
# 		error_count = []
# 		for result in futures:
# 			if result is not "CaptchaTriggered":
# 				''' without None handling '''
# 				# result_list.append(result)

# 				''' with None handling '''
# 				# [ALT] (error_count.append(result) if result is None else result_list.append(result))
# 				(error_count.append(result) if None in result else result_list.append(result))

# 			else:
# 				executor.shutdown(wait=False)
# 				print("\n\n ERROR: shutdown was triggered!")
# 				for f in futures:
# 					if not f.done():
# 						f.cancel()
# 				break

# 	print(error_count)
# 	print(result_list)
# 	print("exiting program")



# '''* submit'''
# chunk = list(range(80000))
# with ThreadPoolExecutor(max_workers=min(32, (os.cpu_count() or 1) + 4)) as executor:  
# 	with tqdm(total = len(chunk)) as pbar:
# 		futures = [executor.submit(process, i) for i in chunk]
# 		pbar.update(1) 
# 		result_list = []
# 		for future in as_completed(futures):
# 			if future.result() is "CaptchaTriggered":
# 				executor.shutdown(wait=False)
# 				print("\n\n ERROR: shutdown was triggered!")
# 				for f in futures:
# 					if not f.done():
# 						f.cancel()
# 				break
# 			else:
# 				result_list.append(future.result())
# 	print("exiting program")








'''> ORIGINAL <'''
# with ThreadPoolExecutor(max_workers=5) as executor:
	# futures = [executor.submit(process, i) for i in range(80000)]
	# for future in as_completed(futures):
	# 	if future.result() == "result found":
	# 		executor.shutdown(wait=False)
	# 		print("shutdown")
	# 		for f in futures:
	# 			if not f.done():
	# 				f.cancel()
	# 		break
# print("about to exit")