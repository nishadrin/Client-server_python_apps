JIM_MAX_BYTES = 640
ACTIONS_TUPLE = (
    'presence', #  присутствие. Сервисное сообщение для извещения сервера о присутствии клиента online
    'prоbe', # проверка присутствия. Сервисное сообщение от сервера для проверки присутствии клиента online
    'msg', # простое сообщение пользователю или в чат
    'authenticate', # авторизация на сервере
    'quit', # отключение от сервера
    'join', # присоединиться к чату
    'leave', # покинуть чат
    )
ALERTS_MSGS = {
    '100': 'base notification',
    '101': 'important notification',
    '200': 'OK',
    '201': 'created',
    '202': 'accepted',
    '400': 'wrong request/JSON object',
    '401': 'not authorized',
    '402': 'wrong password or no account with that name',
    '403': 'forbidden',
    '404': 'not found chat or user',
    '409': 'conflict with another one connect',
    '410': 'gone offline',
    '500': 'server error',
    }
