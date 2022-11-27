# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)


def multiple(number):
    if number == 1:
        return 1
    else:
        return number * multiple(number- 1)

user_number = int(input("Введите число: "))
list = []
for i in range(1, user_number + 1):
    list.append(multiple(i))

print(f"Произведения чисел от 1 до {user_number}:  {list}")