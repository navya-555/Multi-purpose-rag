from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from youtube_transcript_api import YouTubeTranscriptApi
import docx2txt


class LoadToDB_vid:
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

    def extract(self,url):
        vid_id=url.split('=')[1]
        trans_text=YouTubeTranscriptApi.get_transcript(vid_id)
        self.text=''
        for i in trans_text:
            self.text+=''+i['text']
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
    
