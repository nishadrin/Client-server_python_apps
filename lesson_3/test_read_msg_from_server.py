import unittest
import subprocess

from client import read_msg_from_server
from common.configure import PROJECT_MAIN_PATH


class TestReadMsgFromServer(unittest.TestCase):
    pass


class TestConnections(unittest.TestCase):
    def connection(self, process, addr, port):
        return subprocess.Popen(
            [process, addr, '--port', port],
            stdout=subprocess.PIPE,
            start_new_session=True
            )

    def test_read_msg_from_server(self):
        addr, port = DEFAULT_IP_ADDRESS, DEFAULT_SERVER_PORT
        connect_server = self.connection(
            'python3 ' + PROJECT_MAIN_PATH + 'server.py', addr, port
            )
        connect_client = self.connection(
            'python3 ' + PROJECT_MAIN_PATH + 'client.py', addr, port
            )

        read_msg_from_server(connect_client)
        self.assertIsNotNone()


if __name__ == '__main__':
    unittest.main()
