# Phase 7 – Project Documentation

## 1. Project Name

EduGenie – Google Gemini Powered Learning Assistant

## 2. Project Purpose

EduGenie is an AI-powered educational assistant designed to help students learn concepts easily and interactively.

## 3. Key Features

- Educational question answering
- Simple concept explanations
- AI-generated quizzes
- Educational text summarization
- Personalized learning recommendations

## 4. Technologies Used

- Python
- FastAPI
- HTML
- CSS
- Google Gemini API
- Uvicorn
- Jinja2

## 5. Project Modules

- `main.py` – FastAPI backend and API routes
- `qna.py` – Question answering
- `explanation_module.py` – Concept explanations
- `quiz_module.py` – Quiz generation
- `summary_module.py` – Text summarization
- `learning_path.py` – Learning recommendations
- `templates/index.html` – Web interface

## 6. Security

The Gemini API key is stored using an environment variable and is not included in the GitHub repository.

The `.env` file is excluded using `.gitignore`.

## 7. How to Run

Install the required dependencies:

```bash
pip install -r requirements.txt
