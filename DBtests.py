import sqlite3

conn = sqlite3.connect('data.db')
c= conn.cursor()
c.execute("DROP TABLE Attendence")    
conn.commit()
conn.close()  # Close the database connection

# install: pip install --upgrade arabic-reshaper
# import arabic_reshaper

# # install: pip install python-bidi
# from bidi.algorithm import get_display

# text = "ذهب الطالب الى المدرسة"
# reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
# bidi_text = get_display(reshaped_text)

# import sys
# text = "اطبع هذا النص".encode("utf-8")
# sys.stdout.buffer.write(text)