# from brreg import brregExtractor
from google import googleExtractor
# from gulesider import gulesiderExtractor


def main():
	testmode = 'off'
	# testmode = 'on'
	# brregExtractor(testmode)
	googleExtractor(url = '', )
	# gulesiderExtractor(testmode)

if __name__ == '__main__':
	main()
'''
params for brregExtractor()
	update_url = 'https://data.brreg.no/enhetsregisteret/api/oppdateringer/enheter'
	downlaod_url = 'https://data.brreg.no/enhetsregisteret/api/enheter/lastned'
'''