Voice Calculator (Python)

A simple voice-controlled calculator built using Python. This application listens to spoken mathematical expressions, converts them into valid Python expressions, evaluates them, and speaks the result back to the user.

Features
Accepts voice input using microphone
Converts spoken words into mathematical expressions
Evaluates expressions using Python
Speaks out the result using text-to-speech
Simple and lightweight implementation

Technologies Used
Python
SpeechRecognition
Pyttsx3 (Text-to-Speech Engine)

How It Works
The program activates the microphone and asks the user to speak.
Speech is converted into text using Google's speech recognition API.
The text is processed and converted into a mathematical expression.
The expression is evaluated using Python's eval() function.
The result is spoken back to the user.

Example Commands
You can say:
"5 plus 3"
"10 divided by 2"
"7 times 6"
"2 power 3"

The program will convert these into:
5 + 3
10 / 2
7 * 6
2 ** 3

Installation & Setup
Install Python (3.x recommended)
Install required libraries:
Bash
pip install SpeechRecognition pyttsx3 pyaudio

Note:
Installing pyaudio can be tricky on some systems. You may need to install it using a precompiled wheel.

How to Run
Bash
python voice_calculator.py
Make sure your microphone is connected and working properly.

Limitations
Only supports basic arithmetic operations
Accuracy depends on speech recognition quality
Uses eval(), which is not safe for untrusted input

Requires internet connection for speech recognition

Future Improvements
Add GUI interface
Support complex mathematical expressions
Improve error handling
Replace eval() with a safer parser
Add offline speech recognition

Developers
Mahnoor Nadeem
Tazeem Fatima
