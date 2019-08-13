import sqlite3


conn = sqlite3.connect('MyQuotes.db')
curr = conn.cursor()

curr.execute("""create table quotes_tb(
    title text,
    author text, 
    tag text
)""")

conn.commit()
conn.close()