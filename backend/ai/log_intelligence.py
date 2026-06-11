class LogIntelligence:

    def analyze(self, log):

        if "OOMKilled" in log:
            return {
                "summary": "Application terminated due to memory exhaustion",
                "severity": "High"
            }

        if "CrashLoopBackOff" in log:
            return {
                "summary": "Application repeatedly crashing during startup",
                "severity": "Critical"
            }

        if "ImagePullBackOff" in log:
            return {
                "summary": "Container image could not be downloaded",
                "severity": "Medium"
            }

        return {
            "summary": "No significant issue detected",
            "severity": "Low"
        }