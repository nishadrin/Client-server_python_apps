from common.client.form_request import client_message
from common.send_and_pack_data import pack_data
from common.configure import JIM_MAX_BYTES


msg_to = '1234567890123456789012345'
msg_from = '1234567890123456789012346'
msg = 'a' * 499

jim_msg_lenght = len(pack_data(client_message(msg_to, msg_from, msg, encoding='utf-8'),
        encoding='ascii'))

print(jim_msg_lenght)

if jim_msg_lenght > JIM_MAX_BYTES:
    print('Больше')
elif jim_msg_lenght == JIM_MAX_BYTES:
    print('Равно')
else:
    print('Меньше')

# проведя небольшие исследования, пришел к выводу, что в
# form_request.client_message необходимо изменить название сообщений на
# msg, вместо message, тогда можем себе позволить 499 символов на
# само сообщение.
