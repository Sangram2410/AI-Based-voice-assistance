# ============================================================
# Voice Input Module
# Converts speech into text
# ============================================================

import speech_recognition as sr


class VoiceInput:

    def __init__(self):
        self.recognizer = sr.Recognizer()

        self.recognizer.energy_threshold = 300

        self.recognizer.dynamic_energy_threshold = True

    def listen(self):

        with sr.Microphone() as source:

            print("\n🎤 Listening...")

            try:
                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )

            except sr.WaitTimeoutError:
                print("No speech detected.")
                return ""

        try:

            print("🔄 Processing...")

            text = self.recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            print(f"You: {text}")

            return text.lower()

        except sr.UnknownValueError:

            print("Could not understand the speech.")

            return ""

        except sr.RequestError:

            print(
                "Speech recognition service is unavailable."
            )

            return ""