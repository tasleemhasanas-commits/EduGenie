# Phase 3 – Project Design

## 1. System Architecture

EduGenie follows a simple web-based AI application architecture.

User
↓
HTML/CSS Web Interface
↓
FastAPI Backend
↓
EduGenie Modules
↓
Google Gemini API
↓
AI-Generated Response
↓
User Interface

## 2. Project Modules

### Question and Answer Module

File: `qna.py`

Purpose:
- Accept educational questions.
- Send the question to Google Gemini.
- Return a clear AI-generated answer.

### Explanation Module

File: `explanation_module.py`

Purpose:
- Explain difficult concepts.
- Use simple language.
- Provide definitions, main points, examples, and conclusions.

### Quiz Module

File: `quiz_module.py`

Purpose:
- Generate educational quiz questions.
- Provide multiple-choice questions for practice.

### Summary Module

File: `summary_module.py`

Purpose:
- Summarize educational text.
- Provide concise and useful information.

### Learning Path Module

File: `learning_path.py`

Purpose:
- Generate personalized learning paths.
- Organize learning from beginner to advanced levels.

## 3. Backend

The backend is developed using FastAPI.

Main API endpoints:

- `/qa`
- `/explain`
- `/quiz`
- `/summarize`
- `/learn/recommendations`

## 4. Frontend

The frontend uses:

- HTML
- CSS
- JavaScript

The interface allows students to select a learning task, enter their question or topic, and view the AI-generated response.

## 5. Technology Stack

- Python
- FastAPI
- Google Gemini API
- HTML
- CSS
- JavaScript
- Jinja2
- Uvicorn

## 6. Data Flow

1. Student selects a learning task.
2. Student enters a question, topic, or text.
3. Frontend sends the request to the FastAPI backend.
4. The appropriate EduGenie module processes the request.
5. Google Gemini generates the response.
6. The backend returns the result.
7. The result is displayed on the web interface.
