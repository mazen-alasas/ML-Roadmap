import streamlit as st
import pandas as pd

st.header("Button")
primary_btn = st.button(
    label="Primary",
    type="primary"
)

secondary_btn = st.button(
    label='Secondary',
    type='secondary'
)

if primary_btn:
    st.write("Primary")
if secondary_btn:
    st.write("Secondary")

st.divider()

st.header("Radio Button")
df = pd.read_csv("assets/sample.csv")

radio = st.radio(
    "Choose a column",
    options=df.columns[1:],
    index=1,
    horizontal=True
)

st.write(radio)

st.divider()

st.header("Select Box")
select = st.selectbox(
    "Choose a column",
    options=df.columns[1:],
    index=0
)
st.write(select)

st.divider()

st.header("Checkbox")

checkbox = st.checkbox("Remember Me")

if checkbox:
    st.write("I will")
else:
    st.write("I won't")

st.divider()

st.header("Multi Select")
multiselect = st.multiselect(
    "Choose as many columns as you want",
    options=df.columns[1:],
    default=["col2"],
    max_selections=2
)
st.write(multiselect)

st.divider()

st.header("Slider")

slider = st.slider(
    "Pick a number",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.1
)

st.divider()

st.header("Text Input")
text_input = st.text_input(
    "What's your name?",
    placeholder="Hero"
)
st.write(f"Your name is {text_input}")

st.divider()

st.header("Number Input")
num_inp = st.number_input(
    "Pick a Number",
    min_value=0,
    max_value=10,
    value=0,
    step=1
)

st.divider()

st.header("Text Area")
text_area = st.text_area(
    "Text Area",
    height=500,
    placeholder="Write your message here"
)