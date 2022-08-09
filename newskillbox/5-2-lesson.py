# 1
coord_x = int(input('Введите икс: '))
coord_y = int(input('Введите игрек: '))

if coord_y == coord_x:
    print('X равен Y')
if coord_y > coord_x:
    print('X меньше Y')
if coord_y < coord_x:
    print('X больше Y')


# ////////////////////////////////////////////
# 2
course_price = 75000
bank = int(input('Сколько днег на счету? '))
if bank >= course_price:
    bank -= course_price
    if bank < 5000:
        bank += 1000
        print('Сделана скидка')
    print('Курс успешно приобретен')
else:
    print('Не хватает денег на счету')
print('Остаток на счете', bank)
print('Хорошего дня')


# //////////////////////////////////////////////
# 3
cheese = 60
ice_cream = 20
babosy = int(input("Сколько денег дали? "))
if babosy >= cheese:
    babosy -= cheese
    print('На сыр денег хватило')
    if babosy >= ice_cream:
        babosy -= ice_cream
        print('И на мороженое тоже!')
    else:
        print('Денег маловато')
else:
    print('Денег не хватило даже на сыр')
print('Остаток денег', babosy)