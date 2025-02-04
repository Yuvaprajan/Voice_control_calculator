# File: src/voice_recognition.py
import speech_recognition as sr
import time

class VoiceRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self, prompt=None, timeout=5):
        """
        Listen to voice input with configurable timeout
        """
        if prompt:
            print(prompt)
        
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            try:
                audio = self.recognizer.listen(source, timeout=timeout)
                text = self.recognizer.recognize_google(audio).lower()
                print(f"Recognized: {text}")
                return text
            except sr.WaitTimeoutError:
                print("Listening timed out.")
                return None
            except sr.UnknownValueError:
                print("Could not understand audio.")
                return None
            except sr.RequestError:
                print("Speech recognition service error.")
                return None