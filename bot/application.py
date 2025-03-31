from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from config.settings import settings
from config.database import get_db
from database.repositories.schedule import GroupWeekRepository, GroupDayRepository, GroupLectureRepository


def start(update: Update, context: CallbackContext) -> None:
  update.message.reply_text('Привет! Это бот для просмотра расписания.')


def help_command(update: Update, context: CallbackContext) -> None:
  update.message.reply_text('Используйте /search для поиска расписания, /free_rooms для просмотра свободных аудиторий.')


def search(update: Update, context: CallbackContext) -> None:
  query = ' '.join(context.args)
  db = next(get_db())

  group_repo = GroupWeekRepository(db)
  groups = group_repo.get_all()

  buttons = [[InlineKeyboardButton(group.group_name, callback_data=group.id)] for group in groups]
  keyboard = InlineKeyboardMarkup(buttons)

  update.message.reply_text('Search results:', reply_markup=keyboard)


def free_rooms(update: Update, context: CallbackContext) -> None:
  db = next(get_db())
  lecture_repo = GroupLectureRepository(db)

  free_lectures = lecture_repo.get_all()

  lecture_info = "\n".join([f"{lec.lecture_name} at {lec.lecture_time} in {lec.lecture_room}" for lec in free_lectures])
  update.message.reply_text(f'Free rooms:\n{lecture_info}')


def button(update: Update, context: CallbackContext) -> None:
  query = update.callback_query
  query.answer()

  group_id = query.data
  db = next(get_db())
  day_repo = GroupDayRepository(db)
  lecture_repo = GroupLectureRepository(db)

  days = day_repo.get_all()
  lectures = lecture_repo.get_all()

  lecture_info = "\n".join([f"{lec.lecture_name} at {lec.lecture_time} in {lec.lecture_room}" for lec in lectures])
  query.edit_message_text(text=f"Schedule for group {group_id}:\n{lecture_info}")


def main() -> None:
  updater = Updater(settings.TELEGRAM_TOKEN)

  dispatcher = updater.dispatcher

  dispatcher.add_handler(CommandHandler("start", start))
  dispatcher.add_handler(CommandHandler("help", help_command))
  dispatcher.add_handler(CommandHandler("search", search))
  dispatcher.add_handler(CommandHandler("free_rooms", free_rooms))
  dispatcher.add_handler(CallbackQueryHandler(button))

  updater.start_polling()
  updater.idle()


if __name__ == '__main__':
  main()