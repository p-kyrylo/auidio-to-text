# Audio-to-text application

# Description

Whisper model based application for transcribing audio files into text. App can read your audiofile, trinscibe it into text and then let you save the text in .docx format. There are two sctipts *main.py* and *original.py*, basically both of them are the same app, the only difference is the first one is built using *customtkinter* GUI, the second one using *streamlit*, so it can be executed in the docker container.

# Installation 

In requirements.txt file all needed dependecies are listed, you can use *"pip install -r requirements.txt"* in order to get all needed packages and modules. 

# Usage 

Here is simple step-by-step instruction (if ***main.py*** is executed):

1. Press an "upload audio file" button and specify which audio file you want to transcribe
2. Press a "transcribe audio into text" button and wait until label "audio is transcribed" appears
3. Click a "write a transcription into docx file" button in order to save a transcription in the .docx file

