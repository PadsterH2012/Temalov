import sys
import os

from flask import Flask, request, jsonify
from extractor.ai_agent_content_parser import (
    extract_text_from_pdf, extract_names, consolidate_names,
    process_character_details, generate_book_details, get_summary
)
from shared.models.entities import Character
from shared.models.database import db
from extractor.settings import get_setting
from shared.routes.creator_routes import upload_bp
import logging

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../shared')))


def create_app():
    # Initialize Flask app
    app = Flask(__name__, template_folder='extractor/templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/gamedb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configure logging
    logging.basicConfig(level=logging.DEBUG)

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(upload_bp, url_prefix='/upload')

    @app.route('/')
    def home():
        return "Content Creator Home"

    @app.route('/extract/characters', methods=['POST'])
    def characters():
        with app.app_context():
            db.create_all()  # Ensure tables are created
            db.session.commit()
        
        try:
            ollama_url = get_setting('ollama_url', db.session)
            ollama_model = get_setting('ollama_model', db.session)
            app.logger.debug(f"Ollama URL: {ollama_url}")
            app.logger.debug(f"Ollama Model: {ollama_model}")

            if not ollama_url or not ollama_model:
                return "Ollama settings are not configured correctly.", 500

            file = request.files.get('file')
            if not file:
                return "No file uploaded.", 400

            pdf_content = file.read()
            text = extract_text_from_pdf(pdf_content)

            names = extract_names(text)
            consolidated_names = consolidate_names(names)

            book_details_dict = generate_book_details(text, db.session, ollama_url, ollama_model)
            processed_characters = process_character_details(consolidated_names, db.session, book_details_dict, ollama_url, ollama_model)

            return jsonify(processed_characters)
        finally:
            db.session.close()

    @app.route('/extract/quests', methods=['POST'])
    def quests():
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files.get('file')
        if not file or file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        pdf_content = file.read()
        text = extract_text_from_pdf(pdf_content)

        try:
            ollama_url = get_setting('ollama_url', db.session)
            ollama_model = get_setting('ollama_model', db.session)
            summary = get_summary(text, db.session, ollama_url, ollama_model)
            return jsonify({"summary": summary})
        finally:
            db.session.close()

    @app.route('/health')
    def health():
        return "OK", 200

    return app
