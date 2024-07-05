import sqlite3

conn = sqlite3.connect('data.db')
c= conn.cursor()
c.execute("INSERT INTO Attendence (Cname)  VALUES (?) WHERE Aid = 1 ", ('Mina',))    
conn.commit()
conn.close()  # Close the database connection