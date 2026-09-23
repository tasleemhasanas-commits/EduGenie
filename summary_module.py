from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

MODEL = "gemini-3.6-flash"


def summarize_text(text: str) -> str:
    """Summarize educational text for students."""

    prompt = f"""
You are EduGenie, an AI learning assistant.

Summarize the following educational text in simple language.

Requirements:
- Keep the important points.
- Remove unnecessary details.
- Use clear bullet points where helpful.
- Make the summary easy for a student to understand.

Text:
{text}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text