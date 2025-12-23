from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer to user queries."),
        ("user", "Query: {query}"),
    ]
)

#LLM initialization
llm = OllamaLLM(
    model="llama3",
    temperature=0.7
)

# Output parser
output_parser = StrOutputParser()

# Chain assembly
chain = prompt | llm | output_parser

#streamlit framework
st.title("Simple LangChain-Streamlit App")
input_query = st.text_input("Enter your query:")

if input_query:
    response = chain.invoke({"query": input_query})
    st.write("Response:", response)