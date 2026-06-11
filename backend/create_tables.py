from backend.config.database import Base, engine

from backend.models.log import Log
from backend.models.metric import Metric

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully")