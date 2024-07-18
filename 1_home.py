import streamlit as st

st.title("🐦 CHIRPY")

st.markdown("# What is Chipy?")

st.markdown('''
CHIRPY represents an innovative integration of AI solutions that can integrate
into Sparrow - Smart API management software. It revolutionizes how
developers interact with and manage APIs by introducing features such as
Smart Chirpy, Nerdy Chirpy, and Creative Chirpy. CHIRPY aims to significantly
enhance the user experience and productivity when creating APIs.
            
CHIRPY's integration into Sparrow has the
potential to redefine industry standards by:

Enhancing User Engagement: Smart Chirpy's
conversational interface makes API
management more accessible and user-friendly, catering to developers of all skill
levels.
            
Improving Efficiency: Nerdy Chirpy
streamlines AI and ML workflows, reducing
development cycles and operational costs.
            

Boosting Documentation Accuracy: Creative
Chirpy ensures developers have up-to-date
and accurate API documentation at their
fingertips, enhancing overall software
reliability and developer satisfaction.
            ''')

st.markdown("# Problem Statements")

st.markdown('''
**Build an AI-powered chatbot for Sparrow API Tool**
Develop an AI-powered chatbot for Sparrow, that enhances user experience by assisting
with backend development and REST API tool-related features. The chatbot should be
able to:
Engage users with a conversational interface that is intuitive and user-friendly.
Assist developers with backend development queries, providing best practices.
Any other cool feature that will be helpful to the developer community.
Provide documentation + video explaining the features developed.

            
**AI Dev-Boost Library**
Developers often face repetitive tasks in AI and machine learning projects, such as data
preprocessing, feature engineering, model training, model evaluation, and deployment.
These tasks can be time-consuming and error-prone if done from scratch each time. By
creating a library of well-documented AI-powered code snippets, we can streamline
these processes, allowing developers to focus on the more creative aspects of their
projects.
This library should not only include code snippets but also provide comprehensive
documentation and examples to facilitate easy integration and understanding, ensuring
that developers of all skill levels can benefit from the resource.
            

**AI-Powered API Documentation**
Develop AI-powered features for Sparrow that provide intelligent, context-aware API
documentation. The goal is to enhance the developer experience by simplifying
interaction with APIs and making documentation more accessible and useful.
Context-Aware API Documentation:
Develop an AI-powered documentation assistant that provides relevant API
documentation.
Enable the assistant to understand and respond to natural language questions about
API endpoints, parameters, and usage examples.
Ensure the documentation provided is detailed, accurate, and helps in
troubleshooting common issues.
Provide documentation explaining the features developed.

''')

st.markdown(
    ''' # Solutions'''
)

st.markdown('''

## Smart Chirpy 💡🐦
Smart Chirpy is an AI-powered chatbot designed to assist users in creating and managing APIs within Sparrow. Acting as a
virtual assistant, Smart Chirpy provides real-time guidance on API creation, suggesting the most appropriate Sparrow tools to
resolve specific problems. With its intuitive conversational interface, Smart Chirpy makes backend development and API
management more accessible and efficient, helping developers navigate through complex tasks with ease.

           
## Nerdy Chirpy 🤓🐦
Nerdy Chirpy serves as an intelligent guide for the library and its documentation. Users can select a library, choose a module,
and receive comprehensive assistance on its functions and classes. By typing in queries, developers can learn about the inputs,
outputs, and workings of various components. Nerdy Chirpy simplifies the learning curve and resolves problems by providing
detailed explanations, ensuring developers have all the information they need to effectively utilize Sparrow's resources.

           
## Creative Chirpy 🖌️🐦
Creative Chirpy transforms API documentation by automatically generating detailed docs for your APIs. Users simply provide
the API function, and Creative Chirpy takes care of the rest, creating thorough and accurate documentation. This feature
ensures that your API documentation is always up-to-date and easy to understand, saving time and effort while enhancing the
overall quality and usability of your Sparrow's API resources.          
''')

st.markdown("## TechStack")

st.image("images\langchain.png")
st.image("images\llama3.jfif")
st.image("images\pinecone.png")
st.image("images\streamlit.png")