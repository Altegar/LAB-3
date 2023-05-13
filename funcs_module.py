from numpy import array, fliplr, ndarray, trace, unravel_index


def bubble_sort(lst: list) -> list:
    """
    Сортує переданий список методом бульбашки на місці.

    Parameters:
    -----------
        lst (list): список

    Returns:
    --------
        list: новий відсортований список

    Examples:
    ---------
    >>> fm.bubble_sort([6, 4, 1, 3, 8, 5, 2, 7, 9])
    [1, 2, 3, 5, 6, 7, 8, 9]
    """
    new_lst = lst[:]
    for num in range(len(new_lst) - 1, 0, -1):
        for j in range(num):
            if new_lst[j] > new_lst[j + 1]:
                new_lst[j], new_lst[j + 1] = new_lst[j + 1], new_lst[j]

    return new_lst


def swap_max_min(lst: list) -> ndarray:
    """
    Міняє місцями максимальний та мінімальний елемент списку.

    Parameters:
    -----------
        lst (list): список

    Returns:
    --------
        ndarray: масив

    Examples:
    ---------
    >>> fm.swap_max_min([[4, 2], [5, 7], [1, 8]])
    [[4 2]
     [5 7]
     [8 1]]
    """
    square_matrix = array(lst)  # Перетворюємо список у масив numpy

    max_pos = unravel_index(square_matrix.argmax(), square_matrix.shape)  # Знаходимо позицію максимального елемента
    min_pos = unravel_index(square_matrix.argmin(), square_matrix.shape)  # Знаходимо позицію мінімального елемента

    # Замінюємо місцями максимальний та мінімальний та елементи
    square_matrix[max_pos], square_matrix[min_pos] = square_matrix[min_pos], square_matrix[max_pos]

    return square_matrix


def sum_diag_elems(lst: list) -> int:
    """
    Обчислює суму діагональних елементів.

    Parameters:
    -----------
        lst (list): список у вигляді квадратної матриці

    Returns:
    --------
        int: сума діагональних елементів

    Examples:
    ---------
    >>> fm.sum_diag_elems([[4, 2, 9], [5, 7, 2], [1, 8, 6]])
    34
    """
    square_matrix = array(lst)  # Перетворюємо список у масив numpy

    return square_matrix.trace() + trace(fliplr(square_matrix))


def swap_diagonals(lst: list) -> ndarray:
    """
    Міняє місцями головну та побічну діагоналі масиву (матриці).

    Parameters:
    -----------
        lst (list): список у вигляді квадратної матриці

    Returns:
    --------
        ndarray: масив з поміняними місцями діагоналями

    Examples:
    ---------
    >>> fm.swap_diagonals([[4, 2, 9], [5, 7, 2], [1, 8, 6]])
    [[9 2 4],
     [5 7 2],
     [6 8 1]]
    """
    square_matrix = array(lst)  # Перетворюємо список у масив numpy

    n = len(square_matrix)  # Розмірність матриці

    # Міняємо місцями головну та побічну діагоналі
    for i in range(n):
        square_matrix[i][i], square_matrix[i][n - i - 1] = square_matrix[i][n - i - 1], square_matrix[i][i]

    return square_matrix


def swap_rows(lst: list) -> ndarray:
    """
    Міняє місцями перший і останній рядок масиву (матриці).

    Parameters:
    -----------
        lst (list): список у вигляді матриці

    Returns:
    --------
        ndarray: масив

    Examples:
    ---------
    >>> fm.swap_rows([[4, 2, 9], [5, 7, 2], [1, 8, 6]])
    [[1 8 6],
     [5 7 2],
     [4 2 9]]
    """
    square_matrix = array(lst)  # Перетворюємо список у масив numpy

    # Міняємо місцями перший і останній рядки
    square_matrix[0], square_matrix[-1] = square_matrix[-1], square_matrix[0]

    return square_matrix


def swap_cols(lst: list) -> ndarray:
    """
    Міняє місцями перший і останній стовпець масиву (матриці).

    Parameters:
    -----------
        lst (list): список у вигляді матриці

    Returns:
    --------
        ndarray: масив

    Examples:
    ---------
    >>> fm.swap_cols([[4, 2, 9], [5, 7, 2], [1, 8, 6]])
    [[9, 2, 4],
     [2, 7, 5],
     [6, 8, 1]]
    """
    square_matrix = array(lst)  # Перетворюємо список у масив numpy

    # Міняємо місцями перший і останній стовпці
    square_matrix[:, [0, -1]] = square_matrix[:, [-1, 0]]

    return fliplr(square_matrix)


def search_max(lst: list) -> tuple:
    """
    Визначає позицію максимального елемента масиву (матриці).

    Parameters:
    -----------
        lst (list): список

    Returns:
    --------
        tuple: кортеж координат максимального елемента

    Examples:
    ---------
    >>> fm.search_max([[4, 2, 9], [5, 7, 2], [1, 8, 6]])
    (0, 2)
    """
    square_matrix = array(lst)  # Перетворюємо список у масив numpy

    max_pos = unravel_index(square_matrix.argmax(), square_matrix.shape)  # Знаходимо позицію максимального елемента

    return max_pos


def search_min(lst: list) -> tuple:
    """
    Визначає позицію мінімального елемента масиву (матриці).

    Parameters:
    -----------
        lst (list): список

    Returns:
    --------
        tuple: кортеж координат мінімального елемента

    Examples:
    ---------
    >>> fm.search_min([[4, 2, 9], [5, 7, 2], [1, 8, 6]])
    (2, 0)
    """
    square_matrix = array(lst)  # Перетворюємо список у масив numpy

    min_pos = unravel_index(square_matrix.argmin(), square_matrix.shape)  # Знаходимо позицію мінімального елемента

    return min_pos


if __name__ == "__main__":
    print("This is my module")
