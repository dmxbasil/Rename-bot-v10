# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")   
    SESSION_NAME = os.environ.get("SESSION_NAME", "Rename-Bot-0")
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1287407305))
    CAPTION = "ㅤ "
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    ONE_PROCESS_ONLY = bool(os.environ.get("ONE_PROCESS_ONLY", False))
    START_TEXT = """
This is Telegram File Renameing Bot.

Send me any type of media  or File to Rename it .

Made with ❣️ by @mkn_bots_updates.
    """
    HELP_TEXT = """**Follow these Steps For Using Meh..**
 
**➠ Configure the Settings before using me.....
➠ Send a photo to set it as your custom thumbnail..... 
➠ Send any File or media you want to rename..... 
➠ That's it, and rest is mine work..... 
📝 Available Commands 📝
- /start - Start the Bot
- /help - How to Use
- /about - About Me
- /settings - Configure Settings 
- /show_thumb & /del_thumb - For Thumbnail
© Made with ❣️ @mkn_bots_updates**
"""
    ABOUT_TEXT = """
This is a Renamer bOt with Permanent Thumbnail Support. 
Send Me any Media or File I can Rename It. 
╭───[🔅RENAMER BOT🔅]──⍟
│
├🤖**My Name:** [MKN file rename bot](https://t.me/mkn_file_rename_bot)
│
├📝**Language:** [Python3](https://www.python.org)
│
├📚**Library:** [Pyrogram](https://docs.pyrogram.org)
│
├📡**Hosted On:** [Heorku](https://heroku.com)
│
├👨‍💻**Owner:** [Mr.MKN TG](https://t.me/mr_MKN) 
│
├👥**Developer:** [AbirHasan2005](https://t.me/AbirHasan2005)
│
├🔔**Bot Updates:** [Mᴋɴ Bᴏᴛᴢ™](https://t.me/mkn_bots_updates)
│
╰──────[ 😎 ]───────────⍟
    """
    PROGRESS = """\n
╭───[**🔅Progress Bar🔅**]───⍟
│
├📁 Size : {2}
├✅ Done : {1}
├🚀 Percentage : {0}%
├⚡ Speed : {3}/s
├⏱️ Time : {4}
╰─────────────────⍟"""
