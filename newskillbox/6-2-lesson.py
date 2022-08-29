# 1
# number = int(input('Введите число: '))
# summ = 0
# while number != 0:
#     summ += number
#     number = int(input('Введите число: '))
# print(summ)

# 2
# password = input("Введите пароль: ")
#
# while password != "235":
#     print("Неверный палоль!")
#     password = input("Попробуйте еще раз: ")
# print("Пароль верный! Добро пожаловать.")

# 3
portion = int(input("Сколько отложить денег? "))
summ = 0
summ += portion
while summ <= 500000:
    print("Пока не хватает. На счету:", summ)
    portion = int(input("Сколько отложить денег? "))
    summ += portion
print("Поздравляю, вы накопили", summ)