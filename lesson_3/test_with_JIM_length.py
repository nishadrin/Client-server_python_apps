from common.client.form_request import client_message
from common.send_and_pack_data import pack_data
from common.configure import JIM_MAX_BYTES


msg_to = '1234567890123456789012345'
msg_from = '1234567890123456789012346'
msg = 'б' * 83

jim_msg_lenght = len(pack_data(client_message(msg_to, msg_from, msg, encoding='utf-8'),
        encoding='ascii'))

print('Длина передаваемого сообщения:', jim_msg_lenght)

if jim_msg_lenght > JIM_MAX_BYTES:
    print('Сообщение не пройдет')
elif jim_msg_lenght == JIM_MAX_BYTES:
    print('Сообщение пройдет')
else:
    print('Сообщение пройдет')

# проведя небольшие исследования, пришел к выводу, что в
# form_request.client_message необходимо изменить название сообщений на
# msg, вместо message, тогда можем себе позволить 499 символов на
# само сообщение, поддерживающее русский язык - 83

# PS: почему в методичке указан именно такой вариант с 500 символами?
# как это должно работать? (: