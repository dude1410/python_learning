#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint

# Есть словарь координат городов

cites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

moscow = cites['Moscow']
london = cites['London']
paris = cites['Paris']

london_moscow = int(((london[0] - moscow[0]) ** 2 + (london[1] - moscow[1]) ** 2) ** 0.5)
london_paris = int(((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5)
moscow_paris = int(((paris[0] - moscow[0]) ** 2 + (paris[1] - moscow[1]) ** 2) ** 0.5)

distances['moscow'] = {'london': london_moscow, 'paris': moscow_paris}
distances['london'] = {'moscow': london_moscow, 'paris': london_paris}
distances['paris'] = {'london': london_paris, 'moscow': moscow_paris}

pprint(distances)




