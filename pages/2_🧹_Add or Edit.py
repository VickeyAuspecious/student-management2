import streamlit as st
import pandas as pd

# Function to view Excel file and delete selected rows
def view_excel():
    st.title("Students Data")
    # Read Excel file from folder
    file_path = "pages/students.xlsx"
    df = pd.read_excel(file_path)
    
    # Display DataFrame as table
    st.write("###")
    rows_to_delete = st.multiselect("Select rows to delete", df.index.tolist())
    if st.button("Delete Selected Rows"):
        df.drop(rows_to_delete, inplace=True)
        df.to_excel(file_path, index=False)
        st.success("Selected rows deleted successfully!")
    
    st.write(df)

# Function to add new student
def add_student():
    st.title("Add New Student")
    # Input form for new student details
    student_id = st.text_input("Student ID")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=150)
    course = st.text_input("Course")
    cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
    hosteller_day_scholar = st.radio("Hosteller/Day Scholar", options=["Hosteller", "Day Scholar"])
    transport = st.text_input("Transport")
    fee_pendings = st.number_input("Fee Pendings", min_value=0)

    if st.button("Save"):
        # Add new student to DataFrame
        new_student = pd.DataFrame({"Student ID": [student_id],
                                    "Name": [name],
                                    "Age": [age],
                                    "Course": [course],
                                    "CGPA": [cgpa],
                                    "Hosteller/Day Scholar": [hosteller_day_scholar],
                                    "Transport": [transport],
                                    "Fee Pendings": [fee_pendings]})
        # Write DataFrame back to Excel file
        file_path = "pages/students.xlsx"
        try:
            df = pd.read_excel(file_path)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Student ID", "Name", "Age", "Course", "CGPA", "Hosteller/Day Scholar", "Transport", "Fee Pendings"])
        df = pd.concat([df, new_student], ignore_index=True)
        df.to_excel(file_path, index=False)
        st.success("New student added successfully!")


def main():
    # Create a navigation menu
    menu = ["Students Data", "Add Student"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Students Data":
        view_excel()
    elif choice == "Add Student":
        add_student()

if __name__ == "__main__":
    main()
