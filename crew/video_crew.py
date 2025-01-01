from agents.video_agent import video_agent, video_task
from crewai import Crew

tasks = [video_task]
agents = [video_agent]

crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True,
    )

def execute_video_crew(query):
    result = crew.kickoff(
        inputs={"question":query}
    )
    return result
