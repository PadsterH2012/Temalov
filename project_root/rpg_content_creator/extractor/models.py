# Remove the old SQLAlchemy setup and use the models from the shared models directory
from shared.models.entities import Quest, Setting, Character
from shared.models.database import db
