#!/usr/bin/python3
"""Create a new view for User object"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from models import storage


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_user():
    """Retrieves the list of all User objects"""
    list_user = []
    for obj in storage.all(User).values():
        list_user.append(obj.to_dict())

    return jsonify(list_user)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def obj_user(user_id):
    """Retrieves a User object"""
    obj_user = storage.get(User, user_id)
    if obj_user is None:
        abort(404)

    return jsonify(obj_user.to_dict())


@app_views.route('/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    storage.delete(user)
    storage.save()

    return jsonify({})


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a User"""
    json_data = request.get_json()
    if json_data is None:
        return jsonify({"error": "Not a JSON"}), 400

    elif 'email' not in json_data:
        return jsonify({"error": "Missing email"}), 400

    elif 'password' not in json_data:
        return jsonify({"error": "Missing password"}), 400

    new_user = User(email=json_data['email'], password=json_data['password'])
    storage.new(new_user)
    storage.save()

    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Updates a User object"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    data = request.get_json()

    if not data:
        abort(400, description='Not a JSON')

    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(user, key, value)

    storage.save()
    return jsonify(user.to_dict()), 200
