from .base import BaseRepository
from database.models.schedule import Lecturer, Course, GroupWeek, GroupDay, GroupLecture

class LecturerRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, Lecturer)

class CourseRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, Course)

class GroupWeekRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, GroupWeek)

class GroupDayRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, GroupDay)

class GroupLectureRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, GroupLecture)