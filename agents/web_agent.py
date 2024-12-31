from agents.gemini_llm import llm
from crewai import Agent,Task
from static import tool_website

db_agent = Agent(
    role='Retriever',
    goal='Retrieve information from the vectorstore based on the {question}.',
    backstory='''This is a RAG application for websites and you will work on retrieving the answer from the vectorstore.
    For this purpose you will use tool. You are expert in querying vectorstores for precise and relevant information.
    Frame the answer in a way that is precise and acurate.
    If you don't find an answer tell what the website is all about.''',
    tools=tool_website,
    allow_delegation=True,
    verbose=True,
    llm=llm
)

db_task = Task(
    description='Retrieve information from the vectorstore based on {question}.',
    agent=db_agent,
    expected_output='A well framed answer that is precise and acurate.'
)