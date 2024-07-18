import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain.prompts import PromptTemplate

#Configuring API keys
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')
hf_token = os.getenv('HF_TOKEN')
pinecone_api_key = os.getenv("PINECONE_API_KEY")


#Instantiating the LLM
chat = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
     api_key= groq_api_key
)

#Embedding Model 
embedding = HuggingFaceInferenceAPIEmbeddings(api_key= hf_token)


# Connect to Pinecone
vectorstore = PineconeVectorStore.from_existing_index(
    index_name= 'backend-chirpy',
    embedding= embedding,
)

#Setting up the retriever
retriever = vectorstore.as_retriever()

#Prompt Template
template = '''
You are Smart-Chirpy, an AI-powered chatbot designed to enhance the developer experience by 
assisting with backend development and REST API tool-related features. 
Engage users with a friendly, intuitive conversational interface. Provide best practices 
and guidance on backend development, including security, database management, and API 
operations. Offer code snippets, troubleshooting assistance, and recommend tools, libraries, 
and learning resources to improve developer productivity and workflow.
{context}:
{Question}:

Answer:

'''
prompt_template = PromptTemplate.from_template(template=template)

#Setting up the chain
set_ret = RunnableParallel(
    {"context": retriever, "Question": RunnablePassthrough()} 
)
rag_chain = set_ret |  prompt_template | chat | StrOutputParser()

#Defining the response function
def generate_response(text):
    response = rag_chain.invoke(text)
    return response




