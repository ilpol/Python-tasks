#Задание
#На вход программы поступает последовательность из N целых чисел
#в диапазоне от 0 до 1000. Необходимо найти наиболее часто встречающееся
#в последовательности число (при нескольких – максимальное из них).
#Пример: 
#Вход ­– “0, 2, 3, 9, 0, 15, 21, 36, 8, 3”
#Выход – “3”

numbers = eval(input())
countNuumbers = {}

for i in numbers:
    countNuumbers[i] = countNuumbers.get(i,0) + 1

results = [k for k, v in countNuumbers.items() if v == max(countNuumbers.values())]
res = max(results)
print(res)