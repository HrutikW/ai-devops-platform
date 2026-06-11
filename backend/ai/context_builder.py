from backend.config.database import SessionLocal
from backend.models.log import Log
from backend.models.metric import Metric


def build_context(service: str):

    db = SessionLocal()

    try:
        # -------------------
        # FETCH LOGS
        # -------------------
        logs = (
            db.query(Log)
            .filter(Log.service == service)
            .order_by(Log.timestamp.desc())
            .limit(20)
            .all()
        )

        # -------------------
        # FETCH METRICS
        # -------------------
        metrics = (
            db.query(Metric)
            .filter(Metric.service == service)
            .order_by(Metric.timestamp.desc())
            .limit(20)
            .all()
        )

    finally:
        db.close()

    # -------------------
    # FORMAT FOR LLM
    # -------------------
    formatted_logs = [
        f"[{log.level}] {log.message}" for log in logs
    ]

    formatted_metrics = [
        f"{m.metric_name}={m.value}" for m in metrics
    ]

    return {
        "service": service,
        "logs": formatted_logs,
        "metrics": formatted_metrics
    }