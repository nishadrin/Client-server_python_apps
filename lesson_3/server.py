import time
from socket import socket, SOCK_STREAM, AF_INET

from common.form_alert_or_error import form_alert_or_error
from common.get_and_unpack_data import get_data
from common.send_and_pack_data import send_data
from common.configure import *


def read_msg_from_client(client: socket):
    print('connect: ', client)
    data = get_data(client)
    print('data: ', data)
    if data.get('response'):
        return
    if data is None or data.get('action') not in ACTIONS_TUPLE:
        send_data(client, form_alert_or_error(400))
        return
    if data.get('action') == 'presence':
        send_data(client, form_alert_or_error(200))
        return
    return data


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

        read_msg_from_client(client)
        client.close()


if __name__ == '__main__':
    command_line(DEFAULT_IP_ADDRESS, DEFAULT_SERVER_PORT)
