# AirBnB Clone - The Console
The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.
This project is a Python-based RESTful API developed using Flask and SQLAlchemy to manage a database of objects. The API allows for CRUD (Create, Read, Update, Delete) operations on various types of objects, such as States, Cities, Amenities, Users, Places, and Reviews.

#### Functionalities of this command interpreter:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [Getting Started](#getting-started)
* [File Descriptions](#file-descriptions)
* [Features](#features)
* [API Documentation](#api-documentation)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## Installation
* Clone this repository: `git clone "https://github.com/alexaorrico/AirBnB_clone.git"`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## Getting Started
To get started with the API, follow these steps:

1. Create a virtual environment (optional but recommended).
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Configure environment variables such as `HBNB_API_HOST` and `HBNB_API_PORT` if needed.
4. Run the API using the command `python -m api.v1.app`.

The API will be accessible at `http://<HOST>:<PORT>/api/v1/`.

## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console current supports:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 

#### `api/` directory contains the RESTful API for the project:

#### `/v1` directory contains Version 1 of the API:
[app.py](/api/v1/app.py) - Entry point for the API with Flask initialization and route registration.

#### `/views` directory contains view files for different object types:
[amenities.py](api/v1/views/amenities.py) This module contains views for handling Amenity objects in the API
* `def list_get_amenities()` - Retrieves the list of all Amenity objects
* `def get_amenity(amenity_id)` - Retrieves a specific Amenity object by ID
* `delete_amenity(amenity_id)` - Deletes a specific Amenity object by ID
* `def create_amenity()` - Creates a new Amenity object
* `def update_amenity(amenity_id)` - Updates a specific Amenity object by ID

[cities.py](api/v1/views/cities.py) This module contains views for handling City objects in the API
* `def list_state_cities(state_id)` - Returns a list of cities in a state
* `def get_list_city(city_id)` - Retrieves a City object by ID
* `def delete_city(city_id)` - Deletes a City object by ID
* `def create_city(state_id)` - Creates a City object in a state
* `def update_city(city_id)` - Updates a City object by ID

[index.py](api/v1/views/index.py) This module contains views for handling the /status and /stats routes in the API
* `def get_status()` - Returns a JSON response with "status": "OK"
* `def stats_objt()` - Retrieves statistics about various objects in the system, including the counts of amenities, cities, places, reviews, states, and users.

[places_reviews.py](api/v1/views/places_reviews.py) This module contains views for handling Review objects in the API
* `def get_list_reviews(place_id)` - Retrieves the list of all Review objects of a Place
* `def obj_review(review_id)` - Retrieves a specific Review object by ID
* `def delete_review(review_id)` - Deletes a specific Review object by ID
* `def create_review(place_id)` - Creates a new Review object associated with a Place
* `def update_review(review_id)` -  Updates a specific Review object by ID

[places.py](api/v1/views/places.py) This module contains views for handling Place objects in the API
* `def get_list_place(city_id)` - Retrieves the list of all Place objects of a City
* `def obj_place(place_id)` - Retrieves a Place object
* `def delete_place(place_id)` - Deletes a Place object
* `def create_place(city_id)` - Creates a Place
* `def update_place(place_id)` - Updates a Place object

[states.py](api/v1/views/states.py) This module contains views for handling State objects in the API
* `def get_states()` - Retrieves a list of all State objects
* `def get_state(state_id)` - Retrieves a specific State object by ID
* `def delete_state(st_id)` - Deletes a State object and returns an empty dictionary with the status code 200
* `def crete_state()` - Creates a new State and returns it with the status code 201
* `def update_state(state_id)` - Updates a State object and returns it with the status code 200

[api/v1/views/users.py](api/v1/views/users.py) This module contains views for handling User objects in the API.

* `def list_user()` - Retrieves the list of all User objects
* `def obj_user(user_id)` - Retrieves a specific User object by ID
* `def delete_user(user_id)` - Deletes a User object
* `def create_user()` - Creates a new User
* `def update_user(user_id)` - Updates a User object

#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

#### `/models/engine` directory contains File Storage class that handles JASON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* ` def reload(self)` -  deserializes the JSON file to __objects

#### `/tests` directory contains all unit test cases for this project:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes
TestBaseModelDocs class:
* `def setUpClass(cls)`- Set up for the doc tests
* `def test_pep8_conformance_base_model(self)` - Test that models/base_model.py conforms to PEP8
* `def test_pep8_conformance_test_base_model(self)` - Test that tests/test_models/test_base_model.py conforms to PEP8
* `def test_bm_module_docstring(self)` - Test for the base_model.py module docstring
* `def test_bm_class_docstring(self)` - Test for the BaseModel class docstring
* `def test_bm_func_docstrings(self)` - Test for the presence of docstrings in BaseModel methods

TestBaseModel class:
* `def test_is_base_model(self)` - Test that the instatiation of a BaseModel works
* `def test_created_at_instantiation(self)` - Test created_at is a pub. instance attribute of type datetime
* `def test_updated_at_instantiation(self)` - Test updated_at is a pub. instance attribute of type datetime
* `def test_diff_datetime_objs(self)` - Test that two BaseModel instances have different datetime objects

[/test_models/test_amenity.py](/tests/test_models/test_amenity.py) - Contains the TestAmenityDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_amenity(self)` - Test that models/amenity.py conforms to PEP8
* `def test_pep8_conformance_test_amenity(self)` - Test that tests/test_models/test_amenity.py conforms to PEP8
* `def test_amenity_module_docstring(self)` - Test for the amenity.py module docstring
* `def test_amenity_class_docstring(self)` - Test for the Amenity class docstring

[/test_models/test_city.py](/tests/test_models/test_city.py) - Contains the TestCityDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_city(self)` - Test that models/city.py conforms to PEP8
* `def test_pep8_conformance_test_city(self)` - Test that tests/test_models/test_city.py conforms to PEP8
* `def test_city_module_docstring(self)` - Test for the city.py module docstring
* `def test_city_class_docstring(self)` - Test for the City class docstring

[/test_models/test_file_storage.py](/tests/test_models/test_file_storage.py) - Contains the TestFileStorageDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_file_storage(self)` - Test that models/file_storage.py conforms to PEP8
* `def test_pep8_conformance_test_file_storage(self)` - Test that tests/test_models/test_file_storage.py conforms to PEP8
* `def test_file_storage_module_docstring(self)` - Test for the file_storage.py module docstring
* `def test_file_storage_class_docstring(self)` - Test for the FileStorage class docstring

[/test_models/test_place.py](/tests/test_models/test_place.py) - Contains the TestPlaceDoc class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_place(self)` - Test that models/place.py conforms to PEP8.
* `def test_pep8_conformance_test_place(self)` - Test that tests/test_models/test_place.py conforms to PEP8.
* `def test_place_module_docstring(self)` - Test for the place.py module docstring
* `def test_place_class_docstring(self)` - Test for the Place class docstring

[/test_models/test_review.py](/tests/test_models/test_review.py) - Contains the TestReviewDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_review(self)` - Test that models/review.py conforms to PEP8
* `def test_pep8_conformance_test_review(self)` - Test that tests/test_models/test_review.py conforms to PEP8
* `def test_review_module_docstring(self)` - Test for the review.py module docstring
* `def test_review_class_docstring(self)` - Test for the Review class docstring

[/test_models/state.py](/tests/test_models/test_state.py) - Contains the TestStateDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_state(self)` - Test that models/state.py conforms to PEP8
* `def test_pep8_conformance_test_state(self)` - Test that tests/test_models/test_state.py conforms to PEP8
* `def test_state_module_docstring(self)` - Test for the state.py module docstring
* `def test_state_class_docstring(self)` - Test for the State class docstring

[/test_models/user.py](/tests/test_models/test_user.py) - Contains the TestUserDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_user(self)` - Test that models/user.py conforms to PEP8
* `def test_pep8_conformance_test_user(self)` - Test that tests/test_models/test_user.py conforms to PEP8
* `def test_user_module_docstring(self)` - Test for the user.py module docstring
* `def test_user_class_docstring(self)` - Test for the User class docstring

## Features

The project includes the following key features:

- **DBStorage and FileStorage Update**: Changes have been made to the `DBStorage` and `FileStorage` classes to add two new methods:
  1. `get(self, cls, id)`: This method allows you to retrieve an object by its ID and class. If the object is not found, it returns `None`.
  2. `count(self, cls=None)`: This method allows you to count the number of objects in storage that match a given class. If no class is provided, it returns the count of all objects in storage.

- **RESTful API**: A RESTful API has been implemented with multiple endpoints for interacting with stored data. Endpoints include operations for listing, retrieving, creating, updating, and deleting objects of different types.

- **Error Handling**: Error handling has been implemented, including formatted JSON responses for 404 (Not Found) and 400 (Bad Request) errors.

- **CORS (Cross-Origin Resource Sharing)**: Preliminary CORS handling has been configured to allow requests from any origin (0.0.0.0). This should be updated for production.

## API Documentation
This documentation provides details on the available endpoints and their functionality in the API.

### Amenity Endpoints

#### Retrieve All Amenities
- **URL:** `/api/v1/amenities`
- **Method:** `GET`
- **Description:** Retrieves a list of all Amenity objects.
- **Response:** JSON array containing Amenity objects.

#### Retrieve Amenity by ID
- **URL:** `/api/v1/amenities/<amenity_id>`
- **Method:** `GET`
- **Description:** Retrieves a specific Amenity object by ID.
- **Response:** JSON representation of the Amenity object.

#### Delete Amenity by ID
- **URL:** `/api/v1/amenities/<amenity_id>`
- **Method:** `DELETE`
- **Description:** Deletes a specific Amenity object by ID.

#### Create Amenity
- **URL:** `/api/v1/amenities`
- **Method:** `POST`
- **Description:** Creates a new Amenity object.
- **Request Body:** JSON representation of the new Amenity.
- **Response:** JSON representation of the newly created Amenity.

#### Update Amenity by ID
- **URL:** `/api/v1/amenities/<amenity_id>`
- **Method:** `PUT`
- **Description:** Updates a specific Amenity object by ID.
- **Request Body:** JSON representation of the updated Amenity.
- **Response:** JSON representation of the updated Amenity.

### City Endpoints

#### Retrieve Cities in a State
- **URL:** `/api/v1/states/<state_id>/cities`
- **Method:** `GET`
- **Description:** Retrieves a list of cities in a specific State.
- **Response:** JSON array containing City objects.

#### Retrieve City by ID
- **URL:** `/api/v1/cities/<city_id>`
- **Method:** `GET`
- **Description:** Retrieves a specific City object by ID.
- **Response:** JSON representation of the City object.

#### Delete City by ID
- **URL:** `/api/v1/cities/<city_id>`
- **Method:** `DELETE`
- **Description:** Deletes a specific City object by ID.

#### Create City
- **URL:** `/api/v1/states/<state_id>/cities`
- **Method:** `POST`
- **Description:** Creates a new City object within a State.
- **Request Body:** JSON representation of the new City.
- **Response:** JSON representation of the newly created City.

#### Update City by ID
- **URL:** `/api/v1/cities/<city_id>`
- **Method:** `PUT`
- **Description:** Updates a specific City object by ID.
- **Request Body:** JSON representation of the updated City.
- **Response:** JSON representation of the updated City.

### Status and Statistics Endpoints

#### Check API Status
- **URL:** `/api/v1/status`
- **Method:** `GET`
- **Description:** Returns the status of the API as "OK."
- **Response:** JSON with "status" field set to "OK."

#### Get API Statistics
- **URL:** `/api/v1/stats`
- **Method:** `GET`
- **Description:** Returns statistics on various data models in the API.
- **Response:** JSON object with counts of Amenities, Cities, Places, Reviews, States, and Users.

### Review Endpoints

#### Retrieve Reviews for a Place
- **URL:** `/api/v1/places/<place_id>/reviews`
- **Method:** `GET`
- **Description:** Retrieves a list of all Review objects associated with a Place.
- **Response:** JSON array containing Review objects.

#### Retrieve Review by ID
- **URL:** `/api/v1/reviews/<review_id>`
- **Method:** `GET`
- **Description:** Retrieves a specific Review object by ID.
- **Response:** JSON representation of the Review object.

#### Delete Review by ID
- **URL:** `/api/v1/reviews/<review_id>`
- **Method:** `DELETE`
- **Description:** Deletes a specific Review object by ID.

#### Create Review
- **URL:** `/api/v1/places/<place_id>/reviews`
- **Method:** `POST`
- **Description:** Creates a new Review object associated with a Place.
- **Request Body:** JSON representation of the new Review.
- **Response:** JSON representation of the newly created Review.

#### Update Review by ID
- **URL:** `/api/v1/reviews/<review_id>`
- **Method:** `PUT`
- **Description:** Updates a specific Review object by ID.
- **Request Body:** JSON representation of the updated Review.
- **Response:** JSON representation of the updated Review.

### User Endpoints

#### Retrieve All Users
- **URL:** `/api/v1/users`
- **Method:** `GET`
- **Description:** Retrieves a list of all User objects.
- **Response:** JSON array containing User objects.

#### Retrieve User by ID
- **URL:** `/api/v1/users/<user_id>`
- **Method:** `GET`
- **Description:** Retrieves a specific User object by ID.
- **Response:** JSON representation of the User object.

#### Delete User by ID
- **URL:** `/api/v1/users/<user_id>`
- **Method:** `DELETE`
- **Description:** Deletes a specific User object by ID.

#### Create User
- **URL:** `/api/v1/users`
- **Method:** `POST`
- **Description:** Creates a new User object.
- **Request Body:** JSON representation of the new User.
- **Response:** JSON representation of the newly created User.

#### Update User by ID
- **URL:** `/api/v1/users/<user_id>`
- **Method:** `PUT`
- **Description:** Updates a specific User object by ID.
- **Request Body:** JSON representation of the updated User.
- **Response:** JSON representation of the updated User.

## Examples of use
```
vagrantAirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
```

## Bugs
No known bugs at this time. 

## Authors
Alexa Orrico - [Github](https://github.com/alexaorrico) / [Twitter](https://twitter.com/alexa_orrico)  
Jennifer Huang - [Github](https://github.com/jhuang10123) / [Twitter](https://twitter.com/earthtojhuang)
Jose Suarez - [Github](https://github.com/jsuarez19)
Yerti Mosqueira - [Github](https://github.com/yerti)

Second part of Airbnb: Joann Vuong
## License
Public Domain. No copy write protection. 


