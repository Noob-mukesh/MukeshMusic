from MukeshMusic.core.bot import Mukesh
from MukeshMusic.core.dir import dirr
from MukeshMusic.core.git import git
from MukeshMusic.core.userbot import Userbot
from MukeshMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Mukesh()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
