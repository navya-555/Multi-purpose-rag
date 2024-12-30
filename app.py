import streamlit as st
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from process import LoadToDB
from crew_handler import execute_crew

embedder = GoogleGenerativeAIEmbeddings(model="models/embedding-001",
                                          google_api_key=st.secrets['GOOGLE_API'])

def handle_userinput(user_question,db):
    with st.spinner('Fetching Information...'):
        if os.path.isdir(db):
            response=execute_crew(user_question)
            return response.raw
        else:
            return "No Info in DB"

            
def main():
    st.set_page_config(page_title="Multi-Purpose-Rag", page_icon=":books:")
    st.header("Chat with your PDF :books:")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input('Enter your query...'):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            response = handle_userinput(prompt, './Database')
            message_placeholder.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

    with st.sidebar:

        pdf_docs = st.file_uploader("Upload your PDFs here")

        if st.button("📤 Upload"):
            if pdf_docs is not None:
                
                with st.spinner("Processing"):
                    with open("uploaded_files.txt", "a") as f:
                        f.write(pdf_docs.name + "\n")
                    data=LoadToDB(embedder,'Database/',3300,300)
                    data.load_in_memory(pdf_docs)
                    chunk=data.chunk()
                    if not os.path.isdir('./Database'):
                        data.database()
                    else:
                        vector = Chroma(
                            embedding_function=embedder,
                            persist_directory='./Database'
                            )
                        vector.add_texts(chunk)
                st.success("✅ File Processed Successfully!!!")
                
            else:
                st.error('No file uploaded !!! ')
        
        uploaded_file_names = []
        if os.path.exists("uploaded_files.txt"):
            with open("uploaded_files.txt", "r") as f:
                uploaded_file_names = [line.strip() for line in f]

        st.subheader("Your documents 📁")
        if uploaded_file_names:
            st.write("Uploaded Files:")
            for file_name in uploaded_file_names:
                st.write(f"- {file_name}")
        else:
            st.write("No files uploaded yet.")

if __name__ == '__main__':
    main()
