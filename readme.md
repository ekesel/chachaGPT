# 🔮 CHACHA-GPT

CHACHA-GPT is a FastAPI-based AI assistant that leverages GROQ’s blazing-fast LLaMA 3.3 70B Versatile model with LangChain, LangGraph, OpenAI, and Google SERP for advanced agentic tasks like search, creativity, and humor generation.

---

## 🚀 Features

- ✨ Agentic multi-step workflows using `LangGraph`
- ⚡ Super-fast responses with `GROQ` + `LLaMA 3.3 70B Versatile`
- 🔍 Web search powered by `Google SERP API`
- 🤖 Flexible architecture with support for OpenAI and Groq models
- 🧠 LangChain integration for prompt and tool orchestration
- 📄 HTML templating with Jinja2 for web response rendering

---

## 🧱 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [GROQ](https://groq.com/)
- [OpenAI](https://openai.com/)
- [Google SERP API](https://serpapi.com/)
- [Jinja2](https://palletsprojects.com/p/jinja/)

---

## 🛠 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chachaGPT.git
cd chachaGPT
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements

Install from the provided requirements.txt:

```bash
pip install -r requirements.txt
```

or install manually

```bash
pip install fastapi[all] jinja2
pip install langchain langgraph openai groq
pip install -U langchain-community
pip install langchain-openai
pip install langchain-groq
pip install google-search-results
pip install groq
```

### 4. 🔑 Environment Variables

Create a .env file based on the template below:
.env.example

```bash
# GROQ LLM
GROQ_API_KEY=""
GROQ_MODEL="llama-3.3-70b-versatile"

# OPENAI LLM (Optional)
OPENAI_API_KEY=""
OPENAI_MODEL=""

# SERP API KEY FOR WEBSEARCH
SERP_WEB_API_KEY=""
```
✅ Rename .env.example to .env and fill in the API keys.

### 🧪 Run the App
```bash
uvicorn app.main:app --reload
```

Navigate to http://127.0.0.1:8000 or the API docs at http://127.0.0.1:8000/docs.


### 📦 Project Structure

```bash
chachaGPT/
├── app/
│   ├── main.py           # FastAPI app entrypoint
│   ├── ai_config.py      # LLM PICKER LOGIC
│   ├── prompts.py        # CHACHA, SEARCH, JOKE, CREATIVE prompts
│   └── templates/        # Jinja2 templates
│   └── tools/            # LangChain, LangGraph Logic
├── .env.example
├── requirements.txt
├── README.md
└── venv/
```

### 🤝 Contributing

Pull requests and suggestions are welcome!
For major changes, please open an issue first.

### 🙏 Acknowledgments
LangChain
GROQ
OpenAI
LangGraph
FastAPI