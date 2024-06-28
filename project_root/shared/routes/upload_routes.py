from flask import Blueprint, request, jsonify
import os
import tempfile
import logging
from extractor.ai_agent_content_parser import (
    extract_text_from_pdf, extract_names, consolidate_names,
    process_character_details, generate_book_details, get_setting
)
from shared.models.models import Character, SessionLocal

upload_bp = Blueprint('upload', __name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@upload_bp.route('/api/upload', methods=['POST'])
def upload_api():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file:
        # Save the file temporarily
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, file.filename)
        file.save(temp_path)

        try:
            with open(temp_path, 'rb') as f:
                pdf_content = f.read()
            text = extract_text_from_pdf(pdf_content)
            names = extract_names(text)
            consolidated_names = consolidate_names(names)
            db_session = SessionLocal()
            try:
                ollama_url = get_setting('ollama_url', db_session)
                ollama_model = get_setting('ollama_model', db_session)
                book_details_dict = generate_book_details(text, db_session, ollama_url, ollama_model)
                characters = process_character_details(consolidated_names, db_session, book_details_dict, ollama_url, ollama_model)

                # Add characters to the database
                for char_details in characters:
                    if isinstance(char_details, dict):
                        character = Character()
                        logger.info(f'Character details: {char_details}')
                        character.update_from_dict(char_details)
                        db_session.add(character)
                    else:
                        logger.error(f'Expected dictionary for character details, got {type(char_details)}')

                db_session.commit()  # Commit the session to save data to the database
                logger.info('Characters successfully added to the database.')
                return jsonify({'characters': characters}), 200
            except Exception as e:
                db_session.rollback()  # Rollback in case of error
                logger.error(f'Error during database transaction: {str(e)}')
                return jsonify({'error': str(e)}), 500
            finally:
                db_session.close()  # Ensure the session is closed
                logger.info('Database session closed.')
        finally:
            # Ensure the temporary file is deleted
            os.remove(temp_path)
            logger.info('Temporary file deleted.')
    return jsonify({'error': 'File processing failed'}), 500
