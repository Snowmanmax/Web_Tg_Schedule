import os

class Settings:
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://Parcer:JBk%Vl2KnU#lA0{@79.174.88.177:18699/mtusi')
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '7022799237:AAF6WxrQpgiaqpckxLCslQf87kisIK-onsw')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

settings = Settings()