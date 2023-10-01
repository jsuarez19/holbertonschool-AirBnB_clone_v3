#!/usr/bin/python3
"""
Creates the variable app that is an instance of Flask
and handles app.teardown_appcontext
"""

from flask import Flask, jsonify
from models import storage
from flask_cors import CORS
from api.v1.views import app_views
from os import getenv



app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, origins="0.0.0.0")


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()


@app.errorhandler(404)
def not_found(error):
    response = jsonify({"error": "Not found"})
    response.status_code = 404
    return response


if __name__ == '__main__':
    try:
        h = "0.0.0.0"
        host = getenv("HBNB_API_HOST") if getenv("HBNB_API_HOST") else h
        port = getenv("HBNB_API_PORT") if getenv("HBNB_API_PORT") else 5000
        app.run(host=host, port=port, threaded=True)
    except Exception as e:
        print(e)
