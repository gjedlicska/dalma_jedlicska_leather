from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pathlib import Path

from fastapi.middleware import Middleware

from starlette_babel import get_translator, LocaleMiddleware
from starlette_babel.contrib.jinja import configure_jinja_env

root_dir = Path(__file__).parent.parent

supported_locales = ["en", "hu"]
shared_translator = get_translator()  # process global instance
shared_translator.load_from_directories(
    [root_dir.joinpath("locales")]
)  # one or multiple locale directories


app = FastAPI(
    middleware=[
        Middleware(LocaleMiddleware, locales=supported_locales, default_locale="en"),
    ]
)
templates = Jinja2Templates(directory="templates")
configure_jinja_env(templates.env)


app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    context = {"request": request, "logo_active": True}
    response = templates.TemplateResponse("home.html", context)
    return response

@app.get("/products", response_class=HTMLResponse)
async def products(request: Request) -> HTMLResponse:
    context = {"request": request}
    response = templates.TemplateResponse("collections.html", context)
    return response

@app.get("/collections", response_class=HTMLResponse)
async def collections(request: Request) -> HTMLResponse:
    context = {"request": request}
    response = templates.TemplateResponse("collections.html", context)
    return response

@app.get("/stories", response_class=HTMLResponse)
async def stories(request: Request) -> HTMLResponse:
    context = {"request": request}
    response = templates.TemplateResponse("collections.html", context)
    return response

@app.get("/info", response_class=HTMLResponse)
async def info(request: Request) -> HTMLResponse:
    context = {"request": request}
    response = templates.TemplateResponse("collections.html", context)
    return response