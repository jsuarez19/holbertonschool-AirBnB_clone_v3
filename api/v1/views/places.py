#!/usr/bin/python3
"""Create a new view for Place objects."""
from . import app_views
from flask import request, jsonify, abort, make_response
from models import storage
from models.city import City
from models.place import Place
from models.user import User


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def get_list_place(city_id):
    """Retrieves the list of all Place objects of a City."""
    city = storage.get(City, city_id)

    if not city:
        abort(404)

    list_place = [place.to_dict() for place in city.places]
    return jsonify(list_place)


@app_views.route('/places/<place_id>',
                 methods=['GET'], strict_slashes=False)
def obj_place(place_id):
    """Retrieves a Place object."""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """Deletes a Place object."""
    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    storage.delete(place)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """Creates a Place"""
    data = request.get_json()

    if not data:
        abort(400, description="Not a JSON")

    city = storage.get(City, city_id)
    if not city:
        abort(404)
    if 'name' not in data:
        abort(400, description="Missin name")
    if 'user_id' not in data:
        abort(400, description="Missing user_id")

    user = storage.get(User, data['user_id'])
    if not user:
        abort(404)

    new_istancia = Place(**data)
    new_istancia.city_id = city_id
    new_istancia.save()

    return make_response(jsonify(new_istancia.to_dict()), 201)


@app_views.route('/places/<place_id>',
                 methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """Updates a Place object."""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    ignore_keys = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(place, key, value)
    storage.save()

    return jsonify(place.to_dict()), 200
