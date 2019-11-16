from datetime import datetime

from ..settings import ALERTS_MSGS


def alerts_msg_text_from_code(response_code: int) -> str:
    for code, msg in ALERTS_MSGS.items():
        if int(code) == response_code:
            return msg
    return


def form_alert(response_code: int, msg_code: str=None) -> dict:
    if msg_code is None:
        msg_code = alerts_msg_text_from_code(response_code)
    else:
        msg_code = 'alert'
        if response_code > 399:
            msg_code = 'error'

    return {
        "response": response_code,
        "time": int(datetime.now().timestamp()),
        'alert': msg_code
        }
