class TerraformReviewer:

    def review(self, terraform_code):

        findings = []

        if "0.0.0.0/0" in terraform_code:
            findings.append(
                "Security risk: Open access detected"
            )

        if "t2.micro" in terraform_code:
            findings.append(
                "Instance may be underpowered"
            )

        if "encrypted = false" in terraform_code:
            findings.append(
                "Storage encryption disabled"
            )

        if not findings:
            findings.append(
                "No Terraform issues found"
            )

        return findings