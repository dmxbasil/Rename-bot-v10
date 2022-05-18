from pyrogram import Client
import os

API_ID = int(os.environ.get("API_ID", 12345))                                              
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")


if __name__ == "__main__" :
    plugins = dict(
        root="helpers"
    )
    app = Client(
        "bot",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins={"root": "helpers"}, 
    )
    app.run()
