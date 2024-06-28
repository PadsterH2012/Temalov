# project_root/shared/routes/api_routes.py

import logging
from flask import Blueprint, jsonify
from shared.models.entities import db, Character, Quest

api_bp = Blueprint('api', __name__)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@api_bp.route('/api/characters', methods=['GET'])
def list_characters():
    characters = Character.query.all()
    logger.debug(f"Retrieved characters: {characters}")
    return jsonify([char.to_dict() for char in characters])

@api_bp.route('/api/quests', methods=['GET'])
def list_quests():
    quests = Quest.query.all()
    logger.debug(f"Retrieved quests: {quests}")
    return jsonify([quest.to_dict() for quest in quests])
