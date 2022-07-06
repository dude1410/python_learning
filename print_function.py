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