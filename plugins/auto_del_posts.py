from datetime import datetime, timedelta

from pyrogram import Client

# from info import AUTO_DEL

# from bot import app importing app gives err have to find alt

def till_date(date):
    form = "%Y-%m-%d %H:%M:%S.%f"
    z = datetime.strptime(date,form)
    return z

from database.auto_del_mess import auto_del_delete, auto_del_get
"""
async def is_media_post(app: Client, chat, message_id, date):
    mess = message_id
    while True:
        try:
            UwU = await app.get_messages(chat, mess)
        except Exception:
            print("Exception in is_media_post line 22")
            break
        if UwU.empty:
            break
        if UwU.text and UwU.text.lower() != "No such file exist":
            break
        else:
            try:
                auto_del_delete(date, chat, mess)
                await app.delete_messages(chat, mess)
                mess += 1
            except Exception:
                mess += 1
                pass"""
            

async def auto_ddel_postss(app: Client):
    z = auto_del_get()
    for i in z:
        tim = till_date(i["datee"])
        if tim <= datetime.now():
            try:
                await app.delete_messages(i["chat_id"],i["mess_id"])
                auto_del_delete(i["datee"], i["chat_id"], i["mess_id"])
                print("Deleted the post")
            except Exception as e:
                print(f"Failed: {e}\n")
                pass
