import math


def area(r):
'''Возвращает площадь круга.
    Параметры :
        r (int): радиус круга
    Возвращаемое значение:
        area(r)(int): площадь круга
'''
    return math.pi * r * r


def perimeter(r):
    '''Возвращает периметр.
    Параметры :
        r (int): радиус фигуры
    Возвращаемое значение:
        perimeter(r)(int): периметр фигуры
'''
    return 2 * math.pi * r

