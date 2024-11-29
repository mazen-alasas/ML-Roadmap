import streamlit as st

st.title("Basic App")

st.header("Header1")

st.subheader("Subheader")
st.markdown("**Markdown**")

st.caption("Caption")

st.code(
    """
import pandas as pd
df = pd.read_csv("assets/train.csv")
"""
)

st.text("Text element")

st.latex("x = 2 ^ 2")

st.divider()

st.write("After Divider")