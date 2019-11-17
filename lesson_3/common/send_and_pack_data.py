import json
from socket import socket


def send_data(sock: socket, data: dict, encoding: str='ascii'):
    sock.send(pack_data(data, encoding))


def pack_data(data: dict, encoding: str) -> bytes:
    return json.dumps(data).encode(encoding)
