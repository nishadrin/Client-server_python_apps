import unittest
import json
from datetime import datetime

from send_and_pack_data import pack_data


class TestPackData(unittest.TestCase):
    def test_data(self):
        data: dict = {
            "action": "msg",
            "time": int(datetime.now().timestamp()),
            "to": 'test',
            "from": 'msg_from',
            "encoding": 'encoding',
            "message": 'msg'
            }
        encoding: str = 'ascii'
        self.assertEqual(pack_data(data, encoding), json.dumps(data).encode(encoding))

    def test_encoding(self):
        data: dict = {
            "action": "msg",
            "time": int(datetime.now().timestamp()),
            "to": 'test',
            "from": 'msg_from',
            "encoding": 'encoding',
            "message": 'msg'
            }
        encodings: tuple = ('ascii', 'utf-8')
        for encoding in encodings:
            self.assertEqual(pack_data(data, encoding), json.dumps(data).encode(encoding))


if __name__ == '__main__':
    unittest.main()