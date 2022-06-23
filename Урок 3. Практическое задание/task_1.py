"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def main(one, two):
    "Значения"
    try:
        return one / two
    except ZeroDivisionError:
        return "Ошибка деления на 0"


x = int(input("Введите число x >>> "))
y = int(input("Введите число y >>> "))

print(main(x, y))
