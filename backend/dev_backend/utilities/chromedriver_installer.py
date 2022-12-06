import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Chrome:
	def __init__(self) -> None:
		self.is_installed = None
		self.driver_path = r"backend/dev_backend/utilities/.wdm/drivers/chromedriver/win32/107.0.5304/chromedriver.exe"
		# self.driverFile = None

	# def installDriver(self) -> None:
		# ''' default; will download and install chromedriver. 
		# '''
	# 	ChromeDriverManager().install()

	def checkIfDriver(self):
		path = Path(self.driver_path)
		if path.exists():
			self.is_installed = True

	def installDriver(self):
		''' default; will download and install chromedriver. 
		'''
		ChromeDriverManager(path = os.path.dirname(os.path.abspath(__file__))).install()

	# def fetchDriverFromPath(self) -> None:
	# 	''' alternative to downloading [ installDriver() ]
	# 	'''
	# 	dirname = os.path.dirname(__file__)
	# 	self.driver_path = os.path.join(dirname, '..//utilities//chromedriver.exe')
	
	def getPath(self) -> webdriver:
		if not self.checkIfDriver():
			self.installDriver()
		return self.driver_path



# import os
# os.path.dirname(os.path.abspath(__file__))
# # If you mean the current working directory:

# import os
# os.path.abspath(os.getcwd())


	# def getDriverFile(self):
	# 	if self.is_installed:
	# 		return self.driver_path
	# 		return webdriver.Chrome(executable_path = self.driver_path, options = self.getDriverOptions)
	# 	else:
	# 		webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))