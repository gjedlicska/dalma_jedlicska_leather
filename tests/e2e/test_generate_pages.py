from typing import cast
from fastapi.testclient import TestClient
from fastapi.routing import APIRoute
from jinja2 import Template


def test_render_pages(test_client: TestClient):

    print(test_client.app.routes)

    for route in test_client.app.routes:
        if not isinstance(route, APIRoute):
            continue
        if "GET" not in route.methods:
            continue
        result = test_client.get(route.path)
        print(result)


def test_jinja_render():
    from app.main import templates

    template_paths = [t for t in templates.env.list_templates()]
    for template_path in template_paths:

        template = cast(Template, templates.get_template(template_path))
        result = template.render()

        print(result)
