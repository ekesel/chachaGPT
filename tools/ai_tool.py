from langchain.utilities import SerpAPIWrapper
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.tools import Tool
from ai_config import SERP_API_KEY, llm_picker
from .prompts import SEARCH_PROMPT, CREATIVE_PROMPT, JOKE_PROMPT, COMBINED_PROMPT

# 1. Pick the LLM
llm = llm_picker("groq")

serp = SerpAPIWrapper(serpapi_api_key=SERP_API_KEY)

search_prompt_runnable = RunnableSequence(
    ChatPromptTemplate.from_template(SEARCH_PROMPT),
    llm
)

creative_prompt_runnable = RunnableSequence(
    ChatPromptTemplate.from_template(CREATIVE_PROMPT),
    llm
)

joke_prompt_runnable = RunnableSequence(
    ChatPromptTemplate.from_template(JOKE_PROMPT),
    llm
)

def search_tool_func(query: str) -> str:
    """
    Generates a refined search query from the user input, performs a SerpAPI search,
    and returns the raw search results.
    """
    # Step 1: Generate a clean search query
    refined_query = search_prompt_runnable.invoke({"input": query}).content.strip()
    # Step 2: Run SerpAPI with the refined query
    results = serp.run(refined_query)
    return results


search_tool = Tool(
    name="web_search",
    func=search_tool_func,
    description="Given a user query, generates a search query, runs SerpAPI, and returns search results."
)

def creative_tool_func(search_results: str) -> str:
    """
    Takes raw search results as input and generates a dramatic conspiracy story.
    """
    story = creative_prompt_runnable.invoke({"input": search_results}).content.strip()
    return story

creative_tool = Tool(
    name="generate_conspiracy",
    func=creative_tool_func,
    description="Given raw search results, generates a creative conspiracy story."
)

def joke_tool_func(conspiracy: str) -> str:
    """
    Takes a conspiracy narrative and produces the final monologue with a punchline.
    """
    monologue = joke_prompt_runnable.invoke({"input": conspiracy}).content.strip()
    return monologue

joke_tool = Tool(
    name="generate_joke_monologue",
    func=joke_tool_func,
    description="Given a conspiracy story, returns a monologue with a punchline."
)

# combined_prompt_template = ChatPromptTemplate.from_template(COMBINED_PROMPT)
system_template = SystemMessagePromptTemplate.from_template(COMBINED_PROMPT)

tools = [search_tool, creative_tool, joke_tool]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={
        "prompt": system_template, 
        "return_direct": True 
    },
)

# 3) run_gpt using sequential calls
def run_gpt(query: str) -> str:
    try:
        return agent.run(query)
    except Exception as e:
        return "An error occurred: " + str(e)
