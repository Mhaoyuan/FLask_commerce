from flask import Blueprint

api = Blueprint('api', __name__)

from . import user
from . import auth
from . import address