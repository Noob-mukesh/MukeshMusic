import asyncio

from pyrogram import filters

from config import *
from strings import get_command
from MukeshMusic import app
from MukeshMusic.misc import SUDOERS
from MukeshMusic.utils.database.memorydatabase import get_video_limit
from MukeshMusic.utils.formatters import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND) & filters.user(OWNER_ID))
async def varsFunc(_, message):
    mystic = await message.reply_text(
        "ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ... ɢᴇᴛᴛɪɴɢ ʏᴏᴜʀ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs..."
    )
    v_limit = await get_video_limit()
    MUSIC_BOT_NAME = MUSIC_BOT_NAME
    up_r = f"[ʀᴇᴩᴏ]({UPSTREAM_REPO})"
    up_b = UPSTREAM_BRANCH
    auto_leave = AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = SERVER_PLAYLIST_LIMIT
    fetch_playlist = PLAYLIST_FETCH_LIMIT
    song = SONG_DOWNLOAD_DURATION
    play_duration = DURATION_LIMIT_MIN
    cm = CLEANMODE_DELETE_MINS

    if AUTO_LEAVING_ASSISTANT == str(True):
        ass = "ʏᴇs"
    else:
        ass = "ɴᴏ"
    if PRIVATE_BOT_MODE == str(True):
        pvt = "ʏᴇs"
    else:
        pvt = "ɴᴏ"

    if AUTO_DOWNLOADS_CLEAR == str(True):
        down = "ʏᴇs"
    else:
        down = "ɴᴏ"
    if not START_IMG_URL:
        start = "ɴᴏ"
    else:
        start = f"[ɪᴍᴀɢᴇ]({START_IMG_URL})"
    if not SUPPORT_CHANNEL:
        s_c = "ɴᴏ"
    else:
        s_c = f"[ᴄʜᴀɴɴᴇʟ]({SUPPORT_CHANNEL})"
    if not SUPPORT_GROUP:
        s_g = "ɴᴏ"
    else:
        s_g = f"[sᴜᴩᴩᴏʀᴛ]({SUPPORT_GROUP})"
    if not GIT_TOKEN:
        token = "ɴᴏ"
    else:
        token = "ʏᴇs"
    if (
        not SPOTIFY_CLIENT_ID
        and not SPOTIFY_CLIENT_SECRET
    ):
        sotify = "ɴᴏ"
    else:
        sotify = "ʏᴇs"
    owners = [str(ids) for ids in OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**ᴍᴜsɪᴄ ʙᴏᴛ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs:**

**<u>ʙᴀsɪᴄ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**ᴍᴜsɪᴄ_ʙᴏᴛ_ɴᴀᴍᴇ** : `{MUSIC_BOT_NAME}`
**ᴅᴜʀᴀᴛɪᴏɴ_ʟɪᴍɪᴛ** : `{play_duration} ᴍɪɴᴜᴛᴇs`
**sᴏɴɢ_ᴅᴏᴡɴʟᴏᴀᴅ_ᴅᴜʀᴀᴛɪᴏɴ_ʟɪᴍɪᴛ** :` {song} ᴍɪɴᴜᴛᴇs`
**ᴏᴡɴᴇʀ_ɪᴅ** : `{owner_id}`
    
**<u>ʀᴇᴩᴏsɪᴛᴏʀʏ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**ᴜᴩsᴛʀᴇᴀᴍ_ʀᴇᴩᴏ** : `{up_r}`
**ᴜᴩsᴛʀᴇᴀᴍ_ʙʀᴀɴᴄʜ** : `{up_b}`
**ɢɪᴛʜᴜʙ_ʀᴇᴩᴏ** :` {git}`
**ɢɪᴛ_ᴛᴏᴋᴇɴ**:` {token}`


**<u>ʙᴏᴛ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**ᴀᴜᴛᴏ_ʟᴇᴀᴠɪɴɢ_ᴀssɪsᴛᴀɴᴛ** : `{ass}`
**ᴀssɪsᴛᴀɴᴛ_ʟᴇᴀᴠᴇ_ᴛɪᴍᴇ** : `{auto_leave} sᴇᴄᴏɴᴅs`
**ᴀᴜᴛᴏ_ᴅᴏᴡɴʟᴏᴀᴅs_ᴄʟᴇᴀʀ** : `{down}`
**ᴩʀɪᴠᴀᴛᴇ_ʙᴏᴛ_ᴍᴏᴅᴇ** : `{pvt}`
**ʏᴏᴜᴛᴜʙᴇ_ᴇᴅɪᴛ_sʟᴇᴇᴩ** : `{yt_sleep} sᴇᴄᴏɴᴅs`
**ᴛᴇʟᴇɢʀᴀᴍ_ᴇᴅɪᴛ_sʟᴇᴇᴩ** :` {tg_sleep} sᴇᴄᴏɴᴅs`
**ᴄʟᴇᴀɴᴍᴏᴅᴇ_ᴍɪɴs** : `{cm} ᴍɪɴᴜᴛᴇs`
**ᴠɪᴅᴇᴏ_sᴛʀᴇᴀᴍ_ʟɪᴍɪᴛ** : `{v_limit} ᴄʜᴀᴛs`
**sᴇʀᴠᴇʀ_ᴩʟᴀʏʟɪsᴛ_ʟɪᴍɪᴛ** :` {playlist_limit}`
**ᴩʟᴀʏʟɪsᴛ_ғᴇᴛᴄʜ_ʟɪᴍɪᴛ** :` {fetch_playlist}`

**<u>sᴩᴏᴛɪғʏ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**sᴩᴏᴛɪғʏ_ᴄʟɪᴇɴᴛ_ɪᴅ** :` {sotify}`
**sᴩᴏᴛɪғʏ_ᴄʟɪᴇɴᴛ_sᴇᴄʀᴇᴛ** : `{sotify}`

**<u>Playsize Vars:</u>**
**ᴛɢ_ᴀᴜᴅɪᴏ_ғʟɪᴇsɪᴢᴇ_ʟɪᴍɪᴛ** :` {tg_aud}`
**ᴛɢ_ᴠɪᴅᴇᴏ_ғɪʟᴇsɪᴢᴇ_ʟɪᴍɪᴛ** :` {tg_vid}`

**<u>ᴇxᴛʀᴀ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**sᴜᴩᴩᴏʀᴛ_ᴄʜᴀɴɴᴇʟ** : `{s_c}`
**sᴜᴩᴩᴏʀᴛ_ɢʀᴏᴜᴩ** : ` {s_g}`
**sᴛᴀʀᴛ_ɪᴍɢ_ᴜʀʟ** : ` {start}`
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
