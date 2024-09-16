import streamlit as st
from logics.customer_query_handler import process_user_message
from helper_functions.data_loader import open_courses

st.set_page_config(
    layout="centered",
    page_title="Course Query App"
)

st.title("Course Query App")

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

data = open_courses(output=1) 

if form.form_submit_button("Submit"):
    st.toast(f"Submitted - '{user_prompt}'")
    try:
        response = process_user_message(user_prompt)  # Process the user message
        st.write(response)  # Display the response

        result = [data[course] for course in data if course in response]
        if len(result)>0:
            st.dataframe(result)

    except Exception as e:
        st.error(f"An error occurred: {e}")
    print(f"User Input is {user_prompt}")
