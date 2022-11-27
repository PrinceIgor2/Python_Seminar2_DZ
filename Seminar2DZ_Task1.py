# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:
#     67.82 -> 23
#     (-0.56) -> 11


def summa_digits(number):
    summa = 0
    if float(number) < 0:                            
       number = float(number) * (-1)  
    for i in str(number):
        if i != ".":
            summa += int(i)
    return summa


user_number = float(input('Введите вещественное число: '))

print(f"Сумма цифр вещественно числа составляет {summa_digits(user_number)}")



