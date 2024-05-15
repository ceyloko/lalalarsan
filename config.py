from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "")
API_ID = int(getenv("API_ID", "19675036"))
API_HASH = getenv("API_HASH", "1c3b2db41860eff7b381f8ca3fcb3d13")
BOT_TOKEN = getenv("BOT_TOKEN", "5527373880:AAEsgsf3I26T1uCW6QZMbJop2gLFjoLbSCc")
BOT_NAME = getenv("BOT_NAME", "FeveranMusic") 
BOT_USERNAME = getenv("BOT_USERNAME", "FeveranMusicBot")
BOT_CHANNEL = getenv("BOT_CHANNEL", "")
ASS_USERNAME = getenv("ASS_USERNAME", "")
OWNER = getenv("OWNER", "1111099757")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", 500))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1111099757").split()))
