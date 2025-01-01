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
    
class GetSumInput(BaseModel):
    """Input schema for GetInfoTool."""
    query: str = Field(..., description="The search query for retrieving information from Chroma DB.")

class GetSumTool(BaseTool):
    name: str = "Get Info Tool"
    description: str = "Search Chroma DB for relevant news information based on a query."
    args_schema: Type[BaseModel] = GetInfoInput

    def _run(self, query: str) -> str:
        """Execute the tool."""
        # Initialize Chroma DB
        vectorstore = Chroma(persist_directory="./video_db", embedding_function=embedder)
        
        # Use the retriever to get results
        retriever = vectorstore.as_retriever()
        results = retriever.get_relevant_documents(query)
        print("\n".join([str(result) for result in results]))
        # Return the results as a formatted string
        return "\n".join([str(result) for result in results])