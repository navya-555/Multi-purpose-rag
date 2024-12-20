from crewai import Agent,Task
from llm import llm
from litellm import completion
from langchain.tools import tool
from langchain_community.vectorstores import Chroma
import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embedder = GoogleGenerativeAIEmbeddings(model="models/embedding-001",
                                          google_api_key=st.secrets['GOOGLE_API'])
class getinfo:
    @tool("Get Info Tool")
    def info(query):
        """Search Chroma DB for relevant news information based on a query."""
        vectorstore = Chroma(persist_directory="./Database", embedding_function=embedder)
        retriever = vectorstore.similarity_search(query)
        return retriever
    
db_agent = Agent(
    role='Retriever',
    goal='Retrieve information from the database based on the user query.',
    backstory='Expert in querying databases for precise and relevant information only if the query is related to the content in the document.',
    tools=[getinfo().info],
    allow_delegation=True,
    verbose=True,
    llm=llm
)

db_task = Task(
    description='Retrieve information from the database based on the user query if the query is related to the content in the document.',
    agent=db_agent,
    expected_output='A precise answer from the database for the query.'
)
