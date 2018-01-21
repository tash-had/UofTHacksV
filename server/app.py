from flask import Flask, jsonify
# from flask_pymongo import PyMongo
# from flask_pymongo import MongoClient
from pymongo import MongoClient

from flask import abort, make_response, request, url_for
from scraper.n import detect_properties, detect_web

import base64
import json

app = Flask(__name__)
# mongo = PyMongo(app)
client = MongoClient(port=27017)
db = client.data


@app.route('/', methods=["GET", "POST"])
def receive_outfit():
    if request.method == "POST":
        json_acceptable_data = request.form['data'].replace("'", "\"")
        pic_data = json.loads(json_acceptable_data)

        try:
            uuid = pic_data['uuid']
            name = pic_data['name']
            gender = pic_data['gender']
            timestamp = pic_data['timestamp']
            image = pic_data['encoded_image']

            user = {"name": name, "gender":gender, "user_id":"",
                    "previous_matches": [], "worn_outfits": []}
            cloth = {"uuid": uuid, "owner":user['name'], "timestamp": timestamp,
                     "image": image, "last_worn_days": 0, "category":"",
                     "web_entities":[], "match":[], "colors":[]}


            with open("imageToSave.png", "wb") as fh:
                fh.write(base64.decodebytes(pic_data))
            cloth['colors'] = detect_properties('imageToSave.png')
            cloth['web_entities'] = detect_web('imageToSave.png')

            if not db.users.find({'UserIDS': user['name']}).count() > 0:
                new_user = {
                    "user": user,
                    "clothes" : [cloth]
                }
                result = db.users.insert_one(new_user)
                print(result.inserted_id)

            else:
                db.users.update({"user.name": user['name']},
                                {"$push": {
                                    'clothes', cloth}})

        except Exception as e:
            print(e)
            return jsonify({"Error": "Error Processing Request"})

        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failure"})


@app.route('/QuickDressed/api/v1.0/outfits/get', methods=['GET'])
def get_outfit():
    return jsonify({"Outfit": "Blue Jeans + White Shirt"})


# @app.route('/QuickDressed/api/v1.0/outfits/post', methods=['PUT'])
# def post_outfit():
#     mongo.db.users.insert({})
#     return jsonify({"Outfit": "Blue Jeans + White Shirt"})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


"""
TODO:
- What happens if the user isn't found during the get_outfit req?
"""
if __name__ == "__main__":
    app.run(host='0.0.0.0')

