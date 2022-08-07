# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
#
# point = sd.get_point(200, 200)
# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(center_position=point, radius=radius)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
#
# def bubble(point, step):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
#
# point = sd.get_point(400, 400)
# bubble(point=point, step=10)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Нарисовать 10 пузырьков в ряд
#
# def bubble(point, step):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
#
# for x in range(100, 1100, 100):
#     point = sd.get_point(x, 100)
#     bubble(point=point, step=5)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# # Нарисовать три ряда по 10 пузырьков
# #
# def bubble(point, step):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
#
# for y in range(100, 400, 100):
#     for x in range(100, 1100, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=5)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
#
def bubble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color=color)

for _ in range(200):
    bubble(sd.random_point(), 5, sd.random_color())

sd.pause()
