# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


# import random
# def power(a, b):
#     if b == 0:
#         return 1
#     if b > 0:
#         return a * power(a, b - 1)
#     else:
#         return 1 / power(a, -b)
# num1 = random.randint(1, 10)
# num2 = random.randint(1, 10)

# result = power(num1, num2)

# print("А =", num1, "B =", num2, "->", result,)


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую
# сумму двух целых \неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

# import random
# def sum(a, b):
#     if a == 0:  
#         return b
#     else:
#         return sum(a - 1, b + 1)  

# num1 = random.randint(1, 100)
# num2 = random.randint(1, 100)

# result = sum(num1, num2)
# print(num1, num2)
# print("   ", result)
