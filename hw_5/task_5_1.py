from typing import Tuple
from os.path import split, splitext

def split_file_path(file_path: str) -> Tuple[str, str, str]:
    """
    Функция принимает на вход строку - абсолютный путь до файла и возвращает кортеж из трех элементов:
    путь, имя файла и расширение файла.

    :param path: Путь до файла.
    :return: Кортеж -> (путь, имя файла, расширение файла)
    """
    file_dir, file_name_ext = split(file_path)
    file_name, file_ext = splitext(file_name_ext)
    return file_dir, file_name, file_ext


def test_split_file_path():
    assert split_file_path('/path/to/file.txt') == ('/path/to', 'file', '.txt')
    assert split_file_path('/another/path/image.png') == ('/another/path', 'image', '.png')
    assert split_file_path('testfile.py') == ('', 'testfile', '.py')
    assert split_file_path('/dir/subdir/') == ('/dir/subdir', '', '')
    assert split_file_path('no/extension/file') == ('no/extension', 'file', '')

if __name__ == '__main__':
    test_split_file_path()