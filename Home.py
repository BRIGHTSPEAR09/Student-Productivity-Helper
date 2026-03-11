import streamlit as st

st.set_page_config(
    page_title="Student Productivity Helper",
    page_icon="📚",
    layout="wide"
)

# Title
st.title("📚 Student Productivity Helper")

# Sidebar message
st.sidebar.success("Select a page above.")

# Hero Section
st.image(
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c",
    use_column_width=True
)

# Introduction
st.header("Stay Focused. Study Smarter. Achieve More. 🚀")

st.write("""
Welcome to the **Student Productivity Helper**.

This application is designed to help students stay organized,
track their study progress, and improve their productivity.
""")

# Motivational quote
st.info("💡 *Small progress each day adds up to big results.*")

# Feature section
st.subheader("What You Can Do With This App")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📊 Track Study Hours")
    st.write("Log and monitor how many hours you spend studying.")

with col2:
    st.markdown("### ✅ Manage Tasks")
    st.write("Keep track of assignments, projects, and deadlines.")

with col3:
    st.markdown("### 📅 Plan Study Sessions")
    st.write("Organize your study schedule for better productivity.")

# Divider
st.divider()

# Optional progress demo
st.subheader("Daily Motivation Meter")

progress_value = st.slider("How motivated are you today?", 0, 100, 70)

st.progress(progress_value)

if progress_value > 70:
    st.balloons()

# Call to action
st.success("👈 Use the sidebar to navigate through the app pages!")