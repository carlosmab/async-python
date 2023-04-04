import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create the books table
c.execute('''CREATE TABLE books
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT,
              author_id INTEGER,
              year INTEGER,
              description TEXT)''')

# Create the authors table
c.execute('''CREATE TABLE authors
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              bio TEXT)''')

conn.commit()
conn.close()