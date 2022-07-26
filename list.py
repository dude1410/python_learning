my_list = [1, 2, 3, 4, 'qwerty', 5, 6.5]

print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[-1::-1])

my_list.append('asd') # добавить в конец элемент
my_list.extend([7, 8, 9]) # добавить новый список в конец
my_list.insert(0, '0000') # вставить на место X новый элемент Y


print(my_list)

del my_list[0]
print(my_list)
# или
my_list.remove(1)
print(my_list)