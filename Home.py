import streamlit as st
import random

st.set_page_config(
    page_title="Student Productivity Helper",
    page_icon="📚",
    layout="wide"
)

st.sidebar.success("Navigate using the pages above 👆")


st.title("📚 EduPlanner (Student Productivity Helper)")

st.image(
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c",
    use_column_width=True
)

st.header("Stay Focused • Study Smarter • Achieve More 🚀")

st.write("""
Welcome to the **Student Productivity Helper**.

This application is designed to help students **stay organized,
track their study progress, and improve productivity** during the semester.
""")

st.info("💡 *Small progress each day adds up to big results.*")

st.divider()

st.subheader("✨ App Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### 📊 Track Study Hours
Monitor how many hours you study each day and observe your progress.
""")

with col2:
    st.success("""
### ✅ Manage Tasks
Keep track of assignments, projects, and important deadlines.
""")

with col3:
    st.warning("""
### 📅 Plan Study Sessions
Organize your study schedule to stay productive and focused.
""")

st.divider()

st.subheader("💬 How are you feeling today?")

mood = st.selectbox(
    "Select your current mood",
    ["😊 Motivated", "😐 Okay", "😞 Stressed", "😴 Tired"]
)

motivated_quotes = [
    "Great! Use that motivation to finish an important task today.",
    "Keep the momentum going. Consistency builds success.",
    "You're doing great. Stay focused and keep learning."
]

okay_quotes = [
    "Small progress is still progress. Start with one task.",
    "Try completing one simple task to build momentum.",
    "Focus on one thing at a time."
]

stressed_quotes = [
    "Take a deep breath. Break tasks into smaller steps.",
    "Focus on one task at a time. You can do it.",
    "Remember: progress is better than perfection."
]

tired_quotes = [
    "Take a short break before studying again.",
    "Drink some water and stretch your body.",
    "Try a short 25-minute study session."
]

if mood == "😊 Motivated":
    st.success(random.choice(motivated_quotes))

elif mood == "😐 Okay":
    st.info(random.choice(okay_quotes))

elif mood == "😞 Stressed":
    st.warning(random.choice(stressed_quotes))

elif mood == "😴 Tired":
    st.warning(random.choice(tired_quotes))

st.divider()

st.subheader("📌 Productivity Tip")

tips = [
    "Use the **Pomodoro Technique**: Study for 25 minutes, then take a 5-minute break.",
    "Remove distractions by putting your phone away while studying.",
    "Plan tomorrow's tasks before going to sleep.",
    "Study the hardest subject when your energy is highest.",
    "Create a dedicated study space to improve focus."
]

st.info(f"💡 {random.choice(tips)}")

st.divider()

st.success("👈 Use the sidebar to explore the study tracker, task manager, and planner!")