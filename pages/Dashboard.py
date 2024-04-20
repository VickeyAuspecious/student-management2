import streamlit as st
import pandas as pd

def view_excel():
    st.title("Excel File Viewer")

    # Read Excel file from folder
    file_path = "pages/students.xlsx"
    df = pd.read_excel(file_path)

    # Display DataFrame as table
    st.write("### DataFrame:")
    st.table(df)

if __name__ == "__main__":
    view_excel()
