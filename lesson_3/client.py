from socket import socket, SOCK_STREAM, AF_INET

import click

from common.utils import DataExchange as DE, FormAlertOrError as FAOE
from common.client.form_request import presence_msg
from common.config import *

FAOE = FAOE()
DE = DE()


def read_msg_from_server(data: dict, sock: socket) -> dict:
    print('connect: ', sock)
    print('data: ', data)
    if data.get('response'):
        return data
    if data is None or data.get('action') not in ACTIONS_TUPLE:
        DE.send_data(sock, FAOE.form_alert_or_error(400))
        return data
    if data.get('action') == 'probe':
        DE.send_data(sock, presence_msg('Nick'))
        return data
    return


@click.command()
@click.argument('addr')
@click.option('--port', type=int, help='port number')
def command_line(addr: str, port: int):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((addr, port))

    DE.send_data(sock, presence_msg('Nick'))
    read_msg_from_server(DE.get_data(sock), sock)

    sock.close()


if __name__ == '__main__':
    command_line()

