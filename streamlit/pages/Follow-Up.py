import streamlit as st
from graph import create_bar_chart
from gets import get_all_info, get_sex, get_island, get_species
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components


st.markdown("<h1 style='text-decoration: underline;'>Penguin follow-up according to ID </h1>", unsafe_allow_html=True)

st.image('./data/culmen_depth.png')

st.sidebar.success("Select an option above 👆🏼 ")

ind_id = st.text_input("Enter the ID of the penguin")

if ind_id:
   data = get_all_info(ind_id)

   df = pd.DataFrame.from_dict(data,orient='index', columns = ['Information'])
   
   st.write(df)


st.markdown("***")

selectbox = st.selectbox("What would you like to see?", ["by sex", "by islands", "by species"])

st.markdown("***")

if selectbox == "by sex":
    data = get_sex()
    graph = create_bar_chart(data, "_id", "count")
elif selectbox == "by islands":
    data = get_island()
    create_bar_chart(data, "_id", "count")
elif selectbox == "by species":
    data = get_species()
    create_bar_chart(data, "_id", "count")
 
 










