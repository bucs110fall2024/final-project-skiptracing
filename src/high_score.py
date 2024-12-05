import sqlite3
# these all need docstrings. 

class HighScore: 
    
    def __init__(self, db_name='high_scores.db'):
        """
        sfiuahdifalfdkjaldfjkhaskdfhlajdfkfs
        """
        self.conn = self.create_connection(db_name)
        self.create_table()
    
    def create_connection(self, db_name):
        conn = sqlite3.connect(db_name)
        return conn 

    def create_table(self):
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
        cur = self.conn.cursor()
        cur.execute("SELECT score FROM scores ORDER BY score DESC LIMIT ?", (limit,))
        rows = cur.fetchall()
        return rows 