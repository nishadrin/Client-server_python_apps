from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime
import json

import click


def presence_msg():
    return json.dumps({
        "action": "presence",
        "time": int((datetime.now() - datetime(1970, 1, 1)).total_seconds()),
        "type": "status"
        }).encode('ascii')

def send_msg_to_server(socket, data):
    return socket.send(data)

def receive_msg_from_server(socket):
    return socket.recv(1400).decode('ascii')

def make_msg_from_server(data):
    return data.decode('ascii')


@click.command()
@click.option('--port', type=int, help='port number')
@click.argument('addr')
def command_line(addr, port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((addr, port))

    send_msg_to_server(sock, presence_msg())

    print('Сообщение с сервера:', receive_msg_from_server(sock))

    sock.close

if __name__ == '__main__':
    command_line()
