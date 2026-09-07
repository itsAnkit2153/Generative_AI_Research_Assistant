import os
from crewai import Agent, LLM

# LLM configuration
model = os.getenv("WRITER_AGENT_LLM")
temperature = float(os.getenv("WRITER_AGENT_TEMPERATURE"))

llm = LLM(
    model=model,
    temperature=temperature,
    max_tokens=250   # slightly reduced for safety
)

content_writer_agent = Agent(
    role="Content Writer",
    goal="Create comprehensive and well-structured reports based on research and analysis.",

    backstory=(
        "You are a professional content writer with expertise in transforming complex "
        "research and analytical findings into clear, engaging, and well-structured reports. "
        "You focus on clarity, readability, and accuracy."
    ),

    llm=llm,

    # ❌ REMOVED FileWriterTool (VERY IMPORTANT)
    # tools=[FileWriterTool()],

    verbose=True,
)
