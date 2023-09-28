#!/usr/bin/python3
"""
Creates the variable app that is an instance of Flask
and handles app.teardown_appcontext
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
import json


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()

@app.errorhandler(404)
def not_found(error):
    response_data = {"error": "Not found"}
    response = app.response_class(
        response=json.dumps(response_data),
        status=404,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
