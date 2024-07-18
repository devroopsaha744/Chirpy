import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate

#Configuring API keys
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

#Instatiating our ChatModel
chat = ChatGroq(model="llama3-70b-8192")

#Prompt Template
template = '''
You are Creative Chirpy. Creative Chirpy is an AI-powered API documentation assistant transforms
how developers access and utilize API documentation. By interpreting natural language 
queries and providing context aware responses. Creative Chirpy delivers comprehensive 
insights into API endpoints, parameters, usage examples,and troubleshooting tips. 
This feature simplifies documentation lookup, improves developer productivity,
and reduces errors during API integration

{Question}:

Answer:

'''
prompt_template = PromptTemplate.from_template(template=template)

chain = prompt_template | chat | StrOutputParser()

def generate_docs(text):
        response = chain.invoke({
        'Question': text
    })

        return response

