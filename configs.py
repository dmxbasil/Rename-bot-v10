import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")   
    SESSION_NAME = os.environ.get("SESSION_NAME", "Rename-Bot-0")
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1287407305))
    CAPTION = "γ€ "
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    ONE_PROCESS_ONLY = bool(os.environ.get("ONE_PROCESS_ONLY", False))
    START_TEXT = """
ππππ ππ ππππππππ π΅πππ πππππππ π±ππ.
ππππ ππ πππ’ ππ’ππ ππ πππππ  ππ π΅πππ ππ ππππππ ππ .

πΌπππ π πππ β£οΈ ππ’ @basildmx.
    """
    HELP_TEXT = """**π΅πππππ  πππππ πππππ π΅ππ πππππ πΌππ..**
 
β  π²ππππππππ πππ ππππππππ ππππππ πππππ ππ.....
β  ππππ π πππππ ππ πππ ππ ππ π’πππ ππππππ πππππππππ..... 
β  ππππ πππ’ π΅πππ ππ πππππ π’ππ π πππ ππ ππππππ..... 
β  ππππ'π ππ, πππ ππππ ππ ππππ π πππ.....

π π°ππππππππ π²πππππππ π

- /start - πππππ πππ π±ππ
- /help - π·ππ  ππ πππ
- /about - π°ππππ πΌπ
- /settings - π²ππππππππ ππππππππ 
- /show_thumb & /del_thumb - π΅ππ πππππππππ

Β© πΌπππ by @basildmx
"""
    ABOUT_TEXT = """
ππππ ππ π πππππππ ππΎπ π πππ πΏππππππππ πππππππππ πππππππ. 
ππππ πΌπ πππ’ πΌππππ ππ π΅πππ πΈ πππ ππππππ πΈπ. 
β­βββ[πΚα΄Ι΄α΄α΄α΄ Κα΄α΄π]βββ
β
βπ€**α΄y Ι΄α΄α΄α΄** [α΄α΄x Κα΄Ι΄α΄α΄α΄Κ 01](http://t.me/dmx_renamer_01_bot)
β
βπ**Κα΄Ι΄Ι’** [α΄©yα΄Κα΄Ι΄ 3](https://www.python.org)
β
βπ**ΚΙͺΚΚα΄Κy** [α΄©yΚα΄Ι’Κα΄α΄](https://docs.pyrogram.org)
β
βπ‘**κ±α΄Κα΄ α΄Κ** [Κα΄Κα΄α΄α΄](https://heroku.com)
β
βπ¨βπ»**α΄Ι΄α΄‘α΄Κ** [Κα΄κ±ΙͺΚ α΄α΄x](https://t.me/basildmx)                                                                              
β
βπ**α΄α΄©α΄α΄α΄α΄κ±** [α΄α΄x Κα΄α΄α΄’β’](https://t.me/dmx_bots)
β
β°ββββββ[ π ]ββββββββββββ
    """
    PROGRESS = """\n
β­ββββββββββββββββ£
β£βͺΌποΈ α΄α΄α΄α΄Κ κ±Ιͺα΄’α΄ Β» {2}
β£βͺΌβ Ιͺα΄α΄ α΄α΄Ι΄α΄ Β» {1}
β£βͺΌ α΄©ΚΚα΄α΄Ι΄α΄α΄Ι’α΄ Β» {0}%
β£βͺΌπ κ±α΄α΄©α΄ΚΚ κ±α΄©α΄α΄α΄ Β» {3}/s
β£βͺΌβ³οΈ α΄yα΄ Κα΄κ°α΄ Β» {4}
β°ββββββββββββββββ£"""

















                                                                               
