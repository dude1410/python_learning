# 1

# exp = int(input("Введите количество опыта: "))
# text = "Ваш уровень: "
#
# if exp < 1:
#     print("Неверные данные!")
# elif exp < 1000:
#     print(text, 1)
# elif 1000 <= exp < 2500:
#     print(text, 2)
# elif 2500 <= exp < 5000:
#     print(text, 3)
# else:
#     print(text, 4)

# 2

# int_1 = int(input("Введите первое число: "))
# int_2 = int(input("Введите второе число: "))
# int_3 = int(input("Введите третье число: "))
#
# if int_1 > int_2 and int_1 > int_3:
#     print("Маскимум:", int_1)
# elif int_2 > int_1 and int_2 > int_3:
#     print("Маскимум:", int_2)
# else:
#     print("Маскимум:", int_3)

# 3

# x = int(input("Введите икс: "))
#
# if x == 0:
#     print("Игрек равен", 5)
# elif x > 0:
#     print("Игрек равен", x - 12)
# else:
#     print("Игрек равен", x ** 2)

# 4

# place = int(input("Введите место в списке поступающих: "))
# points = int(input("Введите количество баллов за экзамены: "))
#
# if place <= 10:
#     print("Поздравляем, вы поступили!")
#     if points >= 290:
#         print("Бонусом вам будет начисляться стипендия.")
# else:
#     print("К сожалению, вы не поступили.")

# 5


# rating = int(input('Что получил по математике? '))
#
# if rating == 2 or rating == 2:
#     print('Плохо. Марш учиться!')
# elif rating == 4 or rating == 5:
#     print('Молодец! Можешь отдохнуть.')
# else:
#     print("Некорректная оценка")

# 6

# int_for_check = int(input("Введите число: "))
#
# if -100 < int_for_check < -9 or 9 < int_for_check < 100:
#     print("Двузначное")
# else:
#     print("НЕ двузначное")

# 7

# int_1 = int(input("Введите первое число: "))
# int_2 = int(input("Введите второе число: "))
# int_3 = int(input("Введите третье число: "))
#
# if int_1 == int_2 == int_3:
#     print("3 совпадения")
# elif (int_1 == int_2 and int_1 != int_3) or (int_1 != int_2 and int_1 == int_3) or (int_2 == int_3 and int_1 != int_2):
#     print("2 совпадения")
# else:
#     print("нет совпадений")

# 8

# square = int(input("Введите площадь квартиры: "))
# price = int(input("Введите стоимость квартиры: "))
#
# if square >= 100 and price <= 10:
#     print("берем")
# elif square >= 80 and price <= 7:
#     print("подумаем")
# else:
#     print("не подходит")

# 9

# salary = int(input("Введите размер ЗП: "))
# tax = 0
# if salary <= 0:
#     print("Вы неверно ввели сумму")
# elif 0 < salary <= 10000:
#         tax = salary * 0.13
# elif 10000 < salary <= 50000:
#     tax = 10000 * 0.13 + (salary - 10000) * 0.2
# else:
#     tax = 10000 * 0.13 + 40000 * 0.2 + (salary - 50000) * 0.3
# print("к уплате налогов:", tax)

# 10

time = int(input("Введите время в часах (0-23): "))
# if (8 <= time < 10) or (12 <= time < 14) or (15 <= time < 18) or (20 <= time < 22):
#     print("Можно получить посылку")
# else:
#     print("Посылку получить нельзя")

if (0 <= time < 8) or (10 <= time < 12) or (14 <= time < 15) or (18 <= time < 20) or (time > 22):
    print("Посылку получить нельзя")
else:
    print("Можно получить посылку")

