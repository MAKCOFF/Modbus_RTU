import sqlite3


def get_values_from_db():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = """ SELECT value FROM expenses """
        try:
            cursor.execute(query)
        except sqlite3.DatabaseError as err:
            print("Ошибка:", err)
        values = []
        for i in cursor:
            value = i[0]
            values.append(value)
    return values


def change_values_in_db(start):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        try:
            query = f'UPDATE start SET value = {start}'
        except sqlite3.DatabaseError as err:
            print("Ошибка:", err)
        cursor.execute(query)
        db.commit()


def get_stop_from_db():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = """ SELECT value FROM start """
        try:
            cursor.execute(query)
        except sqlite3.DatabaseError as err:
            print("Ошибка:", err)
        for i in cursor:
            value = i[0]
    return value


def insert_value_to_db():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = """ INSERT INTO start (value) VALUES (1) """
        cursor.execute(query)
        db.commit()


# def create_table_in_db():
#     with sqlite3.connect('database.db') as db:
#         cursor = db.cursor()
#         query = """ CREATE TABLE IF NOT EXISTS start (value INTEGER) """
#         cursor.execute(query)
#         db.commit()

# change_values_in_db(1)
# insert_value_to_db()
# query = """ INSERT INTO expenses (id, value) VALUES """
# query = """ CREATE TABLE IF NOT EXISTS expenses(id INTEGER, value INTEGER) """
