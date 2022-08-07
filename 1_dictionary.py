my_box = {}
print(my_box)
my_box["слон", "лиса"] = "elephant", "fox"
print(my_box)

my_box = {"стол": "тэйбл", "стул": "чэйр"}
print(my_box)

# в качестве ключа только неизменяемые объекты

print(my_box.values())
print(my_box.keys())

print("стол" in my_box)  # проверка на вхождение

print(my_box['стол'])

print(my_box.get('кот', 'кэт'))  # если такого ключа нет, дай второе значение
print(my_box.get('стол', 'кэт'))  # если ключ есть, то дай значение
print(my_box.setdefault("кот", 'кэт'))  # если ключа нет, то добавь новую пару
print(my_box)

print('-----')
# МНОЖЕСТВА (список уникальных объектов)
my_set = set([1, 1, 1, 1, 2, 3, 45, 45, 20, 111111])  # повторяющмеся элементы выкинуты
print(my_set)
other_set = {1, 2, 2, 3, 45, 45, 20, 100, 0, 1000}
print(other_set)

# операции на сэтами
print('------')
print(my_set | other_set)  # объединение сэтов
print(my_set & other_set)  # только совпадающие в двух сэтах
print(my_set - other_set)  # есть в первом, но нет во втором

my_set.add(22222222)
print(my_set)
my_set.pop()  # удаление первого
print(my_set)
my_set.discard(45)  # указание на удаляемый элемент
print(my_set)
my_set.update([12, 11, 10, 18])  # расширение сэта новым списком/сэтом
print(my_set)
