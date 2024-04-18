#!/usr/bin/python3
"""Index route."""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route("/status", methods=["GET"])
def status():
    """Return the API status."""
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=["GET"])
def stats():
    """
    Retrieves the number of each object by type.
    """
    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User",
    }
    counts = {cls: storage.count(classes[cls]) for cls in classes}
    return jsonify(counts)
