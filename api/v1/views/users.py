#!/usr/bin/python3
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models.user import User
from models import storage


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_user():
    list_user = []
    for obj in storage.all(User).values():
        list_user.append(obj.to_dict())

    return jsonify(list_user)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def obj_user(user_id):
    obj_user = storage.get(User, user_id)
    if obj_user is None:
        abort(404)

    return jsonify(obj_user.to_dict())


@app_views.route('/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    storage.delete(user)
    storage.save()

    return jsonify({})

