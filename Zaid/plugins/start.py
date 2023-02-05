from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
ʜᴇʏᴀ! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖ 
♡ **ɪ'ᴍ ᴀ ꜱɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜꜱɪᴄ ʙᴏᴛ**.
♡ **ɪ ᴄᴀɴ ᴘʟᴀʏ ꜱᴏɴɢꜱ ɪɴ ʏᴏᴜʀ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs**.
♡ **ᴛʜɪs ʙᴏᴛ ʀᴜɴs ᴏɴ ᴛᴇʟᴇᴛʜᴏɴ sᴏ ɪᴛ's ғᴀsᴛᴇʀ ᴀɴᴅ ᴍᴏʀᴇ sᴛᴀʙʟᴇ ᴛʜᴀɴ ᴀɴʏ ᴏᴛʜᴇʀ ᴍᴜsɪᴄ ʙᴏᴛ**
♡ **ᴏɴʟɪɴᴇ 𝟸𝟺/𝟽 & ᴀʟᴡᴀʏs ᴀᴄᴛɪᴠᴇ ᴀssɪsᴛᴀɴᴛ**!
♡ **ᴊᴏɪɴ @Walhalla_Network ғᴏʀ ᴍᴏʀᴇ ᴏғ ᴏᴜʀ ʙᴏᴛs ᴀɴᴅ ᴛᴏ ᴋɴᴏᴡ ᴡʜᴀᴛ ᴡᴇ ᴅᴏ**.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
♡ **ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ 🔘 ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ℹ️**.
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", "https://github.com/ITZ-ZAID/Telethon-Music")],
        [Button.url("🗣️ ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ! ɪ'ᴍ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ ♡**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", "https://github.com/ITZ-ZAID/Telethon-Music")],
        [Button.url("🗣️ ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return
