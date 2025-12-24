from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langserve import add_routes
import uvicorn
import os

app = FastAPI(
    title="LangChain Ollama API",
    description="An API to interact with Ollama LLM using LangChain",
    version="1.0.0",
)

add_routes(
    app,
    OllamaLLM(model="llama3", temperature=0.7),
    path="/ollama",
)

prompt1  = ChatPromptTemplate.from_template("Write an essay about {topic} in less than 200 words.")
prompt2 = ChatPromptTemplate.from_template("Compose a poem about {topic} with a rhyming scheme.")

llm = OllamaLLM(model="llama3", temperature=0.7)

add_routes(
    app,
    prompt1|llm,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)