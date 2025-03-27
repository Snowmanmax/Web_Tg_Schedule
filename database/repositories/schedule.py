# database/repositories/schedule.py

from database.repositories.base import BaseRepository

class ScheduleRepository(BaseRepository):
    def get_lectures_by_lecturer(self, lecturer_id):
        query = """
            SELECT l.LECTURE_NAME, l.LECTURE_TIME, l.LECTURE_ROOM
            FROM schedule.GROUP_LECTURES l
            WHERE l.LECTURER_ID = %s
        """
        return self.fetch_all(query, (lecturer_id,))

    def get_courses_for_group(self, group_name):
        query = """
            SELECT c.COURSE_NAME, g.GROUP_NAME
            FROM schedule.GROUP_WEEKS g
            JOIN schedule.GROUP_DAYS d ON g.ID = d.WEEK_ID
            JOIN schedule.GROUP_LECTURES l ON l.DAY_ID = d.ID
            JOIN schedule.COURSE c ON l.COURSE_ID = c.ID
            WHERE g.GROUP_NAME = %s
        """
        return self.fetch_all(query, (group_name,))
