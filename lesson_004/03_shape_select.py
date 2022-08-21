# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 1200)

start_point = sd.get_point(600, 600)

length_for_any_figure = 300


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def triangle(point, length, color_index, angle=0):
    paint_fugure(point=point, length=length, angle=angle, sides=3, color=color_index)


def square(point, length, color_index, angle=0):
    paint_fugure(point=point, length=length, angle=angle, sides=4, color=color_index)


def rectangle_5(point, length, color_index, angle=0):
    paint_fugure(point=point, length=length, angle=angle, sides=5, color=color_index)


def rectangle_6(point, length, color_index, angle=0):
    paint_fugure(point=point, length=length, angle=angle, sides=6, color=color_index)


def paint_fugure(point, length, angle, sides, color):
    start_point = point

    angle_for_figure = int(360 / sides)

    for i in range(sides):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v.draw(color)
        point = v.end_point
        angle = angle + angle_for_figure

    if start_point is point:
        print("Закрытый контур")
    else:
        sd.line(point, start_point)


figure_index = int(input("Введите желаемую фтгуру: \n1 - треугольник\n2 - квадрат\n3 - пятиугольник"
                         "\n4 - шестиугольник\n>>> "))

if figure_index == 1:
    triangle(point=start_point, length=length_for_any_figure, color_index=sd.random_color(), angle=random.randint(0, 360))
elif figure_index == 2:
    square(point=start_point, length=length_for_any_figure, color_index=sd.random_color(), angle=random.randint(0, 360))
elif figure_index == 3:
    rectangle_5(point=start_point, length=length_for_any_figure, color_index=sd.random_color(), angle=random.randint(0, 360))
elif figure_index == 4:
    rectangle_6(point=start_point, length=length_for_any_figure, color_index=sd.random_color(), angle=random.randint(0, 360))
else:
    print("Вы неверно ввели номер фигуры")


sd.pause()
