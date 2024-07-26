from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from app import db



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db.engine)

class Player(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Player {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

class Game(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Game {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }

class PlayerGame(db.Model):
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    game_id = Column(Integer, ForeignKey('game.id'), nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)

    player = relationship('Player', backref=db.backref('games', lazy=True))
    game = relationship('Game', backref=db.backref('players', lazy=True))

    def __repr__(self):
        return f'<PlayerGame {self.player_id} - {self.game_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'game_id': self.game_id,
            'joined_at': self.joined_at.isoformat()
        }

class Character(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    sex = Column(String(10), nullable=False)
    age = Column(String(10), nullable=False)
    traits = Column(Text, nullable=False)
    behaviors = Column(Text, nullable=False)
    background = Column(Text, nullable=False)
    book_title = Column(String(200), nullable=True)
    author = Column(String(200), nullable=True)
    dialogue_examples = Column(Text, nullable=True)
    genre = Column(String(100), nullable=True)

    def __repr__(self):
        return f'<Character {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'sex': self.sex,
            'age': self.age,
            'traits': self.traits,
            'behaviors': self.behaviors,
            'background': self.background,
            'book_title': self.book_title,
            'author': self.author,
            'dialogue_examples': self.dialogue_examples,
            'genre': self.genre
        }

class Quest(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    objectives = Column(Text, nullable=False)

    def __repr__(self):
        return f'<Quest {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'objectives': self.objectives
        }

class Setting(db.Model):
    id = Column(Integer, primary_key=True)
    key = Column(String(100), unique=True, nullable=False)
    value = Column(Text, nullable=False)

    def __repr__(self):
        return f'<Setting {self.key}>'

    def to_dict(self):
        return {
            'id': self.id,
            'key': self.key,
            'value': self.value
        }
