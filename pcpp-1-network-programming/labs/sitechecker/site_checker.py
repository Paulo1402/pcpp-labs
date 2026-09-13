import socket
import requests
from http import HTTPStatus
from abc import ABC, abstractmethod

from sitechecker.exception import (
    SiteCheckerInsufficientParametersError,
    SiteCheckerBadParameterError,
    SiteCheckerTimeoutError,
    SiteCheckerError,
)


class SiteChecker(ABC):
    def __init__(self, timeout_error):
        self._timeout_error = timeout_error

    def check(self, *args):
        server, port = self._validate_args(*args)

        try:
            self._check(server, port)
        except self._timeout_error:
            raise SiteCheckerTimeoutError("Connection timed out") from e
        except Exception as e:
            raise SiteCheckerError(f"Something went wrong: {e}") from e

    @abstractmethod
    def _check(self, server, port):
        pass

    def _validate_args(self, *args):
        if len(args) not in [1, 2]:
            raise SiteCheckerInsufficientParametersError(
                "Improper number of arguments: at least one is required and not more than two are allowed:\n"
                "- http server's address (required)\n"
                "- port number (defaults to 80 if not specified)"
            )

        server = args[0]
        port = 80

        if len(args) == 2:
            try:
                port = int(args[1])

                if port < 1 or port > 65535:
                    raise ValueError("Invalid range")
            except (TypeError, ValueError) as e:
                raise SiteCheckerBadParameterError(
                    "Port number is invalid - exiting"
                ) from e

        return server, port


class SocketSiteChecker(SiteChecker):
    def __init__(self):
        super().__init__(timeout_error=socket.timeout)

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.settimeout(5)

    def _check(self, server, port):
        self._sock.connect((server, port))

        data = (
            "HEAD / HTTP/1.1\r\n"
            + f"Host: {server}\r\n"
            + "Connection: close\r\n"
            + "\r\n"
        )

        self._sock.sendall(bytes(data, encoding="utf8"))

        response = b""

        while True:
            data = self._sock.recv(4096)
            if not data:
                break
            response += data

        print(response.decode(errors="replace"))

        self._sock.shutdown(socket.SHUT_RDWR)
        self._sock.close()


class HTTPSiteChecker(SiteChecker):
    HTTP_VERSIONS = {
        9: "HTTP/0.9",
        10: "HTTP/1.0",
        11: "HTTP/1.1",
    }

    def __init__(self):
        super().__init__(TimeoutError)

    def _check(self, server, port):
        if port == 80:
            prefix = "http"
        elif port == 443:
            prefix = "https"
        else:
            raise ValueError(
                f"{self.__class__.__name__} only supports http(80) and https(443) ports"
            )

        response = requests.head(f"{prefix}://{server}:{port}")
        metadata = self._get_response_metadata(response)

        print(
            metadata["http_version"],
            metadata["status_code"],
            metadata["status_code_name"],
        )

        for header, value in response.headers.items():
            print(f"{header}: {value}")

    def _get_response_metadata(self, response):
        return {
            "http_version": self.HTTP_VERSIONS.get(response.raw.version),
            "status_code": response.status_code,
            "status_code_name": HTTPStatus(response.status_code).phrase,
        }
