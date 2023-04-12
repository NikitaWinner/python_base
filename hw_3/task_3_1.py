# Решение со словарём.
"""
def return_duplicate_list(list_in: list):
    dublicate_dict = {}
    for item in list_in:
        dublicate_dict[item] = dublicate_dict.get(item, 0) + 1
    return [item for item in dublicate_dict if dublicate_dict[item] > 1]
"""
# Решение с множествами.
def return_duplicate_list(list_in: list) -> list:
    """
    Возвращает список дублирующихся элементов в списке, который принимает.

    :param list_in: Список, содержащий дублирующиеся элементы.
    :return: Список, содержащий уникальные элементы списка list_in, которые дублируются.
    """
    seen = set()
    duplicate_list = set()
    for item in list_in:
        if item in seen:
            duplicate_list.add(item)
        else:
            seen.add(item)
    return list(duplicate_list)


def test_return_duplicate_list():
    assert set(return_duplicate_list([1, 2, 3, 4, 4, 5, 6, 6, 6])) == {4, 6}
    assert set(return_duplicate_list([1, 2, 3, 4, 5])) == set()
    assert set(return_duplicate_list(['apple', 'banana', 'pear', 'banana'])) == {'banana'}
    assert set(return_duplicate_list([True, False, True, False, True])) == {True, False}
    assert set(return_duplicate_list([1, 1, 1, 1, 1, 1, 1, 1])) == {1}
    assert set(return_duplicate_list([])) == set()


if __name__ == '__main__':
    test_return_duplicate_list()