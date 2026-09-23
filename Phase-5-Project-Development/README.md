# Phase 5 – Project Development

## 1. Development Overview

EduGenie is developed as a lightweight AI-powered learning assistant using Python, FastAPI, HTML, CSS, and Google Gemini.

## 2. Development Modules

The project includes the following modules:

1. Q&A Module
2. Concept Explanation Module
3. Quiz Generation Module
4. Text Summarization Module
5. Personalized Learning Path Module

## 3. Backend Development

FastAPI is used to create the backend APIs and connect the frontend with the AI modules.

Main API endpoints:

- `/qa`
- `/explain`
- `/quiz`
- `/summarize`
- `/learn/recommendations`

## 4. AI Integration

Google Gemini API is integrated to generate educational responses, explanations, quizzes, summaries, and learning recommendations.

The API key is stored securely using an environment variable and is not included in the source code.

## 5. Web Interface

The frontend provides a simple interface where students can enter their questions or learning requirements and receive AI-generated responses.

## 6. Development Process

- Set up the Python environment
- Install required dependencies
- Configure the Gemini API
- Develop individual AI modules
- Develop the FastAPI backend
- Build the web interface
- Connect frontend and backend
- Test the application

## 7. Expected Output

EduGenie provides students with interactive AI-based learning support through question answering, explanations, quizzes, summaries, and personalized learning recommendations.
