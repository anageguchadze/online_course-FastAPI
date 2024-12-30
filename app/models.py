from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)

  


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    duration = Column(Integer)
    instructor_id = Column(Integer, ForeignKey('users.id'))

    

class Lesson(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))

    

class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    progress = Column(Integer)

    