import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
scw_api_key = os.getenv("SCW_API_KEY")

# API Endpoint
API_URL = "https://api.scaleway.ai/b8067d35-6555-480c-b19c-d52d1369df33/v1/chat/completions"

# Streamlit App
st.title("LLM-Powered Web Application")

st.sidebar.header("Select a Function")
option = st.sidebar.radio("Choose an action:", ["Generate Transcript", "Extract Information"])

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {scw_api_key}"
}

# Generate Transcript
if option == "Generate Transcript":
    st.header("Generate a Call Transcript")
    subject = st.text_input("Enter the subject of the call:")

    if st.button("Generate Transcript"):
        if not subject:
            st.error("Please enter a subject.")
        else:
            payload = {
                "model": "mistral-nemo-instruct-2407",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Generate a brief call transcript between a client and an agent about: {subject}"}
                ],
                "max_tokens": 512,
                "temperature": 0.7,
                "top_p": 1,
                "presence_penalty": 0
            }

            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                response.raise_for_status()
                result = response.json()
                transcript = result["choices"][0]["message"]["content"]
                st.success("Transcript generated successfully!")
                st.text_area("Transcript:", transcript, height=300)

            except requests.exceptions.RequestException as e:
                st.error(f"Error in API request: {str(e)}")
            except KeyError:
                st.error("Error in the format of the API response.")

# Extract Information
elif option == "Extract Information":
    st.header("Extract Information from a Transcript")
    transcript = st.text_area("Enter the transcript:", height=200)
    paragraph = st.text_area("Enter the paragraph or request for information extraction:", height=100)

    if st.button("Extract Information"):
        if not transcript or not paragraph:
            st.error("Please provide both the transcript and the paragraph.")
        else:
            payload = {
                "model": "mistral-nemo-instruct-2407",
                "messages": [
                    {"role": "system", "content": "You are an expert in information extraction."},
                    {"role": "user", "content": f"Given the following request: {paragraph}. Here is the transcript: {transcript}. Please extract the relevant information from the transcript and return it in a structured format."}
                ],
                "max_tokens": 512,
                "temperature": 0.7,
                "top_p": 1,
                "presence_penalty": 0
            }

            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                response.raise_for_status()
                result = response.json()
                extracted_info = result["choices"][0]["message"]["content"]
                st.success("Information extracted successfully!")
                st.json({"extracted_information": extracted_info})

            except requests.exceptions.RequestException as e:
                st.error(f"Error in API request: {str(e)}")
            except KeyError:
                st.error("Error in the format of the API response.")