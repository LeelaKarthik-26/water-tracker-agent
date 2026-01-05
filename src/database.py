import sqlite3
from datetime import datetime

DB_NAME = "water_tracker.db"

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wate_intake(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            intake_ml INTERGER,
            data TEXT
        )               
    """)
    conn.commit()
    conn.close()
    

def log_intake(user_id, intake_ml):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    date_today = datetime.today().strftime('%Y-%m-%d')
    cursor.execute("INSERT INTO water_intake (user_id, intake_ml, date) VALUES(?,?,?)", (user_id, intake_ml, date_today))
    conn.commit()
    conn.close()
    
def get_intake_history(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT intake_ml, data from water_intake WHERE user_id=?", user_id)
    records = cursor.fetchall()
    conn.close()
    return records

create_tables()