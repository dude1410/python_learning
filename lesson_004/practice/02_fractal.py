# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 1200)

# нарисовать ветку дерева из точки (300, 5) вертикально вверх длиной 100

point_0 = sd.get_point(600, 50)


# сделать функцию рисования ветки из заданной точки,
# заданной длины, с заданным наклоном
def branch(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    return v1.end_point

# angle_0 = 90
# length_0 = 200
# next_point = branch(point=point_0, angle=angle_0, length=length_0)
# next_angle = angle_0 - 30
# next_length = length_0 * .75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)
# next_angle = next_angle - 30
# next_length = next_length * .75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)
#
# написать цикл рисования ветвей с постоянным уменьшением длины на 25% и отклонением на 30 градусов
angle_0 = 90
length_0 = 200

next_angle = angle_0
next_length = length_0
next_point = point_0

# while next_length > 10:
#     next_point = branch(point=next_point, angle=next_angle, length=next_length)
#     next_angle = next_angle - 30
#     next_length = next_length * .75

# сделать функцию branch рекурсивной

def branch(point, angle, length, delta):
    if length < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - delta
    next_length = length * .75
    branch(point=next_point, angle=next_angle, length=next_length, delta=delta)


# branch(point=point_0, angle=90, length=100, delta=30)


for delta in range(5, 51, 5):
    branch(point=point_0, angle=90, length=150, delta=delta)
for delta in range(-50, -4, 5):
    branch(point=point_0, angle=90, length=150, delta=delta)


sd.pause()

