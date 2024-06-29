from sqlalchemy.orm import Session
from shared.models.entities import Setting
import logging

logger = logging.getLogger('app')

def get_setting(key: str, db: Session):
    logger.debug(f"Fetching setting for key: {key}")
    setting = db.query(Setting).filter_by(key=key).first()
    if setting:
        logger.debug(f"Found setting for key {key}: {setting.value}")
        return setting.value
    logger.debug(f"No setting found for key: {key}")
    return None

def get_ollama_settings(db: Session):
    logger.debug("Fetching Ollama settings")
    ollama_url_setting = db.query(Setting).filter(Setting.key == 'ollama_url').first()
    ollama_model_setting = db.query(Setting).filter(Setting.key == 'ollama_model').first()

    if ollama_url_setting and ollama_model_setting:
        logger.debug(f"Ollama URL: {ollama_url_setting.value}")
        logger.debug(f"Ollama Model: {ollama_model_setting.value}")
        return ollama_url_setting.value, ollama_model_setting.value
    else:
        if not ollama_url_setting:
            logger.debug("Ollama URL setting not found")
        if not ollama_model_setting:
            logger.debug("Ollama Model setting not found")
        return None, None
