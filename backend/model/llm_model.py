from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import certifi

load_dotenv()

os.environ["SSL_CERT_FILE"] = certifi.where()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")

llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    temperature=0.3
)
