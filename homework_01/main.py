"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [arg**2 for arg in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(*args):
    """
    функция принимает список чисел
    и возвращает список простых чисел из выборки
    """
    result = []
    for i in args:
        if i == 1 or i == 0: continue
        else:
            for prev_numbers in range(2, i):
                if i % prev_numbers == 0: break
            else:
                result.append(i)
    return result

def filter_numbers(*args, types):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if types == ODD:
        return list(filter(lambda x: x % 2, args))
    if types == EVEN:
        return list(filter(lambda x: x % 2 == 0, args))
    if types == PRIME:
        return is_prime(*args)
    else:
        return "Option must be in ['odd', 'even', 'prime']"
    
