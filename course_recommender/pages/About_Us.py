
import streamlit as st
# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="About Us"
)
# endregion <--------- Streamlit App Configuration --------->

st.title('About this app')
st.text("This is a streamlit app that demonstrates how to use the OpenAI API to generate text completions.")
with st.expander('How to use this app.'):
    st.markdown("1. Enter your prompt in the chat area.")
    st.markdown("2. Click the 'Submit' button")
    st.markdown("3. The app will generate a text completion based on your prompt.")
