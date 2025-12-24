import requests
import streamlit as st

def get_poem(topic) :
    url = "http://localhost:8000/poem/invoke"
    response = requests.post(
        url, 
        json = {
            'input' : {
                'topic' : topic
            }
        }
    )
    return response.json()

def get_essay(topic) :
    url = "http://localhost:8000/essay/invoke"
    response = requests.post(
        url, 
        json = {
            'input' : {
                'topic' : topic
            }
        }
    )
    return response.json()

# Creating UI using streamlit
st.title("Poem and Essay Generator using LangChain Ollama API")
input_essay = st.text_input("Enter a topic for the essay:")
input_poem = st.text_input("Enter a topic for the poem:")

if input_essay:
    st.write("Generating essay...")
    essay_response = get_essay(input_essay)
    st.write("Essay:", essay_response)

if input_poem:
    st.write("Generating poem...")
    poem_response = get_poem(input_poem)
    st.write("Poem:", poem_response)