from telegram.ext import CallbackQueryHandler


def button(update: Update, context: CallbackContext) -> None:
  query = update.callback_query
  query.answer()

  group_id = query.data
  db = next(get_db())
  day_repo = GroupDayRepository(db)
  lecture_repo = GroupLectureRepository(db)

  days = day_repo.get_all()  # Replace with actual filter logic
  lectures = lecture_repo.get_all()  # Replace with actual filter logic

  lecture_info = "\n".join([f"{lec.lecture_name} at {lec.lecture_time} in {lec.lecture_room}" for lec in lectures])
  query.edit_message_text(text=f"Schedule for group {group_id}:\n{lecture_info}")


def main() -> None:
  updater = Updater(settings.TELEGRAM_TOKEN)

  dispatcher = updater.dispatcher

  dispatcher.add_handler(CommandHandler("start", start))
  dispatcher.add_handler(CommandHandler("help", help_command))
  dispatcher.add_handler(CommandHandler("search", search))
  dispatcher.add_handler(CommandHandler("free_rooms.html", free_rooms))
  dispatcher.add_handler(CallbackQueryHandler(button))

  updater.start_polling()
  updater.idle()


if __name__ == '__main__':
  main()