from pyrogram import Client
from configs import Config

class Bot(Client):

    def __init__(self):
        super().__init__(
            "renamer",
            session_name=Config.SESSION_NAME,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=50,
            plugins={"root": "helpers"},
            sleep_threshold=5,
        )

bot = Bot()
bot.run()
