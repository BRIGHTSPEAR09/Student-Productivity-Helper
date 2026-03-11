import streamlit as st
import pandas as pd

st.title("📊 Productivity Dashboard")

tasks = st.session_state.get("tasks", [])
study_data = st.session_state.get("study_data", [])

task_count = len(tasks)
study_hours = sum([item["Hours"] for item in study_data]) if study_data else 0

col1, col2 = st.columns(2)

col1.metric("Tasks Added", task_count)
col2.metric("Total Study Hours", study_hours)

st.divider()

goal = st.slider("Set Weekly Study Goal (hours)", 1, 40, 10)

progress = study_hours / goal if goal else 0

st.progress(min(progress, 1.0))

st.write(f"Progress toward goal: {int(progress*100)}%")