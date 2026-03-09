import os
from crewai import Agent, LLM
from crewai_tools import SerperDevTool


# LLM configuration
model = os.getenv("RESEARCH_AGENT_LLM")
temperature = float(os.getenv("RESEARCH_AGENT_TEMPERATURE"))

llm = LLM(
    model=model,
    temperature=temperature,
    max_tokens=400   # limit response size
)

# Limit search results to reduce token usage
search_tool = SerperDevTool(n_results=3)

research_specialist_agent = Agent(
    role="Research Specialist",
    goal="Gather accurate and relevant information on given topics from reliable sources.",
    
    backstory=(
        "You are an expert research specialist skilled at finding reliable and up-to-date "
        "information quickly. You focus on extracting the most relevant facts, statistics, "
        "and insights from trusted sources."
    ),

    llm=llm,
    tools=[search_tool],
    verbose=True
)