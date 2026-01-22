import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    # Open PDF from Streamlit uploaded file
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    text = ""
    for page in doc:
        text += page.get_text()

    return text
