import streamlit as st

st.title("📂 Assignment Upload")

uploaded_file = st.file_uploader(
    "Upload your assignment",
    type=["pdf","docx","txt"]
)

if uploaded_file:
    st.success("File uploaded successfully!")

    st.write("Filename:", uploaded_file.name)
    st.write("File type:", uploaded_file.type)

agree = st.toggle("Confirm submission")

if agree:
    st.toast("Assignment submitted!")