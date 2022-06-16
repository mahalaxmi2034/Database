import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
conn.execute("insert into participants values(2216103,'snehitha','cseai','Btech')")
conn.execute("insert into participants values(2216101,'maha','cseai','Btech')")
conn.execute("insert into participants values(2216102,'ram','cseai','Btech')")
conn.commit()
conn.close()