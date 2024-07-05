import sqlite3

conn = sqlite3.connect('data.db')
c= conn.cursor()
c.execute("DROP TABLE data")    
conn.commit()
conn.close()  # Close the database connection