from crewai import Agent,Task
from llm import llm
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from db_retriever import db_agent

class search:
    @tool("Search Tool")
    def search(query):
        """Perform DuckDuckGoSearch to get the answer for the query."""
        answer=DuckDuckGoSearchRun(query)
        return answer

search_agent = Agent(
    role='Search Agent',
    goal='Perform a DuckDuckGo search for questions not related to the information in database.',
    backstory='Expert in retrieving information from the web if the query cannot be answered by the db_agent.',
    tools=[search().search],
    allow_delegation=True,
    verbose=True,
    llm=llm
)

search_task = Task(
    description='Perform a DuckDuckGo search for questions not related to the database.',
    agent=search_agent,
    expected_output='A precise answer for the query after searching.'
)
