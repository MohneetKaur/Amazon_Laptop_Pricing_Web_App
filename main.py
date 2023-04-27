import streamlit as st
import app
import eda

PAGES = {
    "Home": app,
    "EDA": eda
}

st.set_page_config(layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", list(PAGES.keys()))

# Run the app
PAGES[page].run()
