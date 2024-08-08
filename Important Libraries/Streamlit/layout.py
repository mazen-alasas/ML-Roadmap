import streamlit as st
import pandas as pd


with st.sidebar:

    st.write("Sidebar Text")

col1, col2, col3 = st.columns(3)

col1.write("Col Text")

slider = col2.slider(
    "Choose a number",
    min_value=0,
    max_value=10
)

col3.write(slider)

st.header("Tabs")

df = pd.read_csv("assets/sample1.csv")

tab1, tab2 = st.tabs(
    ['Line plot', 'Bar Plot']
)

with tab1:
    tab1.write("A Line Plot")
    st.line_chart(
        df,
        x='year',
        y=['col1', 'col2', 'col3']
    )

with tab2:
    tab2.write("A Bar Plot")
    st.bar_chart(
        df,
        x='year',
        y=['col1', 'col2', 'col3']
    )

with st.expander("Click to expand"):
    st.write("I am text that you only see when you expand")


st.header("Container")

with st.container():
    st.write("Inside Container")

st.write("Outside Container")