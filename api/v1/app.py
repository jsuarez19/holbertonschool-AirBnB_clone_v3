#!/usr/bin/python3
"""
Creates the variable app that is an instance of Flask
and handles app.teardown_appcontext
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)

# Define a method to handle teardown_appcontext
@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)