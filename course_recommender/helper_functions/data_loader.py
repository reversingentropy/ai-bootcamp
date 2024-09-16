import json
import pandas as pd
import streamlit as st

@st.cache_data
def open_courses(path=r'data/courses-full.json', output=1):
    """
    Loads and optionally converts a JSON file containing course data into a DataFrame.

    Parameters:
    - path (str): The file path to the JSON file. Default is 'data/courses-full.json'.
    - output (int): Determines the format of the output data. 
        - If output is 1, the function returns the data as a Python list (default behavior).
        - If output is 2, the function converts the data into a pandas DataFrame and returns it.

    Returns:
    - Depending on the value of `output`:
        - If `output` is 1, returns the data as a list.
        - If `output` is 2, returns the data as a pandas DataFrame.
    
    Example:
    >>> data_list = open_courses()  # returns data as a list
    >>> data_df = open_courses(output=2)  # returns data as a DataFrame
    
    Notes:
    - The function uses Streamlit's caching mechanism to avoid reloading the data on every run, improving performance.
    - Ensure that the JSON file is properly formatted and contains data that can be converted into a DataFrame if output is set to 2.
    """
    with open(path, 'r') as file:
        data = json.load(file)
    if output == 2:
        data = pd.DataFrame(data)  # Converts JSON to a DataFrame
    return data