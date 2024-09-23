import whisper
from docx import Document
from tkinter import filedialog
import customtkinter as ctk
from fastapi import FastAPI

# App with customtkinter GUI

# creating an instance of FastApi
app = FastAPI()

# loading a base whisper model
model = whisper.load_model("base")


# function for getting a path of the audio file
def getFpath():
    file_path = filedialog.askopenfilename(
        filetypes=[("Audio files", "*.wav;*.mp3;*.m4a")]
    )
    create_label("file is selected")
    print("Selected file:", file_path)
    global selected_file
    selected_file = file_path


# function for creating labels
def create_label(text):
    label = ctk.CTkLabel(window, text=text)
    label.pack()


# function for transcribing audio file into text
def transcribe_file():
    create_label("audio is transcribed")
    if selected_file:
        global result
        result = model.transcribe(selected_file)
        print(result["text"])


# function to write transcribed text into docx file
def write_to_docx():
    file_name = filedialog.asksaveasfilename(
        defaultextension=".docx", filetypes=[("Word Document", "*.docx")]
    )
    create_label("file is saved")
    if file_name:
        doc = Document()
        doc.add_paragraph(result["text"])

        doc.save(file_name)
        print(f"Text written to {file_name}")


@app.get("/run_app")
def run_app():
    # creating window
    global window
    window = ctk.CTk()
    window.title("Task 2")
    window.geometry("600x400")

    # creating introducing label
    label = ctk.CTkLabel(
        window,
        width=6,
        height=50,
        text="Upload a file which you want to transcribe",
        font=(20, 20),
    )
    label.pack()

    # creating frame
    frame = ctk.CTkFrame(window, fg_color="transparent")
    frame.pack()

    # creating buttons
    upload_button = ctk.CTkButton(frame, text="upload audio file", command=getFpath)
    upload_button.pack()
    transcribe_button = ctk.CTkButton(
        frame, text="transcribe audio into text", command=transcribe_file
    )
    transcribe_button.pack()
    write_button = ctk.CTkButton(
        frame, text="write a transcription into docx file", command=write_to_docx
    )
    write_button.pack()

    window.mainloop()
