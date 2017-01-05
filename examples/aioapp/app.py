import asyncio
import os

from aiohttp.web import Application, Response


ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'static')


def build_application():
    loop = asyncio.get_event_loop()
    app = Application(loop=loop)

    app.router.add_route('GET', r'/', index)
    app.router.add_static(r'/static/', ASSETS_DIR)
    return app


async def index(request):
    return Response(body=b'Hello world from aiohttp app', headers={'Content-type': 'text/html; charset=utf-8'})
