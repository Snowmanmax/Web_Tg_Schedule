class Lecturer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Group:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Lecture:
    def __init__(self, id, course_id, lecturer_id, day_id, lecture_name, lecture_time, room, is_even, lecture_num, is_cancelled):
        self.id = id
        self.course_id = course_id
        self.lecturer_id = lecturer_id
        self.day_id = day_id
        self.lecture_name = lecture_name
        self.lecture_time = lecture_time
        self.room = room
        self.is_even = is_even
        self.lecture_num = lecture_num
        self.is_cancelled = is_cancelled
