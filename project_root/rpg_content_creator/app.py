# project_root/rpg_content_creator/app.py

from . import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
