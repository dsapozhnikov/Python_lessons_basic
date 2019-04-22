# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

#
# #task1
from math import sqrt
import time
from time import strftime
import random

import datetime
print('\n task-1 \n')

origin = [3, 2, 1, 0, 9, 144, 100]
endList = []

for i in origin:
    if i != 0 and i > 0:
     res = sqrt(i)
     if res / int(res)==1:
         endList.append(int(res))
     else:
         print("it is decimal!")

print(endList)




# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
print('\n task-2 \n')
loctime = time.time()
datetim = str.split(strftime('%d, %B, %Y', time.gmtime(loctime)), ", ")

dict = {
    1:'first',
    2:'second',
    3:'third',
    4:'fourth',
    5:'fifth',
    6:'sixth',
    7:'seventh',
    8:'eights',
    9:'ninth',
    10:'tenth',
    11:'eleventh',
    12:'twelfth',
    13:'thirteenth',
    14:'fourteenth',
    15:'eighteenth',
    16:'sixteenth',
    17:'seventeenth',
    18:'eighteenth',
    19:'nineteenths',
    20:'twenty',
    30:'thirty'
}

if int(datetim[0]) in dict.keys():

    tmpStr = dict[int(datetim[0])]

    if tmpStr[-1:] == 'y':
         tmpList = list(tmpStr)
         tmpList.pop()
         tmpList.append('ieth')
         print(str('{0} {1} {2}'.format(str("".join(tmpList))+' '+'of', datetim[1], datetim[2])))

elif int(datetim[0]) in range(21, 32):
    temp = list(datetim[0])
    print(str(f"{dict[int(datetim[0])-int(temp[1])]} {dict[int(temp[1])]+' '+'of'} {datetim[1]} {datetim[2]}"))



# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print('\n task-3 \n')
s = {()}
while len(s) < 202:
    s.add(random.randint(-100, 100))

print(s)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
print('\n task-4 \n')

lst = [1, 2, 4, 5, 6, 2, 5, 2]

sortedList = list(filter(lambda x: lst.count(x)<=1, lst ))
print('here: '+str(sortedList))
# lst = [1, 2, 4, 5, 6, 2, 5, 2]
#
# for i, v in enumerate(lst):
#    for c, k in enumerate(lst):
#        if lst.count(i)==2:
#            lst.pop(i)
#
#
# print('here: '+str(lst))