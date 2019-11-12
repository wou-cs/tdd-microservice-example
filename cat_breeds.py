from flask import Flask, jsonify

api_app = Flask(__name__)


cat_breeds = [
    "Siamese",
    "Bengal",
    "Domestic Shorthair"
]


@api_app.route('/api/cat_breed/')
def cat_breed_index():
    return jsonify(cat_breeds)
