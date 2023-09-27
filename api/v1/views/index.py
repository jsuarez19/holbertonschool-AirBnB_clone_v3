#!/usr/bin/python3
"""
Creates a route status in the object app_views
that returns "status": "OK" as a JSON
"""

from os import getenv
from flask import Flask
from flask import jsonify
from api.v1.views import app_views
import json
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models import storage


@app_views.route("/status")
def get_status():
    response = {"status": "OK"}
    return json.dumps(response), 200, {'Content-Type': 'application/json'}


@app_views.route("/stats")
def stats_objt():
    information = {
            "amenities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)
            }
    return jsonify(information)

if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
