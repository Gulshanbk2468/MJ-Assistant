"""
MJ ASSISTANT - MAIN ENTRY FILE
FINAL VERSION
"""

from assistant.ui import launch_ui


def main():
    """
    Start MJ Assistant UI
    """

    try:

        print("🚀 Starting MJ Assistant...")

        launch_ui()

    except KeyboardInterrupt:

        print("\n🛑 MJ Assistant stopped by user.")

    except Exception as e:

        print(f"⚠️ Startup Error: {e}")


if __name__ == "__main__":

    main()