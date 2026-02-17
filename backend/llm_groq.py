import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None
MODEL = "llama-3.3-70b-versatile"

def ask_llm(prompt: str) -> str:
    if not client:
        return "Error: GROQ_API_KEY not found in .env"
        
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error calling LLM: {str(e)}"
