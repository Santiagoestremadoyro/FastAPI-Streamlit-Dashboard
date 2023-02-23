import streamlit as st
from gets import get_sex
from router.pinguins import get_pinguins, get_pinguins_i, get_pinguins_s

st.markdown("<h1 style='text-decoration: underline;'>Palmer Archipelago (Antarctica)</h1>", unsafe_allow_html=True)

st.image('./data/pinguinos.jpg')

selectbox = st.selectbox("What would you like to see?", ["by sex", "by islands", "by species"])




if selectbox == "by sex":
    data = get_pinguins
    create_bar_chart(data, "sex", "count")
elif selectbox == "by islands":
    data = get_pinguins_i
    create_bar_chart(data, "island", "count")
elif selectbox == "by species":
    data = get_pinguins_s
    create_bar_chart(data, "species", "count")