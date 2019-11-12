from flask import Flask, jsonify

api_app = Flask(__name__)


@api_app.route('/api/cat_breed/')
def cat_breed_index():
    return jsonify([1, 2, 3])
