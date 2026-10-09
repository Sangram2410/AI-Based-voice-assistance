# ============================================================
# Accessibility Module
# ============================================================

import os
import platform
import subprocess
import webbrowser


class Accessibility:

    def open_website(self, url):
        webbrowser.open(url)

    def open_folder(self, folder):
        """
        Open a folder using the operating system.
        """

        system = platform.system()

        try:

            if system == "Windows":

                os.startfile(folder)

            elif system == "Darwin":

                subprocess.run(
                    ["open", folder]
                )

            elif system == "Linux":

                subprocess.run(
                    ["xdg-open", folder]
                )

        except Exception as error:

            print("Could not open folder:", error)

    def open_home_folder(self):

        home = os.path.expanduser("~")

        self.open_folder(home)

    def open_documents_folder(self):

        documents = os.path.join(
            os.path.expanduser("~"),
            "Documents"
        )

        if os.path.exists(documents):

            self.open_folder(documents)

        else:

            print("Documents folder not found.")