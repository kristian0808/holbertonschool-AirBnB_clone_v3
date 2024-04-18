#!/usr/bin/python3
"""
The `app_views` module contains the views for the API's version 1.

It imports all the views from the `index.py` module and defines a Blueprint
`app_views` with the URL prefix `/api/v1`.

"""

from api.v1.views import *
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
