from random import randint


def qsort(arr):
    n = len(arr)

    if n < 2:
        return arr

    pivot = 0  # "точка опоры"

    for i in range(1, n):
        if arr[i] <= arr[0]:
            pivot += 1
            tmp1 = arr[pivot]
            arr[pivot] = arr[i]
            arr[i] = tmp1

    tmp2 = arr[0]
    arr[0] = arr[pivot]
    arr[pivot] = tmp2

    left = qsort(arr[0:pivot])
    right = qsort(arr[pivot+1:n])

    # склеиваем две осторитрованные части с опорным эелментов
    arr = left + [arr[pivot]] + right

    return arr


M = 8
matrix = [[0 for i in range(M)] for j in range(M)]  # матрица 8х8

for i in range(M):
    for j in range(M):
        matrix[i][j] = randint(1, 100)  # заполнение случайными числами

# выбор цвета
print("""Выберите цвет клеток ("ч", если черный, иначе "б"): """)

while True:
    string = input()
    if string == "ч":
        black_cells = True
        break
    elif string == "б":
        black_cells = False
        break
    else:
        print("""Вы ввели некорректный символ.\nвведите "ч" или "б": """)

array = [0] * 32

k = 0
for i in range(M):
    for j in range(M):
        if ((i + j) % 2 == 1) == black_cells:  # если клетка указанного цвета
            array[k] = matrix[i][j]
            k += 1

sorted_arr = qsort(array)

for i in range(32):
    print(sorted_arr[i], end=" ")
