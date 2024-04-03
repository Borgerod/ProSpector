class db:
	def GulesiderIndustries(self):
		return "i am Gulesider Industries, beep boop"

	def Gulesider(self):
		return "i am Gulesider, beep boop"

class Query:
	def __init__(self, *type) -> None:
		self.type = type 
		self.name = None
		self.type_variants = [
			'industry',
			'Industry',
			'industries',
			'Industries',
			]

	def get(self, name) -> list:
		self.name = name
		self.checkType()
		# TODO I obviously cant mention the column names, find another solution
		

	def checkType(self):
		if any(variant in self.type for variant in self.type_variants):
			self.name = 'Industry' + self.name

	# def AS(self, ):
	# 	return 
	def getTable(self, ):
		return [s.industries for s in session.query(getattr(db, self.name)).all()]

	def convertToFormat(self, format):
		#todo (CHALLANGE) try not to pass data as a parameter, and return the converter function instead
		data = None
		match format:
			case 'list':
				return Convert(data, self.getColumns).to_list()
				
			case 'dict':
				return 
			case 'numpy':
				return 
			case 'pandas':
				return 
			case 'array':
				return 
			case 'dataframe':
				return

	# TODO make a function that returns the industries for tablename
	@property
	def getColumns(self) -> dict:
		return getattr(db, self.name).__dict__.keys() #[1:] #Due to the first one not being a column
		# return []
		
class Convert:
	''' the idea: premade converter function with a an empty spot for the data '''
	def __init__(self, data, columns) -> None:
		self.data = data
		self.columns = columns

	def to_list(self, ):
		for key, data_row in zip(self.columns, self.data):
			[]
			[s.industries for s in session.query(getattr(db, self.name)).all()]



	def to_dict(self, ):
		return

	def to_pandas(self, ):
		return

	def to_numpy(self, ):
		return

class Query:
	def get(self, name, **format): #todo find annotation for multiple types
		self.name = name
		self.checkType()
		table = self.getTable()
		if format:
			self.convertToFormat(format)
		else:





Query().get(
	'IndustryGulesider', 
	format = 'pandas'
	)

# class Query():
# 	# if type == "industry":


# 	# __slots__ = 'get_industries', 'kwargs', 'type_variants',
	
# 	def __init__(self, *type) -> None:
# 		self.get_industries = False
# 		self.type = type
# 		self.type_variants = [
# 			'industry',
# 			'Industry',
# 			'industries',
# 			'Industries',
# 			]

# 	def get(self, name):

# 		# if self.type == 'industry':
# 		# 	func = getIndustryTables()
# 		# else:
# 		# 	func = getMainTables()
		
# 		func = self.getBaseFunc(name)
# 		return func
# 		# if any(variant in self.type for variant in self.type_variants):
# 		# # if self.type == 'industry':
# 		# 	func = func+"Industries"
# 		# return func 
	
# 	def getMainTables(self, name):
# 		pass
	
# 	def getBaseFunc(self, name):
# 		func = None
# 		match name:
# 			case 'proff':
# 				func = "db.Proff"

# 			case 'Gulesider':
# 				func = "db.Gulesider"

# 			case '1881':
# 				func = "db._1881"

# 			case 'google':
# 				func = "db.Google"

# 			case 'InputTable':
# 				func = "db.InputTable"
# 		if any(variant in self.type for variant in self.type_variants):
# 			func = func+"Industries"
# 		return func 		



# # data = Query('industries').get('Gulesider')
# # print(data)

# class db:
# 	def GulesiderIndustries(self):
# 		return "i am Gulesider Industries, beep boop"

# 	def Gulesider(self):
# 		return "i am Gulesider, beep boop"

# class Query:
# 	def __init__(self, *type) -> None:
# 		self.type = type 
# 		self.name = None
# 		self.type_variants = [
# 			'industry',
# 			'Industry',
# 			'industries',
# 			'Industries',
# 			]
			
# 	def get(self, name):
# 		self.name = name
# 		self.checkType()
# 		return getattr(db, self.name)

# 	def checkType(self):
# 		if any(variant in self.type for variant in self.type_variants):
# 			self.name = self.name + 'Industries'


# x1 = Query('industry').get('Gulesider')
# x2 = Query().get('Gulesider')
# print(x1())
# print(x2())

# # x = getattr(foo, 'industry')
# # result = x()
# # print(result)

# # def test(**type):
# # 	print(f"{type}")

# # def test(*type):
# # 	print(f"{type}")


# # test()
# # test('foo')






# 	# def getIndustryTables(self, name):
# 	# 		match name:
# 	# 			case 'proff':
# 	# 				return "db.ProffIndustries"

# 	# 			case 'Gulesider':
# 	# 				return "db.GulesiderIndustries"
					
# 	# 			case '1881':
# 	# 				return "db._1881Industries"

# 	# def getFuncFromArg(self, name):
# 	# 	match name:
# 	# 		case 'proff':
# 	# 			if self.get_industries:
# 	# 				return "db.ProffIndustries"
# 	# 			else:
# 	# 				return "db.Proff"

# 	# 		case 'Gulesider':
# 	# 			if self.get_industries:
# 	# 				return "db.GulesiderIndustries"
# 	# 			else:
# 	# 				return "db.Gulesider"

# 	# 		case '1881':
# 	# 			if self.get_industries:
# 	# 				return "db._1881Industries"
# 	# 			else:
# 	# 				return "db._1881"

# 	# 		case 'google':
# 	# 			return "db.Google"

# 	# 		case 'InputTable':
# 	# 			return "db.InputTable"


	
# 	# @property
# 	# def industries(self):
# 	# 	self.get_industries = True
	
# 	# # def getIndustry(self, name):
# 	# # 	func = self.getFuncFromArg(name)
# 	# # 	data = func()

# 	# def get(self, name):
# 	# 	func = self.getFuncFromArg()
# 	# 	# if self.get_industries:
# 	# 	# func = self.getFuncFromMainTables(name)
# 	# 	# else:
# 	# 	# 	func = self.getFuncFromIndustryTables(name)


# # data = Query('industry').get('Gulesider')


