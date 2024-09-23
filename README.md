# Audio-to-text application

# Description

Whisper model based application for transcribing audio files into text. App can read your audiofile, trinscibe it into text and then let you save the text in .docx format.

# Installation 

In requirements.txt file all needed dependecies are listed, you can use *"pip install -r requirements.txt"* in order to get all needed packages and modules. 

# Usage 

1. Build a docker image:
     
     Navigate to the Dockerfile folder and run:
     `docker build -t image_name:tag .`

2. After the image is built uvicorn server will start on 8501 port
 
Here is simple step-by-step instruction to use the app:

1. Press an "upload audio file" button and specify which audio file you want to transcribe
2. Press a "transcribe audio into text" button and wait until label "audio is transcribed" appears
3. Click a "write a transcription into docx file" button in order to save a transcription in the .docx file

