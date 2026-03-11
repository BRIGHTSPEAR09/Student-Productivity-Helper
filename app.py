import streamlit as st

st.set_page_config(
    page_title="Student Productivity Helper",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Student Productivity Helper")

st.sidebar.title("Navigation")
st.sidebar.info(
"""
Use the pages in the sidebar to explore the app:

• Dashboard  
• Task Manager  
• Study Analytics  
• File Upload  
• About
"""
)

st.write("""
Welcome to the **Student Productivity Helper App**.

This tool helps students:
- Track study hours
- Manage tasks
- Upload assignments
- View productivity analytics
""")

st.success("Use the sidebar to navigate through the app.")