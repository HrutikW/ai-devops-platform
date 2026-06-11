from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.config.database import SessionLocal
from backend.models.log import Log

router = APIRouter()


@router.post("/logs")
def create_log(payload: dict):

    db: Session = SessionLocal()

    log = Log(
        service=payload["service"],
        level=payload["level"],
        message=payload["message"]
    )

    db.add(log)
    db.commit()
    db.close()

    return {"status": "stored"}