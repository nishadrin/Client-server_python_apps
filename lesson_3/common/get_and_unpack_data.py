import json
import socket

from .configure import JIM_MAX_BYTES


def unpack_data(data: bytes, encoding: str) -> dict:
    return json.loads(data.decode(encoding))


def get_data(sock: socket, encoding: str='ascii') -> dict:
    recieve_bytes = sock.recv(JIM_MAX_BYTES)
    if not recieve_bytes:
        return
    return unpack_data(recieve_bytes, encoding)
