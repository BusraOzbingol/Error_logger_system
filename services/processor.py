from core.logger_interface import ILogger


class SyncProcessor:
    """
    Processes user input synchronously.

    This class depends on the ILogger abstraction
    (Dependency Inversion Principle).
    """

    def __init__(self, logger: ILogger):
        """
        Initialize the processor.

        :param logger: Logger implementation
        :type logger: ILogger
        """
        self.logger = logger

    def process_request(self, user_input: str, mode: str) -> str:
        """
        Process user input and generate a response.

        :param user_input: User input string
        :type user_input: str
        :param mode: Current application mode
        :type mode: str
        :return: Generated response
        :rtype: str
        """

        if mode == "Summarization":
            response = f"Summarized content: {user_input[:30]}..."
        else:
            response = f"Q&A response: {user_input}"

        self.logger.log_event(
            level="INFO",
            mode=mode,
            message=user_input,
            extra={"response": response}
        )

        return response
