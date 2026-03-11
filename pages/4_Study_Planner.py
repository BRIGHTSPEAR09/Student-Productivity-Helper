import streamlit as st

st.title("🗓 Study Planner")

study_topic = st.text_input("What will you study today?")

duration = st.slider("Study Duration (minutes)", 15, 180, 60)

start = st.button("Start Study Session")

if start:
    st.success(f"Study session started for {study_topic} ({duration} minutes)")
    st.progress(0.0)

st.subheader("Motivation")

quote = st.selectbox(
    "Pick a motivation",
    [
        "Small progress is still progress",
        "Consistency beats intensity",
        "Focus on the process"
    ]
)

st.write("Motivation:", quote)