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
    db.credentials.insert_one({"username": username, "password": password})
    st.success("Credentials saved!")

with st.form(key='my_form'):
   username = st.text_input('Username')
   password = st.text_input('Password', type='password')
   submitted = st.form_submit_button('Register')
   if submitted:
        save_credentials(username, password)

