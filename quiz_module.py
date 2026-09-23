from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

MODEL = "gemini-3.6-flash"


def generate_quiz(topic: str) -> str:
    """Generate a short multiple-choice quiz for students."""

    prompt = f"""
You are EduGenie, an AI learning assistant.

Create a quiz for a student about the following topic.

Requirements:
- Create exactly 3 multiple-choice questions.
- Give 4 options for each question.
- Clearly show the correct answer.
- Keep the questions suitable for students.
- Return the quiz in simple readable text.

Topic:
{topic}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text