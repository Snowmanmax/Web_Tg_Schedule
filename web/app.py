from flask import Flask, render_template, request
from config.database import get_db
from database.repositories.schedule import GroupWeekRepository, GroupDayRepository, GroupLectureRepository

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/search')
def search():
  query = request.args.get('query')
  db = next(get_db())

  # Example search logic
  group_repo = GroupWeekRepository(db)
  groups = group_repo.get_all()  # Replace with actual search logic

  return render_template('search/results.html', query=query, groups=groups)


@app.route('/schedule/<group_id>')
def schedule(group_id):
  db = next(get_db())
  day_repo = GroupDayRepository(db)
  lecture_repo = GroupLectureRepository(db)

  days = day_repo.get_all()  # Replace with actual filter logic
  lectures = lecture_repo.get_all()  # Replace with actual filter logic

  return render_template('search/details.html', group_id=group_id, days=days, lectures=lectures)


@app.route('/free_rooms')
def free_rooms():
  db = next(get_db())
  lecture_repo = GroupLectureRepository(db)

  free_lectures = lecture_repo.get_all()  # Replace with actual free rooms logic

  return render_template('search/free_rooms.html', free_lectures=free_lectures)


if __name__ == '__main__':
  app.run(debug=True)