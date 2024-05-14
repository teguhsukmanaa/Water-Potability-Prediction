import EDA
import prediction
import streamlit as st

PAGES = {
    "Home" : EDA,
    "Data Prediction" : prediction
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to:", list(PAGES.keys()))
page = PAGES[selection]
page.app()