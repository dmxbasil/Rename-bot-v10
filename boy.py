from reflective_listening import ReflectiveListening
from pyrogram import Client
from configs import Config


class App(Client):

    def __init__(self):
        super().__init__(
            "telegram",                        
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(
                root="helpers"
            )
        )

bot = App()
bot.run()




