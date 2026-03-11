import streamlit as st

st.title("✅ Task Manager")

with st.form("task_form"):
    task = st.text_input("Task Name")

    priority = st.selectbox(
        "Priority",
        ["Low", "Medium", "High"]
    )

    deadline = st.date_input("Deadline")

    submit = st.form_submit_button("Add Task")

if submit:
    st.success(f"Task '{task}' added!")

st.subheader("Today's Task List")

tasks = [
    {"Task":"Finish Math Homework","Priority":"High"},
    {"Task":"Review Python","Priority":"Medium"},
]

st.table(tasks)

done = st.checkbox("Mark all tasks completed")

if done:
    st.balloons()