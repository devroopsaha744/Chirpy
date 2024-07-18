import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_pinecone import PineconeVectorStore
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

#Configuring API Keys
load_dotenv()
hf_token = os.getenv('HF_TOKEN')
pinecone_api_key = os.getenv('PINECONE_API_KEY')
pinecone_url = os.getenv("PINECONE_URL")

#loading the Knwledge using PDF Loader
#data_dir = 'node+express\\node-v16-docs.pdf'

data_dir = "node+express\\express-handbook.pdf"
loader = PyPDFLoader(data_dir)
docs = loader.load()


#print(len(docs))

#Splitting the data
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(docs)

#Embedding Model 
embedding = HuggingFaceInferenceAPIEmbeddings(api_key= hf_token)

#Indexing the documents in on vectorDB
index_name = "backend-chirpy"

docsearch = PineconeVectorStore.from_documents(docs, embedding, index_name=index_name)

print("Indexing done!")
