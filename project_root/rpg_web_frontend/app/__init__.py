from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import logging

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_class='app.config.Config'):
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    
    # Set up logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.debug('Creating Flask app')

    # Log configuration details
    logger.debug(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    
    # Import and register blueprints
    try:
        from shared.routes.api_routes import api_bp
        from shared.routes.auth_routes import auth_bp
        from shared.routes.settings_routes import settings_bp
        from shared.routes.web_routes import main_bp
        from app.routes.upload_routes import upload_bp

        app.register_blueprint(auth_bp, url_prefix='/auth')
        app.register_blueprint(settings_bp, url_prefix='/settings')
        app.register_blueprint(main_bp, url_prefix='/')
        app.register_blueprint(api_bp, url_prefix='/api')
        app.register_blueprint(upload_bp, url_prefix='/upload')
    except Exception as e:
        logger.error(f'Error importing blueprints: {e}')
        raise
    
    # Import models after db is initialized to avoid circular imports
    with app.app_context():
        try:
            from shared.models.entities import Player, Game, PlayerGame, Character, Quest
            db.create_all()  # Ensure all tables are created
        except Exception as e:
            logger.error(f'Error importing models: {e}')
            raise

    @login_manager.user_loader
    def load_user(user_id):
        return Player.query.get(int(user_id))
    
    return app
