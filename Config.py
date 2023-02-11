import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21927988"))
    API_HASH = os.environ.get("API_HASH", "e18f720acdff1e5b0ec80616aecd8a5a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5862886147:AAGEojnWiVRhJCRhwOM_HY4PoCqeg7ZZI6U")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKkBu7qc3871ALp6r-t5CX6aRoyd_inEXodtHa5xaqPFVgyYsZP8KthoOxDnSRzzezyQicXkIa1tKZd4AL3zqdkJAFPLz8YUKfHgzrDxufPAuPQY6kKxglzBL4iv9HCqEPcbCpIII0kz448ZibaOz8JXfyW6oryiC4-0j6zMEdPm4908A4n99m_KEl5BB-XdGnoIMr_A1WiXOx-s9itaONgntBV3X9V4RnWJfT1CxP-afPX5rUdQYxODcNiqVjLOVWvz7-NcTUYglB9yswuLK0N91GBXlZ17aCFit7jReH-OEWuuyvL_wn-gbqX9loOte7JCSWHfkHF9CmkIvgSWTnzg6Go=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", False)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", False)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "NajimiMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "theoneandonlymurim") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "RimuruBots") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/dbf22b96f1564fe19331b.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/d20a4122a92144882c503.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5743885958")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "5400000000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', False) # Change it to "True"
