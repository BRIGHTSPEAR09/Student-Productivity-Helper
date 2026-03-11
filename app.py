import streamlit as st

st.set_page_config(
    page_title="Student Productivity Helper",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Student Productivity Helper")

st.sidebar.success("Select a page above.")

st.write("""
Welcome to the **Student Productivity Helper**.

This app helps students:

• Track study hours  
• Manage tasks  
• Analyze study productivity  
• Plan study sessions  
""")