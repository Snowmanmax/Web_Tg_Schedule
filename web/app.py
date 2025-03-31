from flask import Flask, render_template
from config.database import get_db
from database.repositories.schedule import GroupWeekRepository

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search/results.html')

@app.route('/schedule/<group_id>')
def schedule(group_id):
    db = next(get_db())
    repository = GroupWeekRepository(db)
    group = repository.get_by_id(group_id)
    return render_template('search/details.html', group=group)

if __name__ == '__main__':
    app.run(debug=True)