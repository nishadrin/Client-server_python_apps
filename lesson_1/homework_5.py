import subprocess

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
# результаты из байтовового в строковый тип на кириллице.

def ping_coding_UTF8(addr, requests):
    args = ['ping', addr, '-c', str(requests)]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    [print(line.decode('utf-8')) for line in subproc_ping.stdout]

def main():
    request_counts = 4
    dest_addrs = [
        'yandex.ru',
        'youtube.com',
        ]
    for addr in dest_addrs:
        print('*' * 50, f'Пинг до {addr}', sep='\n')
        ping_coding_UTF8(addr, requests=request_counts)

if __name__ == '__main__':
    main()
