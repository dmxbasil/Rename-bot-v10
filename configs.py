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
𝙷𝙴𝙻𝙻𝙾 {} 👋

𝚃𝚑𝚒𝚜 𝚒𝚜 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝙵𝚒𝚕𝚎 𝚁𝚎𝚗𝚊𝚖𝚎𝚛 𝙱𝚘𝚝.
𝚂𝚎𝚗𝚍 𝚖𝚎 𝚊𝚗𝚢 𝚝𝚢𝚙𝚎 𝚘𝚏 𝚖𝚎𝚍𝚒𝚊  𝚘𝚛 𝙵𝚒𝚕𝚎 𝚝𝚘 𝚁𝚎𝚗𝚊𝚖𝚎 𝚒𝚝 .

𝙼𝚊𝚍𝚎 𝚠𝚒𝚝𝚑 ❣️ 𝚋𝚢 @mkn_bots_updates.
    """
    HELP_TEXT = """**𝙵𝚘𝚕𝚕𝚘𝚠 𝚝𝚑𝚎𝚜𝚎 𝚂𝚝𝚎𝚙𝚜 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝙼𝚎𝚑..**
 
➠ 𝙲𝚘𝚗𝚏𝚒𝚐𝚞𝚛𝚎 𝚝𝚑𝚎 𝚂𝚎𝚝𝚝𝚒𝚗𝚐𝚜 𝚋𝚎𝚏𝚘𝚛𝚎 𝚞𝚜𝚒𝚗𝚐 𝚖𝚎.....
➠ 𝚂𝚎𝚗𝚍 𝚊 𝚙𝚑𝚘𝚝𝚘 𝚝𝚘 𝚜𝚎𝚝 𝚒𝚝 𝚊𝚜 𝚢𝚘𝚞𝚛 𝚌𝚞𝚜𝚝𝚘𝚖 𝚝𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕..... 
➠ 𝚂𝚎𝚗𝚍 𝚊𝚗𝚢 𝙵𝚒𝚕𝚎 𝚘𝚛 𝚖𝚎𝚍𝚒𝚊 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝 𝚝𝚘 𝚛𝚎𝚗𝚊𝚖𝚎..... 
➠ 𝚃𝚑𝚊𝚝'𝚜 𝚒𝚝, 𝚊𝚗𝚍 𝚛𝚎𝚜𝚝 𝚒𝚜 𝚖𝚒𝚗𝚎 𝚠𝚘𝚛𝚔.....

<u>📝 𝙰𝚟𝚊𝚒𝚕𝚊𝚋𝚕𝚎 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜 📝</u>

- /start - 𝚂𝚝𝚊𝚛𝚝 𝚝𝚑𝚎 𝙱𝚘𝚝
- /help - 𝙷𝚘𝚠 𝚝𝚘 𝚄𝚜𝚎
- /about - 𝙰𝚋𝚘𝚞𝚝 𝙼𝚎
- /settings - 𝙲𝚘𝚗𝚏𝚒𝚐𝚞𝚛𝚎 𝚂𝚎𝚝𝚝𝚒𝚗𝚐𝚜 
- /show_thumb & /del_thumb - 𝙵𝚘𝚛 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕

© 𝙼𝚊𝚍𝚎 𝚠𝚒𝚝𝚑 ❣️ @mkn_bots_updates 
"""
    ABOUT_TEXT = """
𝚃𝚑𝚒𝚜 𝚒𝚜 𝚊 𝚁𝚎𝚗𝚊𝚖𝚎𝚛 𝚋𝙾𝚝 𝚠𝚒𝚝𝚑 𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 𝚂𝚞𝚙𝚙𝚘𝚛𝚝. 
𝚂𝚎𝚗𝚍 𝙼𝚎 𝚊𝚗𝚢 𝙼𝚎𝚍𝚒𝚊 𝚘𝚛 𝙵𝚒𝚕𝚎 𝙸 𝚌𝚊𝚗 𝚁𝚎𝚗𝚊𝚖𝚎 𝙸𝚝. 
╭───[🔅RENAMER BOT🔅]──⍟
│
├🤖**𝙼𝚈 𝙽𝙰𝙼𝙴:** [𝗠𝗞𝗡 𝗳𝗶𝗹𝗲 𝗿𝗲𝗻𝗮𝗺𝗲 𝗯𝗼𝘁](https://t.me/mkn_file_rename_bot)
│
├📝**𝙻𝚊𝚗𝚐𝚞𝚊𝚐𝚎:** [𝙿𝚈𝚃𝙷𝙾𝙽 3](https://www.python.org)
│
├📚**𝙻𝙸𝙱𝚁𝙰𝚁𝚈:** [𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼](https://docs.pyrogram.org)
│
├📡**𝙷𝙾𝚂𝚃𝙴 𝙾𝙽:** [𝙷𝙴𝚁𝙾𝙺𝚄](https://heroku.com)
│
├👨‍💻**𝙾𝚆𝙽𝙴𝚁:** [𝑀𝑟.𝑀𝐾𝑁 𝑇𝐺](https://t.me/mr_MKN) 
│
├👥**𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛:** [ᗩᗷIᖇᕼᗩՏᗩᑎ2005](https://t.me/AbirHasan2005)                                                                             
│
├🔔**𝙱𝚘𝚝 𝚄𝚙𝚍𝚊𝚝𝚎𝚜:** [Mᴋɴ Bᴏᴛᴢ™](https://t.me/mkn_bots_updates)
│
╰──────[ 😎 ]───────────⍟
    """
    PROGRESS = """\n
╭━━━━━━━━━━━━━━━➣
┣⪼🗂️ 𝚂𝙸𝚉𝙴 : {2}
┣⪼✅ 𝙳𝙾𝙽𝙴 : {1}
┣⪼🌀 𝙿𝙴𝚁𝙲𝙴𝙽𝚃𝙰𝙶𝙴 : {0}%
┣⪼🚀 𝚂𝙿𝙴𝙴𝙳 : {3}/s
┣⪼⏳️ Time : {4}
╰━━━━━━━━━━━━━━━➣"""

















                                                                               
