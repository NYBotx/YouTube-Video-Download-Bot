import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6093083729:AAFQwRfqq1DVQrMpLvpWVRwoSBsG08EPvGU")
    API_ID = int(os.environ.get("API_ID", 13963336))
    API_HASH = os.environ.get("API_HASH", "a144d1e22ef0b29738e8c00713d02678")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "6093083729:AAFQwRfqq1DVQrMpLvpWVRwoSBsG08EPvGU")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
