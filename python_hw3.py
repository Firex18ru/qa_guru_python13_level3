import math
import random
from random import randint

def test_greeting():
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = f'Привет, {name}! Тебе {age} лет.'

    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."
    print(output)

def test_rectangle():
    a = 10
    b = 20
    # TODO сосчитайте периметр
    perimeter = (a + b) * 2

    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a * b

    assert area == 200


def test_circle():
    r = 23
    pi = math.pi
    # TODO сосчитайте площадь
    area = pi * r ** 2

    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = 2 * pi * r

    assert length == 144.51326206513048
    print(f'square  = {area}')
    print(f'circle = {length}')

def test_random_list():

    # TODO создайте список
    l = []
    for i in range(10):
        l.append(random.randrange(1,101))
    l.sort()
    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def test_unique_elements():
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    l = (list(set(l)))
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():

    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second