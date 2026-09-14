import markdown
from fpdf import FPDF
import re

with open("SENTINEL_Comprehensive_Submission.md", "r") as f:
    md_content = f.read()

# FPDF's write_html can struggle with complex nested markdown structures. 
# We'll do a simple conversion that FPDF handles well.
html = markdown.markdown(md_content)
# Clean up emoji for FPDF which might fail on unsupported unicode chars
html = re.sub(r'[✅]', '(*)', html)

class PDF(FPDF):
    pass

pdf = PDF()
pdf.add_page()
pdf.add_font("Arial", "", fname="/System/Library/Fonts/Supplemental/Arial.ttf", uni=True)
pdf.add_font("Arial", "B", fname="/System/Library/Fonts/Supplemental/Arial Bold.ttf", uni=True)
pdf.add_font("Arial", "I", fname="/System/Library/Fonts/Supplemental/Arial Italic.ttf", uni=True)
pdf.set_font("Arial", size=11)
pdf.write_html(html)
pdf.output("SENTINEL_Comprehensive_Submission.pdf")
