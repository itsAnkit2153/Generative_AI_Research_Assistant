import os
from crewai import Agent, LLM
from crewai_tools import FileWriterTool


# LLM configuration
model = os.getenv("WRITER_AGENT_LLM")
temperature = float(os.getenv("WRITER_AGENT_TEMPERATURE"))

llm = LLM(
    model=model,
    temperature=temperature,
    max_tokens=600   # limit output to prevent Groq rate-limit errors
)

content_writer_agent = Agent(
    role="Content Writer",
    goal="Create comprehensive and well-structured reports based on research and analysis.",
    
    backstory=(
        "You are a professional content writer with expertise in transforming complex "
        "research and analytical findings into clear, engaging, and well-structured reports. "
        "You focus on clarity, readability, and accurate citation of sources."
    ),

    llm=llm,
    tools=[FileWriterTool()],
    verbose=True,
)