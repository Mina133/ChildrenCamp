import sqlite3
import streamlit as st
import pandas as pd
import QR
import childData as CD



def home():
    st.title('Welcom to Childern Camp ')
    st.image('camp.jpg')
   



if __name__ == '__main__':
    menu = ['home', 'Add Data', 'View Data', 'QR Code', 'QR Scanner', 'Attendance']
    currentPage = st.sidebar.selectbox('Menu', menu)

    if currentPage == 'home':
        home()
    elif currentPage == 'Add Data':
       CD.AddData()
    
    elif currentPage == 'View Data':
        CD.ViewData()

    elif currentPage == 'QR Code':
        QR.GenerateQRCode()

    elif currentPage == 'QR Scanner':
        QR.qrScanner()

    elif currentPage == 'Attendance':
        
        st.title("Student Attendance Management")
        CD.AttendByDay()
        # conn = sqlite3.connect('data.db')
        # c = conn.cursor()
        # c.execute('SELECT * FROM Attendence')
        # st.table(c.fetchall())
        # conn.close()


       

        

 
    
 
    
