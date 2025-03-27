# config/database.py

import psycopg2
from config.settings import DATABASE_CONFIG
import logging

logger = logging.getLogger(__name__)


def create_connection():
  try:
    # Подключение к базе данных PostgreSQL
    conn = psycopg2.connect(
      host=DATABASE_CONFIG['HOST'],
      port=DATABASE_CONFIG['PORT'],
      user=DATABASE_CONFIG['USER'],
      password=DATABASE_CONFIG['PASSWORD'],
      dbname=DATABASE_CONFIG['DB_NAME'],
      schema=DATABASE_CONFIG['SCHEMA']
    )
    logger.info("Соединение с базой данных успешно установлено.")

    # Устанавливаем схему по умолчанию для работы с данными
    with conn.cursor() as cursor:
      cursor.execute(f'SET search_path TO {DATABASE_CONFIG["SCHEMA"]}')
      conn.commit()

    return conn
  except Exception as e:
    logger.error(f"Ошибка подключения к базе данных: {e}")
    raise


def close_connection(conn):
  try:
    conn.close()
    logger.info("Соединение с базой данных закрыто.")
  except Exception as e:
    logger.error(f"Ошибка при закрытии соединения: {e}")
