# 1
coord_x = int(input('Введите икс: '))
coord_y = int(input('Введите игрек: '))

if coord_y == coord_x:
    print('X равен Y')
elif coord_y > coord_x:
    print('X меньше Y')
else:
    print('X больше Y')

# /////////////////////////////////////////////////////////////
# 2
profit = int(input('Enter your profit: '))
if profit <= 0:
    print('Error! Profit must by greater than 0 $')
else:
    if profit < 10000:
        tax_rate = 13
    elif 10000 <= profit < 50000:
        tax_rate = 20
    else:
        tax_rate = 30
    print('Your taxe rate =', tax_rate, '%')
    print('You have to pay', profit * tax_rate / 100, '$')

# ////////////////////////////////////////////////////////////
# 3
weight_1 = int(input('Введите вес первой монеты: '))
weight_2 = int(input('Введите вес второй монеты: '))
weight_3 = int(input('Введите вес третьей монеты: '))

if weight_1 > weight_2:
    print('Фальшивая вторая монета')
elif weight_1 < weight_2:
    print('Фальшивая первая монета')
else:
    print('Фальшивая третья монета')