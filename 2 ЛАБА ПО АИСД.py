'''
Лабораторная работа № 2
Вариант 24
Шеснадцатиричные числа, не превышающие 1024_10 расположенные в порядке убывания.
Для каждой такой последовательности максимальное число вывести прописью.
'''
import re
slovar = {0:'ноль',1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять',\
     'A':'десять','B':'одинадцать','C':'двенадцать','D':'тринадцать','E':'четырнадцать','F':'пятнадцать'}
maxim = "0"
p = 1
b = ['999999']
file = open("text.txt", "r")
marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''
def chi(n):#вывод числа словами
    for j in range(len(maxim)):
        for l in slovar:
            if str(l) == maxim[j]:
                print(slovar[l], end=' ')
                break
while True:
    a = file.readline().split()
    if not a:
        print('\nКонец файла')
        break
    for j in a:
        for x in j:
            if x in marks:
                j = j.replace(x, "")
        res = re.findall(r'[4]{1}[0]{1}[0]{1}|[1-3]?[0-9 A-F]?[0-9 A-F]{1}|[0-9]+\.[0-9]+', j)
        if len(res) == 1 and len(j) == len(res[0]) and len(j)>0:
            if int(b[-1],16) > int(res[0],16):
                if p == 1:
                    b = b[1:]
                    p -=1
                b.append(res[0])
            elif int(b[-1],16) < int(res[0],16):
                print("Последовательность:",' '.join(b),)
                maxim = b[0]
                print("Максимальное число:",end =' ')
                chi(maxim)
                print('')
                b = []
                b.append(res[0])
    print("Последовательность:",' '.join(b),) # выводим последний массив и мин число
    maxim = b[0]
    print("Максимальное число:", end=' ')
    chi(maxim)
if maxim == 0:
    print('В файле нет чисел, удовлетворяющих условию')
