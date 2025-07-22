import json
import requests
import streamlit as st
from openai import AzureOpenAI
import base64
import os
from gtts import gTTS
import tempfile
import uuid
from mslearnvoiceui import voicemain
from aiassess import assesmentmain
from stfinetuneasses import finetuneassesment
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use the wide layout
st.set_page_config(
    page_title="AI Assesment and Learn",
    layout="wide"  # 'centered' is default; use 'wide' for full page width
)

# Sidebar navigation
nav_option = st.sidebar.selectbox("Navigation", ["Home", 
                                                "MS Learn",
                                                "AI Assesment",
                                                "Fine Tuning Assesment",
                                                "About"])

# Display the selected page
if nav_option == "Home":
    assesmentmain()
elif nav_option == "MS Learn":
    voicemain()
elif nav_option == "AI Assesment":
    assesmentmain()
elif nav_option == "Fine Tuning Assesment":
    finetuneassesment()
else:
    voicemain()
