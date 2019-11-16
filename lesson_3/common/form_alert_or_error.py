from datetime import datetime

from .configure import ALERTS_MSGS


def alerts_msg_text_from_code(response_code: int) -> str:
    for code, msg in ALERTS_MSGS.items():
        if int(code) == response_code:
            return msg
    return


def form_alert_or_error(response_code: int, text_msg_code: str=None) -> dict:
    alert = 'alert'
    if response_code > 399:
        alert = 'error'
    if text_msg_code is None:
        text_msg_code = alerts_msg_text_from_code(response_code)
    return {
        "response": response_code,
        "time": int(datetime.now().timestamp()),
        alert: text_msg_code
        }
