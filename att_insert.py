import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
conn.execute("insert into attendance values(2216103,'snehitha',99)")
conn.execute("insert into attendance  values(2216101,'maha',99)")
conn.execute("insert into attendance  values(2216102,'ram',98)")
conn.commit()
conn.close()