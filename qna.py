from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

# Create Gemini client
client = genai.Client()

# Gemini model
MODEL = "gemini-3.7-flash"

def answer_question(question: str) -> str:
    """Answer an educational question using Gemini."""

    prompt = f"""
You are EduGenie, an AI learning assistant.

Answer the student's question clearly and accurately.
Use simple language suitable for a student.
If useful, give examples.

Student question:
{question}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text