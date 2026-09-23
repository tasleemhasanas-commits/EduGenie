from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

MODEL = "gemini-3.6-flash"


def recommend_learning_path(topic: str) -> str:
    """Create a personalized learning path for a student."""

    prompt = f"""
You are EduGenie, an AI learning assistant.

Create a simple learning path for a student who wants to learn:
{topic}

Organize it from beginner to advanced.

Include:
1. Beginner concepts
2. Intermediate concepts
3. Advanced concepts
4. Suggested practice activities
5. Short conclusion

Use simple language suitable for students.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text