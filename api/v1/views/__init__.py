#!/usr/bin/python3
"""Init"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from .states import *
from .cities import *
from .amenities import *
from .users import *
