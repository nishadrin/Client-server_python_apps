import os
import locale

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла
# о умолчанию. Принудительно открыть файл в формате Unicode и вывести его
# содержимое.
test_file_path = os.path.abspath('test_file.txt')
words = [
    'сетевое программирование\n',
    'сокет\n',
    'декоратор\n',
    ]
with open(test_file_path, 'w') as file:
    file.writelines(words)

print('Стандартная кодировка: ', locale.getpreferredencoding(), '\n')

print('Данные из файла:')
with open(test_file_path, 'r', encoding='utf-8') as file:
    for line in file.readlines():
        print(line.strip())
