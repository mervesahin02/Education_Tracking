from sqlalchemy import Column, Integer, String, Boolean, Enum, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class CourseEnvEnum(str, enum.Enum):
    online = "online"
    in_person = "in_person"

class CourseTypeEnum(str, enum.Enum):
    program = "Program"
    class_edu = "Sınıf Eğitimi"
    workshop = "Atölye"
    event = "Etkinlik"
    scorm = "Scorm"
    video = "StreamX Video"
    wowslides = "Wowslides"

class Training(Base):
    __tablename__ = "trainings"

    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String, nullable=False)
    course_code = Column(String, nullable=True, unique=True)
    instructor_name = Column(String)
    instruction_type = Column(String)  # Kurum İçi / Dışı gibi
    course_env = Column(Enum(CourseEnvEnum), nullable=False)
    course_type = Column(Enum(CourseTypeEnum), nullable=False)
    category = Column(String)
    target_group = Column(String)
    education_hours = Column(Integer)
    education_city = Column(String)
    project = Column(String)
    year = Column(Integer, nullable=False)
    is_deleted = Column(Boolean, default=False)
