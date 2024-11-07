import streamlit as st
from pymongo import MongoClient
import pandas as pd

def login():
    st.title("Login to PawSome AI")
    client = MongoClient('mongodb+srv://harsh:harsh123@cluster0.ips03mz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

    db = client['paw_some_ai']
    collection = db['users']
    collection.insert_one({"name": "yash"})
    
    # Username and password input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Initialize login state
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    # Login button logic
    if st.button("Login"):
        if username == "admin" and password == "password":  # Replace with your own authentication logic
            st.session_state['logged_in'] = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

def logout():
    # Set logged_in to False to log out the user
    st.session_state['logged_in'] = False
    st.info("You have been logged out.")