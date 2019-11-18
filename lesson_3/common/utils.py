import json
import socket
from datetime import datetime

from config import JIM_MAX_BYTES, ALERTS_MSGS


class DataPacking:
    def pack_data(data: dict, encoding: str) -> bytes:
        return json.dumps(data).encode(encoding)

    def unpack_data(data: bytes, encoding: str) -> dict:
        return json.loads(data.decode(encoding))


class DataExchange:
    def get_data(sock: socket, encoding: str='ascii') -> dict:
        recieve_bytes: bytes = sock.recv(JIM_MAX_BYTES)
        if not recieve_bytes:
            return
        return DataPacking.unpack_data(recieve_bytes, encoding)

    def send_data(sock: socket, data: dict, encoding: str='ascii'):
        sock.send(DataPacking.pack_data(data, encoding))


class FormAlertOrError:
    def alerts_msg_text_from_code(self, response_code: int) -> str:
        for code, msg in ALERTS_MSGS.items():
            if int(code) == response_code:
                return msg
        return

    def form_alert_or_error(self, response_code: int,
                            text_msg_code: str = None) -> dict:
        alert: str = 'alert'
        if response_code > 399:
            alert = 'error'
        if text_msg_code is None:
            text_msg_code: str = self.alerts_msg_text_from_code(
                response_code)
        return {
            "response": response_code, "time": int(datetime.now().timestamp()),
            alert: text_msg_code
            }