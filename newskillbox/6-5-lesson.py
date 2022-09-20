# 1
# amount = int(input("Введите кол-во повторений: "))
# count = 0
# while amount > count:
#     print("Я — программист!")
#     count += 1

# 2
# amount = int(input("Сколько раз вам напомнить о событии: "))
# while amount > 0:
#     print("Вы хотели не забыть о чём-то")
#     amount -= 1

# 3
amount = int(input("Сколько мешков наловили: "))
total_weight = 0
while amount > 0:
    weight = int(input("Масса мешка: "))
    total_weight += weight
    amount -= 1
print("Наловили", total_weight, "кг")