# Сушинський Ігор
# Лабораторна робота №3
# Числові списки. Сортування

import funcs_module as fm
from numpy import amax, matrix, transpose
from random import randint
from tabulate import tabulate

# Заголовки стовпців
headers = ["Задача", "Результат"]

# Завдання №1
myList = [randint(1, 20) for i in range(10)]
myListTest = [randint(1, 20) for j in range(10)]
data1 = [
    ["Невідсортований список:", str(myList)],
    ["Максимальний елемент списку:", max(myList)],
    ["Відсортований список:", fm.bubble_sort(myList)],
    ["Перевірка сортування:", sorted(myListTest)]
]

table = tabulate(data1, headers, tablefmt="fancy_grid")
print(table)

# Завдання №2
squareMatrix = [
    [4, 7, 2],
    [1, 9, 5],
    [6, 3, 8]
]
data2 = [
    ["Задана матриця:", matrix(squareMatrix)],
    ["Матриця з поміняними місцями макс. та мін. елементами:", fm.swap_max_min(squareMatrix)],
    ["Сума діагональних елементів:", fm.sum_diag_elem(squareMatrix)],
    ["Матриця з поміняними місцями діагоналями:", fm.swap_diagonals(squareMatrix)],
    ["Максимальний елемент кожного стовпця:", amax(squareMatrix, axis=0)],
    ["Матриця з поміняними місцями першим і останнім рядками:", fm.swap_rows(squareMatrix)],
    ["Максимальний елемент кожного рядка:", amax(squareMatrix, axis=1)],
    ["Матриця з поміняними місцями першим і останнім стовпцями:", fm.swap_cols(squareMatrix)],
    ["Транспонована матриця:", transpose(squareMatrix)],
    ["Координати максимального елемента:", fm.search_max(squareMatrix)],
    ["Координати мінімального елемента:", fm.search_min(squareMatrix)]
]

table = tabulate(data2, headers, tablefmt="fancy_grid")
print(table)
