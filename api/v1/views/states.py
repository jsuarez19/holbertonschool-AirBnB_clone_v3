#!/usr/bin/python3
"""new view for State objects that handles all default RESTFul API actions"""
from flask import Flask, Blueprint, request, jsonify, abort
from models import storage
from models.state import State


app = Flask(__name__)
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """list of all State objects"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """list of all State objects"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<st_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(st_id):
    """Returns an empty dictionary with the status code 200"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def crete_state():
    """Returns the new State with the status code 201"""
    if not request.is_json:
        abort(400, description='Not a JSON')

    data = request.get_json()
    if 'name' not in data:
        abort(400, description='Missing name')

    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Returns the State object with the status code 200"""
    if not request.is_json:
        abort(400, description='Not a JSON')

    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    data = request.get_json()
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(state, key, value)

    state.save()
    return jsonify(state.to_dict()), 200


if __name__ == '__main__':
    app.register_blueprint(app_views)
    app.run(host='0.0.0.0', port=5000)
