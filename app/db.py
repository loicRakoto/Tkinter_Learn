import sqlite3
from app.config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            firstname TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            isbn TEXT UNIQUE
        )
    """)
    
    conn.commit()
    conn.close()

def add_user(email, name, firstname, password):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (email, name, firstname, password) VALUES (?, ?, ?, ?)", (email, name, firstname, password))
        conn.commit()
    except sqlite3.IntegrityError:
        pass 
    conn.close()

def check_user(email, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    result = cur.fetchone()
    conn.close()
    return result is not None

def get_all_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, name, firstname, email, password 
        FROM users
        WHERE email != 'admin@gmail.com'
    """)
    users = cur.fetchall()
    conn.close()
    return users


def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()

def update_user(user_id, email, name, firstname, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET email=?, name=?, firstname=?, password=? WHERE id=?", (email, name, firstname, password, user_id))
    conn.commit()
    conn.close()