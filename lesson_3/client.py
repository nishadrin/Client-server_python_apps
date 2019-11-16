from socket import socket, SOCK_STREAM, AF_INET

import click

from common.get_and_unpack_data import get_data
from common.send_and_pack_data import send_data
from common.form_alert_or_error import form_alert_or_error
from common.client.form_request import presence_msg
from common.configure import *


def read_msg_from_server(connect: socket, data: dict) -> dict:
    if data is None or data.get('action') not in ACTIONS_TUPLE:
        send_data(connect, form_alert_or_error(400))
        return
    if data.get('action') == 'probe':
        send_data(connect, presence_msg('Nick'))
        return
    return data


@click.command()
@click.argument('addr', default=DEFAULT_SERVER_IP_ADDRESS)
@click.option('--port', default=DEFAULT_SERVER_IP_ADDRESS, type=int, help='port number')
def command_line(addr: str, port: int):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((addr, port))

    send_data(sock, presence_msg('Nick'))
    msg_from_server = read_msg_from_server(sock, get_data(sock))
    print(msg_from_server)
    if msg_from_server is not None:
        print('Сообщение с сервера:', msg_from_server)

    sock.close()


if __name__ == '__main__':
    command_line()
