import sys
import platform

print('hello, world')
print(sys.version)
print(platform.release())

print("привет".encode())

print(b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode())

str_test = "qwerty"
print(str_test[0])
print(str_test[-1])
print(str_test[1:4])
print(str_test[:4])
print(str_test[:])

str_test2 = "qwertyuiopasdfghjkl"
print(str_test2[1:15:3])
print(len(str_test2))
print(str_test2[::-1])
print(str_test2[18:0:-1])

a, b, c = "word1", 12.005, 123

print(a, b, c)
print(type(a))
print(type(b))
print(type(c))

print(isinstance(b, float))

print(id(a))

# x, y = map(int, input().split()) # ожидание ввода от нас двух интовых значений через запятую
# print(type(x))
# print(type(y))
# print(x, y)

# методы строк
car = "Тойота Королла"
print(len(car))
print(car.upper())
print(car.lower())
print(car.isalpha()) # проверка, все ли знаки буквы
print(car.find('й'))
print(car.rfind('о')) # только первое значение с головы
print(car.rfind('о')) # только первое значение с хвоста
print(car.replace('о', '0'))
