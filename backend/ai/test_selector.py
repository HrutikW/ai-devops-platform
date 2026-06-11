class TestSelector:

    def select(self, files):

        tests = []

        for file in files:

            if "auth" in file:
                tests.append("test_auth.py")

            elif "payment" in file:
                tests.append("test_payment.py")

            elif "user" in file:
                tests.append("test_user.py")

        if not tests:
            tests.append("full_regression_suite")

        return tests