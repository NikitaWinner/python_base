from pprint import pprint
from typing import List, Dict, Tuple
from itertools import combinations

camping_gear = {
    'палатка': 3.5,
    'спальный мешок': 1.8,
    'тушенка': 0.6,
    'сгущёнка': 0.7,
    'газовая горелка': 1.2,
    'баллон газовый': 2.0,
    'кастрюля': 0.8,
    'сковорода': 0.6,
    'термос': 0.5,
    'фонарик': 0.3,
    'нож': 0.2,
    'ложка': 0.1,
    'удочка': 1.5,
    'лопатка': 1.1,
    'угли': 2.5
}


def determine_backpack_combinations(things: Dict[str, float], weight_limit: float | int) -> List[List[str]]:
    """
    Функция возвращает все возможные комбинации вещей для рюкзака при заданном ограничении по весу.

    :param things: Словарь, содержащий вещи и их вес в килограммах.
    :param weight_limit: Максимально допустимый вес рюкзака в килограммах.
    :return: Список списков, содержащий все возможные комбинации вещей и их суммарный вес.
    """
    # список для комбинаций
    backpack_combinations = []

    def backtrack(things_list: List[Tuple[str, float]], cur_combination: List[str], cur_weight: float) -> None:
        """
        Рекурсивная функция для поиска всех возможных комбинаций вещей,
        которые можно сложить в рюкзак, не превышая лимит по весу.

        :param things_list: Список вещей и их весов, которые еще не использовались.
        :param cur_combination: Текущая комбинация вещей.
        :param cur_weight: Текущий вес рюкзака.
        :return: None
        """
        # Если текущий вес равен ограничению по весу рюкзака, добавляем текущую комбинацию в backpack_combinations
        if cur_weight == weight_limit:
            backpack_combinations.append(cur_combination)
            return

        # Перебираем все вещи, которые еще не использовались
        for i in range(len(things_list)):
            # Если добавление i-й вещи не приведет к превышению ограничения по весу
            if cur_weight + things_list[i][1] <= weight_limit:
                # Рекурсивно вызываем backtrack(), добавляя i-ю вещь в текущую комбинацию и обновляя текущий вес
                backtrack(things_list[i + 1:], cur_combination + [things_list[i][0]], cur_weight + things_list[i][1])

    # Преобразуем словарь things в список кортежей (вещь, вес) и вызываем backtrack() для поиска всех комбинаций
    all_things_list = list(things.items())
    backtrack(all_things_list, [], 0)

    # Возвращаем список всех найденных комбинаций
    return backpack_combinations

if __name__ == '__main__':
    result = determine_backpack_combinations(camping_gear, 5)
    pprint(result)
