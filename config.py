import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "9696783")
    API_HASH = getenv("API_HASH", "3e74a9830493e9261410a947428dbb34")
    TOKEN = getenv("TOKEN", "8098975400:AAGSHD7BSnpUaZPljFJvkjt3RKRpRxMgTC0")
    OWNER_ID = getenv("OWNER_ID", "7538572906")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "")
    STRING_SESSION = getenv("STRING_SESSION", "") #telethon
    OWNER_USERNAME = getenv("OWNER_USERNAME", "@its_deva_heree")
    DB_URI = getenv("DATABASE_URL", "")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1002404751523")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1002404751523")
    SYS_ADMIN = getenv("SYS_ADMIN", "7225660023")
    DEV_USERS = getenv("DEV_USERS", "7225660023")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CHANNEL = getenv("CHANNEL", "TheUpdatesChannel")
    SUPPORT = getenv("SUPPORT", "TheSupportChat")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/4a7c28726502e24ea0fe0.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/4a7c28726502e24ea0fe0.jpg")
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7225660023").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "7225660023").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
