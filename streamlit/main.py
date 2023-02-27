import streamlit as st
from gets import get_sex, get_island, get_species
from graph import create_bar_chart

st.markdown("<h1 style='text-decoration: underline;'>Palmer Archipelago (Antarctica)</h1>", unsafe_allow_html=True)

st.image('./data/pinguinos.jpg')

st.sidebar.success("select an option above")

selectbox = st.selectbox("What would you like to see?", ["by sex", "by islands", "by species"])
data = get_island()


if selectbox == "by sex":
    data = get_sex()
    graph = create_bar_chart(data, "_id", "count")
elif selectbox == "by islands":
    data = get_island()
    create_bar_chart(data, "_id", "count")
elif selectbox == "by species":
    data = get_species()
    create_bar_chart(data, "_id", "count")



st.text_input("Enter the IP address of the penguin:")