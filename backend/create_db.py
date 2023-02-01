import sqlite3

con = sqlite3.connect('todolist1.db')
cursor = con.cursor()

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    description TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0
)
""")
con.commit()
