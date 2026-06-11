class SecurityScanner:

    def scan(self, code):

        issues = []

        if "eval(" in code:
            issues.append("Unsafe eval usage")

        if "password" in code.lower():
            issues.append("Hardcoded credential")

        if not issues:
            issues.append("No security issues found")

        return issues