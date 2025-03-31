from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Lecturer(Base):
    __tablename__ = 'schedule.LECTURER'
    id = Column(UUID, primary_key=True)
    lecturer_name = Column(String(64), nullable=False)

class Course(Base):
    __tablename__ = 'schedule.COURSE'
    id = Column(UUID, primary_key=True)
    course_name = Column(String(64), nullable=False)

class GroupWeek(Base):
    __tablename__ = 'schedule.GROUP_WEEKS'
    id = Column(UUID, primary_key=True)
    group_name = Column(String(256), nullable=False)

class GroupDay(Base):
    __tablename__ = 'schedule.GROUP_DAYS'
    id = Column(UUID, primary_key=True)
    week_id = Column(UUID, ForeignKey('schedule.GROUP_WEEKS.id'), nullable=False)
    day_num = Column(Integer, nullable=False)
    day_name = Column(String(256), nullable=False)

    group_week = relationship("GroupWeek", back_populates="days")

class GroupLecture(Base):
    __tablename__ = 'schedule.GROUP_LECTURES'
    id = Column(UUID, primary_key=True)
    course_id = Column(UUID, ForeignKey('schedule.COURSE.id'))
    lecturer_id = Column(UUID, ForeignKey('schedule.LECTURER.id'))
    day_id = Column(UUID, ForeignKey('schedule.GROUP_DAYS.id'), nullable=False)
    is_even = Column(Boolean, nullable=False)
    lecture_num = Column(Integer, nullable=False)
    lecture_name = Column(String(1024), nullable=False)
    lecture_time = Column(String(256), nullable=False)
    lecture_room = Column(String(256), nullable=False)
    is_cancelled = Column(Boolean)

    course = relationship("Course")
    lecturer = relationship("Lecturer")
    group_day = relationship("GroupDay", back_populates="lectures")

GroupWeek.days = relationship("GroupDay", order_by=GroupDay.id, back_populates="group_week")
GroupDay.lectures = relationship("GroupLecture", order_by=GroupLecture.id, back_populates="group_day")