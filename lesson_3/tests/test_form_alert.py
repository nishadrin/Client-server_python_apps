import unittest

from ..common.forms.form_alert import form_alert, alerts_msg_text_from_code


class TestFormAlert(unittest.TestCase):
    def test_with_standart_alerts_msgs(self):
        for i in ALERTS_MSGS:
            self.assertIsNotNone(self, form_alert(i))