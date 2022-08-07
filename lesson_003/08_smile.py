# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.



def print_smile(x_cord, y_cord, color):

    point = sd.get_point(x_cord, y_cord)
    sd.circle(center_position=point, radius=100, color=color, width=4)
    point = sd.get_point(x_cord - 40, y_cord + 40)
    sd.circle(center_position=point, radius=20, color=color, width=4)
    point = sd.get_point(x_cord + 40, y_cord + 40)
    sd.circle(center_position=point, radius=20, color=color, width=4)


    point_list = []
    point_smile1 = sd.get_point(x_cord - 60, y_cord - 30)
    point_list.append(point_smile1)
    point_smile2 = sd.get_point(x_cord - 10, y_cord - 50)
    point_list.append(point_smile2)
    point_smile3 = sd.get_point(x_cord + 10, y_cord - 50)
    point_list.append(point_smile3)
    point_smile4 = sd.get_point(x_cord + 60, y_cord + -30)
    point_list.append(point_smile4)
    sd.lines(point_list=point_list, color=color, closed=False, width=10)

for _ in range(10):
    x_cord = sd.randint(100, 500)
    y_cord = sd.randint(100, 500)
    print_smile(x_cord=x_cord, y_cord=y_cord, color=sd.random_color())


sd.pause()
