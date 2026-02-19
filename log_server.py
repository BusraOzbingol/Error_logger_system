import socket
import json


def start_log_center(host: str = "127.0.0.1", port: int = 9000):
    """
    Start central UDP log server.

    The server listens for incoming UDP log messages
    and prints them to the console.

    :param host: Server IP address
    :type host: str
    :param port: Server port
    :type port: int
    :return: None
    """

    print(f"[LOG SERVER] Started on {host}:{port}")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    try:
        while True:
            data, address = server_socket.recvfrom(4096)

            try:
                decoded = data.decode("utf-8", errors="ignore")
                log = json.loads(decoded)

                timestamp = log.get("timestamp", "")
                level = log.get("level", "")
                mode = log.get("mode", "")
                message = log.get("message", "")
                extra = log.get("extra", {})

                print(f"\n[LOG CENTER] {timestamp} | {level} | {mode} -> {message}")
                if extra:
                    print(f"    Extra: {extra}")

            except json.JSONDecodeError:
                print("[LOG ERROR] Invalid JSON received")

    except KeyboardInterrupt:
        print("\n[LOG SERVER] Shutting down...")
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_log_center()
