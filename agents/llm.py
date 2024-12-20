import streamlit as st
from crewai import Agent,Task,Crew,LLM

llm = LLM(
    api_key=st.secrets['GOOGLE_API'],
    model="gemini/gemini-1.5-flash",
)