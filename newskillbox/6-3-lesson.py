# 1
# temp = int(input("Введите температуру на улице: "))
# dist = 0
# while temp > 15:
#     dist += 20
#     temp -= 2
#     if temp <= 15:
#         break
#     dist += 10
# print("Пройдено", dist, "метров")

# 2
# number = int(input("Введите число: "))
# summ = 0
# while number != 0:
#     element = number % 10
#     if element == 5:
#         print("Обнаружен разрыв!")
#         break
#     summ += element
#     number //= 10
# print("Сумма =", summ)

# 3
start_sum = int(input("Введите начальное кол-во денег: "))
while start_sum < 10000:
    number = int(input("Что выпало на кубике? "))
    if number < 1 or number > 6:
        print("Не может быть")
        break
    if number == 3:
        print("Вы проиграли все!")
        start_sum = 0
        break
    start_sum += 500
print("Остаток на счету =", start_sum)
