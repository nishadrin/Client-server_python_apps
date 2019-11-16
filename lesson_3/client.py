from socket import socket, AF_INET, SOCK_STREAM

import click

from .common.get_and_unpack_data import get_data
from .common.send_and_pack_data import send_data
from .common.forms.form_alert import form_alert
from .common.forms.client.form_request import presence_msg
from .common.settings import *


def read_msg_from_server(connect: socket, data: dict) -> dict:
    if data is None or data.get('action') not in ACTIONS_TUPLE:
        send_data(connect, form_alert(400))
        return
    if data.get('action') == 'probe':
        send_data(connect, presence_msg('Nick'))
        return
    return data


@click.command()
@click.argument('ip')
@click.option('--port', type=int, help='port number')
def command_line(ip: str, port: int):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((ip, port))

    send_data(sock, presence_msg('Nick'))
    msg_from_server = read_msg_from_server(sock, get_data(sock))

    if msg_from_server is not None:
        print('Сообщение с сервера:', msg_from_server)

    sock.close()


if __name__ == '__main__':
    if DEBUG:
        ip = DEFAULT_SERVER_IP_ADDRESS
        port = DEFAULT_SERVER_PORT
        command_line(ip, port)
    command_line()
