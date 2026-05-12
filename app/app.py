import streamlit as st
import pandas as pd

st.title("🧬 Breast Cancer AI Platform")

file = st.file_uploader("Upload CSV")

if file:
    df = pd.read_csv(file)
    st.write(df.head())