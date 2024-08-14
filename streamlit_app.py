import streamlit as st
import pandas as pd

st.title("Mpox Dashboard")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({'first column': [1, 2, 3, 4], 'second column': [10, 20, 30, 40]}))
