class SLOAlert:

    def check(self, error_rate):

        if error_rate > 10:

            return {
                "alert": True,
                "message": "SLO burn rate critical"
            }

        return {
            "alert": False,
            "message": "SLO healthy"
        }