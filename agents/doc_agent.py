from crewai import Agent,Task
from agents.gemini_llm import llm
from litellm import completion
from langchain.tools import tool
from static import tool_doc


db_agent = Agent(
    role='Retriever',
    goal='Retrieve information from the vectorstore based on the {question}.',
    backstory='''This is a RAG application and you will work on retrieving the answer from the vectorstore.
    For this purpose you will use Get Info Tool. You are expert in querying vectorstores for precise and relevant information.
    Frame the answer in a way that is precise and acurate.
    If you don't find an answer tell what the document is all about.
    For very general questions like 'Hi','How are you', etc. you can answer on your own without using the tool.
    Use the tool only when factual question is asked.''',
    tools=tool_doc,
    allow_delegation=True,
    verbose=True,
    llm=llm
)

db_task = Task(
    description='Retrieve information from the vectorstore based on {question}.',
    agent=db_agent,
    expected_output='A well framed answer that is precise and acurate and source should always be mentioned.'
)
