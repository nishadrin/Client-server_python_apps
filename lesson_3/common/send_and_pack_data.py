import json
from socket import socket

def send_data(connection: socket, data: dict, encoding: str='ascii'):
    connection.send(pack_data(data, encoding))

def pack_data(data: dict, encoding: str) -> bytes:
    return json.dumps(data).encode(encoding)
