# project_root/rpg_web_frontend/app/config.py
import tempfile

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://rpg_user:rpg_pass@rpg_database:5432/rpg'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
    UPLOAD_FOLDER = tempfile.gettempdir()
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Max upload size: 16MB