from logging import lastResort
import os
from pathlib import Path
from typing import Annotated, cast

import arel
from dalma_jedlicska_leather import services, domain, repositories
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.middleware import Middleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette_babel import LocaleMiddleware, get_translator
from starlette_babel.contrib.jinja import configure_jinja_env
from mailjet_rest import Client
from pydantic import Field
from pydantic_settings import BaseSettings

from dalma_jedlicska_leather.domain.product import Product


root_dir = Path(__file__).parent.parent

# TODO: re-enable proper translation
# supported_locales = [locale.value for locale in domain.locale.Locale]
supported_locales = [domain.locale.Locale.HU.value]
shared_translator = get_translator()  # process global instance
shared_translator.load_from_directories(
    [root_dir.joinpath("locales")]
)  # one or multiple locale directories

product_handler = services.products.ProductHandler(
    repositories.products.get_products, repositories.products.get_gap_images
)

ALL_CATEGORIES = "all"


class Settings(BaseSettings):
    mj_api_key_public: str = Field()
    mj_api_key_private: str = Field()
    mj_sender_adress: str = Field()


SETTINGS = Settings()

mailjet = Client(auth=(SETTINGS.mj_api_key_public, SETTINGS.mj_api_key_private) , version='v3.1')


async def create_context(
    request: Request, local_context: dict[str, object] | None = None
) -> dict[str, object]:
    model_categories = await product_handler.get_all_model_categories()
    model_categories.insert(0, ALL_CATEGORIES)
    story_slugs = [s.slug for s in await services.get_stories()]
    global_context = {
        "request": request,
        "supported_locales": supported_locales,
        "model_categories": model_categories,
        "story_slugs": story_slugs,
    }
    if local_context:
        global_context |= local_context
    return global_context


app = FastAPI(
    middleware=[
        Middleware(LocaleMiddleware, locales=supported_locales, default_locale="hu"),
        Middleware(
            TrustedHostMiddleware,
            allowed_hosts=[
                "dalmajedlicskaleather-production.up.railway.app",
                "dalma.jedlicska.com",
                "localhost",
                "testserver",
                "hyperion",
                "hyperion.local",
                "192.168.0.132",
                "192.168.12.22",
            ],
        ),
    ]
)
templates = Jinja2Templates(directory="templates")
configure_jinja_env(templates.env)
templates.env.tests["image_data"] = lambda input: isinstance(
    input, domain.images.ImageData
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware)


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request) -> HTMLResponse:
    slideshow_images = services.get_slideshow_images()
    context = await create_context(
        request,
        {
            "logo_active": True,
            "slideshow_images": slideshow_images,
        },
    )
    response = cast(HTMLResponse, templates.TemplateResponse("home.html", context))
    return response


async def _get_product_or_404(product_id: str) -> Product:
    product = await product_handler.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


async def _render_product_page(
    request: Request, product_id: str, panel_template: str, page_version: str
) -> HTMLResponse:
    product = await _get_product_or_404(product_id)

    context = await create_context(request, {"product": product})
    # hey if we only want the panel info, just render that template
    if request.headers.get("HX-Target") == "product_panel":
        return cast(HTMLResponse, templates.TemplateResponse(panel_template, context))
    else:
        related_products = await product_handler.get_related_products(product.id)
        context |= {
            "related_products": related_products,
            "active_category": product.model.category,
            "product_page": page_version,
        }
        return cast(HTMLResponse, templates.TemplateResponse("product.html", context))


@app.get("/products/{product_id}", response_class=HTMLResponse)
async def single_product_page(request: Request, product_id: str) -> HTMLResponse:
    return await _render_product_page(
        request,
        product_id,
        "components/product_details_panel.html",
        page_version="details",
    )


@app.get("/products/{product_id}/order", response_class=HTMLResponse)
async def product_order_form(request: Request, product_id: str) -> HTMLResponse:
    return await _render_product_page(
        request, product_id, "components/product_order_form.html", page_version="order"
    )

@app.get("/products/{product_id}/success", response_class=HTMLResponse)
async def product_order_success(request: Request, product_id: str) -> HTMLResponse:
    return await _render_product_page(
        request, product_id, "components/product_order_success.html", page_version="success"
    )

