# sql_inject.py

import sqlite3

path = r'C:\Users\15min\Desktop\DimaFront\Lekce Python\Git_Lections\Projects\test_project\db.sqlite3'
connection = sqlite3.connect(path)
cursor = connection.cursor()

search_text = input("Put a searching:")

query = f"""
        select * from todo_task where title like '?%' and user_id = 1
        """

cursor.execute(query, [search_text])

data = cursor.fetchall()

for item in data:
    print(item[0], item[1])

