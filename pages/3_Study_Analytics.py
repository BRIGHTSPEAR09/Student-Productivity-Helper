import streamlit as st
import pandas as pd
from datetime import date

st.title("📈 Study Analytics")

# Initialize session state
if "study_data" not in st.session_state:
    st.session_state.study_data = []

# ADD STUDY RECORD
st.subheader("Add Study Session")

with st.form("study_form"):
    col1, col2 = st.columns(2)

    with col1:
        subject = st.text_input("Subject")

    with col2:
        hours = st.slider("Hours Studied", 1, 10)

    study_date = st.date_input("Study Date", value=date.today())

    submit = st.form_submit_button("Add Study Record")

if submit and subject:
    st.session_state.study_data.append({
        "Subject": subject,
        "Hours": hours,
        "Date": study_date
    })
    st.success("Study record added!")

st.divider()

# ANALYTICS
if st.session_state.study_data:

    df = pd.DataFrame(st.session_state.study_data)

    df["Date"] = pd.to_datetime(df["Date"])

    # METRICS
    total_hours = df["Hours"].sum()
    total_sessions = len(df)
    avg_hours = round(df["Hours"].mean(), 2)

    top_subject = df.groupby("Subject")["Hours"].sum().idxmax()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("⏱ Total Study Hours", total_hours)
    col2.metric("📚 Study Sessions", total_sessions)
    col3.metric("📊 Avg Hours per Session", avg_hours)
    col4.metric("🏆 Top Subject", top_subject)

    st.divider()

    # SUBJECT FILTER
    subjects = ["All"] + sorted(df["Subject"].unique().tolist())

    selected_subject = st.selectbox("Filter by Subject", subjects)

    if selected_subject != "All":
        df = df[df["Subject"] == selected_subject]

    # STUDY TREND 
    st.subheader("📅 Study Trend Over Time")

    trend = df.groupby(df["Date"].dt.date)["Hours"].sum()

    st.line_chart(trend)

    st.divider()

    # SUBJECT DISTRIBUTION
    st.subheader("📊 Study Hours by Subject")

    subject_chart = df.groupby("Subject")["Hours"].sum()

    st.bar_chart(subject_chart)

    st.divider()

    # DAILY STUDY HEATMAP STYLE
    st.subheader("🔥 Daily Study Activity")

    daily_activity = df.groupby(df["Date"].dt.date)["Hours"].sum()

    st.bar_chart(daily_activity)

    st.divider()

    # RECENT STUDY SESSIONS
    st.subheader("📋 Recent Study Sessions")

    st.dataframe(df.sort_values("Date", ascending=False).head(10))

    # STUDY INSIGHT
    st.divider()
    st.subheader("📊 Study Insights")

    if total_hours >= 20:
        st.success("Great job! You're studying consistently! 🚀")
    elif total_hours >= 10:
        st.info("Good progress. Keep building your study habit!")
    else:
        st.warning("Try to increase your study time this week.")

else:
    st.info("No study data added yet.")