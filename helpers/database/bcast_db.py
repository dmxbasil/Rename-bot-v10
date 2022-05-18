import pymongo
import os
from configs import Config

DB_NAME = os.environ.get("DB_NAME","bcast")
mongo = pymongo.MongoClient(Config.MONGODB_URI)
db = mongo[DB_NAME]
dbcol = db["user"]

def insert(chat_id):
    user_id = int(chat_id)
    user_det = {"_id": user_id,"file_id": None, "caption": None}
    try:
      dbcol.insert_one(user_det)
    except:
      pass

def find(chat_id):
    id =  {"_id":chat_id}
    x = dbcol.find(id)
    for i in x:
         thumb = i["file_id"]
         caption = i["caption"]
         return [thumb, caption]

def getid():
    values = []
    for key  in dbcol.find():
         id = key["_id"]
         values.append((id)) 
    return values
