class DriftDetector:

    def detect(self, expected, actual):

        if expected != actual:

            return {
                "drift": True,
                "message": "Infrastructure drift detected"
            }

        return {
            "drift": False,
            "message": "Infrastructure matches desired state"
        }