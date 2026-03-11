import streamlit as st
import pandas as pd
from datetime import date

st.title("✅ Task Manager")

# Initialize tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ---------------- ADD TASK ----------------
st.subheader("Add New Task")

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

# ---------------- FILTER + SORT ----------------
col1, col2 = st.columns(2)

with col1:
    filter_option = st.selectbox(
        "Filter Tasks",
        ["All", "Completed", "Pending"]
    )

with col2:
    sort_option = st.selectbox(
        "Sort By",
        ["Deadline", "Priority"]
    )

tasks = st.session_state.tasks

# Filter logic
if filter_option == "Completed":
    tasks = [t for t in tasks if t["Completed"]]
elif filter_option == "Pending":
    tasks = [t for t in tasks if not t["Completed"]]

# Sort logic
if sort_option == "Deadline":
    tasks = sorted(tasks, key=lambda x: x["Deadline"])
elif sort_option == "Priority":
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    tasks = sorted(tasks, key=lambda x: priority_order[x["Priority"]])

# ---------------- DISPLAY TASKS ----------------
if tasks:

    st.subheader("Your Tasks")

    for i, task in enumerate(st.session_state.tasks):

        if filter_option == "Completed" and not task["Completed"]:
            continue
        if filter_option == "Pending" and task["Completed"]:
            continue

        col1, col2, col3, col4, col5 = st.columns([3,1,2,1,1])

        # Task Name
        with col1:
            if task["Completed"]:
                st.markdown(f"~~{task['Task']}~~ ✅")
            else:
                st.write(task["Task"])

        # Priority Tag
        with col2:
            if task["Priority"] == "High":
                st.error("High")
            elif task["Priority"] == "Medium":
                st.warning("Medium")
            else:
                st.success("Low")

        # Deadline
        with col3:
            st.write(task["Deadline"])

            if not task["Completed"] and task["Deadline"] < date.today():
                st.caption("⚠️ Overdue!")

        # Complete button
        with col4:
            if not task["Completed"]:
                if st.button("✔", key=f"complete_{i}"):
                    st.session_state.tasks[i]["Completed"] = True
                    st.balloons()
                    st.success("🎉 Task completed!")

        # Delete button
        with col5:
            if st.button("🗑", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

    st.divider()

    # ---------------- PROGRESS ----------------
    total_tasks = len(st.session_state.tasks)
    completed_tasks = sum(t["Completed"] for t in st.session_state.tasks)

    st.subheader("Task Progress")

    if total_tasks > 0:
        progress = completed_tasks / total_tasks
        st.progress(progress)
        st.write(f"Completed **{completed_tasks} of {total_tasks} tasks**")

else:
    st.info("No tasks added yet.")