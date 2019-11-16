import unittest
from datetime import datetime

from form_request import client_message, presence_msg


class TestClientFormRequest(unittest.TestCase):
    def test_client_message_with_encodings(self):
        encodings = ('ascii', 'utf-8')
        for encoding in encodings:
            test_msg: dict = {
                "action": "msg",
                "time": int(datetime.now().timestamp()),
                "to": 'msg_to',
                "from": 'msg_from',
                "message": 'msg',
                "encoding": encoding
                }
            self.assertEqual(
                client_message('msg_to', 'msg_from', 'msg', encoding=encoding),
                test_msg
                )


if __name__ == '__main__':
    unittest.main()
