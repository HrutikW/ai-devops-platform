class RootCauseAnalyzer:

    def analyze(self, log):

        if "CrashLoopBackOff" in log:
            return "Application Startup Failure"

        if "OutOfMemory" in log:
            return "Memory Exhaustion"

        if "ImagePullBackOff" in log:
            return "Container Image Issue"

        return "Unknown Cause"