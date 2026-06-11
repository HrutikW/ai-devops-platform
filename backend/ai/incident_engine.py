def analyze_incident(service):

    incidents = {
        "frontend": {
            "root_cause": "CrashLoopBackOff",
            "severity": "High",
            "fix": "Restart deployment and inspect logs"
        },
        "backend": {
            "root_cause": "Database connection timeout",
            "severity": "Critical",
            "fix": "Check database connectivity"
        },
        "jenkins": {
            "root_cause": "Pipeline failure",
            "severity": "Medium",
            "fix": "Review build logs"
        }
    }

    return {
        "service": service,
        "analysis": incidents.get(
            service,
            {
                "root_cause": "Unknown",
                "severity": "Low",
                "fix": "Manual investigation required"
            }
        )
    }