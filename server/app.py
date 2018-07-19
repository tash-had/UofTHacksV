from flask import Flask, jsonify
from pymongo import MongoClient


from flask import abort, make_response, request, url_for
import scraper.n
import base64
import json
import png
# from flask_assistant import Assistant, tell

app = Flask(__name__)
# mongo = PyMongo(app)
client = MongoClient(host='localhost', port=27017)
db = client.data
# client = MongoClient("mongodb://quickdressedadmin:quickdresspassword@cluster0-shard-00-00-qfhms.mongodb.net:27017,cluster0-shard-00-01-qfhms.mongodb.net:27017,cluster0-shard-00-02-qfhms.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
# db = client.users

# assist = Assistant(app)

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


            user_data = {"name": name, "gender":gender, "user_id":"",
                    "previous_matches": [], "worn_outfits": []}
            cloth = {"uuid": uuid, "owner":user_data['name'], "timestamp": timestamp,
                     "image": image, "last_worn_days": 0, "category":"",
                     "web_entities":[], "match":[], "colors":{}}

            # image_64_decode = base64.b64decode(image)
            # image_result = open('hmgo.gif', 'wb')
            # image_result.write(image_64_decode)

            cloth['web_entities'].extend(scraper.n.detect_web(image))
            cloth['colors'].update(scraper.n.detect_properties(image))

            existing_users = db.users.find({"user.name": user_data["name"]}).count()

            if existing_users == 0:
                # user is new
                new_user = {
                    "user": user_data,
                    "clothes": [cloth]
                }
                db.users.insert_one(new_user)

            else:
                db.users.update({"user.name": user_data['name']},
                                {"$push": {'clothes': cloth}})

        except Exception as e:
            print(e)
            return jsonify({"Error": "Error Processing Request"})

        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failure"})


@app.route('/QuickDressed/api/v1.0/outfits/get', methods=['GET'])
def get_outfit():
    return jsonify({"Outfit": "Blue Jeans + White Shirt"})

# @assist.action('get_outfit')
# @app.route('/QuickDressed/api/v1.0/outfits/get', methods=['GET'])
# def get_outfit():
#     speech = 'Microphone check 1, 2 what is this?'
#     return tell(speech)

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

# if os.environ["LOCAL"] == "yes":
#     app.run(host='0.0.0.0', port=8080, debug=True)