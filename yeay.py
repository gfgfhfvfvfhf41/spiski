"""
№1

n = int(input("Введите "))
a = []
for i in range(1, n+1):
    a.append(i)
print(a)
"""



"""
№2
n = int(input("Введите n: "))
x = int(input("Введите x: "))
i = 0
a = []
while n > i:
    a.append(x)
    x+=1
    n-=1
print(a)
"""



"""
№3
n = int(input("Введите n: "))
a = []
for i in range(1, n+1):
    a.append(i*i)
print(a)
"""



"""
№4
n = int(input("Введите n: "))
a = []
for i in range(1, n+1):
    a.append(i)
a.reverse()
print(a)
"""



"""
№5
n = int(input("Введите n: "))
x = int(input("Введите x: "))
i = 0
a = []
while n > i:
    a.append(x)
    n-=1
    x+=1
a.reverse()
print(a)
"""



"""
№6
n = int(input("Введите n: "))
a = []
for i in range(1, n+1):
    a.append(2**i)
a.reverse()
print(a)
"""



"""
№7
from random import randint
n = input("Введите n и через пробел диапозон в квадратных скобках(через запятую): ")
n = n.replace("[", " ").replace("]", " ").replace(",", " ").split()
a = []
s = 0
for i in range(int(n[0])):
    a.append(randint(int(n[1]), int(n[2])))
print(a)
for i in a:
    try:
        i = str(i)
        b = i[1]
        b1 = i[1]
    except IndexError:
        print("Хуй там плавал")
    if len(i) >= 3:
        if int(b) % 2 == 0:
            s+=1
    elif len(i) == 2:
        if int(b) == 0:
            pass
        else:
            if int(b) % 2 == 0:
                s+=1       
print(s)
"""



"""
№8
from random import randint
n = input("Введите n и через пробел диапозон в квадратных скобках(через запятую): ")
n = n.replace("[", " ").replace("]", " ").replace(",", " ").split()
a = []
s = 0
for i in range(int(n[0])):
    a.append(randint(int(n[1]), int(n[2])))
print(a)
chetnye = 0
nechetnye = 0
for i in a:
    if i % 2 == 0:
        chetnye+=1
    elif i % 2 != 0:
        nechetnye+=1
print(f'Количество четных: {chetnye}\nКоличество нечетных: {nechetnye}')
"""



"""
№9
from random import randint
n = input("Введите n и через пробел диапозон в квадратных скобках(через запятую): ")
n = n.replace("[", " ").replace("]", " ").replace(",", " ").split()
a = []
for i in range(int(n[0])):
    a.append(randint(int(n[1]), int(n[2])))
max_value = max(a)
if str(max_value).startswith('-'):
    print("Хуй там плавал")
elif not str(max_value).startswith('-'):
    print(max_value)
else:
    print("-1")
"""



"""
№10
from random import randint
n = input("Введите n и через пробел диапозон в квадратных скобках(через запятую): ")
n = n.replace("[", " ").replace("]", " ").replace(",", " ").split()
a = []
f = 0
for i in range(int(n[0])):
    a.append(randint(int(n[1]), int(n[2])))
for i in a:
    f+=i
print(f/len(a))
"""



"""
№11
from random import randint
n = input("Введите n и через пробел диапозон в квадратных скобках(через запятую): ")
x = int(input("Введите значение Х: "))
n = n.replace("[", " ").replace("]", " ").replace(",", " ").split()
a = []
f = 0
for i in range(int(n[0])):
    a.append(randint(int(n[1]), int(n[2])))
print(a)
for i in range(len(a)):
    if a[i] == x:
        f+=1
print(f'Количество элементов: {f}')
"""



"""
№12
from random import randint
n = input("Введите n и через пробел диапозон в квадратных скобках(через запятую): ")
x = int(input("Введите значение Х: "))
n = n.replace("[", " ").replace("]", " ").replace(",", " ").split()
a = []
f = 0
for i in range(int(n[0])):
    a.append(randint(int(n[1]), int(n[2])))
print(a)
for i in range(len(a)):
    if a[i] == x:
        print(i)
"""



"""
№13
from random import randint
n = input("Введите n и через пробел диапозон в квадратных скобках(через запятую): ")
n = n.replace("[", " ").replace("]", " ").replace(",", " ").split()
a = []
f = 0
for i in range(int(n[0])):
    a.append(randint(int(n[1]), int(n[2])))
max_value = max(a)
print(a)
for i in range(len(a)):
    if a[i] == max_value:
        f+=1
print(f'Max = {max_value} K = {f}')        
"""



"""
№14
from random import randint
n = input("Введите n и через пробел диапозон в квадратных скобках(через запятую): ")
n = n.replace("[", " ").replace("]", " ").replace(",", " ").split()
a = []
b = []
for i in range(int(n[0])):
    a.append(randint(int(n[1]), int(n[2])))
for i in a:
    if i % 2 == 0 and not str(i).startswith('-'):
        b.append(i)
max_value = max(b)
min_value = min(b)
print(f'Max value: {max_value} Min value: {min_value}')
"""
