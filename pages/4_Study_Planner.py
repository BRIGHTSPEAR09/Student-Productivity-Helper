import streamlit as st
import time
from datetime import date

st.title("🗓 Study Planner")

# ---------------- SESSION STATE ----------------
if "study_plan" not in st.session_state:
    st.session_state.study_plan = []

if "timer_running" not in st.session_state:
    st.session_state.timer_running = False

if "timer_paused" not in st.session_state:
    st.session_state.timer_paused = False

if "time_left" not in st.session_state:
    st.session_state.time_left = 0

# ---------------- PLAN STUDY SESSION ----------------
st.subheader("Plan Your Study Session")

with st.form("planner_form"):

    col1, col2 = st.columns(2)

    with col1:
        subject = st.text_input("Subject")

    with col2:
        topic = st.text_input("Topic")

    duration = st.number_input("Study Duration (minutes)", min_value=1, max_value=300, value=60)

    study_date = st.date_input("Study Date", value=date.today())

    submitted = st.form_submit_button("Add Study Plan")

if submitted and subject and topic:

    st.session_state.study_plan.append({
        "Subject": subject,
        "Topic": topic,
        "Duration": duration,
        "Date": study_date,
        "Completed": False
    })

    st.success("Study session added!")

st.divider()

# ---------------- TODAY'S STUDY SESSIONS ----------------
st.subheader("📅 Today's Study Plan")

today_sessions = [s for s in st.session_state.study_plan if s["Date"] == date.today()]

if today_sessions:

    for i, session in enumerate(st.session_state.study_plan):

        if session["Date"] != date.today():
            continue

        col1, col2, col3, col4 = st.columns([3,2,1,1])

        with col1:
            if session["Completed"]:
                st.markdown(f"~~{session['Subject']} - {session['Topic']}~~ ✅")
            else:
                st.write(f"{session['Subject']} - {session['Topic']}")

        with col2:
            st.write(f"{session['Duration']} mins")

        with col3:

            if not session["Completed"]:

                if st.button("Start", key=f"start_{i}"):
                    st.session_state.time_left = int(session["Duration"] * 60)
                    st.session_state.timer_running = True
                    st.session_state.timer_paused = False

                if st.button("Pause", key=f"pause_{i}"):
                    st.session_state.timer_paused = True

                if st.button("Resume", key=f"resume_{i}"):
                    st.session_state.timer_paused = False

        with col4:
            if st.button("🗑", key=f"delete_{i}"):
                st.session_state.study_plan.pop(i)
                st.rerun()

# ---------------- TIMER DISPLAY ----------------
if st.session_state.timer_running:

    progress_bar = st.progress(0)
    timer_text = st.empty()

    total_time = st.session_state.time_left

    while st.session_state.time_left > 0:

        if st.session_state.timer_paused:
            st.warning("⏸ Timer paused")
            break

        mins, secs = divmod(st.session_state.time_left, 60)
        timer_text.markdown(f"⏳ **Time Left: {mins:02d}:{secs:02d}**")

        progress = (total_time - st.session_state.time_left) / total_time
        progress_bar.progress(progress)

        time.sleep(1)
        st.session_state.time_left -= 1

    if st.session_state.time_left == 0:
        st.success("🔔 Time's up! Study session completed!")
        st.balloons()
        st.session_state.timer_running = False

else:
    st.info("No study sessions planned for today.")

st.divider()

# ---------------- DAILY PROGRESS ----------------
st.subheader("📊 Today's Progress")

total_sessions = len(today_sessions)
completed_sessions = sum(s["Completed"] for s in today_sessions)

if total_sessions > 0:

    progress = completed_sessions / total_sessions
    st.progress(progress)

    st.write(f"Completed **{completed_sessions} of {total_sessions} sessions**")

else:
    st.write("No sessions planned today.")

st.divider()

# ---------------- MOTIVATION ----------------
st.subheader("💡 Motivation")

quotes = [
    "Small progress is still progress.",
    "Consistency beats intensity.",
    "Focus on the process.",
    "Success comes from daily discipline.",
    "Study now, relax later."
]

selected_quote = st.selectbox("Pick a motivation", quotes)

st.info(selected_quote)

st.divider()

# ---------------- STUDY TIPS ----------------
st.subheader("📚 Study Tips")

tips = [
    "Use the Pomodoro technique (25 minutes focus, 5 minutes break).",
    "Remove distractions while studying.",
    "Review your notes after every study session.",
    "Teach what you learned to someone else.",
    "Study consistently instead of cramming."
]

st.write(tips)