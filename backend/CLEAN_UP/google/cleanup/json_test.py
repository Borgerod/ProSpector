import pprint
import json



output = {
   "html_attributions" : [],
   "result" : {
      "formatted_address" : "Essendrops gate 3, 0368 Oslo, Norway",
      "formatted_phone_number" : "23 16 15 50",
      "international_phone_number" : "+47 23 16 15 50",
      "name" : "Felleskatalogen AS",
      "opening_hours" : {
         "open_now" : False,
         "periods" : [
            {
               "close" : {
                  "day" : 1,
                  "time" : "1600"
               },
               "open" : {
                  "day" : 1,
                  "time" : "0830"
               }
            },
            {
               "close" : {
                  "day" : 2,
                  "time" : "1600"
               },
               "open" : {
                  "day" : 2,
                  "time" : "0830"
               }
            },
            {
               "close" : {
                  "day" : 3,
                  "time" : "1600"
               },
               "open" : {
                  "day" : 3,
                  "time" : "0830"
               }
            },
            {
               "close" : {
                  "day" : 4,
                  "time" : "1600"
               },
               "open" : {
                  "day" : 4,
                  "time" : "0830"
               }
            },
            {
               "close" : {
                  "day" : 5,
                  "time" : "1600"
               },
               "open" : {
                  "day" : 5,
                  "time" : "0830"
               }
            }
         ],
         "weekday_text" : [
            "Monday: 8:30 AM – 4:00 PM",
            "Tuesday: 8:30 AM – 4:00 PM",
            "Wednesday: 8:30 AM – 4:00 PM",
            "Thursday: 8:30 AM – 4:00 PM",
            "Friday: 8:30 AM – 4:00 PM",
            "Saturday: Closed",
            "Sunday: Closed"
         ]
      },
      "place_id" : "ChIJ2cvRNsVtQUYRF1X85dJ4h_U",
      "rating" : 4.7,
      "reviews" : [
         {
            "author_name" : "Eddie “ði”",
            "author_url" : "https://www.google.com/maps/contrib/116344433358865510753/reviews",
            "language" : "en",
            "profile_photo_url" : "https://lh3.googleusercontent.com/a-/AFdZucqt-FvGVbNntoygBaLteAe8iS-V6d5cpJHYXAIScA=s128-c0x00000000-cc-rp-mo-ba4",
            "rating" : 5,
            "relative_time_description" : "a year ago",
            "text" : "A trustworthy and reliable site.",
            "time" : 1623285673
         },
         {
            "author_name" : "Harley Christine von Betzen",
            "author_url" : "https://www.google.com/maps/contrib/102286977327081248316/reviews",
            "language" : "en-US",
            "profile_photo_url" : "https://lh3.googleusercontent.com/a-/AFdZucqeJmIEstXAwwiKIyCoZYmTIhvWR9puS3N1kDbS=s128-c0x00000000-cc-rp-mo-ba3",
            "rating" : 4,
            "relative_time_description" : "7 months ago",
            "text" : "Get good information about medications",
            "time" : 1639062862
         },
         {
            "author_name" : "Lasse Røvik",
            "author_url" : "https://www.google.com/maps/contrib/117762745202767080655/reviews",
            "language" : "en-US",
            "profile_photo_url" : "https://lh3.googleusercontent.com/a-/AFdZucqEd_B-0l0buJtrIHA-QgdnQGzwsbR6sQcfWZw=s128-c0x00000000-cc-rp-mo-ba5",
            "rating" : 5,
            "relative_time_description" : "a year ago",
            "text" : "Indispensable for both doctors and patients.",
            "time" : 1622436727
         },
         {
            "author_name" : "Hans Tveter",
            "author_url" : "https://www.google.com/maps/contrib/110063171433651418717/reviews",
            "profile_photo_url" : "https://lh3.googleusercontent.com/a/AItbvmmw0-kE7ewo6TqkctHpgQAYfWNcVvcwBzjpZd4d=s128-c0x00000000-cc-rp-mo",
            "rating" : 5,
            "relative_time_description" : "5 years ago",
            "text" : "",
            "time" : 1495141019
         },
         {
            "author_name" : "Hans Martin Johansen",
            "author_url" : "https://www.google.com/maps/contrib/100696207144171598310/reviews",
            "profile_photo_url" : "https://lh3.googleusercontent.com/a-/AFdZucr-MU-LBPNADtAr00b-qyrauD99hJPMGUHdc4qYxQ=s128-c0x00000000-cc-rp-mo-ba4",
            "rating" : 2,
            "relative_time_description" : "3 years ago",
            "text" : "",
            "time" : 1544739681
         }
      ],
      "url" : "https://maps.google.com/?cid=17692242508345267479",
      "user_ratings_total" : 15,
      "website" : "https://www.felleskatalogen.no/medisin"
   },
   "status" : "OK"
}

