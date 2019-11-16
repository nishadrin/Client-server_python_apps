import unittest
from datetime import datetime

from form_request import is_user_online


class TestOwnAlertOrError(unittest.TestCase):
     def test_alert(self):
        msg: dict = {
             "action": "probe",
             "time": int(datetime.now().timestamp()),
             }
        self.assertEqual(is_user_online(), msg)


if __name__ == '__main__':
    unittest.main()
