from agents.retriever_agent import db_agent,db_task
from crewai import Crew

tasks = [db_task]
agents = [db_agent]

crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True,
    )

def execute_crew(query):
    result = crew.kickoff(
        inputs={"question":query}
    )
    return result
