
import streamlit as st

import streamlit as st

import numpy as np
import streamlit.components.v1 as components
import validators

# embed streamlit docs in a streamlit app
# components.iframe("https://docs.streamlit.io/en/latest")
# url = "https://www.cnn.com/2021/07/12/health/us-coronavirus-monday/index.html"





def main():
    st.set_page_config(layout="wide")

    user_input = st.text_input("Add VALID URL here", "")

    url = user_input

    
    valid=validators.url(url)
    
    if valid:

        components.iframe(url, 1700, 900)
    


main()

