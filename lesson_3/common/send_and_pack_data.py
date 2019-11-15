import json

def send_data(client: socket, data: dict, encoding: str='ascii'):
    client.send(pack_data(data, encoding))

def pack_data(data: dict, encoding: str) -> bytes:
    return json.dumps(data).encode(encoding)
