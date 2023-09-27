from os import getenv
from flask import Flask
from api.v1.views import app_views
import json


app = Flask(__name__)
app.register_blueprint(app_views)

@app_views.route('/status', methods=['GET'])
def get_status():
    response = {"status": "OK"}
    return json.dumps(response)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)