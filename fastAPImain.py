from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

import json
from dotenv import load_dotenv
import os

load_dotenv()


scw_api_key = os.getenv("SCW_API_KEY")



app = FastAPI()

#Subject Request 
class Sujet(BaseModel):
    sujet: str

class ExtractionRequest(BaseModel):
    paragraph: str  
    transcript: str  

#1s POST Route to generate the trancsript 
@app.post("/generate-transcript")
async def generate_transcript(request: Sujet):
    sujet = request.sujet

    url = "https://api.scaleway.ai/b8067d35-6555-480c-b19c-d52d1369df33/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {scw_api_key}"
    }
    payload = {
        "model": "mistral-nemo-instruct-2407",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate a call transcript between a client and an agent about: {sujet}"}
        ],
        "max_tokens": 512,
        "temperature": 0.7,
        "top_p": 1,
        "presence_penalty": 0
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  
        result = response.json()

        transcript = result["choices"][0]["message"]["content"]
        return {"transcript": transcript}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error in API request: {str(e)}")
    except KeyError:
        raise HTTPException(status_code=500, detail="Erreur in the format of API response")

#2nd POST Route to extract info from the transcript
@app.post("/extract-information")
async def extract_information(request: ExtractionRequest):
    paragraph = request.paragraph
    transcript = request.transcript

    url = "https://api.scaleway.ai/b8067d35-6555-480c-b19c-d52d1369df33/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {scw_api_key}"
    }

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
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  
        result = response.json()

        # Extraire les informations de la réponse
        extracted_info = result["choices"][0]["message"]["content"]
        
        # Structurer les informations extraites (par exemple sous forme de JSON)
        structured_info = {
            "extracted_information": extracted_info
        }

        return structured_info

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error in API request: {str(e)}")
    except KeyError:
        raise HTTPException(status_code=500, detail="Error in the format of API response")