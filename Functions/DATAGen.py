from sqlite3 import *
import sqlite3

class Data:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def createTable(self):
        with self.connection:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

    def addUser(self,name,age):
        with self.connection:
            self.cursor.execute('INSERT INTO users(name,age) VALUES (?,?)', (name,age))

    def get_user_list(self):
        with self.connection:
            return self.cursor.execute('SELECT * FROM users').fetchall()

    def get_user(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT name,age FROM users WHERE id = ?', (user_id,)).fetchone()




if __name__ == "__main__":
    db = Data("Data.db")
    db.createTable()
    db.addUser('rferf', 21)
    print(db.get_user_list())
    print(db.get_user(4))