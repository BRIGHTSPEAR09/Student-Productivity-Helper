import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Productivity Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Study Hours Today", "5", "+1")
col2.metric("Tasks Completed", "7", "+2")
col3.metric("Focus Score", "82%", "+5%")

st.divider()

st.subheader("Daily Study Goal")

goal = st.slider("Set your study goal (hours)", 1, 12, 6)

hours = st.number_input("Hours studied today", 0, 12)

progress = hours/goal if goal else 0

st.progress(progress)

st.write(f"Progress: {int(progress*100)}%")

st.subheader("Study Mood")

mood = st.radio(
    "How do you feel today?",
    ["Motivated", "Okay", "Tired"]
)

st.write("Selected mood:", mood)

st.subheader("Quick Notes")

st.text_area("Write a quick study note")