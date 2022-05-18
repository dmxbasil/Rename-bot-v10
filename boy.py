import os
import time
import string
import asyncio
import random
import datetime
import aiofiles.os
import traceback
from pyromod import listen
from pyrogram import Client 
from pyrogram import filters
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from configs import Config
from helpers.settings import OpenSettings
from helpers.database.access_db import db
from helpers.forcesub import ForceSub
from helpers.check_gap import CheckTimeGap
from helpers.setup_prefix import SetupPrefix
from helpers.uploader import UploadFile, UploadVideo, UploadAudio
from helpers.database.add_user import AddUserToDatabase
from helpers.display_progress import progress_for_pyrogram
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid


Renamer = Client(
    session_name=Config.SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

broadcast_ids = {}

async def send_msg(user_id, message):
    try:
        if Config.BROADCAST_AS_COPY is False:
            await message.forward(chat_id=user_id)
        elif Config.BROADCAST_AS_COPY is True:
            await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"



@Renamer.on_message(filters.private & filters.command("start"))
async def start_handler(bot: Client, event: Message):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    await event.reply_photo(
        photo="https://telegra.ph/file/2e2a07e86066538ed7406.jpg",
        caption=f"𝙷𝙴𝙻𝙻𝙾 {event.from_user.mention} 👋 \n\n{Config.START_TEXT}",
        quote=True,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝚄𝙿𝚃𝙰𝚃𝙴𝚂", url="https://t.me/mkn_bots_updates"),
            InlineKeyboardButton("𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url="https://t.me/MKN_BOTZ_DISCUSSION_GROUP")
            ],[
            InlineKeyboardButton("🍃 𝙷𝙴𝙻𝙿", callback_data="help"),
            InlineKeyboardButton("⚙️ 𝙰𝙱𝙾𝚄𝚃", callback_data="about")
            ]]
            )
        )


@Renamer.on_message(filters.private & filters.command("help"))
async def start_handler(bot: Client, event: Message):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    await event.reply_text(
        text=f"{Config.HELP_TEXT}",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🏡 𝙷𝙾𝙼𝙴", callback_data="home"),
                 InlineKeyboardButton("⚙️ 𝙰𝙱𝙾𝚄𝚃", callback_data="about")],
                [InlineKeyboardButton("🔐 𝙲𝙻𝙾𝚂𝙴", callback_data="closeMeh")]
            ]
        )
    )


@Renamer.on_message(filters.private & filters.command("about"))
async def start_handler(bot: Client, event: Message):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    await event.reply_text(
        text=f"{Config.ABOUT_TEXT}",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🏡 𝙷𝙾𝙼𝙴", callback_data="home"),
                 InlineKeyboardButton("🍃 𝙷𝙴𝙻𝙿", callback_data="help")],
                [InlineKeyboardButton("🔐 𝙲𝙻𝙾𝚂𝙴", callback_data="closeMeh")]
            ]
        )
    )


