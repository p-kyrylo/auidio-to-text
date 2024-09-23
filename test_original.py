import pytest
import whisper
import os
from app import original
from docx import Document

model = whisper.load_model("base")


def test_transcribe_file():
    file = "test"
    text = original.transcribe_file(file)
    assert text == " 1 2 3 4 5"


def test_write_to_docx():
    text = " 1 2 3 4 5"
    file = "test"

    original.write_to_docx(text, file)
    assert os.path.exists(f"{file}.docx")
    doc = Document(f"{file}.docx")
    paragraphs = [p.text for p in doc.paragraphs]
    assert text in paragraphs
    os.remove(f"{file}.docx")
