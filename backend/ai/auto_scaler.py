class AutoScaler:

    def predict(self, cpu):

        if cpu > 80:

            return {
                "action": "Scale Up",
                "replicas": 5
            }

        if cpu < 20:

            return {
                "action": "Scale Down",
                "replicas": 1
            }

        return {
            "action": "Maintain",
            "replicas": 3
        }