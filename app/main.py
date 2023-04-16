from pathlib import Path
from typing import cast

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware import Middleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette_babel import LocaleMiddleware, get_translator
from starlette_babel.contrib.jinja import configure_jinja_env

from dalma_jedlicska_leather import services
import arel
import os

root_dir = Path(__file__).parent.parent

supported_locales = [locale.value for locale in services.Locale]
shared_translator = get_translator()  # process global instance
shared_translator.load_from_directories(
    [root_dir.joinpath("locales")]
)  # one or multiple locale directories


global_context = {"supported_locales": supported_locales}

app = FastAPI(
    middleware=[
        Middleware(LocaleMiddleware, locales=supported_locales, default_locale="en"),
        Middleware(
            TrustedHostMiddleware,
            allowed_hosts=[
                "dalmajedlicskaleather-production.up.railway.app",
                "dalma.jedlicska.com",
                "localhost",
                "testserver",
                "hyperion",
                "hyperion.local",
            ],
        ),
    ]
)
templates = Jinja2Templates(directory="templates")
configure_jinja_env(templates.env)


app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware)


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request) -> HTMLResponse:
    slideshow_images = services.get_slideshow_images()
    context = {
        "request": request,
        "logo_active": True,
        "slideshow_images": slideshow_images,
    } | global_context
    response = cast(HTMLResponse, templates.TemplateResponse("home.html", context))
    return response


@app.get("/products", response_class=HTMLResponse)
async def products_page(request: Request) -> HTMLResponse:
    products = services.get_products(services.Locale.HU)
    context = {"request": request, "products": products} | global_context
    response = cast(HTMLResponse, templates.TemplateResponse("products.html", context))
    return response


@app.get("/collections", response_class=HTMLResponse)
async def collections_page(request: Request) -> HTMLResponse:
    context = {"request": request} | global_context
    response = cast(
        HTMLResponse, templates.TemplateResponse("collections.html", context)
    )
    return response


@app.get("/stories", response_class=HTMLResponse)
async def stories_page(request: Request) -> HTMLResponse:
    stories = await services.get_stories()
    context = {"request": request, "stories": stories} | global_context
    response = cast(HTMLResponse, templates.TemplateResponse("stories.html", context))
    return response


@app.get("/stories/{story_id}")
async def story_page(story_id: str, request: Request) -> HTMLResponse:
    story = await services.get_story(story_id)
    if not story:
        raise HTTPException(status_code=404, detail="Item not found")
    context = {"request": request, "story": story} | global_context
    response = cast(HTMLResponse, templates.TemplateResponse("story.html", context))
    return response


@app.get("/info", response_class=HTMLResponse)
async def info_page(request: Request) -> HTMLResponse:
    context = {"request": request} | global_context
    response = cast(HTMLResponse, templates.TemplateResponse("info.html", context))
    return response


@app.get("/set_lang")
async def set_language(request: Request, lang: str) -> RedirectResponse:
    # fallback to home if referer is not set for some reason
    referer = request.headers.get("referer") or request.base_url
    response = RedirectResponse(url=referer)
    response.set_cookie("language", lang)
    return response


@app.exception_handler(404)
async def not_found_page(request: Request, _) -> HTMLResponse:
    context = {"request": request} | global_context
    response = cast(HTMLResponse, templates.TemplateResponse("404.html", context))
    return response


if _debug := os.getenv("DEBUG"):
    hot_reload = arel.HotReload(
        paths=[
            arel.Path(str(root_dir.joinpath("static"))),
            arel.Path(str(root_dir.joinpath("templates"))),
        ],
    )
    app.add_websocket_route("/hot-reload", route=hot_reload, name="hot-reload")
    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)
    templates.env.globals["DEBUG"] = _debug
    templates.env.globals["hot_reload"] = hot_reload
