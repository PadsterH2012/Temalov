CREATE TABLE IF NOT EXISTS players (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS games (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS player_games (
    player_id INTEGER REFERENCES players(id),
    game_id INTEGER REFERENCES games(id),
    PRIMARY KEY (player_id, game_id)
);

CREATE TABLE IF NOT EXISTS settings (
    id SERIAL PRIMARY KEY,
    key VARCHAR(50) NOT NULL UNIQUE,
    value VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS characters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    sex VARCHAR(10) NOT NULL,
    age VARCHAR(10) NOT NULL,
    traits TEXT NOT NULL,
    behaviors TEXT NOT NULL,
    background TEXT NOT NULL,
    book_title VARCHAR(200),
    author VARCHAR(200),
    dialogue_examples TEXT,
    genre VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS quests (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    objectives TEXT NOT NULL
);
