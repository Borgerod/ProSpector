from inspect import currentframe, getframeinfo
def getLineNumber():
    cf = currentframe()
    return cf.f_back.f_lineno

def getFilePath():
	return getframeinfo(currentframe()).filename

def getFileName():
	file_path = getFilePath()
	x = file_path.split('\\')
	return '/'.join(map(str, x[-2:]))

result = "beep boop, i am a dataframe"
print(f'line: {getLineNumber()}, print(result): \n{result}')

