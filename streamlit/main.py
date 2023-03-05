import streamlit as st
import io
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

st.markdown("<h1 style='text-decoration: underline;'>Palmer Archipelago (Antarctica)</h1>", unsafe_allow_html=True)
st.subheader("Discover the three types of species that inhabit this wonderful archipelago and their characteristics")

st.markdown("***")

st.image('./data/palmer.png')


selected2 = option_menu(None, [ "Chinstrap", 'Gentoo', "Adelie"], 
    icons=['body-text', 'body-text', "body-text"], 
    menu_icon="cast", default_index=1, orientation="horizontal")




if selected2 == "Chinstrap":
    st.markdown("***")

    st.markdown(
        '''
                # **Chinstrap Penguins!**
        '''
    )

    st.markdown("***")

    st.markdown(
        '''
            Instantly recognizable by the black band that gives them their name, chinstrap penguins are the most abundant penguin in the Antarctic, where they gather in massive breeding colonies.

After spending the winter north of the sea ice, chinstraps return in late October or early November to their nest sites, usually with the same breeding partners. These colonies are on the rocky, ice-free coasts of the South Sandwich Islands, South Shetland Islands, and Antarctic continent.

The sheer number of birds in the colonies is astounding. The largest colony, on the uninhabited South Sandwich island of Zavodovski, hosts some 1.2 million breeding pairs. Baily Head in the South Shetland Islands is home to more than 100,000 pairs.
        '''
)
    st.subheader("Breeding and nesting")



    st.markdown(
        '''
A female chinstrap typically will lay two eggs in a circular nest made from stones. The parents share egg-sitting duties, each spending several days on the nest before a shift change. After about 37 days, the chicks hatch. They spend another few weeks in the nest, then waddle into a crèche, where the fluffy, gray juveniles are cared for communally. At around two months old, they get their adult feathers and are able to head to sea.
'''
)   
    
    st.subheader("Threats")    

    st.markdown(
        '''
In the water, where they feed primarily on krill, the penguins main predator is the leopard seal. On land, chinstraps face threats from skuas, giant petrels, and other birds that steal the penguins eggs and attack chicks, as well as a more unusual threat: volcanic activity. An ill-timed eruption in 2016 on Zavodovski Island covered much of the colony in ash as the birds were undergoing their annual molt. During molt, when they lose their waterproof feathers, they are land-locked and cant go in the sea until their feathers regrow.

Chinstrap penguin numbers increased in the mid-20th century, attributed by some to the rebound of krill from centuries of seal and whale hunting. Today, some populations are declining, though not precipitously. Restrictions are in place to keep tourists from approaching breeding birds too closely.
        '''
)

    st.image('./data/chinstrap_penguin.jpg')

if selected2 == "Adelie":
    st.markdown("***")
    st.markdown(
        '''
                # **Adelie Penguins!**
        '''
    )

    st.markdown("***")

    st.markdown(
        '''
            Adélie penguins live on the Antarctic continent and on many small, surrounding coastal islands. They spend the winter offshore in the seas surrounding the Antarctic pack ice.
            '''
    )

    st.subheader("Diet") 
    st.markdown(
        '''

Adélies feed on tiny aquatic creatures, such as shrimp-like krill, but also eat fish and squid. They have been known to dive as deep as 575 feet in search of such quarry, though they usually hunt in far shallower waters less than half that depth.

Like other penguins, Adélies are sleek and efficient swimmers. They may travel 185 miles round-trip to procure a meal.
'''
    )

    st.subheader("Breeding")

    st.markdown(
        '''

During the spring breeding season (in October), they take to the rocky Antarctic coastline where they live in large communities called colonies. These groups can include thousands of birds.

Once on land, Adélies build nests and line them with small stones. Though they move with the famed “penguin waddle” they are capable walkers who can cover long overland distances. In early spring, before the vast sheets of ice break up, they may have to walk 31 miles from their onshore nests to reach open water.

Male Adélie penguins help their mates rear the young and, without close inspection, the two sexes are nearly indistinguishable. They take turns sitting on a pair of eggs to keep them warm and safe from predators. When food is short, only one of the two chicks may survive. After about three weeks, parents are able to leave the chicks alone, though the offspring gather in groups for safety. Young penguins begin to swim on their own in about nine weeks.
        '''
)

    st.image('./data/adelie_penguin.jpg')


        
if selected2 == 'Gentoo':
    st.markdown("***")
    st.markdown(
        '''
                # **Gentoo Penguins!**
        '''
    )

    st.markdown("***")

    st.markdown(
        '''
           With flamboyant red-orange beaks, white-feather caps, and peach-colored feet, gentoo penguins stand out against their drab, rock-strewn Antarctic habitat.
           '''
    )

    st.subheader("Habitat")
    st.markdown(
        '''

These charismatic waddlers, who populate the Antarctic Peninsula and numerous islands around the frozen continent, are the penguin worlds third largest members, reaching a height of 30 inches and a weight of 12 pounds.

Gentoos are partial to ice-free areas, including coastal plains, sheltered valleys, and cliffs. They gather in colonies of breeding pairs that can number from a few dozen to many thousands.
    '''
    )

    st.subheader("Parenting")

    st.markdown(
        '''

Gentoo parents, which often form long-lasting bonds, are highly nurturing. At breeding time, both parents will work to build a circular nest of stones, grass, moss, and feathers. The mother then deposits two spherical, white eggs, which both parents take turns incubating for more than a month. Hatchlings remain in the nest for up to a month, and the parents alternate foraging and brooding duties.
     '''
    )

    st.subheader("Hunting")
    st.markdown(
        '''

Adults spend the entire day hunting, usually close to shore, but occasionally ranging as far as 16 miles out. When pursuing prey, which includes fish, squid, and krill, they can remain below for up to seven minutes and dive as deep as 655 feet.
        '''
    )

    st.image('./data/gento_penguin.jpg')
    







st.sidebar.success("Select an option above 👆🏼 ")

st.markdown("*********")

st.subheader("Small video where you can see these beautiful penguins in their natural habitat and interacting with each other")

st.markdown("*********")

video_file = open('./data/Manchots_adelie.ogv.240p.webm', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)