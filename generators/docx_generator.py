from docx import Document

def create_docx(text):
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    path = "ATS_Resume.docx"
    doc.save(path)
    return path