@Renamer.on_message(filters.private & (filters.video | filters.document | filters.audio))
async def rename_handler(bot: Client, event: Message):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    isInGap, t_ = await CheckTimeGap(user_id=event.from_user.id)
    if (Config.ONE_PROCESS_ONLY is False) and (isInGap is True):
        await event.reply_text(f"Sorry Sir,\nNo Flooding Allowed!\nSend Video After `{str(t_)}s` !!", quote=True)
        return
    elif (Config.ONE_PROCESS_ONLY is True) and (isInGap is True):
        await event.reply_text(f"Sorry Sir,\nNo Flooding Allowed!\n{t_}", quote=True)
        return
    media = event.video or event.audio or event.document
    if media and media.file_name:
        reply_ = await event.reply_text(
            text=f"**Current File Name:** `{media.file_name}`\n\nSend me New File Name!",
            quote=True
        )
        download_location = f"{Config.DOWNLOAD_PATH}/{str(event.from_user.id)}/{str(time.time())}/"
        if os.path.exists(download_location):
            os.makedirs(download_location)
        try:
            ask_: Message = await bot.listen(event.chat.id, timeout=300)
            if ask_.text and (ask_.text.startswith("/") is False):
                ascii_ = ''.join([i if (i in string.digits or i in string.ascii_letters or i == " ") else "" for i in ask_.text.rsplit('.', 1)[0]])
                prefix_ = await db.get_prefix(event.from_user.id)
                new_file_name = f"{download_location}{prefix_ if (prefix_ is not None) else ''}{ascii_.replace(' ', '_')}.{media.file_name.rsplit('.', 1)[-1]}"
                if len(new_file_name) > 255:
                    await reply_.edit("Sorry Unkil,\nFile Name length is more than 255 bytes!")
                    return
                await ask_.delete(True)
                await reply_.edit("Downloading File ...")
                await asyncio.sleep(Config.SLEEP_TIME)
                c_time = time.time()
                try:
                    await bot.download_media(
                        message=event,
                        file_name=new_file_name,
                        progress=progress_for_pyrogram,
                        progress_args=(
                            "Downloading File ...",
                            reply_,
                            c_time
                        )
                    )
                    if not os.path.lexists(new_file_name):
                        try:
                            await reply_.edit("Something Went Wrong!\nUnable to Find File.")
                        except:
                            print(f"Something Went Wrong!\nUnable to Find File for {str(event.from_user.id)} !!")
                        return
                    await asyncio.sleep(Config.SLEEP_TIME)
                    await reply_.edit("Uploading File ...")
                    upload_as_doc = await db.get_upload_as_doc(event.from_user.id)
                    if upload_as_doc is True:
                        await UploadFile(
                            bot,
                            reply_,
                            file_path=new_file_name,
                            file_size=media.file_size
                        )
                    else:
                        if event.audio:
                            duration_ = event.audio.duration if event.audio.duration else 0
                            performer_ = event.audio.performer if event.audio.performer else None
                            title_ = event.audio.title if event.audio.title else None
                            await UploadAudio(
                                bot,
                                reply_,
                                file_path=new_file_name,
                                file_size=media.file_size,
                                duration=duration_,
                                performer=performer_,
                                title=title_
                            )
                        elif event.video or (event.document and event.document.mime_type.startswith("video/")):
                            thumb_ = event.video.thumbs[0] if ((event.document is None) and (event.video.thumbs is not None)) else None
                            duration_ = event.video.duration if ((event.document is None) and (event.video.thumbs is not None)) else 0
                            width_ = event.video.width if ((event.document is None) and (event.video.thumbs is not None)) else 0
                            height_ = event.video.height if ((event.document is None) and (event.video.thumbs is not None)) else 0
                            await UploadVideo(
                                bot,
                                reply_,
                                file_path=new_file_name,
                                file_size=media.file_size,
                                default_thumb=thumb_,
                                duration=duration_,
                                width=width_,
                                height=height_
                            )
                        else:
                            await UploadFile(
                                bot,
                                reply_,
                                file_path=new_file_name,
                                file_size=media.file_size
                            )
                except Exception as err:
                    try:
                        await reply_.edit(f"Unable to Download File!\n**Error:** `{err}`")
                    except:
                        print(f"Unable to Download File for {str(event.from_user.id)} !!\n**Error:** `{err}`")
            elif ask_.text and (ask_.text.startswith("/") is True):
                await reply_.edit("Current Process Cancelled!")
        except TimeoutError:
            await reply_.edit("Sorry Unkil,\n5 Minutes Passed! I can't wait more. Send me the File Once Again to Rename.")


@Renamer.on_message(filters.private & filters.photo & ~filters.edited)
async def photo_handler(bot: Client, event: Message):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    editable = await event.reply_text("Please Wait ...")
    await db.set_thumbnail(event.from_user.id, thumbnail=event.photo.file_id)
    await editable.edit("Permanent Custom Thumbnail Saved Successfully!")


@Renamer.on_message(filters.private & filters.command(["delete_thumbnail", "delete_thumb", "del_thumb", "delthumb"]) & ~filters.edited)
async def delete_thumb_handler(bot: Client, event: Message):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    await db.set_thumbnail(event.from_user.id, thumbnail=None)
    await event.reply_text(
        "Custom Thumbnail Deleted Successfully!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Check Settings", callback_data="openSettings"),
             InlineKeyboardButton("Close", callback_data="closeMeh")]
        ])
    )


