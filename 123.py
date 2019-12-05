import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

name = 'qwerty2'
qwe = f"SELECT author, book_name, description FROM library_library WHERE book_name = '{name}'"

cursor.execute(qwe)
qwe = cursor.fetchone()
print(cursor.fetchone())
print(qwe[0])
print(qwe)
connection.close()


# print(f"Hello, {name}. You are {age}.")
# cursor.execute("""
#     SELECT author, book_name, description
#     FROM library_library
#     WHERE book_name = 'qwerty2'
#     """)