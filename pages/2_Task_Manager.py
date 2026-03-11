import streamlit as st
import pandas as pd

st.title("✅ Task Manager")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

with st.form("task_form"):
    task = st.text_input("Task Name")
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    deadline = st.date_input("Deadline")

    submitted = st.form_submit_button("Add Task")

if submitted and task != "":
    st.session_state.tasks.append({
        "Task": task,
        "Priority": priority,
        "Deadline": deadline
    })
    st.success("Task added!")

if st.session_state.tasks:
    df = pd.DataFrame(st.session_state.tasks)
    st.dataframe(df)

    completed = st.checkbox("Mark all tasks completed")

    if completed:
        st.balloons()
else:
    st.info("No tasks added yet.")