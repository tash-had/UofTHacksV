from flask import Flask, jsonify
from flask_pymongo import PyMongo

from flask import abort, make_response, request, url_for

app = Flask(__name__)
mongo = PyMongo(app)


@app.route('/', methods=["GET", "POST"])
def receive_outfit():
    print('hey')
    if request.method == "POST":
        print(request.form['data'])
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failure"})


@app.route('/QuickDressed/api/v1.0/outfits/get', methods=['GET'])
def get_outfit():
    return jsonify({"Outfit": "Blue Jeans + White Shirt"})


@app.route('/QuickDressed/api/v1.0/outfits/post', methods=['PUT'])
def post_outfit():
    mongo.db.users.insert({})
    return jsonify({"Outfit": "Blue Jeans + White Shirt"})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


"""
TODO:
- What happens if the user isn't found during the get_outfit req?
"""
if __name__ == "__main__":
    app.run(host='0.0.0.0')

