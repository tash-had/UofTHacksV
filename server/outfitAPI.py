import requests, os
from pymongo import MongoClient
from server.Clothing import Clothing
from nltk.corpus import wordnet
from server.Color import Color
import random
from server.ColorConversionLibrary import get_general_color
from server.ColorSortingAPI import *
import pickle
# from pymongo import MongoClient
# client = MongoClient(host='localhost', port=27017)
# db = client.data

client = MongoClient("mongodb://quickdressedadmin:quickdresspassword@cluster0-shard-00-00-qfhms.mongodb.net:27017,cluster0-shard-00-01-qfhms.mongodb.net:27017,cluster0-shard-00-02-qfhms.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
db = client.users

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

def provide_outfit(city):
    """
    Provide a "Smart" outfit for the user.

    :return: JSON object
    """

    pickle_in = open("total_distinct_pairs.bin", "rb")
    total_distinct_pairs = pickle.load(pickle_in)

    outfit = []

    jacket_needed = False

    # client = MongoClient(host='localhost', port=27017)
    # db = client.data
    x = db.users.find({})

    clothes = []
    all_c = []
    for key in x:
        y = key["clothes"]
        all_c.extend(y)
        for i in y:
            index = 0
            new_dict = {}
            for item in i['web_entities']:
                if len(wordnet.synsets(item)) > 0:
                    if word1.wup_similarity(wordnet.synsets(item)[0]) > 0.5:
                        new_dict['type'] = word1
                    if word1.wup_similarity(wordnet.synsets(item)[0]) > 0.5:
                        new_dict['type'] = word2
                    if word3.wup_similarity(wordnet.synsets(item)[0]) > 0.5:
                        new_dict['type'] = word3
            new_color = Color(i['colors']['red'], i['colors']['green'],
                              i['colors']['blue'])
            new_dict['color'] = new_color
            new_dict['id'] = index
            clothing_article = Clothing(new_dict['color'], new_dict['type'],
                                        new_dict['id'])
            clothes.append(clothing_article)
            index += 1

    # Check weather
    weather = get_weather("Toronto")
    if weather['precipitation'] in precipitation_jacket or weather['temp'] <= 10:
        jacket_needed = True

    if jacket_needed:
        for item in clothes:
            if item.type == "jacket":
                outfit.append(item.id)

    else:
        shirts = []
        for item in clothes:
            if item.type == "shirt":
                shirts.append(item)
        rand_shirt = random.choice(shirts)
        outfit.append(rand_shirt.id)
        general_shirt_tuple = get_general_color(rand_shirt.color.r, rand_shirt.color.g, rand_shirt.color.b)
        corresponding_color = get_corresponding_color(Color(general_shirt_tuple[0], general_shirt_tuple[1]
                                                            , general_shirt_tuple[2]), total_distinct_pairs)
        pants_list = []
        for item in clothes:
            if item.type == "pants":
                pants_list.append(item)
        corresponding_pants = find_corresponding_clothing(pants_list, corresponding_color)
        outfit.append(corresponding_pants.id)


        clothes_images = []
        clothes_images.append(all_c[outfit[0]["image"]])
        clothes_images.append(all_c[outfit[1]["image"]])
        clothes_images.append(all_c[outfit[2]["image"]])
        return clothes_images

        #
        # clothes_images = []
        # for item in stuff:
        #     clothes_images = [item["clothes"][outfit[0]]["image"], item["clothes"][outfit[1]["image"]],
        #                item["clothes"][outfit[2]["image"]]]

