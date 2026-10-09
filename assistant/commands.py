# ============================================================
# Command Processing Module
# ============================================================

import datetime
import webbrowser

from config import WEBSITES
from .accessibility import Accessibility


class CommandHandler:

    def __init__(self, voice_output):

        self.voice_output = voice_output

        self.accessibility = Accessibility()

    def respond(self, text):

        self.voice_output.speak(text)

    def process_command(self, command):

        if not command:

            return True

        command = command.lower().strip()

        # ----------------------------------------------------
        # EXIT COMMAND
        # ----------------------------------------------------

        if any(
            word in command
            for word in [
                "exit",
                "quit",
                "stop assistant",
                "goodbye",
                "close assistant"
            ]
        ):

            self.respond(
                "Goodbye. I am always here when you need help."
            )

            return False

        # ----------------------------------------------------
        # GREETING
        # ----------------------------------------------------

        if any(
            word in command
            for word in [
                "hello",
                "hi",
                "hey"
            ]
        ):

            self.respond(
                "Hello. How can I help you?"
            )

            return True

        # ----------------------------------------------------
        # TIME
        # ----------------------------------------------------

        if "time" in command:

            current_time = datetime.datetime.now().strftime(
                "%I:%M %p"
            )

            self.respond(
                f"The current time is {current_time}"
            )

            return True

        # ----------------------------------------------------
        # DATE
        # ----------------------------------------------------

        if (
            "date" in command
            or "today" in command
        ):

            current_date = datetime.datetime.now().strftime(
                "%A, %d %B %Y"
            )

            self.respond(
                f"Today is {current_date}"
            )

            return True

        # ----------------------------------------------------
        # GOOGLE
        # ----------------------------------------------------

        if (
            "open google" in command
            or "google" == command
        ):

            self.respond(
                "Opening Google."
            )

            webbrowser.open(
                WEBSITES["google"]
            )

            return True

        # ----------------------------------------------------
        # YOUTUBE
        # ----------------------------------------------------

        if (
            "open youtube" in command
            or "youtube" == command
        ):

            self.respond(
                "Opening YouTube."
            )

            webbrowser.open(
                WEBSITES["youtube"]
            )

            return True

        # ----------------------------------------------------
        # GMAIL
        # ----------------------------------------------------

        if (
            "open gmail" in command
            or "gmail" == command
        ):

            self.respond(
                "Opening Gmail."
            )

            webbrowser.open(
                WEBSITES["gmail"]
            )

            return True

        # ----------------------------------------------------
        # WIKIPEDIA
        # ----------------------------------------------------

        if "wikipedia" in command:

            self.respond(
                "Opening Wikipedia."
            )

            webbrowser.open(
                WEBSITES["wikipedia"]
            )

            return True

        # ----------------------------------------------------
        # SEARCH GOOGLE
        # ----------------------------------------------------

        if command.startswith("search"):

            search_text = command.replace(
                "search",
                "",
                1
            ).strip()

            if search_text:

                self.respond(
                    f"Searching Google for {search_text}"
                )

                url = (
                    "https://www.google.com/search?q="
                    + search_text.replace(" ", "+")
                )

                webbrowser.open(url)

            else:

                self.respond(
                    "Please tell me what you want to search."
                )

            return True

        # ----------------------------------------------------
        # OPEN HOME FOLDER
        # ----------------------------------------------------

        if (
            "open home" in command
            or "open home folder" in command
        ):

            self.respond(
                "Opening your home folder."
            )

            self.accessibility.open_home_folder()

            return True

        # ----------------------------------------------------
        # OPEN DOCUMENTS
        # ----------------------------------------------------

        if (
            "open documents" in command
            or "open document folder" in command
        ):

            self.respond(
                "Opening your Documents folder."
            )

            self.accessibility.open_documents_folder()

            return True

        # ----------------------------------------------------
        # HELP
        # ----------------------------------------------------

        if (
            "help" in command
            or "what can you do" in command
        ):

            self.respond(
                "I can tell you the time and date, "
                "open websites, search Google, "
                "open folders, create notes, "
                "read notes, and help during an emergency."
            )

            return True

        # ----------------------------------------------------
        # UNKNOWN COMMAND
        # ----------------------------------------------------

        self.respond(
            "Sorry, I did not understand that command. "
            "Please say help to hear what I can do."
        )

        return True