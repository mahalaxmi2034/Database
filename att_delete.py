import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
conn.execute("delete from attendance where branch='cse'")
print(conn.total_changes)
conn.commit()
conn.close()