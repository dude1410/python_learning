# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

brick_length, brick_height = 50, 20
start_y = 0
for x in range(50):
    if x % 2 == 0:
        start_x = 0
    else:
        start_x = - brick_length / 2

    for _ in range(20):
        start_point = sd.get_point(start_x, start_y)

        end_x = start_x + brick_length
        end_y = start_y + brick_height
        end_point = sd.get_point(end_x, end_y)

        sd.rectangle(left_bottom=start_point, right_top=end_point, color=sd.random_color(), width=2)
        start_x += brick_length

    start_y += brick_height


sd.pause()
