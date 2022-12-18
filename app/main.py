from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware)

print("foo")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    context = {"request": request, "logo_active": True}
    response = templates.TemplateResponse("home.html", context)
    return response


@app.get("/collections", response_class=HTMLResponse)
async def collections(request: Request) -> HTMLResponse:
    context = {"request": request}
    response = templates.TemplateResponse("collections.html", context)
    return response
