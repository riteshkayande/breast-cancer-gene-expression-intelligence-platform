import streamlit as st
import pandas as pd

st.set_page_config(page_title="Breast Cancer AI Platform", layout="wide")

st.title("🧬 Breast Cancer Gene Expression Platform")

st.success("App is running successfully 🎉")

uploaded_file = st.file_uploader("Upload dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("### Data Preview")
    st.write(df.head())

    st.write("### Shape")
    st.write(df.shape)

    st.write("### Basic Info")
    st.write(df.describe())