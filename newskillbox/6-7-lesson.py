# 1
# number = int(input("Введите число больше 0: "))
# current_number = 1
# while number >= current_number:
#     print(current_number, "в степени 3 =", current_number ** 3)
#     current_number += 1

# 2
# name = input("Введите имя должника: ")
# debt = int(input("Введите сумму долга: "))
# while True:
#     print(name + ", ваша задолженность составляет", debt, "рублей")
#     money = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
#     debt -= money
#     if debt <= 0:
#         print("Отлично,", name + "! Вы погасили долг. Спасибо!")
#         break

# 3
# number = int(input("Введите число: "))
# count = 1
# while number > 9:
#     count += 1
#     number //= 10
# print("Длинна числа", count, "знак/-а -ов")

# 4
# months = 0
# while True:
#     days = int(input("Сколько дней в этом месяце? "))
#     if days == 0:
#         break
#     if days % 2 == 0:
#         months += 1
#     print("Четных месяцев", months)

# 5
# while True:
#     number_string = input("Введите число: ")
#     length = len(number_string)
#     if length % 2 == 0 and length != 0:
#         number = int(number_string)
#         half_count = length / 2
#         first_sum = 0
#         second_sum = 0
#         while half_count > 0:
#             second_sum += (number % 10)
#             half_count -= 1
#             number //= 10
#
#         half_count = length / 2
#
#         while half_count > 0:
#             first_sum += (number % 10)
#             half_count -= 1
#             number //= 10
#
#         if second_sum == first_sum:
#             print("Счастливый билет")
#         else:
#             print("НЕ счастливый билет")
#     else:
#         print("Неверный ввод")

# 6
# plus_marks = 0
# minus_marks = 0
# while True:
#     mark = int(input("Введите число: "))
#     if mark == 0:
#         break
#     elif mark > 0:
#         plus_marks += 1
#     else:
#         minus_marks += 1
# print("Кол-во положительных чисел:", plus_marks)
# print("Кол-во отрицательных чисел:", minus_marks)

# 7
# hour = 1
# total_task_count = 0
# shop = False
# print("Начался 8-часовой рабочий день")
# while hour <= 8:
#     print(str(hour) + "-й час")
#     hour += 1
#     tasks = int(input("Сколько задач решит Максим? "))
#     total_task_count += tasks
#     wife = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
#     if wife == 1:
#         shop = True
# print("Рабочий день закончился. Всего выполнено задач:", total_task_count)
# if shop:
#     print("Нужно зайти в магазин.")

# 8
# start = int(input("Введите сумму вклада: "))
# end = int(input("Введите желаемую сумму: "))
# procent = int(input("Введите процентную ставку: "))
# years = 0
# while start < end:
#     years += 1
#     start = int(start * (100 + procent) / 100)
#     print(start)
# print("Вы достигли цели за", years, "лет")

# 9
# rigth_number = 7
# number = int(input("Введите число: "))
# attempts = 1
# while number != rigth_number:
#     attempts += 1
#     number = int(input("Введите число: "))
# print("Вы угадали! Число попыток:", attempts)

# 10
lower_border = 1
upper_border = 100
count = 0
while True:
    count += 1
    guess = int((lower_border + upper_border) / 2)
    question = "Твоё число равно, меньше или больше, чем число " + str(guess) + "? (1 — равно, 2 — больше, 3 — меньше)"
    answer = int(input(question))
    if answer == 1:
        print("Ваше число", guess)
        break
    elif answer == 2:
        lower_border = guess
    elif answer == 3:
        upper_border = guess