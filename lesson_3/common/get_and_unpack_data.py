import json
from socket import socket

from .settings import JIM_MAX_BYTES


def unpack_data(data: bytes, encoding: str) -> dict:
    return json.loads(data.decode(encoding))


def get_data(connection: socket, encoding: str='ascii') -> dict:
    print(connection)
    recieve_bytes = connection.recv(JIM_MAX_BYTES)
    if not recieve_bytes:
        return
    return unpack_data(recieve_bytes, encoding)
