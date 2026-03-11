import streamlit as st
import pandas as pd
from datetime import date

st.title("📊 Productivity Dashboard")

tasks = st.session_state.get("tasks", [])
study_data = st.session_state.get("study_data", [])

df = pd.DataFrame(study_data)

# ---------------- METRICS ----------------
st.subheader("Overview")

total_tasks = len(tasks)
completed_tasks = sum(task.get("Completed", False) for task in tasks)
task_completion = (completed_tasks / total_tasks * 100) if total_tasks else 0

study_hours = df["Hours"].sum() if not df.empty else 0
study_sessions = len(df)

col1, col2, col3, col4 = st.columns(4)

col1.metric("📝 Tasks", total_tasks)
col2.metric("✅ Completed", completed_tasks)
col3.metric("⏱ Study Hours", study_hours)
col4.metric("📚 Study Sessions", study_sessions)

st.divider()

# ---------------- TASK COMPLETION ----------------
st.subheader("Task Completion")

st.progress(task_completion / 100)
st.write(f"Task completion rate: **{int(task_completion)}%**")

# ---------------- STUDY GOAL ----------------
st.divider()

st.subheader("🎯 Weekly Study Goal")

goal = st.slider("Set Weekly Study Goal (hours)", 1, 40, 10)

progress = study_hours / goal if goal else 0

st.progress(min(progress, 1.0))
st.write(f"Goal Progress: **{int(progress*100)}%**")

# ---------------- STUDY HEATMAP ----------------
st.divider()
st.subheader("📅 Study Activity (Daily Heatmap)")

if not df.empty and "Date" in df.columns:

    df["Date"] = pd.to_datetime(df["Date"])
    heatmap_data = df.groupby(df["Date"].dt.date)["Hours"].sum()

    st.bar_chart(heatmap_data)

else:
    st.info("No study activity recorded yet.")

# ---------------- SUBJECT DISTRIBUTION ----------------
st.divider()
st.subheader("📚 Study Subjects Distribution")

if not df.empty and "Subject" in df.columns:

    subject_data = df.groupby("Subject")["Hours"].sum()

    st.write("Subjects studied:")
    st.dataframe(subject_data)

    st.bar_chart(subject_data)

else:
    st.info("Add subjects in study sessions to see distribution.")

# ---------------- DAILY STREAK ----------------
st.divider()
st.subheader("🔥 Study Streak")

streak = 0

if not df.empty and "Date" in df.columns:

    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    unique_days = sorted(df["Date"].unique(), reverse=True)

    today = date.today()

    for d in unique_days:
        if d == today or d == today.replace(day=today.day - streak):
            streak += 1
        else:
            break

st.metric("Current Study Streak (days)", streak)

# ---------------- PRODUCTIVITY SCORE ----------------
st.divider()
st.subheader("🏆 Productivity Score")

score = int((task_completion * 0.4) + (progress * 100 * 0.6))

st.metric("Your Productivity Score", f"{score}/100")

if score >= 80:
    st.success("Excellent productivity! 🚀")
elif score >= 50:
    st.info("Good progress, keep going! 💪")
else:
    st.warning("Try to study more and complete tasks.")

# ---------------- RECENT STUDY ----------------
st.divider()
st.subheader("📋 Recent Study Sessions")

if not df.empty:
    st.dataframe(df.tail(5))
else:
    st.write("No study sessions yet.")