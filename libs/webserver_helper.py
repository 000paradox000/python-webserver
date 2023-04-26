from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import threading

import ssl

from libs import utilities


class WebServerHelper(threading.Thread):
    def __init__(self, is_http: bool = True, host: str = "0.0.0.0", port: int | None = None, *args, **kwargs):
        self.host = host
        self.is_http = is_http
        self.is_https = not is_http
        self.protocol = "http" if is_http else "https"

        if not port:
            self.port = 80 if is_http else 443
        else:
            self.port = port

        self.key_path = utilities.get_certs_dir() / "key.pem"
        self.cert_path = utilities.get_certs_dir() / "cert.pem"

        super().__init__(*args, **kwargs)

    def run(self) -> None:
        msg = f"Starting server {self.protocol}://{self.host}:{self.port}"
        print(msg)
        server = HTTPServer((self.host, self.port), ServerHandler)

        if self.is_https:
            if not self.key_path.exists() or not self.cert_path.exists():
                self.generate_certificates()

            server.socket = ssl.wrap_socket(
                server.socket,
                server_side=True,
                certfile=self.cert_path.as_posix(),
                keyfile=self.key_path.as_posix(),
                ssl_version=ssl.PROTOCOL_TLSv1
           )

        server.serve_forever()

    def generate_certificates(self):
        """Generate self-signed certificates using openssl command."""
        cmd = f'openssl req ' \
              f'-newkey rsa:4096 ' \
              f'-x509 ' \
              f'-sha256 ' \
              f'-days 3650 ' \
              f'-nodes ' \
              f'-out {self.cert_path.as_posix()} ' \
              f'-keyout {self.key_path.as_posix()} ' \
              f'-subj "/C=IN/ST=ST/L=L/O=O/OU=OU Department/CN=localhost"'

        os.system(cmd)


class ServerHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        base_dir = utilities.get_base_dir()
        directory = base_dir / "static" / "linux_distributions"

        super().__init__(*args, directory=directory.as_posix(), **kwargs)
