# Phase 2 – Requirement Analysis

## 1. Functional Requirements

EduGenie should provide the following functions:

1. Answer educational questions using Google Gemini.
2. Explain difficult concepts in simple language.
3. Generate quizzes for learning and practice.
4. Summarize educational text.
5. Recommend personalized learning paths.

## 2. Non-Functional Requirements

- The system should be easy for students to use.
- Responses should be clear and understandable.
- The web interface should be simple and responsive.
- The application should provide quick AI-generated responses.
- API keys must be stored securely using environment variables.

## 3. Target Users

- School students
- College students
- Learners preparing for exams
- Students who need quick concept explanations

## 4. Input Requirements

The user can enter:

- Questions
- Topics
- Educational text
- Topics for quizzes
- Topics for learning-path recommendations

## 5. Output Requirements

EduGenie should provide:

- AI-generated answers
- Simple concept explanations
- Quiz questions
- Summaries
- Personalized learning recommendations

## 6. Technology Requirements

- Python 3.10+
- FastAPI
- Google Gemini API
- HTML/CSS
- Jinja2
- Uvicorn

## 7. Security Requirements

- Store the Gemini API key in an environment variable.
- Do not expose the API key in the source code.
- Do not commit the `.env` file to GitHub.
