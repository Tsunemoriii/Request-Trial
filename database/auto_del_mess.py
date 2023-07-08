import pymongo

from info import DATABASE_URI, DATABASE_NAME

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

myclient = pymongo.MongoClient(DATABASE_URI)
mydb = myclient[DATABASE_NAME]
mycol = mydb['AUTODEL']

def auto_del_insert(date, chat_id:int, message_id:int):
    query = mycol.find_one({"chat_id":chat_id,"mess_id":message_id,"datee":date})
    if not query:
        mycol.insert_one({"chat_id":chat_id,"mess_id":message_id,"datee":date})
        
    return

def auto_del_get():
    query = list(mycol.find({}))
    return query

def auto_del_delete(date, chat_id:int, message_id:int):
    query = mycol.find_one({"chat_id":chat_id,"mess_id":message_id,"datee":date})
    if not query:
        mycol.insert_one({"chat_id":chat_id,"mess_id":message_id,"datee":date})
    return
