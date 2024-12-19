import streamlit as st
import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from process import LoadToDB

embedder = GoogleGenerativeAIEmbeddings(model="models/embedding-001",
                                          google_api_key="Your API key")



llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro',temperature=0,max_tokens=None, api_key="Your API key")

system_prompt=(
    '''You are an assistant for question—answering tasks.
    Use the following pieces of retrieved context to answer
    question. If you don't know the answer, say that you
    don't know.
    \n\n
    {context}''' 
)

prompt=ChatPromptTemplate.from_messages(
    [
        ('system', system_prompt),
        ('human','{input}'),
    ]
)
def handle_userinput(user_question,db):
    if os.path.isdir(db):
        vector = Chroma(
            embedding_function=embedder,
            persist_directory=db
        )
        retriever=vector.as_retriever()
        qa=create_stuff_documents_chain(llm,prompt)
        rag_chain=create_retrieval_chain(retriever,qa)
        response=rag_chain.invoke({'input':user_question})
        st.write(response['answer'])
    else:
        st.error("No Info in DB")

def add_doc(chunk,db):
    vector = Chroma(
            embedding_function=embedder,
            persist_directory=db
        )
    vector.add_documents(chunk)

            
def main():


    st.set_page_config(page_title="Chat with your PDF",
                       page_icon=":books:")

    st.header("Chat with your PDF :books:")
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question,'./Database')

    with st.sidebar:
        st.subheader("Your documents")

        if not os.path.exists('Documents'):
            os.makedirs('Documents')

        pdf_docs = st.file_uploader("Upload your PDFs here")
        if pdf_docs is not None:
            with open(os.path.join('Documents', pdf_docs.name), "wb") as f:
                f.write(pdf_docs.getbuffer())
                
        if st.button("Upload"):
            with st.spinner("Processing"):
                data=LoadToDB(embedder,'Documents/','Database/',3300,300)
                data.load()
                data.chunk()
                data.database()
                st.success("File Processed Successfully!!!")

        if st.button('Add'):

            with st.spinner("Processing"):
                data=LoadToDB(embedder,'Documents/','Database/',3300,300)
                data.load()
                add_doc(data.chunk(),'./Database')
                
            st.success("File Processed Successfully!!!")


if __name__ == '__main__':
    main()