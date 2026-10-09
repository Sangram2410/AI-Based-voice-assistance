# ============================================================
# AI Voice Assistant Core
# ============================================================

from .voice_input import VoiceInput
from .voice_output import VoiceOutput
from .commands import CommandHandler


class VoiceAssistant:

    def __init__(self):

        self.voice_input = VoiceInput()

        self.voice_output = VoiceOutput()

        self.command_handler = CommandHandler(
            self.voice_output
        )

        self.running = True

    def start(self):

        self.voice_output.speak(
            "Hello. I am Nova, your accessible voice assistant."
        )

        self.voice_output.speak(
            "Say help to hear the available commands."
        )

        while self.running:

            command = self.voice_input.listen()

            if command:

                self.running = (
                    self.command_handler
                    .process_command(command)
                )