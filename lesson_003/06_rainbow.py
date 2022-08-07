# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
#
# start_x, start_y, end_x, end_y, width = 50, 50, 350, 450, 10
#
# for color in rainbow_colors:
#     start_point = sd.get_point(start_x, start_y)
#     end_point = sd.get_point(end_x, end_y)
#     sd.line(start_point=start_point, end_point=end_point, color=color, width=width)
#     start_x, end_x = start_x + width, end_x + width
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

start_x, start_y, width, radius = 600, -100, 30, 600


for color in rainbow_colors:
    start_point = sd.get_point(start_x, start_y)
    sd.circle(center_position=start_point, radius=radius, color=color, width=width)
    radius += width

sd.pause()
