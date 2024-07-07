from PIL import Image, ImageDraw, ImageFont
import sqlite3
import sys
import streamlit as st
from bidi.algorithm import get_display
import arabic_reshaper


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
    
def printA(text):
        return get_display(arabic_reshaper.reshape(text))

def cardName(id):
    # levvel = QR.getLevelfromID(id)
    # if levvel == 1:
    #     img = Image.open('petraChildrenCampLevel1.png')
    # elif levvel == 2:
    #     img = Image.open('petraChildrenCampLevel2.png')
    img = Image.open('petraChildrenCamp.png')
    name = get_name_from_id(id)
   
   
    printA(name)
    st.write(printA(name))
    

    drawName = ImageDraw.Draw(img)
    drawName.text((500, 300), text=printA(name), fill='black', font=ImageFont.truetype(font='Aria.ttf', size=50))  # Assuming the font is in the same directory
    img.save(f"{name}.png")


# cardName(1)  # Example usage