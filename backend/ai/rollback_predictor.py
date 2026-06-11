class RollbackPredictor:

    def predict(self, failure_rate):

        if failure_rate > 50:
            return {
                "rollback": True,
                "reason": "High deployment failure rate"
            }

        return {
            "rollback": False,
            "reason": "Deployment stable"
        }