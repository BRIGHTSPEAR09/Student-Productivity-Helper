import streamlit as st
import random

st.set_page_config(
    page_title="Student Productivity Helper",
    page_icon="📚",
    layout="wide"
)

# -------------------------------
# Custom CSS (makes it look nicer)
# -------------------------------
st.markdown("""
<style>
.main-title{
    font-size:40px;
    font-weight:700;
}

.subtitle{
    font-size:20px;
    color:gray;
}

.card{
    background-color:#f9f9f9;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
}

.tip{
    background-color:#eef6ff;
    padding:15px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.success("Navigate using the pages above 👆")

# -------------------------------
# Hero Section
# -------------------------------
st.image(
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c",
    use_column_width=True
)

st.markdown('<p class="main-title">📚 Student Productivity Helper</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Stay Focused • Study Smarter • Achieve More</p>', unsafe_allow_html=True)

st.write("""
Welcome! This application helps students **organize tasks, track study sessions,
and maintain productivity throughout the semester.**
""")

st.divider()

# -------------------------------
# Feature Dashboard
# -------------------------------
st.subheader("✨ App Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>📊 Study Tracker</h3>
    <p>Track the number of hours you study each day and monitor your productivity progress.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>✅ Task Manager</h3>
    <p>Organize assignments, projects, and deadlines in one place.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>📅 Study Planner</h3>
    <p>Create a structured study schedule and stay consistent.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# -------------------------------
# Mood-Based Encouragement System
# -------------------------------
st.subheader("💬 How are you feeling today?")

mood = st.selectbox(
    "Select your current mood",
    ["😊 Motivated", "😐 Okay", "😞 Stressed", "😴 Tired"]
)

motivated_quotes = [
    "Great! Keep the momentum going and finish one important task today.",
    "You're on the right track. Consistency is your superpower!",
    "Channel that energy into focused study sessions."
]

okay_quotes = [
    "Even small progress counts today.",
    "Start with an easy task to build momentum.",
    "You don’t have to be perfect, just keep moving forward."
]

stressed_quotes = [
    "Take a deep breath. Break your tasks into smaller steps.",
    "Focus on one task at a time. You can handle it.",
    "Remember: progress is better than perfection."
]

tired_quotes = [
    "Rest for a bit, then try a short 25-minute study session.",
    "Drink some water and stretch before continuing.",
    "Your brain needs rest too. Take care of yourself."
]

if mood == "😊 Motivated":
    message = random.choice(motivated_quotes)
    st.success(message)

elif mood == "😐 Okay":
    message = random.choice(okay_quotes)
    st.info(message)

elif mood == "😞 Stressed":
    message = random.choice(stressed_quotes)
    st.warning(message)

elif mood == "😴 Tired":
    message = random.choice(tired_quotes)
    st.warning(message)

st.divider()

# -------------------------------
# Quick Study Tip
# -------------------------------
st.subheader("📌 Productivity Tip")

tips = [
    "Use the **Pomodoro Technique**: 25 minutes study, 5 minutes break.",
    "Remove distractions by putting your phone away while studying.",
    "Plan tomorrow's tasks before you sleep.",
    "Study the hardest subject when your energy is highest."
]

st.markdown(f"""
<div class="tip">
💡 {random.choice(tips)}
</div>
""", unsafe_allow_html=True)

st.divider()

# Call to action
st.success("👈 Use the sidebar to explore the study tracker, task manager, and planner!")