# ============================================================
# MAIN PROGRAM
# AI Voice Assistant for People with Disabilities
# ============================================================

from assistant.assistant_core import VoiceAssistant


def main():

    print("=" * 60)

    print(
        "       AI VOICE ASSISTANT FOR PEOPLE WITH DISABILITIES"
    )

    print("=" * 60)

    print()

    print("Starting assistant...")

    print(
        "Press Ctrl+C anytime to stop the program."
    )

    print()

    assistant = VoiceAssistant()

    try:

        assistant.start()

    except KeyboardInterrupt:

        print(
            "\nAssistant stopped by user."
        )

    except Exception as error:

        print(
            "\nAn unexpected error occurred:"
        )

        print(error)


if __name__ == "__main__":

    main()