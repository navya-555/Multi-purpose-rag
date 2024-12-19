from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings


class LoadToDB:
    def __init__(
            self,
            embedding_model,
            data_dir,
            db_dir,
            chunk_size,
            chunk_overlap
        ):

        self.embedding_model = embedding_model
        self.data_dir = data_dir
        self.db_dir = db_dir
        self.chunk_size = chunk_size
        self. chunk_overlap = chunk_overlap

    def load(self):
        self.data_loader = PyPDFDirectoryLoader(path = self.data_dir)
        self.data = self.data_loader.load()
        return self.data

    def chunk(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = self.chunk_size,
            chunk_overlap = self.chunk_overlap
        )
        self.data_chunks = self.text_splitter.split_documents(self.data)
        return self.data_chunks

    def database(self):
        self.vector_db = Chroma.from_documents(
            documents = self.data_chunks,
            embedding = self.embedding_model,
            persist_directory = self.db_dir
        )
        return self.vector_db
    
