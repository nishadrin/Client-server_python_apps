import time
from socket import socket, SOCK_STREAM, AF_INET

import click

from common.utils import DataExchange as DE, FormAlertOrError as FAOE
from common.config import *

FAOE = FAOE()
DE = DE()


# по сути это обработчик событий, не могу понять как правильно его
# построить и написать под него тесты
# вижу 2 варианта, либо через is DEBUG внутри функции ниже (+if), либо
# сокеты сразу передавать в виде аргумента, но так вроде не правильно
# тестировать
def read_msg_from_client(data: dict, sock: socket) -> dict:
    print('connect: ', sock)
    print('data: ', data)
    if data.get('response'):
        return data
    if data is None or data.get('action') not in ACTIONS_TUPLE:
        DE.send_data(sock, FAOE.form_alert_or_error(400))
        return data
    if data.get('action') == 'presence':
        DE.send_data(sock, FAOE.form_alert_or_error(200))
        return data
    return


@click.command()
@click.option('--addr', default=DEFAULT_IP_ADDRESS, help='ip address')
@click.option('--port', default=DEFAULT_SERVER_PORT, help='port number')
def command_line(addr: str, port: int):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((addr, port))
    sock.listen(SOCKET_LISTENING)
    while True:
        try:
            client, addr = sock.accept()
        except KeyboardInterrupt:
            sock.close()
            print('Ожидайте закрытия минуту.')
            time.sleep(60)
            print('Порт свободен, можно пользоваться.')
            raise

        read_msg_from_client(DE.get_data(client), client)

        client.close()


if __name__ == '__main__':
    command_line()
