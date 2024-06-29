from flask import Blueprint

upload_bp = Blueprint('upload', __name__)

from ...rpg_web_frontend.app.routes.upload_routes import *
