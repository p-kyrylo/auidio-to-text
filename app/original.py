import whisper
from docx import Document
import streamlit as st

# loading a base whisper model
model = whisper.load_model("base")


# function for transcribing audio file into text
def transcribe_file(file):
    if file:
        file = file + ".m4a"
        result = model.transcribe(file)
        print(result["text"])
        st.write("Files is transcribed")
        return result["text"]


# function to write transcribed text into docx file
def write_to_docx(text, file_name):
    file_name = file_name + ".docx"
    doc = Document()
    doc.add_paragraph(text)
    doc.save(file_name)
    st.write(f"Text written to {file_name}")


file = st.text_input("Enter the base name of the file: ")
transcribe_button = st.checkbox("Transcribe file")
save_path = st.text_input("Enter file path to save into: ")
save_button = st.button("Save file into docx")


text = ""


if transcribe_button:

    text = transcribe_file(file)
    st.write("Result: ", text)
if save_button:
    write_to_docx(text, save_path)
