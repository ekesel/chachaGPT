cd chachaGPT
python3 -m venv venv
source venv/bin/activate
pip install fastapi[all] jinja2
pip install langchain langgraph openai groq
pip install -U langchain-community
pip install langchain-openai
pip install langchain-groq
pip install google-search-results
pip install groq


model used - llama-3.3-70b-versatile