output =  {'html_attributions': [],
 'result': {'formatted_address': 'Essendrops gate 3, 0368 Oslo, Norway',
            'formatted_phone_number': '23 16 15 50',
            'international_phone_number': '+47 23 16 15 50',
            'name': 'Felleskatalogen AS',
            'opening_hours': {'open_now': False,
                              'periods': [{'close': {'day': 1, 'time': '1600'},
                                           'open': {'day': 1, 'time': '0830'}},
                                          {'close': {'day': 2, 'time': '1600'},
                                           'open': {'day': 2, 'time': '0830'}},
                                          {'close': {'day': 3, 'time': '1600'},
                                           'open': {'day': 3, 'time': '0830'}},
                                          {'close': {'day': 4, 'time': '1600'},
                                           'open': {'day': 4, 'time': '0830'}},
                                          {'close': {'day': 5, 'time': '1600'},
                                           'open': {'day': 5, 'time': '0830'}}],
                              'weekday_text': ['Monday: 8:30 AM – 4:00 PM',
                                               'Tuesday: 8:30 AM – 4:00 PM',
                                               'Wednesday: 8:30 AM – 4:00 PM',
                                               'Thursday: 8:30 AM – 4:00 PM',
                                               'Friday: 8:30 AM – 4:00 PM',
                                               'Saturday: Closed',
                                               'Sunday: Closed']},
            'place_id': 'ChIJ2cvRNsVtQUYRF1X85dJ4h_U',
            'rating': 4.7,
            'reviews': [{'author_name': 'Eddie “ði”',
                         'author_url': 'https://www.google.com/maps/contrib/116344433358865510753/reviews',
                         'language': 'en',
                         'profile_photo_url': 'https://lh3.googleusercontent.com/a-/AFdZucqt-FvGVbNntoygBaLteAe8iS-V6d5cpJHYXAIScA=s128-c0x00000000-cc-rp-mo-ba4',
                         'rating': 5,
                         'relative_time_description': 'a year ago',
                         'text': 'A trustworthy and reliable site.',
                         'time': 1623285673},
                        {'author_name': 'Harley Christine von Betzen',
                         'author_url': 'https://www.google.com/maps/contrib/102286977327081248316/reviews',
                         'language': 'en-US',
                         'profile_photo_url': 'https://lh3.googleusercontent.com/a-/AFdZucqeJmIEstXAwwiKIyCoZYmTIhvWR9puS3N1kDbS=s128-c0x00000000-cc-rp-mo-ba3',
                         'rating': 4,
                         'relative_time_description': '7 months ago',
                         'text': 'Get good information about medications',
                         'time': 1639062862},
                        {'author_name': 'Lasse Røvik',
                         'author_url': 'https://www.google.com/maps/contrib/117762745202767080655/reviews',
                         'language': 'en-US',
                         'profile_photo_url': 'https://lh3.googleusercontent.com/a-/AFdZucqEd_B-0l0buJtrIHA-QgdnQGzwsbR6sQcfWZw=s128-c0x00000000-cc-rp-mo-ba5',
                         'rating': 5,
                         'relative_time_description': 'a year ago',
                         'text': 'Indispensable for both doctors and patients.',
                         'time': 1622436727},
                        {'author_name': 'Hans Tveter',
                         'author_url': 'https://www.google.com/maps/contrib/110063171433651418717/reviews',
                         'profile_photo_url': 'https://lh3.googleusercontent.com/a/AItbvmmw0-kE7ewo6TqkctHpgQAYfWNcVvcwBzjpZd4d=s128-c0x00000000-cc-rp-mo',
                         'rating': 5,
                         'relative_time_description': '5 years ago',
                         'text': '',
                         'time': 1495141019},
                        {'author_name': 'Hans Martin Johansen',
                         'author_url': 'https://www.google.com/maps/contrib/100696207144171598310/reviews',
                         'profile_photo_url': 'https://lh3.googleusercontent.com/a-/AFdZucr-MU-LBPNADtAr00b-qyrauD99hJPMGUHdc4qYxQ=s128-c0x00000000-cc-rp-mo-ba4',
                         'rating': 2,
                         'relative_time_description': '3 years ago',
                         'text': '',
                         'time': 1544739681}],
            'url': 'https://maps.google.com/?cid=17692242508345267479',
            'user_ratings_total': 15,
            'website': 'https://www.felleskatalogen.no/medisin'},
 'status': 'OK'}

params = [
  'name',
  'rating', 
  'formatted_phone_number',
  'international_phone_number',
  'formatted_address',
  'opening_hours',
  'photos',
  'place_id',
  'reviews',
  'rating',
  'user_ratings_total',
  'url',
  'website',
  ]
# for key, value in data.items():


def checker(output):
  output = output['result']
  google_checklist = {
'has_name': '',
'has_phone_number': '',
'has_address': '',
'has_opening_hours': '',
'has_photos': '',
'has_reviews': '',
'has_website': '',
  }
  if 'name' in output:
    name = output['name']

  if 'rating' in output:
    google_checklist['has_name'] = True
  else:
    google_checklist['has_name'] = False

  if 'formatted_phone_number' in output:
    google_checklist['has_phone_number'] = True
  else:
    google_checklist['has_phone_number'] = False

  if 'formatted_address' in output:
    google_checklist['has_address'] = True
  else:
    google_checklist['has_address'] = False

  if 'opening_hours' in output:
    google_checklist['has_opening_hours'] = True
  else:
    google_checklist['has_opening_hours'] = False  

  if 'photos' in output:
    google_checklist['has_photos'] = True
  else:
    google_checklist['has_photos'] = False

  if 'reviews' in output:
    google_checklist['has_reviews'] = True
  else:
    google_checklist['has_reviews'] = False  

  if 'website' in output:
    google_checklist['has_website'] = True
  else:
    google_checklist['has_website'] = False


  pprint.pprint(google_checklist)
checker(output)
  # print(pd.DataFrame(google_checklist))

# pprint.pprint(output)

# place_id = output['results'][0]['place_id']
# # print(place_id)



# params = ['has_name',
# 'has_phone_number',
# 'has_address',
# 'has_opening_hours',
# 'has_photos',
# 'has_reviews',
# 'has_website',]
# for i in params:
#   google_checklist[i] =