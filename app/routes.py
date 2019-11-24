from app import app
from flask import request
from . import storage


@app.route("/")
def index():
    return "Hello mr and welcome"


@app.route("/blob", methods=["PUT"])
def blob_put():
    file_id = storage.put(request.stream)
    return f"{file_id}/n"


@app.route("/blob/<file_id>", methods=["GET"])
def blob_get(file_id):
    return storage.get(file_id)
