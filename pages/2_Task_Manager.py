import streamlit as st
import pandas as pd

st.title("✅ Task Manager")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ---- Add Task Form ----
with st.form("task_form"):
    task = st.text_input("Task Name")
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    deadline = st.date_input("Deadline")

    submitted = st.form_submit_button("Add Task")

if submitted and task != "":
    st.session_state.tasks.append({
        "Task": task,
        "Priority": priority,
        "Deadline": deadline,
        "Completed": False
    })
    st.success("Task added successfully!")

st.divider()

# ---- Display Tasks ----
if st.session_state.tasks:

    st.subheader("Your Tasks")

    for i, task in enumerate(st.session_state.tasks):

        col1, col2, col3, col4 = st.columns([3,1,2,1])

        # Task info
        with col1:
            if task["Completed"]:
                st.markdown(f"~~{task['Task']}~~ ✅")
            else:
                st.write(task["Task"])

        # Priority
        with col2:
            st.write(task["Priority"])

        # Deadline
        with col3:
            st.write(task["Deadline"])

        # Complete button
        with col4:
            if not task["Completed"]:
                if st.button("✔️", key=f"complete_{i}"):
                    st.session_state.tasks[i]["Completed"] = True
                    st.balloons()
                    st.success("🎉 Task completed!")

        # Delete button
        if st.button("🗑 Delete", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()

    st.divider()

    # Summary
    completed_tasks = sum(task["Completed"] for task in st.session_state.tasks)
    total_tasks = len(st.session_state.tasks)

    st.progress(completed_tasks / total_tasks)

    st.write(f"Completed **{completed_tasks} out of {total_tasks} tasks**")

else:
    st.info("No tasks added yet.")