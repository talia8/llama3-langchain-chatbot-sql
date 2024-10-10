# chatbot.py

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders.sql_database import SQLDatabaseLoader
from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import create_engine

# Define the prompt template for the chatbot
template = """
    Answer the question below based on the relevant information. 
    If there's no relevant information, answer based on your own knowledge.

    Here is the conversation history: {context}

    Relevant information: {relevant_data}

    Question: {question}

    Answer:
"""

# Initialize the language model
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)

# Load data from an SQL database
engine = create_engine('mysql+pymysql://username:password@localhost:port/db_name')

# Wrap the SQLAlchemy engine in the LangChain SQLDatabase class
db = SQLDatabase(engine)

# Define a query (replace with your actual query)
query = "SELECT <something> FROM <table>"

# Initialize the SQLDatabaseLoader with the query and the database connection
loader = SQLDatabaseLoader(query=query, db=db)

# Load the results from the database
relevant_data = loader.load()

# Create the processing chain
chain = prompt | model

# Function to process the conversation
def get_chatbot_response(context, user_input):
    """Process user input and return the chatbot's response."""
    result = chain.invoke({
        "context": context,
        "relevant_data": relevant_data,
        "question": user_input
    })
    context += f"\nUser: {user_input}\nAI: {result}"
    return result, context
