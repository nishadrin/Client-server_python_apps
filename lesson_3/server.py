from socket import socket, AF_INET, SOCK_STREAM
import time
import json

import click


def receive_msg_from_client(client):
    return client.recv(1400).decode('ascii')

def form_msg_to_client(data):
    return json.dumps(data).encode('ascii')

def send_msg_to_client(client, data):
    return client.send(data)


@click.command()
@click.option('--port', default=7777, help='port number')
@click.option('--addr', default='0.0.0.0', help='ip address')
def command_line(addr, port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((addr, port))
    sock.listen(5)

    while True:
        print('*' * 50)

        try:
            client, addr = sock.accept()
        except KeyboardInterrupt:
            sock.close()
            time.sleep(60)
            print('Порт свободен, можно пользоваться.')
            raise

        print('Сообщение от клиента:', receive_msg_from_client(client))

        send_msg_to_client(client, form_msg_to_client({"response": 200}))

        client.close()


if __name__ == '__main__':
    command_line()
