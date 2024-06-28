CREATE TABLE IF NOT EXISTS player (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS player_game (
    player_id INTEGER REFERENCES player(id),
    game_id INTEGER REFERENCES game(id),
    PRIMARY KEY (player_id, game_id)
);

CREATE TABLE IF NOT EXISTS setting (
    id SERIAL PRIMARY KEY,
    key VARCHAR(50) NOT NULL UNIQUE,
    value VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS character (
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

CREATE TABLE IF NOT EXISTS quest (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    objectives TEXT NOT NULL
);
