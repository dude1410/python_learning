# 1
apples_amount = 41
apples_in_box = 3
print("Целых ящиков -", apples_amount // apples_in_box)
print("Остаток яблок -", apples_amount % apples_in_box)

# ***************************
# 2
number = int(input("Введите число: "))
print("Номер дома:", number % 10)
print("Номер квартиры:", number // 10)

# *****************************
# 3
distance = int(input("Введите пройденную дистанцию: "))
print("Целый кругов", distance // 100)
print("Остаток:", distance % 100)