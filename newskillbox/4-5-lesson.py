# 1
rain = int(input("На улице идёт дождь? "))
if rain == 1:
    print("Пошёл дождь. Возьмите зонтик!")

# ***************************************
# 2
first = int(input("Введите количество баллов по русскому языку: "))
second = int(input("Введите количество баллов по математике: "))
third = int(input("Введите количество баллов по информатике: "))
if first + second + third >= 270:
    print("Поздравляю, ты поступил на бюджет!")
else:
    print("К сожалению, ты не прошёл на бюджет.")

# *******************************************
# 3
date = int(input("Какое сегодня число? "))
if date % 2 == 0:
    print("Маша, нить!")
else:
    print("Маша, расслабься")

# **************************************
# 4
first_price = int(input("Введите первую цену: "))
second_price = int(input("Введите вторую цену: "))
third_price = int(input("Введите третью цену: "))
sumary = first_price + second_price + third_price
if sumary > 10000:
    sumary *= 0.9
print("сумма к оплате:", sumary)

# ***********************************************
# 5
integer = int(input("Введите число: "))
new_int = 0
if integer < 0:
    new_int = integer * -1
else:
    new_int = integer
print("Вы ввели", integer, "ответ", new_int)

# ******************************************************
# 6
kostya = int(input("Кубик Кости: "))
owner = int(input("Кубик владельца: "))
if kostya == owner:
    print("ничья")
elif kostya > owner:
    print("Костя платит", (kostya - owner) * 1000)
else:
    print("Владелец платит", (kostya + owner) * 1000)
print("игра закончена")

# *****************************************************
# 7
money = int(input("Сколько денег снять? "))
if money % 100 == 0:
    print("вы успешно сняли", money)
else:
    print("Такую сумму снять невозможно. Обратитесь в другой банкомат.")

# *************************************
# 8
hours = int(input("Введите отработанные часы: "))
credit = int(input("Введите остаток по кредиту: "))
for_food = int(input("Введите траты на еду: "))
salary = (200 * hours) / (2 ** 3) + hours
if salary >= credit + for_food:
    print("Часов хватает. Можно отдохнуть")
else:
    print("Часов не хватает. Придётся работать!")

# ***************************************
# 9
distance = int(input("Введите пробег: "))
day = int(input("Введите сегодняшнее число: "))
d_1 = distance // 100
d_2 = distance % 100 // 10
d_3 = distance % 10
if d_1 + d_2 + d_3 > day:
    print("Сброс")
    distance = 0
else:
    print("Сегодня не сломался.")
print("Пробег:", distance)

# ****************************************
# 10
a_1 = int(input("Введите первое число: "))
a_2 = int(input("Введите второе число: "))
a_3 = int(input("Введите третье число: "))
maximal = a_1
if maximal < a_2:
    maximal = a_2
if maximal < a_3:
    maximal = a_3
print("Наибольшее число", maximal)