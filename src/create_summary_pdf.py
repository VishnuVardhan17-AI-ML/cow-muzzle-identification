from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import (
    getSampleStyleSheet
)

pdf = SimpleDocTemplate(
    "summary_report.pdf"
)

styles = getSampleStyleSheet()

content = []

content.append(
    Paragraph(
        "Cattle Dataset Image Quality Audit",
        styles["Title"]
    )
)

content.append(
    Spacer(1,12)
)

report = """
Total Images Processed: 9996

Grade A (Excellent): 3369
Grade B (Good): 2942
Grade C (Acceptable): 2130
Grade D (Poor): 1555

A Percentage: 33.70%
B Percentage: 29.43%
C Percentage: 21.31%
D Percentage: 15.56%

Good Quality Images (A+B):
6311 (63.13%)

Low Quality Images (C+D):
3685 (36.87%)

Conclusion:

Most images in the cattle dataset
are of usable quality.

Approximately 63% of images fall
into Excellent or Good categories.

15.56% of images are Poor quality
and may require filtering before
training identification models.
"""

content.append(
    Paragraph(
        report,
        styles["BodyText"]
    )
)

pdf.build(content)

print(
    "summary_report.pdf created"
)