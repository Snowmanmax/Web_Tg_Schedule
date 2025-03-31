import os

class Settings:
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/schedule')
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', 'your-telegram-token')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

settings = Settings()