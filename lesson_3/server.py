import time
from socket import AF_INET, SOCK_STREAM, socket

import click

from .common.forms.form_alert import form_alert
from .common.get_and_unpack_data import get_data
from .common.send_and_pack_data import send_data
from .common.settings import *


def read_msg_from_client(client: socket, data: dict):
    client_request = get_data(client)
    if data is None or client_request.get('action') not in ACTIONS_TUPLE:
        send_data(client, form_alert(400))
        return None
    if client_request.get('action') == 'presence':
        send_data(client, form_alert(200))
        return None
    return client_request


@click.command()
@click.option('--ip', default=DEFAULT_SERVER_IP_ADDRESS, help='ip address')
@click.option('--port', default=DEFAULT_SERVER_PORT, help='port number')
def command_line(ip: str, port: int):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(SOCKET_LISTENING)

    while True:
        try:
            client, ip = sock.accept()
        except KeyboardInterrupt:
            sock.close()
            time.sleep(60)
            print('Порт свободен, можно пользоваться.')
            raise

        read_msg_from_client(client, get_data(sock))

        client.close()


if __name__ == '__main__':
    command_line()
