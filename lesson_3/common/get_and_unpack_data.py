import json
import socket

from .configure import JIM_MAX_BYTES


def unpack_data(data: bytes, encoding: str) -> dict:
    return json.loads(data.decode(encoding))


def get_data(connect: socket, encoding: str='ascii') -> dict:
    print(connect)
    recieve_bytes = connect.recv(JIM_MAX_BYTES)
    print(recieve_bytes)
    if not recieve_bytes:
        return
    return unpack_data(recieve_bytes, encoding)
