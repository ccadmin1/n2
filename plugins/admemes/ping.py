"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import os
import random
import heroku3
import requests
import math
import asyncio
import time
from pyrogram import Client, filters
from info import COMMAND_HAND_LER, ADMINS
from plugins.helper_functions.cust_p_filters import f_onw_fliter
from plugins.Dyno.dyno import bot_status_cmd
from database.users_chats_db import db

#=====================================================
BOT_START_TIME = time.time()
CMD = ['.', '/']
HEROKU_API_KEY = (os.environ.get("HEROKU_API_KEY", ""))
#=====================================================

@Client.on_message(filters.private & filters.user(ADMINS) & filters.command("dyno", CMD))         
async def bot_status_cmd(client,message):
    if HEROKU_API_KEY:
        try:
            server = heroku3.from_key(HEROKU_API_KEY)

            user_agent = (
                'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.149 Mobile Safari/537.36'
            )
            accountid = server.account().id
            headers = {
            'User-Agent': user_agent,
            'Authorization': f'Bearer {HEROKU_API_KEY}',
            'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
            }

            path = "/accounts/" + accountid + "/actions/get-quota"

            request = requests.get("https://api.heroku.com" + path, headers=headers)

            if request.status_code == 200:
                result = request.json()

                total_quota = result['account_quota']
                quota_used = result['quota_used']

                quota_left = total_quota - quota_used
                
                total = math.floor(total_quota/3600)
                used = math.floor(quota_used/3600)
                hours = math.floor(quota_left/3600)
                minutes = math.floor(quota_left/60 % 60)
                days = math.floor(hours/24)

                usedperc = math.floor(quota_used / total_quota * 100)
                leftperc = math.floor(quota_left / total_quota * 100)

#---------text--------🔥

                quota_details = f"""
💫SERVER STATUS💫

💠 ToTal dyno ➪ {total}hr 𝖿𝗋𝖾𝖾 𝖽𝗒𝗇𝗈!
 
💠 Dyno used ➪ {used} 𝖧𝗈𝗎𝗋𝗌 ( {usedperc}% )
        
💠 Dyno remaining ➪ {hours} 𝖧𝗈𝗎𝗋𝗌 ( {leftperc}% )
        
💠 Approximate days ➪ {days} days left!"""

#----------end---------💯

            else:
                quota_details = ""
        except:
            print("Check your Heroku API key")
            quota_details = ""
    else:
        quota_details = ""

    uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - BOT_START_TIME))

    try:
        t, u, f = shutil.disk_usage(".")
        total = humanbytes(t)
        used = humanbytes(u)
        free = humanbytes(f)

        disk = "\n**Disk Details**\n\n" \
            f"> USED  :  {used} / {total}\n" \
            f"> FREE  :  {free}\n\n"
    except:
        disk = ""

    await message.reply_text(
        "<u>💥 CURRENT STATUS OF YOUR BOT💥</u>\n\n"
        "💫DB STATUS\n"
        f"➪ 𝖡𝗈𝗍 𝖴𝗉𝗍𝗂𝗆𝖾: {uptime}\n"
        f"{quota_details}"
        f"{disk}",
        quote=True,
        parse_mode="html"
    )


# -- Constants -- #
ALIVE = "ചത്തിട്ടില്ല മുത്തേ ഇവിടെ തന്നെ ഉണ്ട്.. നിനക്ക് ഇപ്പൊ എന്നോട് ഒരു സ്നേഹവും ഇല്ല. കൊള്ളാം.. നീ പാഴെ പോലെയേ അല്ല മാറിപോയി..😔 ഇടക്ക് എങ്കിലും ചുമ്മാ ഒന്ന് /start ചെയ്തു നോക്ക്..🙂" 
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    await message.reply_sticker(sticker="CAACAgUAAxkBAAFMES9i7nknE3lSO20KTf9j5Zu1U9lRJwACvQMAAg472FWXnTfo27wNfR4E")
    #message = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    uptime = time.strftime("%Hh | %Mm | %Ss", time.gmtime(time.time() - BOT_START_TIME))
    await message.reply_text(f"🏓 <b>ᴘɪɴɢ</b> : <code>{time_taken_s:.3f} ms</code>\n\n⏰<b> ᴜᴘᴛɪᴍᴇ : </b><code>{uptime}</code>")
    await asyncio.sleep(5)
    await message.delete()   
    
