import streamlit as st
import pandas as pd

st.title("📈 Study Analytics")

if "study_data" not in st.session_state:
    st.session_state.study_data = []

with st.form("study_form"):
    subject = st.text_input("Subject")
    hours = st.slider("Hours Studied", 1, 10)

    submit = st.form_submit_button("Add Study Record")

if submit and subject:
    st.session_state.study_data.append({
        "Subject": subject,
        "Hours": hours
    })
    st.success("Study record added!")

if st.session_state.study_data:

    df = pd.DataFrame(st.session_state.study_data)

    st.subheader("Study Data")
    st.dataframe(df)

    st.subheader("Study Hours by Subject")
    chart = df.groupby("Subject")["Hours"].sum()

    st.bar_chart(chart)

else:
    st.info("No study data added yet.")