import json
from socket import socket


def send_data(connect: socket, data: dict, encoding: str='ascii'):
    print(connect.send(pack_data(data, encoding)))


def pack_data(data: dict, encoding: str) -> bytes:
    return json.dumps(data).encode(encoding)
