# LIPSYNC

Lip Sync is a desktop app that syncs user uploaded video to an audio with the help of an AI model. After syncing the video to the audio, it downloads the file into the computer.

## Requirements

- customtkinter
- pillow
- opencv

## Running LipSync

- Clone or fork the lipsyc repo
- Install the necessary requirements needed so as to run the app smoothly
- Run the app from your console _python3 main.py_ or from your IDE

## Understanding the Codebase

### The main

The _main.py_ file contains the default screen for app. In the development of the app, an OOP paradigm is employed for readability and best practices.

In the _main.py_, it contains the _class App_ which is inherit from the customtkinter module. Inside of the _class App_ we have the **init** function that initialize the app and shows the default screen you see when the program is launched.

### The edit

The _edit.py_ file contains the screen where user upload a video, audio and also do needed settings for AI model to give a desired output

The _edit.py_ file contains two section the _settings frame_ and the _upload frame_. The _settings frame_ holds all of the widgets for required parameter to pass to the AI model'. The _upload frame_ contains where user can upload their video, audio and still show them the file path and a video preview

The screen in the _edit.py_ is activated when the generate button in the default screen is pressed
