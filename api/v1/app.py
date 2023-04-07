#!/usr/bin/python3
""" A flask app to server the API
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS
from flasgger import Swagger


app = Flask(__name__)
swagger = Swagger(app)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": " 0.0.0.0"}})


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


# 404 error handler
@app.errorhandler(404)
def not_found(error):
    """Returns a JSON-formatted 404 status code response"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True, debug=True)
