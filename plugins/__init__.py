from aiohttp import web
from .route import routes
from info import AUTO_DEL, AUTO_DEL_IN
from datetime import datetime, timedelta
#from bot import app

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app 

def get_del_time():
    now = datetime.now()
    if AUTO_DEL_IN.lower() == "minute":
        total = now + timedelta(minutes=AUTO_DEL)
    else:
        total = now + timedelta(hours=AUTO_DEL)
    return total

def till_date(date):
    form = "%Y-%m-%d %H:%M:%S.%f"
    z = datetime.strptime(date,form)
    return z

