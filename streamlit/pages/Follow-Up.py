import streamlit as st
from graph import create_bar_chart
from gets import get_all_info, get_info
import pandas as pd
import plotly.express as px


st.markdown("<h1 style='text-decoration: underline;'>Penguin follow-up according to ID </h1>", unsafe_allow_html=True)

st.image('./data/culmen_depth.png')

st.sidebar.success("Select an option above 👆🏼 ")

ind_id = st.text_input("Enter the ID of the penguin")

if ind_id:
    data = get_all_info(ind_id)
    graph = create_bar_chart(data, "_id", "Culmen Length (mm)")

























