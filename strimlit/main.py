import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #1a1a1a;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-decoration: underline;'>Palmer Archipelago (Antarctica)</h1>", unsafe_allow_html=True)

st.image('./pinguinos.jpg')

st.selectbox("What would you like to see?", ["by sex", "by islands", "by species"])