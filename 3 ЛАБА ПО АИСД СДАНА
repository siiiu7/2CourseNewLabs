'''
Лабораторная работа №3
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
Для тестирования использовать не случайное заполнение, а целенаправленное.

Вариант 24
Формируется матрица F следующим образом: если в Е количество чисел, больших К в четных столбцах в области 2 больше,
чем произведение чисел в нечетных строках в области 4, то поменять в С симметрично области 1 и 4 местами, иначе С и В поменять местами несимметрично.
При этом матрица А не меняется. После чего вычисляется выражение: К*(A*F)+ K* F T .
Выводятся по мере формирования А, F и все матричные операции последовательно.

Матрица:
B C
D E

Вид матрицы:
  2
1   3
  4
'''
from random import randint
print('Введите N:', end=' ')
n = int(int(input()))
print('Введите K:', end=' ')
k = int(int(input()))
F = []
AKT = []
Ftrans = []
Proizv = []
Sum = []
kol = 0
proiz = 1
chek = 0
fji = 0
for i in range(n):#заполнение матриц для дальнешей работы с ними
    F.append([0]*n)
    AKT.append([0]*n)
    Ftrans.append([0]*n)
    Proizv.append([0] * n)
    Sum.append([0] * n)
print('Основная матрица:')
for i in range(len(F)):
    for j in range(len(F)):
        F[i][j] = randint(-10,10)
        print("{:4d}".format(F[i][j]), end = "")
    print()
print()
A = F
if (n//2) % 2 != 0:#проверка на то что матрица и подматрица нечётны
    chek+=1
    for i in range(n//2+1,n//4 + n//2+2):
        for j in range(n//2+1,n//4 + n//2+2):
            if i <= j and j % 2== 0 and F[i][j]>k and F[i][n//2 - j] > k:
                    kol += 1
    for i in range(n//4 + n//2,n):
        for j in range(n//4 + n//2,n):
            if i >= j and j != j - n//4:
                proiz = proiz *F[i][j]*F[i][n//4 - j]
            elif i >= j and j == n//4 - j:
                proiz *= F[i][j]
elif (n//2) % 2 == 0:
    for i in range(n//2,n//4 + n//2):
        for j in range(n//2,n//4 + n//2):
            if i <= j and j % 2== 0 and F[i][j]>k and F[i][n//2 -1 - j] > k:
                kol += 1
    for i in range(n//4 + n//2,n):
        for j in range(n//4 + n//2,n):
            if i >= j and j != j - n // 4:
                proiz = proiz * F[i][j] * F[i][n//4+2 - j]
            elif i >= j and j == n//4+2 - j:
                proiz *= F[i][j]
if kol > proiz:
    for i in range(0,n//2):
        for j in range(n//2+1,n):
            if i >= (j-n//2-1):
                F[i][j],F[n - j-1][n -i-1] = F[n - j-1][n -i-1],F[i][j]
if kol <= proiz:
    for i in range(0,n//2):
        for j in range(0,n//2):
            F[i][j], F[i][j+n//2] = F[i][j+n//2],F[i][j]
print('')
print('Преобразованная матрица:')
for i in range(len(F)):
    for j in range(len(F)):
        print("{:4d}".format(F[i][j]), end = "")
    print()
print()
print('A*F:')
for mad1 in range(n):
    for mad2 in range(n):
        for mad3 in range(n):
            fji = fji + (A[mad1][mad3] * F[mad3][mad2])
        Proizv[mad1][mad2] = fji
        fji = 0
for i in range(len(F)):
    for j in range(len(F)):
        print("{:4d}".format(Proizv[i][j]), end="")
    print()
print()
print('K*(A*F):')
for i in range(len(F)):
    for j in range(len(F)):
        AKT[i][j] = k * Proizv[i][j]
        print("{:4d}".format(AKT[i][j]), end = "")
    print()
print()
print("K * F транспонированная:")
for i in range(len(F)):
    for j in range(len(F)):
        Ftrans[i][j] = k * F[j][i]
        print("{:4d}".format(Ftrans[i][j]), end="")
    print()
print()ф
print("К*(A*F)+ K* F транспонированная:")
for i in range(len(F)):
    for j in range(len(F)):
        Sum[i][j] = AKT[i][j] + Ftrans[i][j]
        print("{:4d}".format(Sum[i][j]), end="")
    print()
print()
