from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BAGex0UAQTE8Iie-SyyK_k4H8V4OYasYUQJaDv8AaNlATSKX6dmCCjio0MNjU-z1CKaYdYcSIjFrKFW9EPgNpI1cHpQFkRmGTVrrdh0ZLgK7d0I1ve8p3JC_cbRdJBRi9APGJNUcpbdNUrlYLxVYnTHuY4GNq_8BQpzy6cD3re2vvNV-s3Gax3Y1u_Wf3-vpylw-uR21-eFBDL8G_xR9MAghbBd4F5NJe7vigxv7rav21HbcmDISngYJm3JEhRzRlI6qiSE2G8BIybIOS8NVazg6ZxMt0ns2QrojufXwI9YSYFXkW08uBECWct5kPKphCtBtzjvlRRjAD-NBkB8r-0CFrMKynwAAAABZq4ZiAA")
API_ID = int(getenv("API_ID", "27182917"))
API_HASH = getenv("API_HASH", "e627c805adc5719f484d84fc829bc11b")
BOT_TOKEN = getenv("BOT_TOKEN", "5527373880:AAEsgsf3I26T1uCW6QZMbJop2gLFjoLbSCc")
BOT_NAME = getenv("BOT_NAME", "FeveranMusic") 
BOT_USERNAME = getenv("BOT_USERNAME", "FeveranMusicBot")
BOT_CHANNEL = getenv("BOT_CHANNEL", "-768634825")
ASS_USERNAME = getenv("ASS_USERNAME", "")
OWNER = getenv("OWNER", "1111099757")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", 500))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1111099757").split()))
