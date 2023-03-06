import streamlit as st
from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("url"))
db = client.get_database("midbootcamp")

st.sidebar.success("Select an option above 👆🏼 ")

st.markdown("<h1 style='text-decoration;'>Sign up to our community!</h1>", unsafe_allow_html=True)



st.image('./data/logo.png')

st.markdown(
        '''
                 Create an account with us and be part of our community!
        '''
    )

st.markdown("***")

def save_credentials(username, password):
    existing_user = db.credentials.find_one({"username":username})
    if existing_user:
        st.warning("Username/password already exists. Please choose another username.")
    else:
        db.credentials.insert_one({"username": username, "password": password})
        st.success("Credentials saved!")

def check_credentials(username, password):
    existing_user = db.credentials.find_one({"username":username})
    if existing_user:
        st.success("Thank you so much! Please enter the data of the new penguin")
    else:
        st.warning("Username/password already exists. Please choose another username.")
              

with st.form(key='my_form'):
   username = st.text_input('Username')
   password = st.text_input('Password', type='password')
   submitted = st.form_submit_button('Register')
   sign_in = st.form_submit_button('Sign-In')
   if submitted:
        save_credentials(username, password)
   elif sign_in:
       existing_user = db.credentials.find_one({"username":username})
       if existing_user:
        st.success("sign in successfully")

if sign_in:
        st.success("Thank you so much! Please enter the data of the new penguin")
        with st.form(key='my_forms'):
            IndividualID = st.text_input('Individual ID  (N1A1)')
            Species = st.text_input('Species  (Adelie)')
            Island = st.text_input('Island  (Torgersen)')
            culmen_length = st.text_input('culmen_length_mm  (39.1)')
            culmen_depth = st.text_input('culmen_depth_mm  (18.7)')
            flipper_length = st.text_input('flipper_length_mm  (181)')
            body_mass = st.text_input('body_mass_g  (3750)')
            sex = st.text_input('sex  (MALE)')
            sign_in = st.form_submit_button('Submit a new penguin')
        if sign_in:
            db.credentials.insert_one({"Individual ID":IndividualID},{"species":Species},{"island":Island},{"culmen_length_mm":culmen_length},{"culmen_depth_mm":culmen_depth},{"flipper_length_mm":flipper_length},{"body_mass_g":body_mass},{"sex":sex})
        
         




   