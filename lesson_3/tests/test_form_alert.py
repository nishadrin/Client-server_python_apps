import unittest

from ..common.forms.form_alert import form_alert, alerts_msg_text_from_code


class TestFormAlert(unittest.TestCase):
    def test_form_alert(self):

        self.assertIsNotNone(self, form_alert(), msg)