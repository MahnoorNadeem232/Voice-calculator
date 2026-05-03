import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak output
def speak(text):
    print("Output:", text)
    engine.say(text)
    engine.runAndWait()

# Convert spoken words into math expression
def convert_text_to_math(text):
    text = text.lower()
    
    replacements = {
        "plus": "+",
        "minus": "-",
        "times": "*",
        "multiplied by": "*",
        "into": "*",
        "divide": "/",
        "divided by": "/",
        "over": "/",
        "power": "**"
    }

    for word, symbol in replacements.items():
        text = text.replace(word, symbol)

    return text

# Main loop
def voice_calculator():
    with sr.Microphone() as source:
        speak("Speak your calculation")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)

            expression = convert_text_to_math(text)
            print("Expression:", expression)

            result = eval(expression)
            speak(f"The result is {result}")

        except Exception as e:
            speak("Sorry, I could not understand or calculate that.")
            print("Error:", e)

# Run
voice_calculator()