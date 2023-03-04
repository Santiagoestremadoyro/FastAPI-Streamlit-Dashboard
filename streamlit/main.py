import streamlit as st
from gets import get_sex, get_island, get_species
from graph import create_bar_chart
import io
import pdfkit
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.markdown("<h1 style='text-decoration: underline;'>Palmer Archipelago (Antarctica)</h1>", unsafe_allow_html=True)
st.subheader("Discover the three types of species that inhabit this wonderful archipelago and their characteristics")

st.markdown("***")

st.image('./data/palmer.png')

st.sidebar.success("Select an option above 👆🏼 ")

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

st.markdown("***")

st.markdown(
        '''
                # **Chinstrap Penguins!**
        '''
    )

st.markdown("***")

st.markdown(
        '''
            Chinstrap penguins have an average height of 72 cm and a weight of 3-5 kg, however their weight can decrease to 3 kg based on the breeding cycle.

The flippers of adult chinstrap penguins are black with a white border: the inner sides of the flippers are white. The white face extends to behind the eyes, which are reddish brown; the chin and throat are also white, while the short beak they have is black. The strong legs are pink, also its short and flattened legs give it a characteristic style of waddling when walking. The chinstrap penguin's black and white plumage helps camouflage it in the water from predators such as seals. When the penguin is observed from above, the bird's black back blends into the dark-colored water of the seabed, likewise the bird's underside blends into the sun when viewed from the seabed.
        '''
)

st.image('./data/chinstrap_penguin.jpg')



st.markdown(
        '''
                # **Gentoo Penguins!**
        '''
)

st.markdown("***")

st.markdown(
        '''
           The gentoo penguin is easily recognized by the wide, white stripe extending like a bonnet across the top of its head and its bright orange-red bill. It has pale whitish-pink, webbed feet and a fairly long tail the most prominent tail of all penguin species. Chicks have grey backs with white fronts. As the gentoo penguin waddles along on land, its tail sticks out behind, sweeping from side to side, hence the scientific name Pygoscelis, which means "rump-tailed. Gentoo penguins can reach a height of 51 to 90 cm (20 to 35 in), making them the third-largest species of penguin after the emperor penguin and the king penguin. Males have a maximum weight around 8.5 kg (19 lb) just before molting and a minimum weight of about 4.9 kg (11 lb) just before mating. For females, the maximum weight is 8.2 kg (18 lb) just before molting, but their weight drops to as little as 4.5 kg (9.9 lb) when guarding the chicks in the nest."
        '''
    )

st.image('./data/gento_penguin.jpg')




st.markdown(
        '''
                # **Adelie Penguins!**
        '''
)

st.markdown("***")

st.markdown(
        '''
            The Adélie penguin is a mid-sized bird, measuring 70-73 cm (28-29 in) in length and weighing 3.8 to 8.2 kg (8.4 to 18.1 lb). Although the sexes look the same, 
females have shorter wings and beaks, and weigh significantly less. The adult is black on the head, throat and upperparts, with snowy white underparts. It has a conspicuous 
white eye ring around a black iris. The beak is largely covered with black feathers, leaving only the tip exposed; this is primarily black, though it can show indistinct reddish-brown
markings. The upper surface of the wing is black with a white trailing edge, while the underside is white with a narrow black leading edge and a small black tip. The legs and feet,
which are mostly unfeathered, are pinkish.
        '''
)

st.image('./data/adelie_penguin.jpg')



st.markdown("***")




