from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, index=True)
    participation_id = Column(Integer, ForeignKey("participations.id"))
    certificate_number = Column(String, unique=True, nullable=False)
    issued_at = Column(DateTime, default=datetime.utcnow)
    file_url = Column(String)  # Sertifika PDF'inin dosya yolu/linki

    participation = relationship("Participation")

    def __repr__(self):
        return f"<Certificate(number={self.certificate_number}, date={self.issued_at})>"
