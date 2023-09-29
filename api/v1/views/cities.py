#!/usr/bin/python3
"""create a new view for City objects that
handles all default RESTFul API actions"""
from flask import Blueprint, Flask, request, jsonify, abort
from models import storage
from models.city import City
from models.state import State


app = Flask(__name__)
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def list_state_cities(state_id):
    """returns a list of all cities in a state"""
    cities_list = []
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    for city in state.cities:
        cities_list.append(city.to_dict())
    return jsonify(cities_list)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def object_city(city_id):
    """returns information about a city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """removes a city and returns an empty array"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    storage.delete(city)
    storage.save()

    return jsonify({})


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """create a new city"""
    city = storage.get(State, state_id)
    if not city:
        abort(404)
    if not request.get_json():
        abort(404, description='Not a JSON')
    if 'name' not in request.get_json():
        abort(400, description='Missing name')

    data = request.get_json()
    new_city = City(**data)
    new_city.state_id = state_id
    new_city.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """update city data"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    if not request.get_json():
        abort(400, description='Not a JSON')

    ignore = ['id', 'state_id', 'created_at', 'updated_at']

    data = request.get_json()
    for k, v in data.items():
        if k not in ignore:
            setattr(city, k, v)
        storage.save()

    return jsonify(city.to_dict()), 200


if __name__ == '__main__':
    app.register_blueprint(app_views)
    app.run(host='0.0.0.0', port=5000)
