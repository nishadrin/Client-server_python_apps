from socket import socket, SOCK_STREAM, AF_INET

from common.get_and_unpack_data import get_data
from common.send_and_pack_data import send_data
from common.form_alert_or_error import form_alert_or_error
from common.client.form_request import presence_msg
from common.configure import *


def read_msg_from_server(connect: socket) -> dict:
    print('connect: ', connect)
    data = get_data(connect)
    print('data: ', data)
    if data.get('response'):
        return
    if data is None or data.get('action') not in ACTIONS_TUPLE:
        send_data(connect, form_alert_or_error(400))
        return
    if data.get('action') == 'probe':
        send_data(connect, presence_msg('Nick'))
        return
    return data


def command_line(addr: str, port: int):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((addr, port))

    send_data(sock, presence_msg('Nick'))
    read_msg_from_server(sock, )

    sock.close()



if __name__ == '__main__':
    command_line('localhost', 7777)
