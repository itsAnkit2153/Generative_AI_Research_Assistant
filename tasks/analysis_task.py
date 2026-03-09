import textwrap
from crewai import Task

from agents.data_analyst import data_analyst_agent
from tasks.research_task import research_task


analysis_task = Task(
    agent=data_analyst_agent,

    description=textwrap.dedent("""
        Analyze the research findings for the topic: {topic}.

        First summarize the research briefly, then perform deeper analysis.

        Your tasks:
        1. Review the research findings from the previous task
        2. Identify patterns, trends, and key insights related to {topic}
        3. Analyze the implications and significance
        4. Provide expert interpretation of the findings
        5. Highlight the most important conclusions

        Keep the response concise (maximum 500 words).

        Provide the analysis in the following structure:

        Title: Comprehensive Analysis Report on {topic}

        - Key Insights
        - Patterns and Trends
        - Implications and Significance
        - Expert Interpretation
        - Actionable Conclusions
    """),

    expected_output="""
    A structured analysis report on {topic} containing:
    - Key insights
    - Identified trends and patterns
    - Interpretation of findings
    - Important conclusions
    """,

    context=[research_task],

    output_file="analysis_report.md"
)