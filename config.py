from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "29806287"
# -------------------------------------------------------------
API_HASH = "e5e73ff83480fc8ea3ba6f2d2423a078"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "1801698508"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/yourtoofan/CHATBOT")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
SUPPORT_GRP = "https://t.me/FRIENSHIP_CLUB_GROUP"
UPDATE_CHNL = "https://t.me/ABOUT_RADHA_78"
OWNER_USERNAME = "@god_hyper_op"
# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", "")
    
