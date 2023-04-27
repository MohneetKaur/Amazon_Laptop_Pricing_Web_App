import streamlit as st
import pandas as pd
from PIL import Image
import base64
import os


def run():

    st.markdown("###### Company v/s Price")
    image = Image.open('company_price.png')
    st.image(image, use_column_width=True)


    st.markdown("###### CPU Brand v/s Price")
    image = Image.open('cpubrand_price.png')
    st.image(image, use_column_width=True)

    st.markdown("###### GPU Brand v/s Price")
    image = Image.open('gpubrand_price.png')
    st.image(image, use_column_width=True)

    st.markdown("###### Operating System v/s Price")
    image = Image.open('os_price.png')
    st.image(image, use_column_width=True)

    st.markdown("###### RAM v/s Price")
    image = Image.open('ram_price.png')
    st.image(image, use_column_width=True)

    st.markdown("###### Touch Screen v/s Price")
    image = Image.open('touchscreen_price.png')
    st.image(image, use_column_width=True)

    st.markdown("###### Type of Laptop v/s Price")
    image = Image.open('typename_price.png')
    st.image(image, use_column_width=True)

    st.markdown("###### Weight of Laptop v/s Price")
    image = Image.open('weight_price.png')
    st.image(image, use_column_width=True)


