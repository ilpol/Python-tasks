#Задание
#Дана квадратная матрица размера NxN.
#Необходимо найти в ней побочную диагональ с минимальной суммой чисел, 
#вывести на экран все элементы этой диагонали 
# (при совпадении сумм вывести ту, где больше элементов).

#Предположение, что матрица вводится построчно. Элементы строки разделены
#пробелом с запятой, строки разделены новой строкой.
#Конец ввода - просто enter
#Пример
#1, 2
#4, 5
#
#Пояснение алгоритма:
#При вводе матрицы сразу заполняеся список диагоналей.
#Затем из них выбирается диагональ с минимальной суммой
#элементов и максимальной длиной.

matrix = []
row = list((input().split(', ')))
diags = []
mLength = len(row)

#Матрица квадратная, поэтому сразу по длине
#строки можно узнать их количество
for i in range(mLength*2-1):
  diags.append([])

base = 0
curMin = 0
while row!=['']:
  row = list(map(int, row))
  for i in range(base, mLength + base):
    diags[i].append(row[i - base])
  base+=1
  row = list((input().split(', ')))

def sumVals (arr):
  sum = 0
  for i in arr:
    sum +=i
  return sum

curDiags = []
curMin = sumVals(diags[0])
curLength = -1
res = ''
for diag in diags:
  curSum = sumVals(diag)
  if curSum<=curMin and len(diag) > curLength:
    res = diag
    curLength = len(diag)
    curMin = curSum

print(' '.join(str(v) for v in res))




    