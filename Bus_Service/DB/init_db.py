import sqlite3

connection=sqlite3.connect('bus.db')

with open('DB/schema.sql') as f:
    connection.executescript(f.read())

cursor=connection.cursor()

connection.commit()
connection.close()