@app.post("/products/{product_id}/order")
async def product_order(
    _: Request,
    product_id: str,
    email: Annotated[str, Form()],
    first_name: Annotated[str, Form()],
    last_name: Annotated[str, Form()],
    zip: Annotated[str, Form()],
    city: Annotated[str, Form()],
    address: Annotated[str, Form()],
    phone: Annotated[str | None, Form()] = None,
):
    product = await _get_product_or_404(product_id)
    print(email, first_name, last_name, zip, city, phone)
    data = {
        "Messages": [
            {
                "From": {"Email": SETTINGS.mj_sender_adress, "Name": "Dalma Jedlicska"},
                "To": [{"Email": email, "Name": f"{first_name} {last_name}"}],
                "Subject": "Rendeles visszaigazolas",
                "TextPart": "Koszonjuk a rendelest",
                "HTMLPart": f"""<h3>Köszönjük a rendelésed {first_name}!<h3/>
                <br/><br/><p>Hamarosan keresni fogunk.<p/><br/><p>Udv Dalma<p/>""",
            },
            {
                "From": {"Email": SETTINGS.mj_sender_adress, "Name": "Dalma Jedlicska"},
                "To": [{"Email": SETTINGS.mj_sender_adress, "Name": "Jedlicraft Bt."}],
                "Subject": "Rendeles ertesito",
                "TextPart": "Uj rendeles erkezett",
                "HTMLPart": f"""<h3>{last_name} {first_name} uj rendelest adott le!<h3/>
<br/><br/><p>{product.model.name} {product.model.category} {product_id} termekre.<br/>Adatok:<br/>{email} {zip} {city} {address}<p/>""",
            }
        ]
    }
    # TODO: move this call to a background job, it's costly
    mailjet.send.create(data=data)
    # redirecting with a see other status, turns post into get
    return RedirectResponse(f"/products/{product_id}/success", status_code=303)


@app.get("/products/{product_id}/summary", response_class=HTMLResponse)
async def product_order_summary(request: Request, product_id: str) -> HTMLResponse:
    return await _render_product_page(
        request,
        product_id,
        "components/product_summary_panel.html",
        page_version="summary",
    )


@app.get("/products", response_class=HTMLResponse)
async def products_page(request: Request, q: str | None = None) -> HTMLResponse:
    model = None if q == ALL_CATEGORIES else q
    paginated_product_data = await product_handler.get_paginated_translated_products_with_gap_images(
        # TODO: determine locale from request
        services.products.ProductQuery(cursor=None, model=model, color=None),
        domain.locale.Locale.HU,
    )
    context = await create_context(
        request,
        {
            "active_category": q if q else ALL_CATEGORIES,
            "paginated_product_data": paginated_product_data,
        },
    )
    response = cast(HTMLResponse, templates.TemplateResponse("products.html", context))
    return response


@app.get("/collections", response_class=HTMLResponse)
async def collections_page(request: Request) -> HTMLResponse:
    context = await create_context(request)
    response = cast(
        HTMLResponse, templates.TemplateResponse("collections.html", context)
    )
    return response


@app.get("/stories", response_class=HTMLResponse)
async def stories_page(request: Request) -> HTMLResponse:
    stories = await services.get_stories()
    context = await create_context(request, {"stories": stories})
    response = cast(HTMLResponse, templates.TemplateResponse("stories.html", context))
    return response


@app.get("/stories/{story_id}")
async def story_page(story_id: str, request: Request) -> HTMLResponse:
    story = await services.get_story(story_id)
    if not story:
        raise HTTPException(status_code=404, detail="Item not found")
    context = await create_context(request, {"story": story})
    response = cast(HTMLResponse, templates.TemplateResponse("story.html", context))
    return response


@app.get("/info", response_class=HTMLResponse)
async def info_page(request: Request) -> HTMLResponse:
    context = await create_context(request)
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
    context = await create_context(request)
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

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", reload=True, host="0.0.0.0", reload_includes=["*.mo"])
