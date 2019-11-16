from datetime import datetime


def msg(msg_to: str, msg_from: str, msg: str, encoding="ascii") -> dict:
    return {
        "action": "msg",
        "time": int(datetime.now().timestamp()),
        "to": msg_to,
        "from": msg_from,
        "encoding": encoding,
        "message": msg
        }


def presence_msg(user_name: str, type: str='status') -> dict:
    return {
        "action": "presence",
        "time": int(datetime.now().timestamp()),
        "type": type,
        "user": {
            "account_name": user_name,
            "status": "Hello world!"
            }
        }


def auth(user_name: str, password: str, type: str='Status') -> dict:
    return {
        "action": "authenticate",
        "time": int(datetime.now().timestamp()),
        "type": type,
        "user": {
            "account_name": user_name,
            "password": password
            }
        }


def join_or_leave_chat(room_name, leave: bool=False) -> dict:
    action = 'join'
    if leave:
        action = 'leave'
    return {
        "action": action,
        "time": int(datetime.now().timestamp()),
        "room": room_name
        }
