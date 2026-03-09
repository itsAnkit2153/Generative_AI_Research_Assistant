import textwrap
from crewai import Task

from agents.research_specialist import research_specialist_agent


research_task = Task(
    agent=research_specialist_agent,

    description=textwrap.dedent("""
        Conduct comprehensive research on the topic: {topic}.

        Your tasks:
        1. Search for the most relevant and recent information about {topic}
        2. Use at most 3 internet searches to gather reliable sources
        3. Extract key facts, statistics, and expert insights
        4. Organize the findings clearly

        Provide the research summary in the following format:

        Title: Research Findings on {topic}

        - Key Findings
        - Important Statistics
        - Expert Opinions
        - Recent Developments
        - Sources
    """),

    expected_output="""
    A structured research summary on {topic} including:
    - Key findings
    - Important statistics
    - Expert insights
    - Recent developments
    - Reliable sources
    """,

    output_file="research_findings.md"
)