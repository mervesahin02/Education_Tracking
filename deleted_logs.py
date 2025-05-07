from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class DeletedLog(Base):
    __tablename__ = "deleted_logs"

    id = Column(Integer, primary_key=True, index=True)
    training_id = Column(Integer, ForeignKey("trainings.id"))
    deleted_by_user_id = Column(Integer, ForeignKey("users.id"))
    deleted_at = Column(DateTime, default=datetime.utcnow)
    reason = Column(String)

    training = relationship("Training")
    deleted_by = relationship("User")

    def __repr__(self):
        return f"<DeletedLog(training={self.training_id}, deleted_by={self.deleted_by_user_id})>"
