# Задание на закрепление знаний по модулю CSV. Написать скрипт,
# осуществляющий выборку определенных данных из файлов info_1.txt,
# info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате
# CSV.

# PS: Добавил немного "отсебятины", мне кажется, так универсальнее +
# читабельнее, isn't it?
import re
import os
import csv

def search_info_in_file(regex_list, file_read):
    output_list = []
    for regex in regex_list:
        re_search = re.search(f'{regex}:\ +.*', file_read)
        re_split = re.split(':', re_search.group())
        output_list.append(re_split[1].lstrip())
    return output_list

def get_data(files_list, regex_list):
    main_data = []
    for name in regex_list:
        main_data.append(name)
    info = []
    for file in files_list:
        with open(file, 'r') as f:
            file_read = f.read()
        search_info = search_info_in_file(regex_list, file_read)
        info.append(search_info)
    return (main_data, *info)

def write_to_csv(csv_path, files_list, regex_list):
    data = get_data(files_list, regex_list)
    with open(csv_path, 'w') as f:
        f_writer = csv.writer(f)
        f_writer.writerows(data)
    return True

def main():
    csv_path = os.path.abspath('homework1.csv')
    files_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    regex_list = (
        'Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы',
        'Язык системы', 'Язык ввода'
        )
    write_csv = write_to_csv(csv_path, files_list, regex_list)

if __name__ == '__main__':
    main()
