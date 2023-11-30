# 1. Написати програму обчислення суми і добутку елементів масиву з використанням однієї функції.
# 2. Обчислити maх і min в одновимірному масиві і поміняти їх місцями з використанням функцій.
# 3. Написати програму визначення індексу першого позитивного/негативного елементу масиву з використанням функції. Умови пошуку змінювати за допомогою параметру із значенням за замовчуванням True, що відповідає пошуку позитивного елемента. У разі відсутності позитивного/негативного елементу повернути відповідне повідомлення.

from functools import reduce
from typing import Optional


# exercise 1
def exercise_1(array: list[int]) -> int:
    if array:
        return reduce(lambda x, y: x + y, array)
    return 0


def exercise_1_1(array: list[int]) -> int:
    x = 0
    for i in array:
        x += i
    return x


# exercise 2


# exercise 3


def exercise_3(array: list[int], positive: bool = True) -> Optional[int]:
    if not array:
        print("Empty element")
        return None

    for i, el in enumerate(array):
        if not isinstance(el, int):
            print("All elements must be an int")
            return None

        if positive:
            if el > 0:
                return i
        else:
            if el < 0:
                return i