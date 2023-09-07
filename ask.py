import streamlit as st
import pyperclip
import os
from langchain.llms import OpenAI

# Set the page title and icon
st.set_page_config(page_title="Langchain Demo", page_icon=":robot:")

# Page title
st.header("ASK")

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = "your key here"

# Initialize the text variable with an empty string
text = ""

# Function to get user input


def get_text():
    input_text = st.text_input("You", key="input")
    return input_text

# Function to get the AI response


def get_response(question):
    llm = OpenAI(model_name="text-davinci-003")
    answer = llm(question)
    return answer


# Main application code
user_input = get_text()

submit = st.button("Generate response")

if submit:
    response = get_response(user_input)
    st.subheader("Answer:")
    st.write(response)

    # Copy the response to the clipboard
    pyperclip.copy(response)

    # Display a confirmation message
    st.subheader("Answer copied to your clipboard..😉")
