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
vectorstore_1 = PineconeVectorStore.from_existing_index(
    index_name= 'nerdy-chirpy-sklearn',
    embedding= embedding,
)

vectorstore_2 = PineconeVectorStore.from_existing_index(
    index_name= 'nerdy-chirpy-pandas',
    embedding= embedding,
)

vectorstore_3 = PineconeVectorStore.from_existing_index(
    index_name= 'nerdy-chirpy-matplotlib',
    embedding= embedding,
)
#Setting up the retriever
retriever_1 = vectorstore_1.as_retriever()
retriever_2 = vectorstore_2.as_retriever()
retriever_3 = vectorstore_3.as_retriever()

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

#1
set_ret_1 = RunnableParallel(
    {"context": retriever_1, "Question": RunnablePassthrough()} 
)
rag_chain_1 = set_ret_1 |  prompt_template | chat | StrOutputParser()

#2
set_ret_2 = RunnableParallel(
    {"context": retriever_2, "Question": RunnablePassthrough()} 
)
rag_chain_2 = set_ret_2 |  prompt_template | chat | StrOutputParser()

#3
set_ret_3 = RunnableParallel(
    {"context": retriever_3, "Question": RunnablePassthrough()} 
)
rag_chain_3 = set_ret_3 |  prompt_template | chat | StrOutputParser()


#Defining the response function
#1
def generate_response_1(text):
    response = rag_chain_1.invoke(text)
    return response

#2
def generate_response_2(text):
    response = rag_chain_2.invoke(text)
    return response

#3
def generate_response_3(text):
    response = rag_chain_3.invoke(text)
    return response

#query = "How to set up POST request method?"
#print(generate_response(query))

#query = "Code to plot a piechart"

