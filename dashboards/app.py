import pandas as pd
import streamlit as st

st.title("OpenQC Dashboard")
df = pd.read_csv("data/sample.csv")
st.write(df.describe())
st.line_chart(df["temperature"])
