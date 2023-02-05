import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21927988"))
    API_HASH = os.environ.get("API_HASH", "e18f720acdff1e5b0ec80616aecd8a5a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5862886147:AAHy2oKUjJJYfTsGPYxy_W6fTFzz82MpR0o")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOI4Bu8aaLQ4vArNanG6nwvZMkuab-Qyg-WQlX7Qx91PN1WoORQiB0FiFciC47ca3lkV2DyvhWT3e01_ZAlzYRHxy_7pwJPIJvFh4xcYyzGBbvaB-dSo9hPWcCvtgLtJ1tmkVdjXV-ETkAcIzOCCnODIVbhqJiU_Tbf4s5_S0oPsWpprsrQ_abd_HeF2Boj51uVQI2xkKdgHlj6s8zXj2GzQWNdMTmCd1xY4VIa7lZ67Gm1C2dtwjwjod6WgzG3QUsWkocCoNeGwCLcH6urau7SZUKHVZfc7iNQwHdF7x9nuaPdNDz1DcyIqwaiWFfK2jOPi4J6MQRZY7H7FgAcM-XnBFRfo=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", False)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", False)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "NajimiMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "theoneandonlymurim") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "RimuruBots") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/dbf22b96f1564fe19331b.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/d20a4122a92144882c503.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5743885958")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "540000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
