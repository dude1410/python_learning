# 1
# count = 10
# while count <= 10:
#  if count == 0:
#    print('Время вышло!')
#    break
#  else:
#    print(count)
#    count -= 1

# 2
# while True:
#     next = int(input("Продолжаем работать? 1/0: "))
#     if next == 0:
#         print("Приложение закрывается…")
#         break

# 3
password = input("Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки! --->>> ")
while password != '0550':
    password = input("Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки! --->>> ")
print("Код верный, завершаю работу...")