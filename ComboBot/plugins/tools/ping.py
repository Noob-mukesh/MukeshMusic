from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from ComboBot import app
from ComboBot.core.call import Mukesh
from ComboBot.utils import bot_sys_stats
from ComboBot.utils.decorators.language import language
from ComboBot.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_video(
        photo="https://telegra.ph/file/b53c9825d5f18c6831fee.mp4",
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await Mukesh.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
