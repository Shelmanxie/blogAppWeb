import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
import aiomysql
from aiohttp import web
from ALOG import loggerInfo

def creatTag(tag,content):
   # with loggerInfo('creatTag') as l:
    str = '<'+tag+'>'+content+'</'+tag+'>'
    logging.info('tag:%s, content:%s',tag,content)
    return str


def index(request):
    return web.Response(body=creatTag('h1','welcome to my website!!!'),content_type='text/html',status=200)

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()