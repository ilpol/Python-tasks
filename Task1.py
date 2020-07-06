#Задание
#На входе имеется символьная строка, необходимо написать код,
#осуществляющий ее RLE-преобразование, заключающееся в подсчете
#подряд идущих букв.
#Пример: 
#Вход – “aaaaBBbbCooa”
#Выход – “4a2B2bC2oa” 

inputString = input()
res = []
if str!="":
  count = 0
  curChar = inputString[0] 
  for i in inputString:
      if i==curChar:
        count+=1
      else:
        if count>1:
          res.append(str(count))
        count = 1
        res.append(curChar)
        curChar = i
  if count==1:
    res.append(curChar)
  else:
    res.append(str(count))
    count = 1
    res.append(curChar)  

print(''.join(res))
