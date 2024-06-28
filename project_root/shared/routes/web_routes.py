from flask import Blueprint

main_bp = Blueprint('main', __name__)
settings_bp = Blueprint('settings', __name__)
auth_bp = Blueprint('auth', __name__)
api_bp = Blueprint('api', __name__)

from .main_routes import *
from .settings_routes import *
from .auth_routes import *
from .api_routes import *
