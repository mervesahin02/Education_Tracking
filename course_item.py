from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class CourseItem(Base):
    __tablename__ = "course_items"

    id = Column(Integer, primary_key=True, index=True)
    training_id = Column(Integer, ForeignKey("trainings.id"))
    name = Column(String, nullable=False)  # Örnek: "Eğitmen Bilgi Formu Gönderildi"
    is_done = Column(Boolean, default=False)
    done_at = Column(DateTime)
    done_by_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    training = relationship("Training", backref="course_items")
    done_by_user = relationship("User")

    def __repr__(self):
        return f"<CourseItem(name={self.name}, done={self.is_done})>"
