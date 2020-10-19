n = input()
print(n)
number = []
for i in n:
    number.append(i)
print(number)
lenn = len(number)
print(lenn)
proverka1 = 0
if number[0] == '8' or (number[0] == '+' and number[1] == '7'):
    proverka1 += 1
vavod = 0


'''
Пример 1
Ввод	                 Вывод
+7(902)123-4567          +79021234567
Пример 2
Ввод	                 Вывод
8(902)1-2-3-45-67        +79021234567
Пример 3
Ввод	                 Вывод
504))635(22))9	9        error
Пример 4
Ввод	                 Вывод
8--9019876543-22-3--4    error
'''