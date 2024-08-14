from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum,Text
from sqlalchemy.orm import relationship
from db.models.user import User
from ..db_setup import Base 
import enum 
from .user import User
from sqlalchemy_utils import URLType
from .mixins import Timestamp





class Course(Timestamp,Base): 
    __tablename__ = "courses"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String[100], index = True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable= False)

    created_by = relationship("User", back_populates="courses")
    
    sections = relationship("Section", back_populates="course", uselist=False)


class Section(Timestamp, Base): 
    __tablename__ = "sections"
    id = Column(Integer, primary_key = True, index = True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)

    course = relationship("Course", back_populates="sections")