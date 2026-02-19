import socket
import json
from datetime import datetime
from .logger_interface import ILogger


class AssistantNetworkLogger(ILogger):
    """
    UDP-based logger implementation.

    Sends structured log messages to a central log server.
    """

    def __init__(self, host: str = "127.0.0.1", port: int = 9000):
        """
        Initialize the network logger.

        :param host: Log server IP address
        :type host: str
        :param port: Log server port
        :type port: int
        """
        self.address = (host, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def log_event(self, level: str, mode: str, message: str, extra: dict = None):
        """
        Send a log event to the central server.

        :param level: Log severity level
        :type level: str
        :param mode: Application mode
        :type mode: str
        :param message: Log message
        :type message: str
        :param extra: Additional contextual information
        :type extra: dict, optional
        """
        payload = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level": level,
            "mode": mode,
            "message": message,
            "extra": extra or {}
        }

        try:
            encoded = json.dumps(payload).encode("utf-8")
            self.socket.sendto(encoded, self.address)
        except Exception as e:
            print(f"[LOG ERROR] Failed to send log: {e}")
