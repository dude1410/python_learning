# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 1200)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви


def draw_brunches(start_point, angle, length):
    delta = 20
    if length < 3:
        return
    angle_left = angle + delta
    angle_right = angle - delta
    new_length = length * 0.75


    v1 = sd.get_vector(start_point=start_point, angle=angle_left, length=length)
    v1.draw(color=sd.COLOR_RED)
    v2 = sd.get_vector(start_point=start_point, angle=angle_right, length=length)
    v2.draw(color=sd.COLOR_GREEN)

    draw_brunches(start_point=v1.end_point, angle=angle_left, length=randomize_length(new_length))
    draw_brunches(start_point=v2.end_point, angle=angle_right, length=randomize_length(new_length))


def randomize_length(length):
    return length * 0.7 + length * 0.6 * random.randint(0, 100) / 100

def randomize_angle(angle):
    return angle * 0.6 + angle * 0.8 * random.randint(0, 100) / 100





# 3) первоначальный вызов:
root_point_1 = sd.get_point(600, 100)
root_point_2 = sd.get_point(600, 200)
sd.line(root_point_1, root_point_2)

draw_brunches(start_point=root_point_2, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


