import sqlite3
# these all need docstrings. 

class HighScore: 
    
    def __init__(self, db_name='high_scores.db'):
        """
        Initializes HighScore class with a connection to the database 
        Creates the scores table if it does not exist. 
        
        Args: 
            db_name(str): The name of the database file. Defaults to 'high_scores.db'
        """
        self.conn = self.create_connection(db_name)
        self.create_table()
    
    def create_connection(self, db_name):
        """
        Creates a connection to the SQLite database. 

        Args:
            db_name (str): The name of the database file. 

        Returns:
            sqlite3.Connection: A connection object to the SQLite database. 
        """
        conn = sqlite3.connect(db_name)
        return conn 

    def create_table(self):
        """
        Creates the scores table in the SQLite database if it does not exist
        """
        sql = '''CREATE TABLE IF NOT EXISTS scores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    score INTEGER NOT NULL
                )''' # sql command to create a table named scores w two colums, id/score
        try: 
            c = self.conn.cursor() # create cursor object from conn 
            c.execute(sql)
        except Exception as e: 
            print(e) # catch exceptions 
            
    def insert_score(self, score): 
        """
        Inserts a new score into the database if it does not already exist. 

        Args:
            score (int): The score to be inserted. 

        Returns:
            int = The id of the inserted row, or None if the score already exists 
        """
        sql_check = '''SELECT COUNT(*) FROM scores WHERE score = ?'''
        cur = self.conn.cursor()
        cur.execute(sql_check, (score,))
        if cur.fetchone()[0] == 0:
            # insert score if it doesn't exist 
            sql = '''INSERT INTO scores(score) VALUES(?)'''
            cur.execute(sql, (score,))
            self.conn.commit()
            return cur.lastrowid
        else: 
            return None # score already exists 
        
    def get_high_scores(self, limit=3):
        """
        Retrieves the top high scores from the database. 

        Args:
            limit (int): The number of high scores to receive. Defaults to 3.

        Returns:
            list: A list of tuples containing the high scores. 
        """
        cur = self.conn.cursor()
        cur.execute("SELECT score FROM scores ORDER BY score DESC LIMIT ?", (limit,))
        rows = cur.fetchall()
        return rows 