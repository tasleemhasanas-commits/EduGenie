from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning_path


app = FastAPI(title="EduGenie")

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


class TextRequest(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.post("/qa")
def ask_question(data: TextRequest):
    text = data.text.strip()

    if not text:
        return {"answer": "Please enter a question."}

    return {"answer": answer_question(text)}


@app.post("/explain")
def explain(data: TextRequest):
    text = data.text.strip()

    if not text:
        return {"answer": "Please enter a topic."}

    return {"answer": explain_concept(text)}


@app.post("/quiz")
def quiz(data: TextRequest):
    text = data.text.strip()

    if not text:
        return {"answer": "Please enter a topic."}

    return {"answer": generate_quiz(text)}


@app.post("/summarize")
def summarize(data: TextRequest):
    text = data.text.strip()

    if not text:
        return {"answer": "Please enter text to summarize."}

    return {"answer": summarize_text(text)}


@app.post("/learn/recommendations")
def learning_path(data: TextRequest):
    text = data.text.strip()

    if not text:
        return {"answer": "Please enter a topic."}

    return {"answer": recommend_learning_path(text)}