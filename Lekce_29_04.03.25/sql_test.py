# sql_test.py

import sqlite3

path = r'C:\Users\15min\Desktop\DimaFront\Lekce Python\Git_Lections\Projects\test_project\db.sqlite3'

print(path)

connection = sqlite3.connect(path)
cursor = connection.cursor()

print(connection)
print(cursor)

query = 'select * from todo_task limit 5'
cursor.execute(query)

data = cursor.fetchall()
print(data)

cursor.execute(f"""delete from todo_task where id > 15""")
connection.commit()

if False:
    for n in range(5):
        cursor.execute(f"""
                    insert into todo_task
                    (title, desc, is_finished, create_dt, update_dt, user_id)
                    values ('Title_{n}', 'Description_{n}', 0, '2025-01-01', '2025-01-01', 1)
                    """)
        connection.commit()

connection.close()

