import sqlite3
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)''')
for i in range(1,11):
    cursor.execute("INSERT INTO Users (username,email,age,balance) VALUES (?,?,?,?)",
                   (f'User{i}', f'example{i}@gmail.com', f'{i*10}', f'1000'))

cursor.execute("UPDATE Users SET balance = ? WHERE id % 2", ('500',))
count_ = cursor.execute("SELECT COUNT(*) FROM Users").fetchone()[0]
for i in range(1, count_ + 1, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (i,))
users = cursor.execute("SELECT username, email, age , balance FROM Users WHERE age != ?", (60,)).fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')
connection.commit()
connection.close()