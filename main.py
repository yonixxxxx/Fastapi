from fastapi import FastAPI
from starlette.responses import HTMLResponse

app=FastAPI()
@app.get("/")
def read_root():
    html_content="<h1>Hello FastAPI</h1>"
    return HTMLResponse(content=html_content)
