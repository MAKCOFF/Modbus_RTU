import sqlite3

"""
ДБ использется для разделения потоков управления приложение
в expenses хранятся значения для записи в формате int (id, value)
id считается с 0
в start хранится int value
"""


def get_values_from_db(count=4):
    """
    :param count (default=4) сколько значений забрать с базы
    для записи в регистры
    """
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = f'SELECT value FROM expenses WHERE id < {count}'
        try:
            cursor.execute(query)
        except sqlite3.DatabaseError as err:
            print("Ошибка:", err)
        values = []
        for i in cursor:
            value = i[0]
            values.append(value)
    return print(values)


def change_values_in_db(item, count=0):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        try:
            query = f'UPDATE expenses SET value = {item} WHERE id = {count}'
        except sqlite3.DatabaseError as err:
            print("Ошибка:", err)
        cursor.execute(query)
        db.commit()


def change_value_in_db(start):
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


def insert_values_to_db():
    """
    Добавляет 10 новых значение в таблицу.
    !!! Перед вызовом проверить текущую таблицу,
    поменять id по порядку добавления
    """
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        querys = dict(
            query0=""" INSERT INTO expenses (id, value) VALUES (30, 943) """,
            query1=""" INSERT INTO expenses (id, value) VALUES (31, 943) """,
            query2=""" INSERT INTO expenses (id, value) VALUES (32, 943) """,
            query3=""" INSERT INTO expenses (id, value) VALUES (33, 943) """,
            query4=""" INSERT INTO expenses (id, value) VALUES (34, 943) """,
            query5=""" INSERT INTO expenses (id, value) VALUES (35, 943) """,
            query6=""" INSERT INTO expenses (id, value) VALUES (36, 943) """,
            query7=""" INSERT INTO expenses (id, value) VALUES (37, 943) """,
            query8=""" INSERT INTO expenses (id, value) VALUES (38, 943) """,
            query9=""" INSERT INTO expenses (id, value) VALUES (39, 943) """,
        )
        for query in querys:
            cursor.execute(querys[query])
        db.commit()


# insert_values_to_db()
# get_values_from_db()
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
# querys = dict(
#     query0=f'SELECT value FROM expenses WHERE id < 5',
#     query1=f'SELECT value FROM expenses WHERE id < 5',
#     query2=f'SELECT value FROM expenses WHERE id < 5',
#     query3=f'SELECT value FROM expenses WHERE id < 5',
#     query4=f'SELECT value FROM expenses WHERE id < 5',
#     query5=f'SELECT value FROM expenses WHERE id < 5',
#     query6=f'SELECT value FROM expenses WHERE id < 5',
#     query7=f'SELECT value FROM expenses WHERE id < 5',
#     query8=f'SELECT value FROM expenses WHERE id < 5',
#     query9=f'SELECT value FROM expenses WHERE id < 5',
# )
