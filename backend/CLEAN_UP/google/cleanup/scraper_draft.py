from environs import Env
import googlemaps
import requests
from bs4 import BeautifulSoup
# import time
from fake_headers import Headers

# ____ Local Imports _____
from config import cred




'''
	TODO: 
		Create formula for PAGE_TOKENS
'''
def get_hdr():
	hdr = Headers().generate()
	return hdr

def get_api_values(name):              
	api_key = cred[name]['API_KEY']
	return api_key


def loop(api_key, radius, loc):
	videofeed = pd.DataFrame()
	response = nearby_search(api_key, radius, loc)
	resp_df, max_res = parse_data(response)
	videofeed = pd.concat([videofeed, resp_df], ignore_index = True)
	while len(videofeed) < max_res:
		token = None
		try:
			response = request.execute()
			resp_df, max_res = parse_data(response)
			videofeed = pd.concat([videofeed, resp_df], axis=0, ignore_index = True)
			request = youtube.search().list_next(request, response)
		except AttributeError:
			return videofeed
	return videofeed


def parse_data(response):
	results 
	name = []
	business_status = []
	opening_hours = []
	photos = []
	price_level = []
	rating = []
	types = []



	# titles = []
	# videoIds = []
	# channelIds = []
	# img = []
	# date = []
	max_res = response['pageInfo']["totalResults"]
	resp_df = pd.DataFrame()
	for item in response['items']:
		titles.append(item['snippet']['title'])
		channelIds.append(item['snippet']['channelTitle'])
		videoIds.append(item['id']['videoId'])
		img.append(item['snippet']['thumbnails']['high']['url'])
		date.append(item['snippet']['publishTime'])
	if "nextPageToken" in response:
		print("..next page..")
		token = response["nextPageToken"]
		resp_df['date'] = date
		resp_df['channelId'] = channelIds
		resp_df['title'] = titles
		resp_df['videoId'] = videoIds
		resp_df['thumbnail'] = img
		return resp_df, max_res
	else:
		try:
			resp_df['date'] = date
			resp_df['channelId'] = channelIds
			resp_df['title'] = titles
			resp_df['videoId'] = videoIds
			resp_df['thumbnail'] = img
			print("..FINISHED!")
			return resp_df, max_res
		except:
			print("..FINISHED!")
			return resp_df, max_res


def all_vids_loop(channelId, youtube):
	request = youtube.search().list(part = 'id,snippet',
									channelId = channelId,
									type = 'video',
									maxResults = 50,
									relevanceLanguage = 'en',)
	return request



def location_list():

	locations : {'bergen': '60.244958, 5.636803',} #TEMPORARTY

	# locations = { 	'bergen': '60.244958, 5.636803', 			# Bjøørnafjorden
	# 				'oslo' : '59.987955, 10.527667', 			# Bærum (skogen) 
	# 				'tønnsberg': '59.226256, 10.807865',		# Vikanetoppen 1
	# 				'stavanger' : '58.969629, 5.737280',		# Brødregata
	# 				'kristiansand' : '58.230649, 7.898547',		# Mosby
	# 				'trondheim' : '63.455406, 10.451043',		# Lade
	# 				'bodø' : '67.191863, 14.976926', 			# Støvsetvatnet
	# 				'tromsø' : '69.653363, 18.968658',		}	# Fylkesvei 862
	return locations

def nearby_search(api_key, radius, loc):
	'''
	Builds url string for google api engine
	'''

	url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={loc}&radius={radius}&key={api_key}"
	print(url)
	payload = {}
	headers = get_hdr()
	# response = requests.request("GET", url, headers = headers)
	# response = requests.request("GET", url, headers=headers, data=payload)
	# return response.text

def main():
	# ___ Setu p______
	api_key = get_api_values('google')
	radius = 50000
	loc = location_list()
	for i in loc:
		nearby_search(api_key, radius, loc[i])
# main()

'''
# fra googles eksempel
	import requests

	url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522%2C151.1957362&radius=1500&type=restaurant&keyword=cruise&key=YOUR_API_KEY"

	payload = {}
	headers = {}

	response = requests.request("GET", url, headers=headers, data=payload)

	print(response.text)
'''



