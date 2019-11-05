# Задание на закрепление знаний по модулю yaml. Написать скрипт,
# автоматизирующий сохранение данных в файле YAML-формата.
import os
import yaml

data = {
    1: [1, 2, 3],
    2: 4,
    3: {1: '€'}
    }
yaml_path = os.path.abspath('file.yaml')
with open(yaml_path, 'w') as file:
    yaml.dump(data, file, allow_unicode=True, default_flow_style=True)
