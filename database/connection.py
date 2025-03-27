# database/connection.py

import psycopg2
from config.settings import DATABASE_CONFIG
import logging

logger = logging.getLogger(__name__)

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=DATABASE_CONFIG['HOST'],
                port=DATABASE_CONFIG['PORT'],
                user=DATABASE_CONFIG['USER'],
                password=DATABASE_CONFIG['PASSWORD'],
                dbname=DATABASE_CONFIG['DB_NAME'],
                schema=DATABASE_CONFIG['SCHEMA']
            )
            with self.connection.cursor() as cursor:
                cursor.execute(f'SET search_path TO {DATABASE_CONFIG["SCHEMA"]}')
                self.connection.commit()
            logger.info("Соединение с базой данных установлено.")
        except Exception as e:
            logger.error(f"Ошибка подключения к базе данных: {e}")
            raise

    def close(self):
        if self.connection:
            try:
                self.connection.close()
                logger.info("Соединение с базой данных закрыто.")
            except Exception as e:
                logger.error(f"Ошибка при закрытии соединения: {e}")
