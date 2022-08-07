my_list = [1, 2, 3, 4, 0, 'qwerty', 100, 'end']

print(my_list[-3::-1]) # от 3 с конца до начала с шагом -1

my_list.append(77) # добавить в конец

print(my_list)

my_list.extend([111, 110, 1009]) # расширение списка путем добавления в конец нового списка

print(my_list)

my_list.insert(0, 'new element') # вставить на позицию х элемент у

print(my_list)

del my_list[0] # оператор языка для удаления

print(my_list)

my_list.remove(100) # удаление первого попавшегося указанного элемента

print(my_list)

my_list += [0.1, 0.2, 0.3] # еще способ добавить новый список

print(my_list)

car = "audi"

my_list.append(car)

print(my_list)

print(my_list * 2) # вывод списка дважды

matrix = [[1, 2, 3], [4, 'dad', 6], [7, 8, 9]]

print(matrix[1][1][1]) # достать 1-ый элемент из списка (элемента) 1

print([1, 1, 1, 0] > [3, 0]) # сравнение по очереди по элементам

print(77 in my_list) # проверка на вхождение элемента в список

print(id(my_list))

print(list(range(1, 56, 2))) # создание списка на лету от х до у (тут от до с шагом)

# создание списков
print(list())
print(list([1, 10, 100]))

print(my_list.count(1)) # посчитать, сколько у нас элеиментов Х в списке

# нельзя сравнивать, пока в списке есть элементы разного типа
del my_list[5]
del my_list[5]
del my_list[-1]
print(my_list)
print(min(my_list))
print(max(my_list))
my_list.sort()
print(my_list)

my_list[0] = 5555 # изменение элемента из списка
print(my_list)

new_list = [[], [], []]
print(new_list)
new_new = new_list * 3
new_list[0].append(2) # при умножении списков добавление в первый список дает добавление во все (так как это ссылка)
print(new_new)