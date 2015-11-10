import sqlite3
con = sqlite3.connect('mydiary.db') # Warning: This file is created in the 
con.execute("CREATE TABLE mydiary (id INTEGER PRIMARY KEY, time char(1000) NOT NULL ,diary char(1000) NOT NULL)")
con.commit()