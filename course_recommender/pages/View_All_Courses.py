import json
import pandas as pd
import streamlit as st
from helper_functions.data_loader import open_courses

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="View all courses"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("View all courses")

st.dataframe(open_courses(output=2))
