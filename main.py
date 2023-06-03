import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy import text

app = FastAPI()
engine = create_engine('postgresql://postgres:postgres@localhost/Testing_Map')
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM table_name'))
        output = result.fetchall()
    data = {"request": request, "output": output}
    return templates.TemplateResponse("index.html", data)

@app.get("/map", response_class=HTMLResponse)
async def map(request: Request):
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM table_name'))
        output = result.fetchall()
    data = {"request": request, "output": output}
    return templates.TemplateResponse("map.html", data)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=9595, log_level="info", reload=True)
