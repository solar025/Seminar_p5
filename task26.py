# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 
def st(a, b):
    if b == 0:
        return 1
    elif b >= 1:
        return pow(a, b)


a = int(input("Введите своё число: "))
b = int(input("Введите степень, в которую будем возводить число: "))

print(st(a,b))