import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21927988"))
    API_HASH = os.environ.get("API_HASH", "e18f720acdff1e5b0ec80616aecd8a5a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5862886147:AAHXJIyAvuQVDK8c9eld_BSeoSEOSbCTG3I")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOL0Bu6OHAnlkh9ZJFfC2KXVA15x8Ziv3qAEa0MhWFnIDOY-b1LjrcLGsoA3k10ptloTDvMr5zUmMY38Vkk_VXBkbPWHbS0SmJB71TCAh5Erb3-pBAhW6ceC_KuAL5D04UxFew_up588Est8YSx-8dtHCjch5rU385ywxbQbZ4H_2t4nB04x_yy2TqMHjv6Y-AS3Gl2k_pi4OZ0g6IeLj8Vf0194fISNGiGUifCzXJX56Igh7xMpRnsECKLnZkfbbnwiIsy8ofUnU72e5e_Qd2KarVfssBRdrAZZ-mnunF4APyNQ5ApNASS8uFBhl32QrK4SR-HZnGdKiAngSl9-yXQYVV9A=")
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
