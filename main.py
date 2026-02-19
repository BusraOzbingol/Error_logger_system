from core.log_handlers import AssistantNetworkLogger
from services.processor import SyncProcessor


def main():
    """
    Main CLI application entry point.
    """

    logger = AssistantNetworkLogger()
    processor = SyncProcessor(logger)

    current_mode = "Q&A"

    print("=" * 50)
    print(" Logging System Active (UDP port 9000)")
    print("=" * 50)

    while True:
        try:
            user_input = input(f"\n[{current_mode}] You: ").strip()

            if not user_input:
                continue

            if user_input == "/exit":
                break

            if user_input.startswith("/"):
                if "/summarizer" in user_input:
                    current_mode = "Summarization"
                    print("✓ Switched to Summarization mode.")
                elif "/qa" in user_input:
                    current_mode = "Q&A"
                    print("✓ Switched to Q&A mode.")
                continue

            response = processor.process_request(user_input, current_mode)
            print(f"Assistant: {response}")

        except KeyboardInterrupt:
            break

    print("\nSystem shutting down... Goodbye!")


if __name__ == "__main__":
    main()
