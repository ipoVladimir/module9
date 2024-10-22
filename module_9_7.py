# Задание: Декораторы в Python
#
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
#
# Задание:
# Напишите 2 функции:
#
#     Функция, которая складывает 3 числа (sum_three)
#     Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет
#     простым числом и "Составное" в противном случае.
#
# Пример:
# result = sum_three(2, 3, 6)
# print(result)
#
# Результат консоли:
# Простое
# 11
#
# Примечания:
#
#     Не забудьте написать внутреннюю функцию wrapper в is_prime
#     Функция is_prime должна возвращать wrapper
#     @is_prime - декоратор для функции sum_three

def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        # алгоритм нахождения простого числа взят
        # https://foxford.ru/wiki/informatika/proverka-chisla-na-prostotu-v-python?srsltid=AfmBOoomZS2xPsurAi3dpLLoCJQ8dLPpq3SJtCt8lXnx9kxC9kuN-XgG&utm_referrer=https%3A%2F%2Fwww.google.com%2F
        if res % 2 == 0:
            res_is_prime = res == 2
        else:
            d = 3
            while d * d <= res and res % d != 0:
                d += 2
            res_is_prime = d * d > res
        if res_is_prime:
            print("Простое")
        else:
            print("Составное")
        return res
    return wrapper


@is_prime
def sum_three(num1, num2, num3):
    return num1 + num2 + num3

result = sum_three(1, 2, 4)
print(result)
