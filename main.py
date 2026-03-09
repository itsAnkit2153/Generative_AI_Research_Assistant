import time
from crew import research_crew


def run(topic: str):
    """Run the research crew for the given topic."""
    
    if not topic:
        topic = "Artificial Intelligence"   # fallback topic

    result = research_crew.kickoff(
        inputs={"topic": topic}
    )

    # prevent Groq rate limit (free tier)
    time.sleep(20)

    return result


if __name__ == "__main__":
    topic = input("Enter research topic: ")
    result = run(topic)

    print("\nResearch Completed\n")
    print(result)