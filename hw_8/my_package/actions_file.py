import os
import csv
import json
import pickle
import hashlib


def convert_txt_to_json(filename_txt: str, filename_json: str) -> None:
    """
    Функция создаёт json-файл из txt-файла.
    :param filename_txt: Имя входного txt-файла
    :param filename_json: Имя выходного json-файла
    """
    res_dict = {}
    with open(filename_txt, 'r', encoding='utf-8') as f_txt:
        for line in f_txt.readlines():
            name, num = line.split()
            name = name.capitalize()
            res_dict[name] = int(num)
        with open(filename_json, 'w', encoding='utf-8') as f_json:
            json.dump(res_dict, f_json, indent=4)


def check_unicue_id(user_id: str, data: dict) -> bool:
    """
    Функция проверяет уникальность идентификатора
    :param user_id: идентификатор пользователя
    :param data: словарь с данными о пользователях
    :return: True, если идентификатор уникальный, иначе False
    """
    for user_level in data.values():
        if user_id in user_level.keys():
            return False
    return True


def create_json_file(filename: str) -> None:
    """
    Создает и обновляет файл JSON с информацией о пользователях.
    :param filename: Имя файла для сохранения и загрузки данных
    """
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}

    while True:
        print(data)
        name = input('Введите имя: ')
        id_ = input('Введите ID: ')
        while not check_unicue_id(id_, data):
            print('Такой ID уже существует. Введите другой')
            id_ = input('Введите ID: ')
        level = int(input('Введите уровень доступа: '))
        while not 1 <= level <= 7:
            print('Уровень доступа должен быть от 1 до 7. Введите другой')
            level = int(input('Введите уровень доступа: '))
        level = str(level)
        if level in data:
            data[level][id_] = name
        else:
            data[level] = {id_: name}

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)


def convert_json_to_csv(json_filename: str, csv_filename: str) -> None:
    """
    Преобразует файл формата JSON в файл формата CSV.

    :param json_filename: Имя входного файла формата JSON.
    :param csv_filename: Имя выходного файла формата CSV.
    """
    with open(json_filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(csv_filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        header = ['user_id', 'user_name', 'access_level']
        writer.writerow(header)

        for level, users in data.items():
            for user_id, user_name in users.items():
                writer.writerow([user_id, user_name, level])


def convert_csv_to_json(csv_file: str, json_file: str) -> None:
    """
    Функция читает csv файл, выполняет преобразования и сохраняет результат в json файл.
    :param csv_file: Имя csv файла.
    :param json_file: Имя json файла.
    """
    with open(csv_file, 'r', encoding='utf-8', newline='') as csv_f:
        csv_read = csv.reader(csv_f, delimiter=',')
        print(csv_read)
        rows = [row for row in csv_read]
        print(rows)

    data = []
    for row in rows:
        user_id = row[0].zfill(10)
        username = row[1].capitalize()
        access_level = row[2]
        hash_ = hashlib.sha256(f'{user_id}{username}'.encode()).hexdigest()
        data.append({
            'user_id': user_id,
            'user_name': username,
            'access_level': access_level,
            'hash': hash_
        })

    with open(json_file, 'w', encoding='utf-8') as json_f:
        for row in data:
            json.dump(row, json_f)
            json_f.write('\n')


def convert_json_to_pickle(dir_path: str):
    """
    Функция ищет JSON файлы и конвертирует их pickle-файлы.
    :param dir_path: Путь к директории.
    """
    for file_name in os.listdir(dir_path):
        if file_name.endswith('.json'):
            with open(os.path.join(dir_path, file_name), 'r', encoding='utf-8') as json_f:
                data = json.load(json_f)

            with open(os.path.join(dir_path, file_name[:-5] + '.pickle'), 'wb') as pickle_f:
                pickle.dump(data, pickle_f)


def save_as_json(filename: str, data: list[dict]) -> None:
    """
    Сохраняет данные в файл в формате json.

    :param filename: Имя файла
    :param data: Данные, которые нужно сохранить
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def save_as_csv(filename: str, fieldnames: list[str], data: list[dict]) -> None:
    """
    Сохраняет данные в файл в формате csv.

    :param filename: Имя файла
    :param fieldnames: Названия полей
    :param data: Данные, которые нужно сохранить
    """
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for res_dict in data:
            writer.writerow([res_dict['name'], res_dict['type'],
                             res_dict['size_bytes'], res_dict['parent_dir']])


def save_as_pickle(filename: str, data: list[dict]) -> None:
    """
    Сохраняет данные в файл в формате pickle.

    :param filename: Имя файла
    :param data: Данные, которые нужно сохранить
    """
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def get_size(dir_path: str) -> int:
    """
    Возвращает размер директории в байтах с учетом всех вложенных файлов и директорий.

    :param dir_path: Путь к директории
    :return: размер всех файлов во входящей директории.
    """
    size = 0
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            size += os.path.getsize(file_path)
    return size


def read_directory(dir_path: str):
    """
    Рекурсивно обходит указанную директорию и
    сохраняет результаты обхода в json, csv и pickle файлы.
    """
    results = []
    for root, dirs, files in os.walk(dir_path):
        for name in dirs + files:
            path = os.path.join(root, name)
            parent_dir = os.path.basename(os.path.dirname(path))
            if os.path.isdir(path):
                size = get_size(path)
                data = {'name': name, 'type': 'directory',
                        'size_bytes': size, 'parent_dir': parent_dir}
                results.append(data)
            elif os.path.isfile(path):
                size = os.path.getsize(path)
                data = {'name': name, 'type': 'file',
                        'size_bytes': size, 'parent_dir': parent_dir}
                results.append(data)

    # сохраняем результаты в json, csv и pickle файлы
    save_as_json('result_file.json', results)
    save_as_csv('result_file.csv', ['name', 'type', 'size_bytes', 'parent_dir'], results)
    save_as_pickle('result_file.pickle', results)
