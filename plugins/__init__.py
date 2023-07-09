from aiohttp import web
from .route import routes
from info import AUTO_DEL
from datetime import datetime, timedelta
#from bot import app

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app 

def get_del_time():
    now = datetime.now()
    total = now + timedelta(hours=AUTO_DEL)
    return total

def till_date(date):
    form = "%Y-%m-%d %H:%M:%S.%f"
    z = datetime.strptime(date,form)
    return z

