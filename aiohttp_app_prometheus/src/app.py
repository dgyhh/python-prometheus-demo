from aiohttp import web
from helpers.middleware import error_middleware, setup_metrics


async def test(request):
    return web.Response(text='test')

async def test1(request):
    1/0

if __name__ == '__main__':
    app = web.Application(middlewares=[error_middleware])
    setup_metrics(app, "webapp_1")
    app.router.add_get('/test', test)
    app.router.add_get('/test1', test1)
    web.run_app(app, port=8080)
