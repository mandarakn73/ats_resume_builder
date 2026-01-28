from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_pdf(text):
    path = "ATS_Resume.pdf"
    c = canvas.Canvas(path, pagesize=A4)
    t = c.beginText(40, 800)
    for line in text.split("\n"):
        t.textLine(line)
    c.drawText(t)
    c.save()
    return path
