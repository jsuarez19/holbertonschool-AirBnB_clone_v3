#!/usr/bin/python3
"""
Creates a route status in the object app_views
that returns "status": "OK" as a JSON
"""

from flask import Flask
from flask import jsonify
from api.v1.views import app_views
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models import storage


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def get_status():
    response = {"status": "OK"}
    return jsonify(response)


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
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