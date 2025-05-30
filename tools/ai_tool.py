from langchain.utilities import SerpAPIWrapper
from langchain import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from ai_config import SERP_API_KEY, llm_picker
from .prompts import SEARCH_PROMPT, CREATIVE_PROMPT, JOKE_PROMPT

# 1) Pick the LLM
llm = llm_picker("groq")

# 2) Setup tools and chains

# Search chain (outputs a cleaned-up search query)
search_prompt_chain = LLMChain(
    llm=llm,
    prompt=ChatPromptTemplate.from_template(SEARCH_PROMPT)
)

# SerpAPI setup (performs actual search using query)
serp = SerpAPIWrapper(serpapi_api_key=SERP_API_KEY)

# Creative chain
creative_prompt_chain = LLMChain(
    llm=llm,
    prompt=ChatPromptTemplate.from_template(CREATIVE_PROMPT)
)

# Joke chain (final output generator)
joke_prompt_chain = LLMChain(
    llm=llm,
    prompt=ChatPromptTemplate.from_template(JOKE_PROMPT)
)

# 3) run_gpt using sequential calls
def run_gpt(query: str) -> str:
    try:
        # Step 1: Generate search query
        search_query = search_prompt_chain.predict(input=query).strip()
        
        # Step 2: Use SerpAPI to search
        search_results = serp.run(search_query).strip()

        # Step 3: Generate conspiracy story
        conspiracy = creative_prompt_chain.predict(input=search_results).strip()

        # Step 4: Generate final monologue with punchline
        final_monologue = joke_prompt_chain.predict(input=conspiracy).strip()

        return final_monologue

    except Exception as e:
        return "An error occurred: " + str(e)
