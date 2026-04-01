import sqlite3


# create connection to the database
conn  = sqlite3.connect('test.db')

# create cursor object - Lúc nào cũng cần tọa trước khi chạy

cursor = conn.cursor()

# ... create table, query, etc.
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     id  INTEGER PRIMARY KEY AUTOINCREMENT,
#     name  TEXT NOT NULL,
#     age   INTEGER NOT NULL,
#     grade TEXT
# )               
# """)

# cursor.execute("""
# INSERT INTO students(name, age, grade)
# VALUES ('Alice', 20, 'A'),
#          ('Bob', 22, 'B'),
#          ('Charlie', 19, 'C')              
               
# """)

# my_list = [
#     ('Minh', 16, 'D'),
#     ('Hoa', 16, 'E'),
#     ('Huowng', 16, 'F')
# ]
# cursor.executemany("""
# INSERT INTO students(name, age, grade)
# VALUES (?, ?, ?)
# """, my_list)

# query don't use commit

# fetch all rows
# cursor.execute("SELECT * FROM students")
# rows = cursor.fetchall()
# print(type(rows))
# for row in rows:
#     print(row)
#     print(type(row))

# fetch specific columns + condition age > 19
# cursor.execute("SELECT name, grade FROM students WHERE age > 20")
# rows = cursor.fetchall()
# print(rows)


# update data
# cursor.execute("""
# UPDATE students
# SET name = "Auteen"
# WHERE name = "Alice"
# """)

# delete data
cursor.execute("""
DELETE FROM students
WHERE id > 3 and id < 7
""")


# commit changes - save in db
conn.commit()   

# close the connection when done
conn.close()








