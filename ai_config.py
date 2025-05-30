from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

SERP_API_KEY = os.getenv("SERP_WEB_API_KEY")

openai_llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

groq_llm = ChatGroq(
    model=os.getenv("GROQ_MODEL"),
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

def llm_picker(model):
    if model == "openai":
        return openai_llm
    elif model == "groq":
        return groq_llm