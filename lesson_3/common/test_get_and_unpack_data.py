import unittest
import json

from get_and_unpack_data import unpack_data


class TestUnpackData(unittest.TestCase):
    def test_data(self):
        data: bytes = b'{"action": "msg", "time": 1573913065, "to": "test", ' \
            b'"from": "msg_from", "encoding": "encoding", "message": "msg"}'
        encoding: str = 'ascii'
        self.assertEqual(
            unpack_data(data, encoding),
            json.loads(data.decode(encoding))
            )

    def test_encoding(self):
        data: bytes = b'{"action": "msg", "time": 1573913065, "to": "test", ' \
            b'"from": "msg_from", "encoding": "encoding", "message": "msg"}'
        encodings: tuple = ('ascii', 'utf-8')
        for encoding in encodings:
            self.assertEqual(
                unpack_data(data, encoding),
                json.loads(data.decode(encoding))
                )


if __name__ == '__main__':
    unittest.main()