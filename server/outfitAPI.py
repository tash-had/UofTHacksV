import requests, os
from server import Clothing
from nltk.corpus import wordnet
# from pymongo import MongoClient
# client = MongoClient(host='localhost', port=27017)
# db = client.data


"""
API for providing outfits
"""



API_KEY = os.environ.get('OPEN_WEATHER_MAP_KEY', '2f1fc3af6d1791f4a078b27231ac4fad')
token = "1842a5770640473ba7a7479777191e7e"
precipitation_jacket = ["drizzle", "snow", "rain", "blizzard", "hail", "ice", "heavy rain", "Extreme rain", "Extreme snow"]

word1 = wordnet.synset("pants.n.01")
word2 = wordnet.synset("shirt.n.01")
word3 = wordnet.synset("jacket.n.01")

def get_weather(city):
    weather = {}
    api_response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather',
        params={'q': city, 'APPID': API_KEY, "units": "metric"}
    )
    data = api_response.json()
    weather['temp'] = data['main']['temp']
    weather['precipitation'] = data['weather'][0]['main']

    return weather

# def provide_outfit(city):
#     """
#     Provide a "Smart" outfit for the user.
#
#     :return: JSON object
#     """
#
#     jacket_needed = False
#
#     # Check weather
#     weather = get_weather(city)
#     if weather['precipitation'] in precipitation_jacket or weather['temp'] <= 10:
#         jacket_needed = True
#
#     if jacket_needed:
#         # Check database for jacket.
#
#     else:
#         #


if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient(host='localhost', port=27017)
    db = client.data
    clothes = []

    x = db.users.find({})

    clothes = []

    for key in x:
        y = key["clothes"]
        clothes = []
        for i in y:
            new_dict = {}
            for item in i['web_entities']:
                if len(wordnet.synsets(item)[0]) > 0:
                    if word1.wup_similarity(wordnet.synsets(item)[0]) > 0.7:
                        new_dict['type'] = item
                    if word1.wup_similarity(wordnet.synsets(item)[0]) > 0.7:
