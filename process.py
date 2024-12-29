from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from io import BytesIO
from pypdf import PdfReader


class LoadToDB:
    def __init__(
            self,
            embedding_model,
            db_dir,
            chunk_size,
            chunk_overlap
        ):

        self.embedding_model = embedding_model
        self.db_dir = db_dir
        self.chunk_size = chunk_size
        self. chunk_overlap = chunk_overlap

    def load_in_memory(self, file):
        # Read PDF content from BytesIO
        pdf_reader = PdfReader(BytesIO(file.read()))
        self.text = ""
        for page in pdf_reader.pages:
            self.text += page.extract_text()
        return self.text

    def chunk(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = self.chunk_size,
            chunk_overlap = self.chunk_overlap
        )
        self.data_chunks = self.text_splitter.split_text(self.text)
        return self.data_chunks

    def database(self):
        self.vector_db = Chroma.from_texts(
            texts = self.data_chunks,
            embedding = self.embedding_model,
            persist_directory = self.db_dir
        )
        return self.vector_db
    
