# Multi-Purpose RAG Application

This application enables users to retrieve information interactively from diverse sources such as PDF documents, websites, and YouTube videos using a Retrieval-Augmented Generation (RAG) approach. Powered by advanced language models and vector search, it processes and queries content efficiently, providing precise and context-aware responses.


## Features
- **Multi-Source Querying**: Interact with uploaded PDF documents, websites, or YouTube video transcripts to extract and understand content.
- **Advanced NLP Integration**: Uses Google's Gemini model and vector embedding for accurate and contextually relevant answers.
- **Interactive UI**: Built with Streamlit, offering a simple and user-friendly interface for document upload, URL input, and querying.

## Code Structure

The application consists of several key files:

*   *app.py:* The main Streamlit application file. This file handles user input, manages the user interface, and orchestrates the interaction with different data sources.
*   *agents Directory:* Contains agent-specific logic, including gemini_llm.py which manages the LLM interaction.
*   *crew Directory:* Contains modules for processing information from various data sources (doc_crew.py, web_crew.py, video_crew.py).
*   *process_doc.py and process_video.py:* Modules dedicated to processing documents (PDFs) and YouTube video transcripts, respectively.
*   *tools.py:*  Defines custom tools (GetInfoTool, GetSumTool) for interacting with the ChromaDB databases.
*   *static.py:* Contains configuration and setup for the different tools.

## Usage Instructions

1.  *Setup:*
    *   Install required libraries:  pip install -r requirements.txt (You will need to create a requirements.txt file listing the necessary packages).
    *   Obtain a Google Cloud API key and set it as the environment variable GOOGLE_API_KEY or add it to your secrets.toml file using the streamlit secrets manager.
    *   Ensure that you have Google Cloud project configured properly.  The embedding model "models/embedding-001" and the language model "gemini/gemini-1.5-flash" need to be accessible to your application.


2.  *Run:* Launch the Streamlit application using streamlit run app.py.

3.  *Interaction:*
    *   Select a source ("Documents," "Website," or "YouTube Video") from the sidebar.
    *   If choosing "Documents," upload your PDF file.
    *   For "Website" and "YouTube Video," enter the relevant URL.
    *   Type your query into the chat box and receive a response.


## Future Enhancements

*   Implement more robust error handling and logging.
*   Add more advanced features, like summarization and specific data extraction.
*   Explore alternative vector databases and LLM providers.


This README provides a high-level overview. For more detailed information, please refer to the individual code files.
