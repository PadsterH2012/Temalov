import unittest
import psycopg2

class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.conn = psycopg2.connect(
            dbname="rpg",
            user="rpg_user",
            password="rpg_pass",
            host="rpg_database",  # Use the service name defined in docker-compose.yml
            port="5432"
        )
        self.cur = self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_insert_player(self):
        self.cur.execute("INSERT INTO players (username, password) VALUES ('testuser', 'testpass');")
        self.conn.commit()
        self.cur.execute("SELECT * FROM players WHERE username='testuser';")
        player = self.cur.fetchone()
        self.assertIsNotNone(player)

    def test_insert_game(self):
        self.cur.execute("INSERT INTO games (name, description) VALUES ('testgame', 'description');")
        self.conn.commit()
        self.cur.execute("SELECT * FROM games WHERE name='testgame';")
        game = self.cur.fetchone()
        self.assertIsNotNone(game)

if __name__ == '__main__':
    unittest.main()
