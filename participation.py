from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Participation(Base):
    __tablename__ = "participations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    training_id = Column(Integer, ForeignKey("trainings.id"))
    attendance = Column(Boolean, default=False)
    participation_date = Column(DateTime, default=datetime.utcnow)

    # İlişkiler (isteğe bağlı)
    user = relationship("User")
    training = relationship("Training")
