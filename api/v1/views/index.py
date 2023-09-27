#!/usr/bin/python3
"""
Creates a route status in the object app_views
that returns "status": "OK" as a JSON
"""

from os import getenv
from flask import Flask
from api.v1.views import app_views
import json


@app_views.route("/status")
def get_status():
    response = {"status": "OK"}
    return json.dumps(response)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)