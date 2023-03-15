print('Задача 4. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр и смотрите различные программы прошлого горе-программиста. В одной из игр для детей, связанной с мультяшной работой с числами, вам нужно было написать код согласно следующим условиям: программа получает на вход два числа; в первом числе должно быть не менее трёх цифр, во втором — не менее четырёх, иначе программа выдаёт ошибку. Если всё нормально, то в каждом числе первая и последняя цифры меняются местами, а затем выводится их сумма.

# И тут вы натыкаетесь на программу, которая была написана предыдущим программистом и которая как раз решает такую задачу. Однако старший программист попросил вас немного переписать этот код, чтобы он не выглядел так ужасно. Да и вам самим становится, мягко говоря, не по себе от него.

# Постарайтесь разделить логику кода на три отдельные логические части (функции):
# count_numbers — получает число и возвращает количество цифр в числе;
# change_number — получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число;
# main — функция ничего не получает на вход, внутри она запрашивает нужные данные от пользователя, выполняет дополнительные проверки и вызывает функции 1 и 2 для выполнения задачи (проверки и изменения двух чисел).

# Разбейте приведённую ниже программу на функции. Повторений кода должно быть как можно меньше. Также сделайте, чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.

print("0550" == 550)

def main():
    first_number = 0
    while first_number == 0:
        first_n = int(input("Введите первое число: "))
        temporary = count_numbers(first_n)
        if temporary >= 3:
            first_number = first_n
            print("OK")
        else:
            print("Неверный ввод")
        first_n = change_number(first_n, temporary)
# todo: the same logic with the second number

def count_numbers(temp):
    first_num_count = 0
    while temp > 0:
        first_num_count += 1
        temp = temp // 10
    return first_num_count

def change_number(inp_n, first_num_count):
    last_digit = inp_n % 10
    first_digit = inp_n // 10 ** (first_num_count - 1)
    between_digits = inp_n % 10 ** (first_num_count - 1) // 10
    first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
    print('Изменённое первое число:', first_n)
    return first_n

# запуск

main()

# *******************************
# first_n = int(input("Введите первое число: "))
# first_num_count = 0
# temp = first_n
#
# while temp > 0:
#     first_num_count += 1
#     temp = temp // 10
#
# if first_num_count < 3:
#     print("В первом числе меньше трёх цифр.")
# else:
#     last_digit = first_n % 10
#     first_digit = first_n // 10 ** (first_num_count - 1)
#     between_digits = first_n % 10 ** (first_num_count - 1) // 10
#     first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
#     print('Изменённое первое число:', first_n)
#     second_n = int(input("\nВведите второе число: "))
#     second_num_count = 0
#     temp = second_n
#
#     while temp > 0:
#         second_num_count += 1
#         temp = temp // 10
#     if second_num_count < 4:
#         print("Во втором числе меньше четырёх цифр.")
#     else:
#         last_digit = second_n % 10
#         first_digit = second_n // 10 ** (second_num_count - 1)
#         between_digits = second_n % 10 ** (second_num_count - 1) // 10
#         second_n = last_digit * 10 ** (second_num_count - 1) + between_digits * 10 + first_digit
#         print('Изменённое второе число:', second_n)
#         print('\nСумма чисел:', first_n + second_n)
#
# print()
#
#
# def get_number(msg, len_num):
#     num = 0
#     info_msg = 'Введите ' + msg + ' число: '
#     while len(str(num)) != len_num:
#         num = int(input(info_msg))
#     return num
#
#
# def change_num(num, len_num):
#     last_digit = num % 10
#     first_digit = num // 10 ** (len_num - 1)
#     between_digits = num % 10 ** (len_num - 1) // 10
#     num = last_digit * 10 ** (len_num - 1) + between_digits * 10 + first_digit
#     return num
#
#
# def get_first():
#     num = get_number('первое (трёхзначное)', 3)
#     num = change_num(num, 3)
#     print('Изменённое первое число:', num)
#     return num
#
#
# def get_second():
#     num = get_number('второе (четырёхзначное)', 4)
#     num = change_num(num, 4)
#     print('Изменённое второе число:', num)
#     return num
#
#
# first = get_first()
# second = get_second()
#
# print('Сумма чисел:', first + second)