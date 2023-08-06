import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from MukeshMusic import LOGGER, app, userbot
from MukeshMusic.core.call import Mukesh
from MukeshMusic.plugins import ALL_MODULES
from MukeshMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("MukeshMusic").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("MukeshMusic").warning(
            "Sur spotify id aur secret toh daala hi nahi aapne ab toh spotify se nahi chala paaoge gaane."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("MukeshMusic.plugins." + all_module)
    LOGGER("MukeshMusic.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Mukesh.start()
    try:
        await Mukesh.stream_call(
            "https://te.legra.ph/file/e7f41722604de7d56a423.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("MukeshMusic").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Mukesh.decorators()
    LOGGER("MukeshMusic").info("\x47\x72\x6F\x75\x70\x20\x43\x6F\x6E\x74\x72\x6F\x6C\x6C\x65\x72\x20\x4D\x75\x73\x69\x63\x20\x42\x6F\x74\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6C\x6C\x79\x2E\x2E\x2E\x0A\x0A\x4E\x6F\x77\x20\x64\x72\x6F\x70\x20\x79\x6F\x75\x72\x20\x67\x69\x72\x6C\x66\x72\x69\x65\x6E\x64\x27\x73\x20\x6E\x75\x64\x65\x73\x20\x61\x74\x20\x40\x74\x68\x65\x5F\x73\x75\x70\x70\x6F\x72\x74\x5F\x63\x68\x61\x74")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("MukeshMusic").info("Stopping Music Bot...")
