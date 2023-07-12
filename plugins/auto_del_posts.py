from info import AUTO_DEL
from datetime import datetime, timedelta
# from bot import app importing app gives err have to find alt

def till_date(date):
    form = "%Y-%m-%d %H:%M:%S.%f"
    z = datetime.strptime(date,form)
    return z

from database.auto_del_mess import auto_del_get, auto_del_delete

while True:
    z = auto_del_get()
    for i in z:
        tim = till_date(i["datee"])
        if tim == datetime.now():
            app.delete_messages(i["chat_id"],i["mess_id"])
            auto_del_delete(i["datee"], i["chat_id"], i["mess_id"])
