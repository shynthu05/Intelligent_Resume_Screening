import PyPDF2
from docx import Document


def extract_pdf_text(file):

    text = ""

    reader = PyPDF2.PdfReader(file)

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_docx_text(file):

    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"

    return text


def extract_resume_text(file):

    filename = file.name.lower()

    if filename.endswith(".pdf"):

        return extract_pdf_text(file)

    elif filename.endswith(".docx"):

        return extract_docx_text(file)

    else:

        return "Unsupported file format."