@Renamer.on_message(filters.private & filters.command(["show_thumbnail", "show_thumb", "showthumbnail", "showthumb"]) & ~filters.edited)
async def show_thumb_handler(bot: Client, event: Message):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    _thumbnail = await db.get_thumbnail(event.from_user.id)
    if _thumbnail is not None:
        try:
            await bot.send_photo(
                chat_id=event.chat.id,
                photo=_thumbnail,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Delete Thumbnail", callback_data="deleteThumbnail")]]
                ),
                reply_to_message_id=event.message_id
            )
        except Exception as err:
            try:
                await bot.send_message(
                    chat_id=event.chat.id,
                    text=f"Unable to send Thumbnail!\n\n**Error:** `{err}`",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔐 Close 🔐", callback_data="closeMeh")]]),
                    reply_to_message_id=event.message_id
                )
            except:
                pass
    else:
        await event.reply_text("No Thumbnail Found in Database!\nSend a Thumbnail to Save it for New File.", quote=True)


@Renamer.on_message(filters.private & filters.command("settings"))
async def settings_handler(bot: Client, event: Message):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    editable = await event.reply_text(
        text="Please Wait ..."
    )
    await OpenSettings(editable, user_id=event.from_user.id)


@Renamer.on_callback_query()
async def callback_handlers(bot: Client, cb: CallbackQuery):
    if "closeMeh" in cb.data:
        await cb.message.delete(True)
    elif "openSettings" in cb.data:
        await OpenSettings(cb.message, user_id=cb.from_user.id)
    elif "triggerUploadMode" in cb.data:
        upload_as_doc = await db.get_upload_as_doc(cb.from_user.id)
        if upload_as_doc is True:
            await db.set_upload_as_doc(cb.from_user.id, upload_as_doc=False)
        else:
            await db.set_upload_as_doc(cb.from_user.id, upload_as_doc=True)
        await OpenSettings(cb.message, user_id=cb.from_user.id)
    elif "forceNewPrefix" in cb.data:
        await cb.message.edit(
            text="Send me New File Name Prefix!"
        )
        try:
            ask_: Message = await bot.listen(cb.message.chat.id, timeout=300)
            if ask_.text and (ask_.text.startswith("/") is False):
                await ask_.delete(True)
                await SetupPrefix(ask_.text, user_id=cb.from_user.id, editable=cb.message)
            elif ask_.text and (ask_.text.startswith("/") is True):
                await cb.message.edit(
                    text="Current Process Cancelled!",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚶Go Back", callback_data="openSettings")]])
                )
        except TimeoutError:
            await cb.message.edit(
                text="Sorry Unkil,\n5 Minutes Passed! I can't wait more. Send me File Again to Rename.",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚶Go Back", callback_data="openSettings")]])
            )
    elif "triggerPrefix" in cb.data:
        current_prefix = await db.get_prefix(cb.from_user.id)
        if current_prefix is None:
            await cb.answer("Currently you didn't set any File Name Prefix!", show_alert=True)
            await cb.message.edit(
                text="Send me a File Name Prefix!"
            )
            try:
                ask_: Message = await bot.listen(cb.message.chat.id, timeout=300)
                if ask_.text and (ask_.text.startswith("/") is False):
                    await ask_.delete(True)
                    await SetupPrefix(ask_.text, user_id=cb.from_user.id, editable=cb.message)
                elif ask_.text and (ask_.text.startswith("/") is True):
                    await cb.message.edit(
                        text="Current Process Cancelled!",
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚶Go Back", callback_data="openSettings")]])
                    )
            except TimeoutError:
                await cb.message.edit(
                    text="Sorry Unkil,\n5 Minutes Passed! I can't wait more.",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚶Go Back", callback_data="openSettings")]])
                )
        else:
            await cb.message.edit(
                text=f"**Current Prefix:** `{current_prefix}`",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Set New Prefix", callback_data="forceNewPrefix"),
                         InlineKeyboardButton("Go Back", callback_data="openSettings")]
                    ]
                )
            )
    elif "triggerThumbnail" in cb.data:
        thumbnail = await db.get_thumbnail(cb.from_user.id)
        if thumbnail is None:
            await cb.answer("No Thumbnail Found in Database!\nSend a Thumbnail to Save.", show_alert=True)
        else:
            await cb.answer("Thumbnail Found in Database!\nTrying to Send Thumbnail.", show_alert=True)
            try:
                await bot.send_photo(
                    chat_id=cb.message.chat.id,
                    photo=thumbnail,
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Delete Thumbnail", callback_data="deleteThumbnail")]])
                )
            except Exception as err:
                try:
                    await bot.send_message(
                        chat_id=cb.message.chat.id,
                        text=f"Unable to send Thumbnail!\n\n**Error:** `{err}`",
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔐 Close ", callback_data="closeMeh")]])
                    )
                except:
                    pass
    elif "deleteThumbnail" in cb.data:
        await db.set_thumbnail(cb.from_user.id, thumbnail=None)
        await cb.answer("Successfully Removed Custom Thumbnail!", show_alert=True)
        await OpenSettings(cb.message, user_id=cb.from_user.id)
    elif ("triggerCaption" in cb.data) or ("forceChangeCaption" in cb.data):
        custom_caption_ = await db.get_caption(cb.from_user.id)
        if custom_caption_ is not None:
            try:
                await cb.message.edit(
                    text=f"**Current Custom Caption:**\n\n`{custom_caption_}`",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✒ Change Custom Caption ✒", callback_data="forceChangeCaption")]])
                )
            except MessageNotModified:
                pass
            if "forceChangeCaption" not in cb.data:
                return
        elif custom_caption_ is None:
            await cb.answer("Currently you didn't set any File Caption!", show_alert=True)
        await cb.message.edit(
            text="Send me File Caption!"
        )
        try:
            ask_: Message = await bot.listen(cb.message.chat.id, timeout=300)
            if ask_.text and (ask_.text.startswith("/") is False):
                if len(ask_.text) > 1024:
                    await ask_.reply_text(
                        "Sorry Unkil,\nCaption Text length is more than 1024 bytes!",
                        quote=True,
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton("Try Again", callback_data="triggerCaption"),
                                 InlineKeyboardButton("🚶Go Back", callback_data="openSettings")]
                            ]
                        )
                    )
                    return
                caption = ask_.text.markdown
                await ask_.delete(True)
                await db.set_caption(cb.from_user.id, caption=caption)
                await cb.message.edit(
                    "Custom Caption Removed Successfully!",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Here Settings", callback_data="openSettings"),
                         InlineKeyboardButton("🔐 𝙲𝙻𝙾𝚂𝙴", callback_data="closeMeh")]
                    ])
                )
            elif ask_.text and (ask_.text.startswith("/") is True):
                await cb.message.edit(
                    text="Current Process Cancelled!",
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("🚶Go Back", callback_data="openSettings")]])
                )
        except TimeoutError:
            await cb.message.edit(
                text="Sorry Unkil,\n5 Minutes Passed! I can't wait more.",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚶 Go Back", callback_data="openSettings")]])
            )
    elif "about" in cb.data:
        await cb.edit_message_text(
            Config.ABOUT_TEXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("🍃 𝙷𝙴𝙻𝙿", callback_data="help"),
		InlineKeyboardButton("🏠 𝙷𝙾𝙼𝙴", callback_data="home")
	        ]]
	        )
            )

    elif "help" in cb.data:
        await cb.edit_message_text(
            Config.HELP_TEXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("⚙️ 𝙰𝙱𝙾𝚄𝚃", callback_data="about"),
	        InlineKeyboardButton("🏠 𝙷𝙾𝙼𝙴", callback_data="home")
		]]               
                )
            )
            
    elif "home" in cb.data:
        await cb.edit_message_text(
            Config.START_TEXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("𝚄𝙿𝚃𝙰𝚃𝙴𝚂", url="https://t.me/mkn_bots_updates"),
                InlineKeyboardButton("𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url="https://t.me/MKN_BOTZ_DISCUSSION_GROUP")
                ],[
                InlineKeyboardButton("🍃 𝙷𝙴𝙻𝙿", callback_data="help"),
                InlineKeyboardButton("⚙️ 𝙰𝙱𝙾𝚄𝚃", callback_data="about")
                ]]
                )
            )


@Renamer.on_message(filters.command("broadcast") & filters.user(Config.BOT_OWNER) & filters.reply)
async def broadcast_handler(bot: Client,  m: Message):
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text=f"Broadcast Started! You will be notified with log file when all the users are notified."
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(
        total=total_users,
        current=done,
        failed=failed,
        success=success
    )
    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(
                user_id=int(user['id']),
                message=broadcast_msg
            )
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user['id'])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(
                        current=done,
                        failed=failed,
                        success=success
                    )
                )
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(
            text=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.",
            quote=True
        )
    else:
        await m.reply_document(
            document='broadcast.txt',
            caption=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.",
            quote=True
        )
    await aiofiles.os.remove('broadcast.txt')



Renamer.run()
