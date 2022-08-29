# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1300, 1300)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20
speed = 5

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

my_list = []
for _ in range(N):
    my_tuple = list((random.randint(100, 1300), random.randint(300, 1300), random.randint(10, 50), random.randint(1, 5)))
    my_list.append(my_tuple)

def get_random():
    random_int = random.randint(0, 1)
    if random_int == 0:
        return 1
    else:
        return -1

while True:
    sd.clear_screen()

    for i, item in enumerate(my_list):
        point = sd.get_point(item[0], item[1])
        if item[1] < 50:
            item[0] = random.randint(000, 1000)
            item[1] = random.randint(900, 1000)
            # sd.snowflake(center=point, length=item[2], color=sd.COLOR_WHITE)
            # continue
        sd.snowflake(center=point, length=item[2], color=sd.COLOR_WHITE)
        item[0] = item[0] + item[3] * get_random()
        item[1] = item[1] - speed

    sd.sleep(0.15)
    if sd.user_want_exit():
        break




    # for _ in range(N):
    #     point = sd.get_point(start_x, start_y)
    #     sd.snowflake(center=point, length=20)
    #     start_y -= 5
    #     if start_y < 50:
    #         break
    #     start_x = (start_x * 0.99 + start_x * 0.02 * random.randint(0, 100) / 100)
    #
    #     sd.sleep(0.1)
    #     if sd.user_want_exit():
    #         break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


