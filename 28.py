# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# 2 2
#     4

a = int(input("Input 1st number: "))
b = int(input("Input 2nd number: "))


def sumofnumbers(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sumofnumbers(a-1, b+1)


print(f"Sum of {a} and {b} = {sumofnumbers(a,b)}")
