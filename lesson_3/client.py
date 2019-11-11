from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime
import json

import click
from client_common.settings import *


def form_data_msg(msg_to:str, msg_from:str, msg:str, encoding="ascii") -> dict:
    return {
        "action": "msg",
        "time": int(datetime.now().timestamp()),
        "to": msg_to,
        "from": msg_from,
        "encoding": encoding,
        "message": msg
        }

def form_data_presence_msg(user_name:str, type:str='Status') -> dict:
    return {
        "action": "presence",
        "time": int(datetime.now().timestamp()),
        "type": type,
        "user": {
            "account_name": user_name,
            "status": "Hello world!"
            }
        }

def form_data_auth(user_name:str, password:str, type:str='Status') -> dict:
    return {
        "action": "authenticate",
        "time": int(datetime.now().timestamp()),
        "type": type,
        "user": {
            "account_name": user_name,
            "password": password
            }
        }

def form_data_join_or_leave_chat(room_name, leave:bool=False) -> dict:
    action = 'join'
    if leave:
        action = 'leave'
    return {
        "action": action,
        "time": int(datetime.now().timestamp()),
        "room": room_name
        }


def send_data_to_server(connect:socket, data:dict, encoding:str='ascii'):
    connect.send(pack_data(data, encoding))

def get_data_from_server(connect:socket, encoding:str='ascii') -> dict:
    print(connect.recv(JIM_MAX_BYTES).decode(encoding)) # b''
    return unpack_data(connect.recv(JIM_MAX_BYTES), encoding)

def pack_data(data:dict, encoding:str='ascii') -> bytes:
    return json.dumps(data).encode(encoding)

def unpack_data(data:dict, encoding:str) -> dict:
    return json.loads(data.decode(encoding))


def read_msg_from_server(connect:socket, data:dict) -> dict:
    if data.get('action') == 'probe':
        send_data_to_server(connect, form_data_presence_msg('Nick'))
        return None
    return data


@click.command()
@click.option('--port', type=int, help='port number')
@click.argument('addr')
def command_line(addr:str, port:int):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((addr, port))

    send_data_to_server(sock, form_data_presence_msg('Nick'))

    msg_from_server = read_msg_from_server(sock, get_data_from_server(sock))

    if msg_from_server is not None:
        print('Сообщение с сервера:', msg_from_server)

    sock.close()

if __name__ == '__main__':
    command_line()
