import os
from crewai import Agent, LLM


# LLM configuration
model = os.getenv("ANALYST_AGENT_LLM")
temperature = float(os.getenv("ANALYST_AGENT_TEMPERATURE"))

llm = LLM(
    model=model,
    temperature=temperature,
    max_tokens=500
)

data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Analyze gathered information to extract key insights, patterns, and conclusions",

    backstory=(
        "You are a skilled data analyst who specializes in interpreting research findings. "
        "You identify patterns, trends, and meaningful insights from information and "
        "present them clearly for decision making."
    ),

    llm=llm,
    verbose=True
)