# project_root/rpg_content_creator/app.py

from flask import Flask
from extractor.app import initialize_extractor

def create_app():
    app = Flask(__name__)
    initialize_extractor(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8001)
