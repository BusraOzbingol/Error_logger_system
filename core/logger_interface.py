from abc import ABC, abstractmethod


class ILogger(ABC):
    """
    Abstract base class for logging implementations.

    Defines the contract that all logger classes must follow.
    """

    @abstractmethod
    def log_event(self, level: str, mode: str, message: str, extra: dict = None):
        """
        Log an event.

        :param level: Log severity level (e.g., INFO, ERROR)
        :type level: str
        :param mode: Application mode (e.g., Q&A, Summarization)
        :type mode: str
        :param message: Main log message
        :type message: str
        :param extra: Additional contextual data
        :type extra: dict, optional
        :return: None
        """
        pass
