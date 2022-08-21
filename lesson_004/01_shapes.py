 # -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 1200)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:

# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# - треугольника
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# def triangle(point, length, angle=0):
#
#     for i in range(3):
#         v = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         v.draw()
#         point = v.end_point
#         angle = angle + 120
#
# point_triangle = sd.get_point(300, 300)
# triangle(point=point_triangle, length=300, angle=50)

# - квадрата

# def square(point, length, angle=0):
#
#     for i in range(4):
#         v = sd.get_vector(start_point=point, angle=angle, length=length, width=4)
#         v.draw()
#         point = v.end_point
#         angle = angle + 90
#
# point_square = sd.get_point(900, 400)
# square(point=point_square, length=200, angle=20)

# - пятиугольника

# def rectangle_5(point, length, angle=0):
#
#     for i in range(6):
#         v = sd.get_vector(start_point=point, angle=angle, length=length, width=4)
#         v.draw()
#         point = v.end_point
#         angle = angle + 72
#
# point_rectangle_5 = sd.get_point(300, 800)
# rectangle_5(point=point_rectangle_5, length=200, angle=20)

# - шестиугольника

# def rectangle_6(point, length, angle=0):
#
#     for i in range(7):
#         v = sd.get_vector(start_point=point, angle=angle, length=length, width=4)
#         v.draw()
#         point = v.end_point
#         angle = angle + 60
#
# point_rectangle_6 = sd.get_point(800, 800)
# rectangle_6(point=point_rectangle_6, length=100, angle=50)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)

def paint_fugure(point, length, angle, sides):

    start_point = point

    angle_for_figure = int(360 / sides)

    for i in range(sides + 1):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v.draw()
        point = v.end_point
        angle = angle + angle_for_figure

    if start_point != point:
        sd.line(point, start_point)

def triangle(point, length, angle=0):
    paint_fugure(point=point, length=length, angle=angle, sides=3)

point_triangle = sd.get_point(300, 300)
triangle(point=point_triangle, length=300, angle=50)

def square(point, length, angle=0):
    paint_fugure(point=point, length=length, angle=angle, sides=4)

point_square = sd.get_point(900, 400)
square(point=point_square, length=200, angle=20)

def rectangle_5(point, length, angle=0):
    paint_fugure(point=point, length=length, angle=angle, sides=5)

point_rectangle_5 = sd.get_point(300, 800)
rectangle_5(point=point_rectangle_5, length=200, angle=20)

def rectangle_6(point, length, angle=0):
    paint_fugure(point=point, length=length, angle=angle, sides=6)

point_rectangle_6 = sd.get_point(800, 800)
rectangle_6(point=point_rectangle_6, length=100, angle=50)

# point_test = sd.get_point(500, 500)
# paint_fugure(point=point_test, length=500, angle=0, sides=11)

# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
