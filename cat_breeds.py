from flask import Flask

api_app = Flask(__name__)


@api_app.route('/')
def index():
    return ""
