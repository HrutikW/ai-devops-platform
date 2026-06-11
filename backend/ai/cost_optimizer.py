class CostOptimizer:

    def optimize(self, cpu_usage):

        if cpu_usage < 20:

            return {
                "saving_possible": True,
                "recommendation":
                "Scale down resources"
            }

        return {
            "saving_possible": False,
            "recommendation":
            "Current sizing is appropriate"
        }