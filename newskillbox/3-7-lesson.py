# 1
a = 8
b = 10
c = 12
d = 18
result = ((-3 + a ** 2) * b - 2 ** 3) / (c - 2 * d)
print(result)

# ******************************
# 2
a_1 = int(input("Введите первое число: "))
a_2 = int(input("Введите второе число: "))
a_3 = int(input("Введите третье число: "))
a_4 = int(input("Введите четвертое число: "))
print("Результат =", (a_1 + a_2) / (a_3 + a_4))

# *******************************
# 3
number = int(input("Введите число: "))
print("После числа", number, "идет число", number + 1)
print("До числа", number, "идет число",  number - 1)

# *********************************
# 4
first_katet = int(input("Введите первый катет: "))
second_katet = int(input("Введите второй катет: "))
print("Площадь треугольника =", (first_katet * second_katet) / 2)

# **********************************
# 5
minutes = int(input("Введите количество минут: "))
print("Hours =", minutes // 60)
print("Minutes left =", minutes % 60)

# ************************************
# 6
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
first_number %= 100
second_number %= 100
print("Sum =", first_number + second_number)

# *****************************************
# 7
time = int(input("Введите время поездки: "))
speed = int(input("Введите скорогсть поездки: "))
distance = time * speed
mark = distance % 115
print("Cycle stopped at km =", mark)
