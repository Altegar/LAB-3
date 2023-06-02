# Сушинський Ігор
# Лабораторна робота №3
# Числові списки. Сортування

from funcs_module import *
from numpy import amax, array, transpose
from random import randint
from tabulate import tabulate

# Заголовки стовпців
headers = ["Задача", "Результат"]

# Завдання №1
orig_list = [randint(1, 20) for i in range(10)]
sorted_list1 = bubble_sort(orig_list)
sorted_list2 = max_value_sort(orig_list)
data1 = [
    ["Невідсортований список:", str(orig_list)],
    ["Відсортований список методом бульбашки:", sorted_list1],
    ["Невідсортований список:", str(orig_list)],
    ["Відсортований список методом максимального елемента:", sorted_list2],
    ["Перевірка сортування (невідсортований список):", str(orig_list)],
    ["Перевірка сортування (відсортований список):", sorted(orig_list)]
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
    ["Задана матриця:", array(squareMatrix)],
    ["Матриця з поміняними місцями макс. та мін. елементами:", swap_max_min(squareMatrix)],
    ["Сума діагональних елементів:", sum_diag_elems(squareMatrix)],
    ["Матриця з поміняними місцями діагоналями:", swap_diagonals(squareMatrix)],
    ["Максимальний елемент кожного стовпця:", amax(squareMatrix, axis=0)],
    ["Матриця з поміняними місцями першим і останнім рядками:", swap_rows(squareMatrix)],
    ["Максимальний елемент кожного рядка:", amax(squareMatrix, axis=1)],
    ["Матриця з поміняними місцями першим і останнім стовпцями:", swap_cols(squareMatrix)],
    ["Транспонована матриця:", transpose(squareMatrix)],
    ["Координати максимального елемента:", search_max(squareMatrix)],
    ["Координати мінімального елемента:", search_min(squareMatrix)]
]

table = tabulate(data2, headers, tablefmt="fancy_grid")
print(table)
