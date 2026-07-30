import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Simple Form",
    page_icon=":smiley:",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "Simple Streamlit demo app"
    }
)

import streamlit as st
st.title("House Price Prediction")

area = st.number_input(
    "Area (m²)",
    min_value=50,
    max_value=1000,
    step=10
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    step=1
)

owner = st.text_input(
    "Owner Name",
    placeholder="Enter owner's name"
)

description = st.text_area(
    "Property Description",
    placeholder="Write additional details..."
)

st.write("Area:", area)
st.write("Bedrooms:", bedrooms)
st.write("Owner:", owner)
st.write("Description:", description)