from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime
import json

import click

from client_common.settings import *


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


def form_data_msg(msg_to: str, msg_from: str, msg: str, encoding="ascii") -> dict:
    return {
        "action": "msg",
        "time": int(datetime.now().timestamp()),
        "to": msg_to,
        "from": msg_from,
        "encoding": encoding,
        "message": msg
        }

def form_data_presence_msg(user_name: str, type: str='status') -> dict:
    return {
        "action": "presence",
        "time": int(datetime.now().timestamp()),
        "type": type,
        "user": {
            "account_name": user_name,
            "status": "Hello world!"
            }
        }

def form_data_auth(user_name: str, password: str, type: str='Status') -> dict:
    return {
        "action": "authenticate",
        "time": int(datetime.now().timestamp()),
        "type": type,
        "user": {
            "account_name": user_name,
            "password": password
            }
        }


def form_data_join_or_leave_chat(room_name, leave: bool=False) -> dict:
    action = 'join'
    if leave:
        action = 'leave'
    return {
        "action": action,
        "time": int(datetime.now().timestamp()),
        "room": room_name
        }


def send_data_to_server(connect: socket, data: dict, encoding: str='ascii'):
    connect.send(pack_data(data, encoding))

def get_data_from_server(connect: socket, encoding: str='ascii') -> dict:
    recieve_bytes = connect.recv(JIM_MAX_BYTES)
    if not recieve_bytes:
        return None
    return unpack_data(recieve_bytes, encoding)

def pack_data(data: dict, encoding: str='ascii') -> bytes:
    return json.dumps(data).encode(encoding)

def unpack_data(data: bytes, encoding: str) -> dict:
    return json.loads(data.decode(encoding))


def read_msg_from_server(connect: socket, data: dict) -> dict:
    if data is None or client_request.get('action') not in ACTIONS_TUPLE:
        send_data_to_server(connect, form_alert(400))
        return None
    if data.get('action') == 'probe':
        send_data_to_server(connect, form_data_presence_msg('Nick'))
        return None
    return data


@click.command()
@click.option('--port', type=int, help='port number')
@click.argument('addr')
def command_line(addr: str, port: int):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((addr, port))

    send_data_to_server(sock, form_data_presence_msg('Nick'))
    msg_from_server = read_msg_from_server(sock, get_data_from_server(sock))

    if msg_from_server is not None:
        print('Сообщение с сервера:', msg_from_server)

    sock.close()

if __name__ == '__main__':
    command_line()
