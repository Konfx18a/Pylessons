import sqlite3
import random
def initiate_db():
    connection = sqlite3.connect('Usersdata.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER
    )''')
    connection.commit()


def add_user(username, email, age, balance = 1000):
    connection = sqlite3.connect('Usersdata.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username,email,age,balance) VALUES (?,?,?,?)",
                   (f'{username}', f'{email}', f'{age}', f'{balance}'))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('Usersdata.db')
    cursor = connection.cursor()
    user= cursor.execute(f'SELECT * FROM Users WHERE username = ?', (username,)).fetchone()
    if user is not None:
        connection.commit()
        connection.close()
        return True
    connection.commit()
    connection.close()
    return False


def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    all_prods=cursor.execute('''SELECT * FROM Products ''').fetchall()
    connection.commit()
    connection.close()
    return all_prods

def get_db_lenght():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    db_len = cursor.execute('''SELECT COUNT(*) FROM Products ''').fetchone()[0]
    connection.commit()
    connection.close()
    return db_len

# print(is_included('Петя1'))
# initiate_db()
# add_user('Вася', 'asdf@ya.ru', 22, balance = 1000)
# connection = sqlite3.connect('database.db')
# if not connection:
#     print('База данных не существует')
# cursor = connection.cursor()
# for i in range(1, 11):
#     cursor.execute(''' INSERT INTO Products (title,description,price) VALUES (?,?,?)''',
#                    (f'Title №{i}', f'Description № {i}', f'{random.randint(100,1000)}'))
# connection.commit()
# connection.close()
# print(get_all_products())
# print(get_db_lenght())
