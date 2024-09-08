import sqlite3

connection = sqlite3.connect('datab.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
id INTEGER,
username TEXT,
first_name TEXT,
block INTEGER
)''')


def add_user(user_id, user_name, first_name):
    check_user = cursor.execute("SELECT * FROM Users WHERE id= ?", (user_id,))
    if check_user.fetchone() in None:
        cursor.execute(f"INSERT INTO Users VALUES('{user_id}', '{user_name}', '{first_name}', 0)")
    connection.commit()


def show_users():
    users_list = cursor.execute("SELECT * FROM Users")
    message = ''
    for user in users_list:
        message += f'{user[0]} @{user[1]} @{user[2]} \n'
    connection.commit()
    return message


def show_stat():
    count_users = cursor.execute("SELECT COUNT(*) FROM Users").fetchone()
    connection.commit()
    return count_users[0]


def add_to_block(input_id):
    cursor.execute(f"UPDATE Users SET block = ? WHERE id = ?", (1, input_id))
    connection.commit()


def check_block(user_id):
    user = cursor.execute("SELECT block FROM Users WHERE id = ?", (user_id,)).fetchone()
    connection.commit()
    return user[0]


def remove_block(input_id):
    cursor.execute(f"UPDATE Users SET block = ? WHERE id = ?", (0, input_id))
    connection.commit()


connection.close()
