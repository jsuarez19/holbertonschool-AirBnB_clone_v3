#!/usr/bin/python3
"""Create a new view for Amenity objects
that handles all default RESTFul API actions"""
from flask import Flask, Blueprint, request, jsonify, abort
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def list_get_amenities():
    """Retrieves the list of all Amenity objects"""

    obj_amenity = []
    for obj in storage.all(Amenity).values():
        obj_amenity.append(obj.to_dict())

    return jsonify(obj_amenity)


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def obj_amenity(amenity_id):
    """Retrieves a Amenity object."""

    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """Deletes a Amenity object."""

    obj_amenity = storage.get(Amenity, amenity_id)
    if obj_amenity is None:
        abort(404)

    storage.delete(obj_amenity)
    storage.save()

    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    """Creates a Amenity"""

    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400

    if "name" not in data:
        return jsonify({"error": "Missing name"}), 400

    new_amenity = Amenity(**data)
    new_amenity.save()

    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def update_amenities(amenity_id):
    """Updates a Amenity object"""

    if not request.is_json:
        abort(400, description='NOt a JSON')

    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    data = request.get_json()
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(Amenity, key, value)

    amenity.save()
    return jsonify(amenity.to_dict()), 200
