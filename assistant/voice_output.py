# ============================================================
# Voice Output Module
# Converts text into speech
# ============================================================

import pyttsx3
from config import SPEECH_RATE


class VoiceOutput:

    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.setProperty(
            "rate",
            SPEECH_RATE
        )

        # Volume between 0.0 and 1.0
        self.engine.setProperty(
            "volume",
            1.0
        )

    def speak(self, text):
        """
        Speak the supplied text.
        """

        print(f"Nova: {text}")

        self.engine.say(text)
        self.engine.runAndWait()