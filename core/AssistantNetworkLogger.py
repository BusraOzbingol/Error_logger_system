class AssistantNetworkLogger(ILogger):
    """
    Logları UDP üzerinden merkezi sunucuya gönderir.
    """
    def __init__(self, host='127.0.0.1', port=9000):
        self.addr = (host, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def log_event(self, level: str, mode: str, message: str, extra: dict = None):
        """
        Log mesajını JSON formatında sunucuya gönderir.
        """
        payload = {
            "zaman": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "seviye": level,
            "mod": mode,
            "mesaj": message,
            "ekstra": extra or {}
        }
        try:
            msg = json.dumps(payload).encode('utf-8')
            self.sock.sendto(msg, self.addr)
        except Exception as e:
            print(f"[LOG ERROR] Mesaj gönderilemedi: {e}")