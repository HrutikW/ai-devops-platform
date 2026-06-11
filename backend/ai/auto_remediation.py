class AutoRemediation:

    def remediate(self, cause):

        actions = {
            "Application Startup Failure":
                "Restart Deployment",

            "Memory Exhaustion":
                "Scale Deployment",

            "Container Image Issue":
                "Pull Latest Image"
        }

        return actions.get(
            cause,
            "Manual Investigation Required"
        )
