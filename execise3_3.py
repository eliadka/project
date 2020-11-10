#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    value = [a, b, c]
    total = []
    max_1 = max(value)
    total.append(max_1)
    value.remove(max_1)
    max_2 = max(value)
    total.append(max_2)
    print(sum(total))
my_func(40, 2, 50)