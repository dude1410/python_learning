# MyProfile app

# user profile
name = ''
age = 0
phone = ''
email = ''
info = ''
mailbox_index = ''
# bank info
ogrnip = ''
inn = ''
checking_account = ''
bank_name = ''
bik = ''
correspondent_account = ''
# phrases
SEPARATOR = '------------------------------------------'
start_greeting = 'Приложение MyProfile\nСохраняй информацию о себе и выводи ее в разных форматах'
main_menu = SEPARATOR + '\nГЛАВНОЕ МЕНЮ\n1 - Ввести или обновить информацию\n2 - Вывести информацию\n0 - Назад'
select_menu = 'Введите номер пункта меню: '
incorrect_menu = 'Введите корректный пункт меню '
sub_menu_1 = SEPARATOR + '\nВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ\n1 - Общая информация\n2 - Банковская информация\n0 - Назад'
sub_menu_2 = SEPARATOR + '\nВЫВЕСТИ ИНФОРМАЦИЮ\n1 - Общая информация\n2 - Вся информация\n0 - Назад'


def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, info_parameter, mailbox_index_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    print('Почтовый индекс: ', mailbox_index_parameter)
    if info_parameter:
        print('Дополнительная информация:')
        print(info_parameter)


def general_bank_info(ogrnip_parameter, inn_parameter, checking_account_parameter,
                      bank_name_parameter, bik_parameter, correspondent_account_parameter):
    print(SEPARATOR)
    print('ОГРНИП: ', ogrnip_parameter)
    print('ИНН:', inn_parameter)
    print('Расчётный счёт: ', checking_account_parameter)
    print('Название банка: ', bank_name_parameter)
    print('БИК: ', bik_parameter)
    print('Корреспондентский счёт: ', correspondent_account_parameter)


def filter_only_numbers(input_string):
    answer = ''
    for character in input_string:
        if '0' <= character <= '9':
            answer += character
    return answer


def check_input(input_string, count_numbers):
    answer = filter_only_numbers(input_string)
    if len(answer) == count_numbers:
        return True
    else:
        return False


print(start_greeting)

while True:
    # main menu
    print(main_menu)
    option = int(input(select_menu))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(sub_menu_1)

            option2 = int(input(select_menu))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        phone += ch

                email = input('Введите адрес электронной почты: ')
                info = input('Введите дополнительную информацию:\n')
                mailbox_index = filter_only_numbers(input('Введите почтовый индекс: '))

            elif option2 == 2:
                # input bank info
                check = True
                while check:
                    temp = input('Введите ОГРНИП: ')
                    if check_input(temp, 15):
                        ogrnip = temp
                        check = False

                inn = input('Введите ИНН: ')

                check = True
                while check:
                    temp = input('Введите расчётный счёт: ')
                    if check_input(temp, 20):
                        checking_account = temp
                        check = False

                bank_name = input('Введите название банка: ')
                bik = input('Введите БИК: ')
                correspondent_account = input('Введите корреспондентский счёт: ')
            else:
                print(incorrect_menu)
    elif option == 2:
        # submenu 2: print info
        while True:
            print(sub_menu_2)

            option2 = int(input(select_menu))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone, email, info, mailbox_index)

            elif option2 == 2:
                general_info_user(name, age, phone, email, info, mailbox_index)
                general_bank_info(ogrnip, inn, checking_account, bank_name, bik, correspondent_account)
            else:
                print(incorrect_menu)
    else:
        print(incorrect_menu)
