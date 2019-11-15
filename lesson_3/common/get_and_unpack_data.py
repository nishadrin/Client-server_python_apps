import json

def unpack_data(data: bytes, encoding: str) -> dict:
    return json.loads(data.decode(encoding))

def get_data(client: socket, encoding: str='ascii') -> dict:
    recieve_bytes = client.recv(JIM_MAX_BYTES)
    if not recieve_bytes:
        return None
    return unpack_data(recieve_bytes, encoding)
