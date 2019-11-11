from socket import socket, AF_INET, SOCK_STREAM
import time
import json
from datetime import datetime

import click

from server_common.settings import *


def alerts_msg_text_from_code(response_code: int) -> str:
    for code, msg in ALERTS_MSGS.items():
        if int(code) == response_code:
            return msg
    return None


def form_alert(response_code: int, msg_code: str=None) -> dict:
    alert = 'alert'
    if response_code > 299:
        alert = 'error'
    if msg_code is None:
        msg_code = alerts_msg_text_from_code(response_code)
    return {
        "response": response_code,
        "time": int(datetime.now().timestamp()),
        'alert': msg_code
        }

def form_is_online() -> dict:
    return {
        "action": "probe",
        "time": int(datetime.now().timestamp()),
        }


def unpack_data(data: dict, encoding: str) -> dict:
    return json.loads(data.decode(encoding))

def pack_data(data: dict, encoding: str) -> bytes:
    return json.dumps(data).encode(encoding)

def get_data_from_client(client: socket, encoding: str='ascii') -> dict:
    recieve_bytes = client.recv(JIM_MAX_BYTES)
    if not recieve_bytes:
        return None
    return unpack_data(recieve_bytes, encoding)

def send_data_to_client(client: socket, data: dict, encoding: str='ascii'):
    client.send(pack_data(data, encoding))


def read_msg_from_client(client: socket, data: dict):
    client_request = get_data_from_client(client)
    if data is None or client_request.get('action') not in ACTIONS_TUPLE:
        send_data_to_client(client, form_alert(400))
        return None
    if client_request.get('action') == 'presence':
        send_data_to_client(client, form_alert(200))
        return None
    return client_request


@click.command()
@click.option('--port', default=DEFAULT_SERVER_PORT, help='port number')
@click.option('--addr', default=DEFAULT_SERVER_IP_ADDRESS, help='ip address')
def command_line(addr: str, port: int):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((addr, port))
    sock.listen(SOCKET_LISTENING)

    while True:
        try:
            client, addr = sock.accept()
        except KeyboardInterrupt:
            sock.close()
            time.sleep(60)
            print('Порт свободен, можно пользоваться.')
            raise

        read_msg_from_client(client, get_data_from_client(sock))

        client.close()

if __name__ == '__main__':
    command_line()
