import streamlit as st
import pandas as pd

st.title("📊 Productivity Dashboard")

tasks = st.session_state.get("tasks", [])
study_data = st.session_state.get("study_data", [])

# Convert study data to DataFrame
df = pd.DataFrame(study_data)

# Basic metrics
task_count = len(tasks)
study_hours = df["Hours"].sum() if not df.empty else 0
study_sessions = len(df)

# ---- Metrics Section ----
st.subheader("Overview")

col1, col2, col3 = st.columns(3)

col1.metric("📝 Tasks Added", task_count)
col2.metric("⏱ Total Study Hours", study_hours)
col3.metric("📚 Study Sessions", study_sessions)

st.divider()

# ---- Weekly Study Chart ----
st.subheader("📅 Weekly Study Hours")

if not df.empty and "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    weekly_data = df.groupby(df["Date"].dt.date)["Hours"].sum()

    st.line_chart(weekly_data)

else:
    st.info("No study data yet. Start logging your study sessions!")

# ---- Study Goal Section ----
st.divider()
st.subheader("🎯 Weekly Study Goal")

goal = st.slider("Set Weekly Study Goal (hours)", 1, 40, 10)

progress = study_hours / goal if goal else 0

st.progress(min(progress, 1.0))

st.write(f"Progress toward goal: **{int(progress*100)}%**")

# ---- Daily Study Distribution ----
st.divider()
st.subheader("📊 Study Hours Distribution")

if not df.empty and "Subject" in df.columns:
    subject_data = df.groupby("Subject")["Hours"].sum()

    st.bar_chart(subject_data)

else:
    st.info("Add subjects to see study distribution.")

# ---- Recent Activity ----
st.divider()
st.subheader("📋 Recent Study Sessions")

if not df.empty:
    st.dataframe(df.tail(5))
else:
    st.write("No study sessions recorded yet.")