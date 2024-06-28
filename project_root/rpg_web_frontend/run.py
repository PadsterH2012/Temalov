import sys
import os

# Add the 'shared' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'shared'))

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
