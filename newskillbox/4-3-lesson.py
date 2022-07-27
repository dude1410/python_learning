# 1
bank = int(input("Сколько денег на счету? "))
if bank >= 75000:
    bank -= 75000
    print("Покупка совершена")
    print("остаток кэша", bank)
else:
    print("Недостаточно кэша")
print("хорошего дня")

# ***********************************
# 2
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
user_sum = int(input("Сумма этих чисел: "))
if user_sum == (first + second):
    print("Верно!")
else:
    print("Ответ неверный")