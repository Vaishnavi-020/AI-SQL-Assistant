from .prompt_template import get_prompt,analysis_prompt
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import streamlit as st
from backend.database.schema_loader import load_schema
import certifi

load_dotenv()

os.environ["SSL_CERT_FILE"] = certifi.where()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    GROQ_API_KEY=st.secrets["GROQ_API_KEY"]
llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    temperature=0.3
)



