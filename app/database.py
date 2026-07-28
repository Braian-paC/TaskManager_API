import sqlite3

conn = sqlite3.connect("database/TaskManager_DB.db")
cursor = conn.cursor()

sql_result = """SELECT id, name, description FROM 'Tasks'"""
#sql_delet = """DELETE FROM 'Tasks' WHERE id=2"""

cursor.execute(sql_result)
print(cursor.fetchall())