''' ____ place_details ___________
	source: https://developers.google.com/maps/documentation/places/web-service/search

	
	Basic:
	The Basic category includes the following fields: address_component, adr_address, business_status, formatted_address, geometry, icon, icon_mask_base_uri, icon_background_color, name, permanently_closed (deprecated), photo, place_id, plus_code, type, url, utc_offset, vicinity.

	Contact:
	The Contact category includes the following fields: formatted_phone_number, international_phone_number, opening_hours, website

	Atmosphere:
	The Atmosphere category includes the following fields: price_level, rating, review, user_ratings_total.
'''


''' ____ Nearby Search ___________
	Source: https://developers.google.com/maps/documentation/places/web-service/search-nearby

	REQUIRED PARAMETERS
		location - The point around which to retrieve place information. This must be specified as latitude,longitude.
	
	OPTIONAL PARAMETERS
		language - The language in which to return results.
		pagetoken - Returns up to 20 results from a previously run search. Setting a pagetoken parameter will execute a search with the same parameters used previously — all parameters other than pagetoken will be ignored.
		radius - Defines the distance (in meters) within which to return place results. You may bias results to a specified circle by passing a location and a radius parameter. 
'''


'''
Nearby search example:

	import requests

	url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522%2C151.1957362&radius=1500&type=restaurant&keyword=cruise&key=YOUR_API_KEY"

	payload={}
	headers = {}

	response = requests.request("GET", url, headers=headers, data=payload)

	print(response.text)
'''


'''
Nearby search output:

	{
	  "html_attributions": [],
	  "results":
		[
		  {
		"business_status": "OPERATIONAL",
		"geometry":
		  {
			"location": { "lat": -33.8587323, "lng": 151.2100055 },
			"viewport":
			  {
			"northeast":
			  { "lat": -33.85739847010727, "lng": 151.2112436298927 },
			"southwest":
			  { "lat": -33.86009812989271, "lng": 151.2085439701072 },
			  },
		  },
		"icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/bar-71.png",
		"icon_background_color": "#FF9E67",
		"icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/bar_pinlet",
		"name": "Cruise Bar",
		"opening_hours": { "open_now": false },
		"photos":
		  [
			{
			  "height": 608,
			  "html_attributions":
			[
			  '<a href="https://maps.google.com/maps/contrib/112582655193348962755">A Google User</a>',
			],
			  "photo_reference": "Aap_uECvJIZuXT-uLDYm4DPbrV7gXVPeplbTWUgcOJ6rnfc4bUYCEAwPU_AmXGIaj0PDhWPbmrjQC8hhuXRJQjnA1-iREGEn7I0ZneHg5OP1mDT7lYVpa1hUPoz7cn8iCGBN9MynjOPSUe-UooRrFw2XEXOLgRJ-uKr6tGQUp77CWVocpcoG",
			  "width": 1080,
			},
		  ],
		"place_id": "ChIJi6C1MxquEmsR9-c-3O48ykI",
		"plus_code":
		  {
			"compound_code": "46R6+G2 The Rocks, New South Wales",
			"global_code": "4RRH46R6+G2",
		  },
		"price_level": 2,
		"rating": 4,
		"reference": "ChIJi6C1MxquEmsR9-c-3O48ykI",
		"scope": "GOOGLE",
		"types":
		  ["bar", "restaurant", "food", "point_of_interest", "establishment"],
		"user_ratings_total": 1269,
		"vicinity": "Level 1, 2 and 3, Overseas Passenger Terminal, Circular Quay W, The Rocks",
		  }, 
		  ],
		"place_id": "ChIJtwapWjeuEmsRcxV5JARHpSk",
		"plus_code":
		  {
			"compound_code": "45HX+R5 Pyrmont, New South Wales",
			"global_code": "4RRH45HX+R5",
		  },
		"price_level": 2,
		"rating": 4.5,
		"reference": "ChIJtwapWjeuEmsRcxV5JARHpSk",
		"scope": "GOOGLE",
		"types": ["restaurant", "food", "point_of_interest", "establishment"],
		"user_ratings_total": 1916,
		"vicinity": "3/50 Murray St, Pyrmont",
		  },
		],
	  "status": "OK",
}
'''

