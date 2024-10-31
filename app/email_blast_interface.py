#%% STREAMLIT FRONTEND FOR HPG EMAIL BLAST

#%% Imports

import streamlit as st
import pandas as pd

#%% Set up HPG Auth (enable in prod)

def authenticate():
    st.sidebar.header('Login')
    entered_password = st.sidebar.text_input("Password", type='password')
    
    # Access the password from secrets
    correct_password = st.secrets["authentication"]["password"]

    if entered_password == correct_password:
        return True
    elif entered_password:
        st.sidebar.error("Incorrect password")
    return False

#%% Main Page

st.set_page_config(layout="wide")

if authenticate(): # (enable in prod)
    st.title("HPG Email Blaster")
    st.subheader("Follow the prompts below to send out emails.")
    st.text_area("Input HTML Here (see example at bottom of page)")
    st.write("Create a .csv file that has the following columns: 'email', 'name'. Additionally, the file should have a column for any other inputs in your email. Match the column name to the variable inputs in your email html.")
    dump = st.file_uploader("Dump CSV here",'csv')
    if dump is not None:
        emails = pd.read_csv(dump)
        emails

    send = st.button("Send All")

    st.subheader("See below for an example of html text to update")
    st.write("""
        <p>Hey {name},</p>

        <p>My name is Dan Bannon, and I am a partner at the Handy Point Group, a technology firm that builds custom tools for youth sports organizations like yours. I’m also a high school baseball coach, and I understand the pain of staying organized in a sports setting. While researching baseball organizations in {state}, I found {organization}, and thought you might be interested.</p>

        <p>Recently, we worked with the other coaches on my team to deliver a simple, customized, web application where all the coaches can access and share information. The app works on mobile phones and tablets, and allows coaches to input notes, design practices, and view player information with ease. Since implementation, the team’s coaches have not only saved time and effort, but they’ve also stayed more connected to other coaches and aware of each player’s development.</p>

        <p>{organization} could be a fit to implement this app. We believe it will give you a leg up on the competition in {state}.</p>

        <p>If this sounds interesting to you, I’d be happy to share a case study document for the app, and a link to a live demo that you can interact with. If you are all squared away with your tech needs, let us know and we won’t reach out again.</p>

        <p>Best,<br>Dan</p>
        <p>
        <strong>Dan Bannon</strong><br>
        <i>Partner</i><br>
        Handy Point Group<br>
        213-361-1583<br>
        dan@handypointgroup.com<br>
        <a href="https://www.handypointgroup.com">www.handypointgroup.com</a>
        </p>
        """
    )