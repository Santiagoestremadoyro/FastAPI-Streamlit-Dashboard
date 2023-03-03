import streamlit as st
from gets import get_sex, get_island, get_species
from graph import create_bar_chart
import io
import pdfkit



st.markdown("<h1 style='text-decoration: underline;'>Palmer Archipelago (Antarctica)</h1>", unsafe_allow_html=True)

st.image('./data/pinguinos.jpg')

st.sidebar.success("Select an option above 👆🏼 ")

selectbox = st.selectbox("What would you like to see?", ["by sex", "by islands", "by species"])






"""""
if selectbox == "by sex":
    data = get_sex()
    download_report(data, "_id", "count")
elif selectbox == "by islands":
    data = get_island()
    download_report(data, "_id", "count")
elif selectbox == "by species":
    data = get_species()
    download_report(data, "_id", "count")
"""










if selectbox == "by sex":
    data = get_sex()
    graph = create_bar_chart(data, "_id", "count")
elif selectbox == "by islands":
    data = get_island()
    create_bar_chart(data, "_id", "count")
elif selectbox == "by species":
    data = get_species()
    create_bar_chart(data, "_id", "count")

