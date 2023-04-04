import sqlite3
from sqlite3 import Error

DATABASE_FILE = "database.db"


def create_connection():
    """Create a database connection to SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        print(f"Connected to SQLite version {sqlite3.version}")
    except Error as e:
        print(e)

    return conn