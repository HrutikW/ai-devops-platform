from fastapi import APIRouter
from pydantic import BaseModel

from backend.ai.incident_engine import analyze_incident
from backend.ai.anomaly_detector import AnomalyDetector
from backend.ai.root_cause_analyzer import RootCauseAnalyzer
from backend.ai.auto_remediation import AutoRemediation
from backend.ai.intelligence_pipeline import IntelligencePipeline
from backend.ai.code_reviewer import CodeReviewer
from backend.ai.test_selector import TestSelector
from backend.ai.rollback_predictor import RollbackPredictor
from backend.ai.security_scanner import SecurityScanner
from backend.ai.terraform_reviewer import TerraformReviewer
from backend.ai.drift_detector import DriftDetector
from backend.ai.cost_optimizer import CostOptimizer
from backend.ai.auto_scaler import AutoScaler
from backend.ai.log_intelligence import LogIntelligence
from backend.ai.dora_metrics import DoraMetrics
from backend.ai.timeline_generator import TimelineGenerator
from backend.ai.slo_alert import SLOAlert 

# Create router FIRST
router = APIRouter()


# =====================
# Request Models
# =====================

class MetricRequest(BaseModel):
    cpu: int


class LogRequest(BaseModel):
    log: str


class CauseRequest(BaseModel):
    cause: str

class PipelineRequest(BaseModel):
    log: str

class CodeReviewRequest(BaseModel):
    code: str

class TestRequest(BaseModel):
    files: list[str]

class RollbackRequest(BaseModel):
    failure_rate: int

class TerraformRequest(BaseModel):
    code: str

class DriftRequest(BaseModel):
    expected: str
    actual: str

class CostRequest(BaseModel):
    cpu_usage: int

class ScaleRequest(BaseModel):
    cpu: int

class LogIntelligenceRequest(BaseModel):
    log: str

class SLORequest(BaseModel):
    error_rate: int

# =====================
# Incident Analysis
# =====================

@router.get("/incident/{service}")
def incident(service: str):

    result = analyze_incident(service)

    return {
        "service": service,
        "analysis": result
    }


# =====================
# Anomaly Detection
# =====================

@router.post("/anomaly")
def detect_anomaly(data: MetricRequest):

    detector = AnomalyDetector()

    return detector.detect(data.cpu)


# =====================
# Root Cause Analysis
# =====================

@router.post("/root-cause")
def root_cause(data: LogRequest):

    analyzer = RootCauseAnalyzer()

    return {
        "cause": analyzer.analyze(data.log)
    }


# =====================
# Auto Remediation
# =====================

@router.post("/remediate")
def remediate(data: CauseRequest):

    engine = AutoRemediation()

    return {
        "action": engine.remediate(data.cause)
    }



@router.post("/pipeline")
def pipeline(data: PipelineRequest):

    engine = IntelligencePipeline()

    return engine.process(data.log)



@router.post("/code-review")
def code_review(data: CodeReviewRequest):

    reviewer = CodeReviewer()

    return {
        "findings": reviewer.review(data.code)
    }


@router.post("/test-selection")
def test_selection(data: TestRequest):

    selector = TestSelector()

    return {
        "tests": selector.select(data.files)
    }

@router.post("/rollback")
def rollback(data: RollbackRequest):

    predictor = RollbackPredictor()

    return predictor.predict(
        data.failure_rate
    )

@router.post("/security-scan")
def security_scan(data: CodeReviewRequest):

    scanner = SecurityScanner()

    return {
        "issues": scanner.scan(data.code)
    }

@router.post("/terraform-review")
def terraform_review(data: TerraformRequest):

    reviewer = TerraformReviewer()

    return {
        "findings": reviewer.review(data.code)
    }

@router.post("/drift-detection")
def drift_detection(data: DriftRequest):

    detector = DriftDetector()

    return detector.detect(
        data.expected,
        data.actual
    )

@router.post("/cost-optimize")
def cost_optimize(data: CostRequest):

    optimizer = CostOptimizer()

    return optimizer.optimize(
        data.cpu_usage
    )

@router.post("/auto-scale")
def auto_scale(data: ScaleRequest):

    scaler = AutoScaler()

    return scaler.predict(
        data.cpu
    )

@router.post("/log-intelligence")
def log_intelligence(data: LogIntelligenceRequest):

    engine = LogIntelligence()

    return engine.analyze(data.log)

@router.get("/dora")
def dora():

    metrics = DoraMetrics()

    return metrics.calculate()

@router.get("/timeline")
def timeline():

    generator = TimelineGenerator()

    return {
        "events": generator.generate()
    }

@router.post("/slo-alert")
def slo_alert(data: SLORequest):

    checker = SLOAlert()

    return checker.check(
        data.error_rate
    )