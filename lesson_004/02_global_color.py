# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 1200)

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

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

color_index = int(input("Введите желаемый цвет: \n1 - красный\n2 - оранжевый\n3 - желтый"
                        "\n4 - зеленый\n5 - голубой\n6 - синий\n7 - фиолетовый\n"))

color = 0
if color_index == 1:
    color = sd.COLOR_RED
elif color_index == 2:
    color = sd.COLOR_ORANGE
elif color_index == 3:
    color = sd.COLOR_YELLOW
elif color_index == 4:
    color = sd.COLOR_GREEN
elif color_index == 5:
    color = sd.COLOR_CYAN
elif color_index == 6:
    color = sd.COLOR_BLUE
elif color_index == 7:
    color = sd.COLOR_PURPLE
else:
    print("Вы неверно ввели цвет")

if color != 0:
    point_triangle = sd.get_point(300, 300)
    triangle(point=point_triangle, length=300, angle=50, color_index=color)

    point_square = sd.get_point(900, 400)
    square(point=point_square, length=200, angle=20, color_index=color)

    point_rectangle_5 = sd.get_point(300, 800)
    rectangle_5(point=point_rectangle_5, length=200, angle=20, color_index=color)

    point_rectangle_6 = sd.get_point(800, 800)
    rectangle_6(point=point_rectangle_6, length=100, angle=50, color_index=color)

else:
    pass

sd.pause()
