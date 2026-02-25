import requests
from prompts import SYSTEM_PROMPT

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:8b"

def generate_response(user_query):
    prompt = f"""
{SYSTEM_PROMPT}

User Query:
{user_query}
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        return f"Ollama Error: {response.text}"

    result = response.json()
    return result.get("response", "").strip()