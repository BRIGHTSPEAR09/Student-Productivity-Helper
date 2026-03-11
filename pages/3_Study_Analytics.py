import streamlit as st
import pandas as pd
import numpy as np

st.title("📈 Study Analytics")

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
hours = np.random.randint(1,6,7)

data = pd.DataFrame({
    "Day":days,
    "Hours":hours
})

st.subheader("Weekly Study Hours")

st.bar_chart(data.set_index("Day"))

st.subheader("Trend")

st.line_chart(data.set_index("Day"))

st.subheader("Distribution")

st.area_chart(data.set_index("Day"))

st.subheader("Raw Data")

st.dataframe(data)

option = st.multiselect(
    "Select subjects studied",
    ["Math","Science","Programming","History"]
)

st.write("Selected:", option)