from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.config.database import SessionLocal
from backend.models.metric import Metric

router = APIRouter()


@router.post("/metrics")
def create_metric(payload: dict):

    db: Session = SessionLocal()

    metric = Metric(
        service=payload["service"],
        metric_name=payload["metric_name"],
        value=payload["value"]
    )

    db.add(metric)
    db.commit()
    db.close()

    return {"status": "stored"}