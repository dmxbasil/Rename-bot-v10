from pyrogram import Client
from configs import Config

class RenameBot(Client):

    def __init__(self):
        super().__init__(
            "telegram",                        
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=50,
            plugins={"root": "helpers"}
        )

bot = RenameBot()
bot.run()
