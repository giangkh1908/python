import sqlite3

# create connection to the database
conn  = sqlite3.connect('test.db')

# create cursor object - Lúc nào cũng cần tọa trước khi chạy

cursor = conn.cursor()

# ... create table, query, etc.



# close the connection when done
conn.close()








