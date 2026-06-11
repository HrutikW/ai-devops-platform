from backend.ai.root_cause_analyzer import RootCauseAnalyzer
from backend.ai.auto_remediation import AutoRemediation

class IntelligencePipeline:

    def process(self, log):

        analyzer = RootCauseAnalyzer()
        cause = analyzer.analyze(log)

        remediation = AutoRemediation()
        action = remediation.remediate(cause)

        return {
            "cause": cause,
            "recommended_action": action
        }