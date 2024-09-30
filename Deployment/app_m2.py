import streamlit as st
import EDA_m2, predict_m2

st.set_page_config(page_title="Churn_checking", layout="wide", initial_sidebar_state="auto")

st.sidebar.title("Navigation")
nav = st.sidebar.selectbox("Go To", ["EDA", "predict"])
if nav == "EDA":
    EDA_m2.run()
else:
    predict_m2.run()
