import streamlit as st
import sqlite3
import pandas as pd
import datetime
from datetime import datetime, timedelta
def AddData():
    st.title('Welcome to Children\'s Camp Registration Form')

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER NOT NULL PRIMARY KEY, name TEXT, age FLOAT, parentName TEXT, phone TEXT, level INTEGER);')

    form = st.form(key='new entry')
    with form:
        name = form.text_input('Child Name: ')
        age = form.number_input('Child Age: ', step=0)
        parentName = form.text_input('Parent Name: ')
        phone = form.text_input('Phone Number: ')
        level = st.selectbox('Level', options=['1', '2'])
        btn = st.form_submit_button('Save')
        
        if btn:
            if not name or not parentName or not phone or not level or not age :
                st.error('Please fill in all the fields.')
            else:
                try:
                    # Validate age (optional)
                    age = float(age)  # Check if age can be converted to a number
                    c.execute('INSERT INTO data (name, age, parentName, phone, level) VALUES (?, ?, ?, ?, ?)',
                              (name, age, parentName, phone, level))
                    conn.commit()
                    form.success('Data Saved Successfully!')
                except ValueError:
                    st.error("Age must be a number.")

    conn.close()


def ViewData():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM data')
    data = pd.DataFrame(c.fetchall())
    data.columns = ['ID', 'Name', 'Age', 'Parent Name', 'Phone Number', 'Level']

    st.table(data)

    conn.close()


current_time = datetime.now()
formatted_date = current_time.strftime("%Y-%m-%d")
formatted_time = current_time.time().strftime("%H:%M:%S")

def AttendByDay():
    
<<<<<<< HEAD
    """
    Fetches and displays attendance data for a selected date.
    """

    # Connect to the database
    conn = sqlite3.connect('data.db')

    # Create the table if it doesn't exist (simplified)
    cursor = conn.cursor()
    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS Attendence (Aid INTEGER PRIMARY KEY AUTOINCREMENT, Cid INTEGER FORIGN KEY REFRENCE data(id), Cname TEXT , date TEXT,  enter TEXT, leave TEXT)')
        conn.commit()
    except sqlite3.Error as e:
        # Handle any table creation errors (optional)
        pass  # Or print an error message

    # Get a list of available dates
    cursor.execute('SELECT date FROM Attendence')
    dates = [row[0] for row in cursor.fetchall()]
    unique_dates = list(set(dates))  # Remove duplicates
=======
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Attendence(Aid Integer primary key,
    Cid INTEGER NOT NULL,
    FOREIGN KEY (Cid) REFERENCES data(id),
    date TEXT,
    enter text,
    leave text);''')
    c.execute('SELECT date FROM Attendence')
    dates = c.fetchall()
    dates = list(set([date[0] for date in dates]))
    dateSelection = st.selectbox('Select Date', dates)

   
    c.execute('SELECT * FROM Attendence where date = ?', (dateSelection, ))
    table = c.fetchall()
    table.insert(0, ('ID', 'Child ID', 'Date', 'Enter Time', 'Leave Time', 'name'))
    df = pd.DataFrame(table)
    df.columns = df.iloc[0]
    df = df[1:]
>>>>>>> 824354a1f6e4ee8067c070e7dcd7fd1cf3e1dc5c

    # Display a date selection box
    dateSelection = st.selectbox('Select Date', unique_dates)

<<<<<<< HEAD
    # Fetch data for the selected date
    cursor.execute('SELECT * FROM Attendence WHERE date = ?', (dateSelection,))
    table = cursor.fetchall()

    # Display the data or a message if no data exists
    if table:
        df = pd.DataFrame(table)
        df.columns = ['ID', 'Child ID', 'Date', 'Enter Time', 'Leave Time']
        st.table(df)
    else:
        st.info('No data available for the selected date.')

    # Close the connection
    conn.close()
=======
        
>>>>>>> 824354a1f6e4ee8067c070e7dcd7fd1cf3e1dc5c
