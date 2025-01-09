# Multi-Purpose RAG Application

This application enables users to retrieve information interactively from diverse sources such as PDF documents, websites, and YouTube videos using a Retrieval-Augmented Generation (RAG) approach. Powered by advanced language models and vector search, it processes and queries content efficiently, providing precise and context-aware responses.

![Screenshot-rag-1](https://github.com/user-attachments/assets/374bff63-3748-4bb9-a6b4-4111e7d090a0)
![Screenshot](https://github.com/user-attachments/assets/cf091496-63b3-4949-9f42-134dd3220109)
![Screenshot](https://github.com/user-attachments/assets/32b337e1-1b7b-44b4-a5a8-26b0a37fbc6d)


## Features
- **Multi-Source Querying**: Interact with uploaded PDF documents, websites, or YouTube video transcripts to extract and understand content.
- **Advanced NLP Integration**: Uses Google's Gemini model and vector embedding for accurate and contextually relevant answers.
- **Interactive UI**: Built with Streamlit, offering a simple and user-friendly interface for document upload, URL input, and querying.

## Usage
1. Select Data Source: Use the sidebar to choose between "Documents", "Website", or "YouTube Video".
2. Upload or Input Content: Upload PDFs, enter website URLs, or paste YouTube video links.
3. Query the System: Type your question into the chat input box and retrieve responses based on the selected source.
4. Retrieve Results: Processed content is stored in vector databases (Chroma), enabling rapid and relevant querying.

## Project Structure
- `app.py`: Main application script for managing the Streamlit interface and user interactions.
- `tools.py`: Contains tool classes for querying document and video vector databases.
- `static.py`: Configures tools for document, website, and video retrieval tasks.
- `doc_agent.py`: Agent for querying document-based data sources.
- `video_agent.py`: Agent for querying YouTube video transcripts.
- `web_agent.py`: Agent for retrieving information from websites.
- `gemini_llm.py`: Configures the Google Gemini LLM integration.
- `doc_crew.py`: Crew setup for document-based queries
- `video_crew.py`: Crew setup for video-based queries
- `web_crew.py`: Crew setup for website-based queries
- `process_doc.py`: Handles PDF and document processing for database creation.
- `process_video.py`: Handles YouTube video transcript processing for database creation.



## Future Enhancements
*   Add support for additional file types.
*   Implement more robust error handling and logging.
*   Add more advanced features, like summarization and specific data extraction.
*   Explore alternative vector databases and LLM providers.


## License
This project is licensed under the MIT License.
