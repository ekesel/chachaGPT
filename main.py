from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from tools.ai_tool import run_gpt

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request,
    prompt: str = Form(...)
):
    reply = run_gpt(prompt)
    return templates.TemplateResponse(
        "snippet.html",
        {"request": request, "reply": reply}
    )
