from crewai import Agent,Task
from agents.gemini_llm import llm
from litellm import completion
from langchain.tools import tool
from langchain_community.vectorstores import Chroma
import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

embedder = GoogleGenerativeAIEmbeddings(model="models/embedding-001",
                                          google_api_key=st.secrets['GOOGLE_API'])

class GetInfoInput(BaseModel):
    """Input schema for GetInfoTool."""
    query: str = Field(..., description="The search query for retrieving information from Chroma DB.")

class GetInfoTool(BaseTool):
    name: str = "Get Info Tool"
    description: str = "Search Chroma DB for relevant news information based on a query."
    args_schema: Type[BaseModel] = GetInfoInput

    def _run(self, query: str) -> str:
        """Execute the tool."""
        # Initialize Chroma DB
        vectorstore = Chroma(persist_directory="./Database", embedding_function=embedder)
        
        # Use the retriever to get results
        retriever = vectorstore.as_retriever()
        results = retriever.get_relevant_documents(query)
        print("\n".join([str(result) for result in results]))
        # Return the results as a formatted string
        return "\n".join([str(result) for result in results])

db_agent = Agent(
    role='Retriever',
    goal='Retrieve information from the vectorstore based on the {question}.',
    backstory='''This is a RAG application and you will work on retrieving the answer from the vectorstore.
    For this purpose you will use Get Info Tool. You are expert in querying vectorstores for precise and relevant information.
    Frame the answer in a way that is precise and acurate.
    If you don't find an answer tell what the document is all about.''',
    tools=[GetInfoTool()],
    allow_delegation=True,
    verbose=True,
    llm=llm
)

db_task = Task(
    description='Retrieve information from the vectorstore based on {question}.',
    agent=db_agent,
    expected_output='A well framed answer that is precise and acurate along with the source always.'
)
