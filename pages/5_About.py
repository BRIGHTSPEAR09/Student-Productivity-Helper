import streamlit as st

st.set_page_config(page_title="About - Student Productivity Helper", layout="wide")

st.title("ℹ️ About This App")

st.write("""
Welcome to **Student Productivity Helper**, your companion for managing study habits, tasks, 
and productivity analytics in one place.
""")

# Use columns for a dashboard-like feel
col1, col2 = st.columns(2)

with col1:
    st.subheader("What the App Does")
    st.info("""
    The **Student Productivity Helper** helps students:
    - Track study habits
    - Plan and manage tasks
    - Analyze productivity trends over time
    """)

with col2:
    st.subheader("Target Users")
    st.success("""
    This app is designed for:
    - College students  
    - High school students  
    - Self-learners who want to improve productivity
    """)

st.markdown("---")  # separator

# Inputs and Outputs in columns
col3, col4 = st.columns(2)

with col3:
    st.subheader("Inputs Collected")
    st.write("""
    Users can provide the following inputs:
    - Tasks and deadlines
    - Study subjects and allocated hours
    - Planned study sessions
    """)

with col4:
    st.subheader("Outputs Displayed")
    st.write("""
    The app generates:
    - Productivity metrics dashboard
    - Charts showing study trends
    - Tables for task tracking and completion
    """)

# Optional callout
st.markdown("---")
st.info("This app is designed to make productivity tracking simple, visual, and actionable!")