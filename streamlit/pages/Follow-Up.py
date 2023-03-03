import streamlit as st
#from graph import generate_graph
from gets import get_all_info, get_info
import pandas as pd
import plotly.express as px


st.markdown("<h1 style='text-decoration: underline;'>Penguin follow-up according to ID </h1>", unsafe_allow_html=True)

st.image('./data/background.png')

penguin_id = st.text_input("Enter the ID of the penguin")

data = get_info(penguin_id)
st.text(data[0])
           
def generate_graph(penguin_id):
    data = get_info(penguin_id)
    data.pop("_id")
    if st.button("Generate Graph"):
        if "ERROR" in data:
            st.write(data["ERROR"])
        else:
            fig = px.scatter(data[0], x='culmen_length_mm', y='culmen_depth_mm', size='body_mass_g', color='species',
                             hover_data=['_id', 'island', 'flipper_length_mm', 'sex'])
            fig.update_layout(title=f"Information of Penguin with ID {penguin_id}")
            st.plotly_chart(fig)



if penguin_id:
    penguin_data = get_info(penguin_id)
    if "ERROR" in penguin_data:
        st.write(penguin_data["ERROR"])
    else:
        fig = generate_graph(penguin_data)
        st.plotly_chart(fig)






















#pinguins_ident = st.text_input("Please select an ID: ", value=1)
#group = pick_one.pick()

#dt = get_id_follow_up(pinguins_ident, group)s
#specie = [penguin["Species"] for penguin in dt]
#id = [penguin["Individual ID"]for penguin in dt]

#if "Gentoo" in specie:
#     st.header(id)
#     st.text(specie)
#     st.image('.data/gento_penguin.jpg')
#elif "Adelie" in specie:
#     st.header(id)
#     st.text(specie)
#     st.image('.data/adelie_penguin.jpg')
#elif "chinstrap" in specie:
#     st.header(id)
#     st.text(specie)
#     st.image('.data/chinstrap_penguin.jpg')
#

