from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    participation_id = Column(Integer, ForeignKey("participations.id"))
    rating = Column(Integer)  # 1-5 puanlama gibi
    comment = Column(String)
