class CodeReviewer:

    def review(self, code):

        findings = []

        if "password" in code.lower():
            findings.append(
                "Hardcoded password detected"
            )

        if "print(" in code:
            findings.append(
                "Debug statement found"
            )

        if "except:" in code:
            findings.append(
                "Generic exception handling detected"
            )

        if len(findings) == 0:
            findings.append(
                "No issues found"
            )

        return findings