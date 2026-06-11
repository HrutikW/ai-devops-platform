class AnomalyDetector:

    def detect(self, cpu_usage):

        if cpu_usage > 80:
            return {
                "anomaly": True,
                "severity": "High",
                "message": "CPU spike detected"
            }

        return {
            "anomaly": False,
            "severity": "Normal",
            "message": "System healthy"
        }