from numpy import arange, array, diag, fliplr, trace, unravel_index


def bubble_sort(lst):
    """
    Ця функція сортує заданий список методом бульбашки.
    :param lst: список
    :return: повертається відсортований список
    :rtype: list
    """
    for num in range(len(lst) - 1, 0, -1):
        for j in range(num):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


def swap_max_min(lst):
    """
    Ця функція замінює місцями максимальний та мінімальний елемент списку, поданого у вигляді квадратної матриці.
    Функція unravel_index() перетворює індекси або масив індексів на кортеж координат цих індексів.
    Функція shape() повертає розмірність матриці (масиву) у вигляді кортежу.
    :param lst: список
    :return: повертається матриця (масив) з поміняними місцями макс. та мін. елементами
    :rtype: array
    """
    square_matrix = array(lst)  # Перетворюємо список у матрицю numpy

    max_pos = unravel_index(square_matrix.argmax(), square_matrix.shape)  # Знаходимо позицію максимального елемента
    min_pos = unravel_index(square_matrix.argmin(), square_matrix.shape)  # Знаходимо позицію мінімального елемента

    # Замінюємо місцями максимальний та мінімальний та елементи
    square_matrix[max_pos], square_matrix[min_pos] = square_matrix[min_pos], square_matrix[max_pos]

    return square_matrix


def sum_diag_elem(lst):
    """
    Ця функція обчислює суму діагональних елементів та повертає її у вигляді цілого числа.
    :param lst: список
    :return: повертається сума діагональних елементів
    :rtype: int
    """
    square_matrix = array(lst)

    return int(square_matrix.trace() + trace(fliplr(square_matrix)))


def swap_diagonals(lst):
    """
    Ця функція міняє місцями головну та побічну діагоналі матриці (масиву) та повертає її.
    :param lst: список
    :return: повертається матриця (масив) з поміняними місцями діагоналями
    :rtype: array
    """
    square_matrix = array(lst)

    n = len(square_matrix)  # Розмірність матриці
    for i in range(n):
        square_matrix[i][i], square_matrix[i][n - i - 1] = square_matrix[i][n - i - 1], square_matrix[i][i]

    return square_matrix


def swap_rows(lst):
    """
    Ця функція міняє місцями перший і останній рядок матриці.
    :param lst: список
    :return: повертається матриця (масив) з поміняними місцями першим і останнім рядками
    :rtype: array
    """
    square_matrix = array(lst)
    square_matrix[0], square_matrix[-1] = square_matrix[-1], square_matrix[0]

    return square_matrix


def swap_cols(lst):
    """
    Ця функція міняє місцями перший і останній стовпець матриці.
    :param lst: список
    :return: повертається матриця (масив) з поміняними місцями першим і останнім стовпцями
    :rtype: array
    """
    square_matrix = array(lst)
    square_matrix[:, [0, -1]] = square_matrix[:, [-1, 0]]

    return fliplr(square_matrix)


def search_max(lst):
    """
    Ця функція визначає позицію максимального елемента матриці та повертає її у вигляді кортежу.
    :param lst: список
    :return: повертаються координати максимального елемента у вигляді кортежу
    :rtype: tuple
    """
    square_matrix = array(lst)
    max_pos = unravel_index(square_matrix.argmax(), square_matrix.shape)  # Знаходимо позицію максимального елемента

    return max_pos


def search_min(lst):
    """
    Ця функція визначає позицію мінімального елемента матриці та повертає її у вигляді кортежу.
    :param lst: список
    :return: повертаються координати мінімального елемента у вигляді кортежу
    :rtype: tuple
    """
    square_matrix = array(lst)
    min_pos = unravel_index(square_matrix.argmin(), square_matrix.shape)  # Знаходимо позицію мінімального елемента

    return min_pos
