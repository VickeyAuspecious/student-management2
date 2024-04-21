import streamlit as st
import openpyxl as px

# Load the Excel file
wb = px.load_workbook('Users.xlsx')
sheet = wb.active

# Function to check if user exists
def user_exists(username, password):
    for row in sheet.iter_rows(values_only=True):
        if row[0] == username and row[1] == password:
            return True
    return False

# Login page
def login_page():
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        if user_exists(username, password):
            st.success('Logged in successfully')
            
            return True
        else:
            st.error('Invalid username or password')
            return False

if __name__ == "__main__":
    login_page()
