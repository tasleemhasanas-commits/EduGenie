from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

MODEL = "gemini-3.6-flash"


def explain_concept(topic: str) -> str:
    """Explain a topic in simple language for students."""

    prompt = f"""
You are EduGenie, an AI learning assistant.

Explain the following educational topic in simple language.
Make it easy for a student to understand.

Include:
1. Simple definition
2. Main points
3. A simple example
4. Short conclusion

Topic:
{topic}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text