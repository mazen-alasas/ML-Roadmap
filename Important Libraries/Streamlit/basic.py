import streamlit as st
import pandas as pd

df = pd.read_csv("assets\\train.csv")

st.header("Basic App")
st.subheader("Learning StreamLit")
st.title("StreamLit | Tutorials")

st.text("Hello World")

original_text = '<p style="font-family: Courier; color: Blue; font-size: 20px;">Hello World</p>'
st.markdown(original_text, unsafe_allow_html=True)

new_text = '<p style="font-family: sans-serif; color: Green; font-size: 42px;">Hello World</p>'
st.markdown(new_text, unsafe_allow_html=True)

st.success("Success")
st.warning("This is a warning message")
st.error("Error")

st.header("Dataframe")
st.write(df)


st.header("Buttons for Uploading Files")
files_bytes = st.file_uploader("Upload a CSV file", type="csv")