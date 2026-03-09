import textwrap
from crewai import Task

from agents.content_writer import content_writer_agent
from tasks.analysis_task import analysis_task
from tasks.research_task import research_task


writing_task = Task(
    agent=content_writer_agent,

    description=textwrap.dedent("""
        Create a comprehensive report on the topic: {topic}.

        Review both the research findings and analysis results before writing.

        Your tasks:
        1. Summarize the key research findings about {topic}
        2. Integrate the insights from the analysis report
        3. Write a clear, structured, and professional report
        4. Ensure the report is easy to read and logically organized
        5. Cite the sources used in the research findings

        The report should include the following sections:

        - Executive Summary
        - Introduction
        - Main Findings
        - Analysis and Insights
        - Conclusions and Recommendations
        - Sources and References

        Keep the report around **600–800 words**.

        Ensure the report ends with a **complete conclusion** and does not stop mid-sentence.
    """),

    expected_output="""
    A well-structured professional report on {topic} including:
    - Executive Summary
    - Introduction
    - Main Findings
    - Analysis Insights
    - Conclusions
    - Sources and References
    """,

    context=[research_task, analysis_task],

    output_file="final_report.md"
)