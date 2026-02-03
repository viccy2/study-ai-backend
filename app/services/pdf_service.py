import fitz
import tempfile
import os
from fastapi import UploadFile

async def extract_text_from_pdf(file: UploadFile) -> str:
    suffix = os.path.splitext(file.filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        doc = fitz.open(tmp_path)
        text = "".join([page.get_text() for page in doc])
        return text
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
