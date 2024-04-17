#!/usr/bin/python3
"""Index route."""

from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=["GET"])
def status():
    """Return the API status."""
    return jsonify({"status": "OK"})
