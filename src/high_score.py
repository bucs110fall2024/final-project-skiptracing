import sqlite3

def create_connection():
    conn = sqlite3.connect('high_scores.db')
    return conn 

def create_table(conn):
    sql = '''CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                score INTEGER NOT NULL
            )''' # sql command to create a table named scores w two colums, id/score
    try: 
        c = conn.cursor() # create cursor object from conn 
        c.execute(sql)
    except Exception as e: 
        print(e) # catch exceptions 
        
def insert_score(conn, score): 
    sql_check = '''SELECT COUNT(*) FROM scores WHERE score = ?'''
    cur = conn.cursor()
    cur.execute(sql_check, (score,))
    if cur.fetchone()[0] == 0:
        # insert score if it doesn't exist 
        sql = '''INSERT INTO scores(score) VALUES(?)'''
        cur.execute(sql, (score,))
        conn.commit()
        return cur.lastrowid
    else: 
        return None # score already exists 
      
def get_high_scores(conn, limit=3):
    cur = conn.cursor()
    cur.execute("SELECT score FROM scores ORDER BY score DESC LIMIT ?", (limit,))
    rows = cur.fetchall()
    return rows 