#!/usr/bin/python3
"""Endpoints for handling default RESTful API actions for amenities."""
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models.amenity import Amenity
from models import storage


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """Retrieve the list of amenities."""
    all_amenities = storage.all(Amenity).values()
    list_amenities = [amenity.to_dict() for amenity in all_amenities]
    return jsonify(list_amenities)


@app_views.route('/amenities/<a_id>', methods=['GET'], strict_slashes=False)
def get_amenity(a_id):
    """Retrieve an amenity object by ID."""
    amenity = storage.get(Amenity, a_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<a_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(a_id):
    amenity = storage.get(Amenity, a_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def post_amenity():
    """Create an amenity."""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if 'name' not in data:
        abort(400, description="Missing name")
    instance = Amenity(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/amenities/<am_id>', methods=['PUT'], strict_slashes=False)
def put_amenity(am_id):
    """Update an amenity object."""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    ignore = ['id', 'created_at', 'updated_at']
    amenity = storage.get(Amenity, am_id)
    if not amenity:
        abort(404)
    for key, value in data.items():
        if key not in ignore:
            setattr(amenity, key, value)
    storage.save()
    return make_response(jsonify(amenity.to_dict()), 200)
