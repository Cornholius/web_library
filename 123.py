import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

name = 'вы призвали'.capitalize()
print(name)
qwe = f"SELECT author, book_name, description " \
      f"FROM library_library " \
      f"WHERE book_name like '%{name}%' " \
      f"OR author like '%{name}%'"
print(qwe)
cursor.execute(qwe)
qwe = cursor.fetchone()
print(qwe)
connection.close()


# print(f"Hello, {name}. You are {age}.")
# cursor.execute("""
#     SELECT author, book_name, description
#     FROM library_library
#     WHERE book_name = 'qwerty2'
#     """)