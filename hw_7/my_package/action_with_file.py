import os
import random
import string
import shutil


def write_random_pairs(file_name: str, num_lines: int) -> None:
    """
    Функция записывает num_lines случайных пар чисел в файл с именем file_name.
    Первое число в паре - int, второе - float. Числа разделены вертикальной чертой.
    Минимальное число - -1000, максимальное - +1000.

    :param file_name: имя файла для записи случайных пар чисел
    :param num_lines: количество строк, которое необходимо записать в файл
    """
    with open(file_name, "a") as f:
        for i in range(num_lines):
            int_num = random.randint(-1000, 1000)
            float_num = random.uniform(-1000, 1000)
            f.write(f"{int_num} | {float_num:.2f}\n")


def generate_pseudonym(amount_name: int):
    """
    Генерирует псевдоимя и сохраняет его в файл.

    :param amount_name: Кол-во имён для генерации.
    """
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
    CONSONANTS = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in VOWELS]

    for _ in range(amount_name):
        name_length = random.randint(4, 7)
        name = ''.join(random.choices(VOWELS + CONSONANTS, k=name_length))
        while not any(v in name for v in VOWELS):
            name = ''.join(random.choices(VOWELS + CONSONANTS, k=name_length))
            print('1')
        name = name.capitalize()

        with open('pseudonyms.txt', 'a') as f:
            f.write(name + '\n')


def multiply_and_save_result(names_file: str, numbers_file: str, output_file: str) -> None:
    """
     Функция, открывает на чтение созданные в прошлых задачах файлы с числами и именами.

    :param names_file: Имя файла с числами
    :param numbers_file: Имя файла именами
    :param output_file: Имя файла с результатами перемножения.
    """
    # Открываем файлы на чтение
    with open(names_file, 'r') as f_names, open(numbers_file, 'r') as f_numbers:
        names = f_names.readlines()
        numbers = f_numbers.readlines()

        # Открываем файл на запись
        with open(output_file, 'w') as f_output:
            num_lines = max(len(names), len(numbers))

            for i in range(num_lines):
                name = names[i % len(names)].strip()
                num1, num2 = numbers[i % len(numbers)].strip().split('|')
                num1 = int(num1)
                num2 = float(num2)

                product = num1 * num2

                # Проверяем знак произведения и сохраняем результат
                if product < 0:
                    f_output.write(name.lower() + ' ' + str(abs(product)) + '\n')
                else:
                    f_output.write(name.upper() + ' ' + str(round(product)) + '\n')


def create_file_with_extension(extension: str, min_name_len: int = 6, max_name_len: int = 30,
                               min_file_size: int = 256, max_file_size: int = 4096, num_files: int = 42):
    """
    Генерирует указанное количество файлов с указанным расширением,
    каждый файл имеет случайное имя и случайный размер в диапазоне от min_file_size до max_file_size байт.

    :param extension: расширение файла, например 'txt'
    :param min_name_len: минимальная длина имени файла (по умолчанию 6 символов)
    :param max_name_len: максимальная длина имени файла (по умолчанию 30 символов)
    :param min_file_size: минимальный размер файла в байтах (по умолчанию 256 байт)
    :param max_file_size: максимальный размер файла в байтах (по умолчанию 4096 байт)
    :param num_files: количество файлов для создания (по умолчанию 42)
    """
    for i in range(num_files):
        # Генерируем случайное имя файла
        name_len = random.randint(min_name_len, max_name_len)
        file_name = ''.join(random.choices(string.ascii_lowercase, k=name_len))
        file_name += '.' + extension

        # Генерируем случайный размер файла
        file_size = random.randint(min_file_size, max_file_size)

        # Записываем случайные байты в файл
        with open(file_name, 'wb') as f:
            f.write(os.urandom(file_size))


def generate_files_with_extensions(extensions: list, num_files_list: list) -> None:
    """
    Генерирует файлы с разными расширениями.

    :param extensions: Список расширений файлов.
    :param num_files_list: Список с количеством файлов для каждого расширения.
    """
    for ext, num_files in zip(extensions, num_files_list):
        create_file_with_extension(ext, num_files=num_files)


def create_dir(name_dir: str) -> None:
    """
    Функция генерирует файлы в указанную директорию.
    :param name_dir: Имя директории, куда нужно сгенерировать файлы.
    """
    work_dir = os.path.join(os.getcwd(), name_dir)
    if not (os.path.exists(work_dir) and os.path.isdir(work_dir)):
        os.mkdir(work_dir)
    os.chdir(work_dir)

    extensions = ['.txt', '.doc', '.pdf', '.xls']
    file_counts = [2, 2, 2, 2]
    generate_files_with_extensions(extensions, file_counts)


def sort_files_by_extension(src_dir: str) -> None:
    """
    Функция для сортировки файлов по директориям: видео, изображения, текст.

    :param src_dir: Путь до директории для сортировки
    """
    groups = {
        "text": [".txt", ".doc", ".docx", ".pdf"],
        "video": [".mp4", ".avi", ".mov", ".mkv"],
        "image": [".jpg", ".jpeg", ".png", ".bmp"],
    }

    # Создаем директории для каждой группы
    for group in groups:
        os.makedirs(os.path.join(src_dir, group), exist_ok=True)

    # Сортируем файлы по группам
    for file in os.listdir(src_dir):
        file_path = os.path.join(src_dir, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[-1].lower()
            for group, exts in groups.items():
                if ext in exts:
                    shutil.move(file_path, os.path.join(src_dir, group, file))
                    break


def rename_files(dir_path: str, desired_name: str, amount_digits: int,
                 source_extension: str, destination_extension: str,
                 name_range: list[int]) -> None:
    """
    Групповое переименование файлов.

    :param dir_path: Путь к директории, где нужно произвести переименование
    :param desired_name: Желаемое конечное имя файлов.
    :param amount_digits: Количество цифр в порядковом номере.
    :param source_extension: Расширение исходного файла.
    :param destination_extension: Расширение конечного файла.
    :param name_range: Диапазон сохраняемого оригинального имени.
    """
    files = os.listdir(dir_path)

    filtred_files = [file for file in files if file.endswith(source_extension)]
    filtred_files.sort()

    for i, file_name in enumerate(filtred_files):
        new_name = file_name[name_range[0]-1:name_range[1]]
        # Добавляем новое имя файла, если оно не None
        if desired_name:
            new_name += desired_name
        # Добавляем порядковый номер в имя файла и расширение
        new_name += str(i+1).zfill(amount_digits)
        new_name += destination_extension

        src_path = os.path.join(dir_path, file_name)
        dest_path = os.path.join(dir_path, new_name)
        os.rename(src_path, dest_path)
