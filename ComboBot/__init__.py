from ComboBot.core.bot import Mukesh
from ComboBot.core.dir import dirr
from ComboBot.core.git import git
from ComboBot.core.userbot import Userbot
from ComboBot.misc import dbb, heroku

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
