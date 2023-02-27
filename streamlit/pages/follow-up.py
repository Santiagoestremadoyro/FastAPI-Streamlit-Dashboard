import streamlit as st
from gets import get_id_follow_up
from graph import create_bar_chart

st.markdown("<h1 style='text-decoration: underline;'>Penguin follow-up according to ID </h1>", unsafe_allow_html=True)

st.image('./data/background.png')

class pick_one:
        def pick():
               with st.sidebar:
                 st.header("Select family")
                 info = st.slider("Pick", 0, 2)
                 return int(info)
                

pinguins_ident = st.text_input("Please select an ID: ", value=1)
group = pick_one.pick()

dt = get_id_follow_up(pinguins_ident, group)
species = [penguin["species"] for penguin in data]


