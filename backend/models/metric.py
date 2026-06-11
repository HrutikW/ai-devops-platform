from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from backend.config.database import Base


class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)

    service = Column(String, index=True)
    metric_name = Column(String, index=True)
    value = Column(Float)

    timestamp = Column(DateTime, default=datetime.utcnow)