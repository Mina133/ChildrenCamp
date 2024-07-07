from io import BytesIO
import sqlite3
import cv2
import numpy as np
import streamlit as st
import qrcode
import pandas as pd
import datetime
from datetime import datetime, timedelta
import Card



def get_name_from_id(id):
    """Retrieves the name from the database based on the provided ID."""
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT Name FROM data WHERE ID=?', (id,))
    name = c.fetchone()
    if name:
        return name[0]  # Return the first element (name) from the tuple
    else:
        return None
    
    
def getIDFromName(name):
    """Retrieves the ID from the database based on the provided name."""
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT ID FROM data WHERE Name=?', (name,))
    ID = c.fetchone()
    if ID:
        return ID[0]  # Return the first element (ID) from the tuple
    else:
        return None

def getLevelfromID(id):
    """Retrieves the level from the database based on the provided ID."""
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT Level FROM data WHERE ID=?', (id,))
    level = c.fetchone()
    if level:
        return level[0]  # Return the first element (level) from the tuple
    else:
        return None

def GenerateQRCode():
    # Connect to the SQLite database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Read data from the database
    c.execute('SELECT * FROM data')
    data = pd.DataFrame(c.fetchall())
    data.columns = ['ID', 'Name', 'Age', 'Parent Name', 'Phone Number', 'Level']

    # Select a name from the available options
    name = st.selectbox('Select a name', data['Name'].unique())

    if name:  # Check if a name is selected (avoid errors)
        # Get the ID for the selected name
        selected_id = data.loc[data.Name == name].ID.values[0]

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(selected_id)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        # Display the QR code efficiently
        img_bytes = BytesIO()
        img.save(img_bytes, format='PNG')
        st.image(img_bytes.getvalue())  # Use getvalue() to extract byte data

        # Download button using in-memory byte data
        with img_bytes as f:  # Use context manager for automatic closing
            btn = st.download_button(
                label="Download QR Code",
                data=f.getvalue(),  # Get byte data for download
                file_name='{} qr.png'.format(name),
                mime='image/png', 
            )
            if st.button("create Card"):
                Card.cardName(getIDFromName(name))

    else:
        st.warning("Please select a name to generate QR code.")

    conn.close()

   



current_time = datetime.now()
formatted_date = current_time.strftime("%Y-%m-%d")
formatted_time = current_time.time().strftime("%H:%M:%S")

def Attend(cid):
    """save the entring and leaving time """
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Attendence (Aid INTEGER NOT NULL PRIMARY KEY, Cid FOREIGNKEY REFERENCES data(id), date TEXT, enter TEXT, leave TEXT)')

    c.execute("SELECT enter FROM Attendence WHERE Cid = ? AND date = ?", (cid, formatted_date))
    entry = c.fetchone()
    conn.commit()
    if entry != None:
        st.warning("You have already entered the camp.")
        return 
    c.execute("""INSERT INTO Attendence (Cid, date, enter ) VALUES (?, ?, ?)""", (cid, formatted_date, formatted_time))
    conn.commit()    
    conn.close()  # Close the database connection
    st.success("welcome {}".format(get_name_from_id(cid)))

def leave(cid):
    """save the leaving time """
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()

    try:
      cursor.execute("SELECT enter FROM Attendence WHERE Cid = ?", (cid,))
      entry = cursor.fetchone()

      if not entry:
        raise ValueError(f"No entry found for course ID: {cid}")

      leaving_time = datetime.now().strftime("%H:%M:%S")

      # Update existing entry instead of inserting a new one
      cursor.execute("""UPDATE Attendence SET leave = ? WHERE Cid = ?""", (leaving_time, cid))

      name = get_name_from_id(cid)  # Assuming get_name_from_id is defined
      st.success(f"Bye Bye {name}")  # Replace with st.success if using a messaging module

      conn.commit()
    except (sqlite3.Error, ValueError) as error:
      st.error(f"Error logging leaving time: {error}")



def qrScanner():
    """Performs QR code scanning and displays information based on user input."""
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    image = st.camera_input("Scan QR code")
    

    if image is not None:
        bytes_data = image.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        detector = cv2.QRCodeDetector()
        id, data, _ = detector.detectAndDecode(cv2_img)
        name = get_name_from_id(id)
        if name and id != '':
            st.write(f"Welcome, {name}!")
            if st.button("Welcome"):
                Attend(id)
                
            if st.button("Leave"):
                leave(id)
            
        else:
            st.warning(f"No name found for ID: {id} OR No QR code detected.")
       

    conn.close()  # Close the database connection