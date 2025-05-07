from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Phase(Base):
    __tablename__ = "phases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)  # Örn: Havuz, Plan, Teslim, vb.
    order_number = Column(Integer, nullable=False)      # Görüntüleme sırası
    is_active = Column(Boolean, default=True)           # Kullanımda mı?

    def __repr__(self):
        return f"<Phase(name={self.name}, order={self.order_number})>"
