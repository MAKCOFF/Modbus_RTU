import sqlite3


def get_values_from_db():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = """ SELECT value FROM expenses """
        cursor.execute(query)
        values = []
        for i in cursor:
            value = i[0]
            values.append(value)
    return values


def insert_value_to_db():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = """ INSERT INTO start (value) VALUES (1) """
        cursor.execute(query)
        db.commit()


def create_table_in_db():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = """ CREATE TABLE IF NOT EXISTS start (value INTEGER) """
        cursor.execute(query)
        db.commit()


def change_values_in_db(start):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = f'UPDATE start SET value = {start}'
        cursor.execute(query)
        db.commit()


def get_stop_from_db():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = """ SELECT value FROM start """
        cursor.execute(query)
        for i in cursor:
            value = i[0]
    return value


# change_values_in_db(1)
# insert_value_to_db()
# db.commit()
# query = """ INSERT INTO expenses (id, value) VALUES """
# query = """ CREATE TABLE IF NOT EXISTS expenses(id INTEGER, value INTEGER) """
