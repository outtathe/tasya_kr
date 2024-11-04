import numpy as np

def main():
    run_tests()

def run_tests():
    """
    Тесты для задания 1
    """
    assert task_1_var_1([-6, -4, 0, 3, 5, 6]) == 4
    assert task_1_var_1([0, -3, -5, 5, 7, 8]) == -3
    assert task_1_var_1([10, 4, 3, -3, -10]) == 4
    print("Тесты для задания 1 выполнены успешно")

    """
    Тесты для задания 2
    """
    assert task_2_var_1([[1, 2, 3], [4, 5, 6], [7, 8, -9]]) == 0
    assert task_2_var_1([[10, 3, 5], [6, -11, 8], [2, 4, -10]]) == -4
    assert task_2_var_1([[0, -3, 9], [4, -1, 6], [2, -8, 5]]) == -12
    print("Тесты для задания 2 выполнены успешно")

    """
    Тесты для задания 3
    """
    matrix1 = [[2, 3, 4], [1, 5, 6], [3, 1, 7]]
    assert np.array_equal(task_3_var_1(matrix1), [[1, 3, 4], [2, 5, 6], [3, 1, 7]])
    matrix2 = [[8, 3, 5], [4, 1, 6], [7, 2, 9]]
    assert np.array_equal(task_3_var_1(matrix2), [[4, 3, 5], [7, 1, 6], [8, 2, 9]])
    matrix3 = [[10, 3, 7], [6, 4, 8], [2, 5, 9]]
    assert np.array_equal(task_3_var_1(matrix3), [[2, 3, 7], [6, 4, 8], [10, 5, 9]])
    print("Тесты для задания 3 выполнены успешно")

    """
    Тесты для задания 4
    """
    matrix4 = [[3, 1, 2], [7, 5, 6], [9, 8, 4]]
    assert np.array_equal(task_4_var_1(matrix4), [[3, 1, 2], [7, 5, 6], [9, 8, 4]])
    matrix5 = [[5, 2, 1], [9, 3, 4], [6, 8, 7]]
    assert np.array_equal(task_4_var_1(matrix5), [[5, 2, 1], [6, 8, 7], [9, 3, 4]])
    matrix6 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert np.array_equal(task_4_var_1(matrix6), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Тесты для задания 4 выполнены успешно")

def task_1_var_1(array):
    """
    Найдите сумму элементов заданного массива, находящихся в диапазоне значений [-5, 5].
    """
    result = 0
    for x in array:
        if -5 <= x <= 5:
            result += x
    return result

def task_2_var_1(matrix):
    """
    Найдите сумму элементов столбца заданного массива, содержащего минимальный элемент.
    """
    min_value = float('inf')
    min_index = -1
    for row in matrix:
        for j, value in enumerate(row):
            if value < min_value:
                min_value = value
                min_index = j

    column_sum = 0
    for row in matrix:
        column_sum += row[min_index]

    return column_sum

def task_3_var_1(matrix):
    """
    Отсортируйте по возрастанию четные столбцы заданного массива.
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for col in range(0, num_cols, 2):
        for i in range(num_rows - 1):
            for j in range(num_rows - i - 1):
                if matrix[j][col] > matrix[j + 1][col]:
                    matrix[j][col], matrix[j + 1][col] = matrix[j + 1][col], matrix[j][col]

    return matrix

def task_4_var_1(matrix):
    """
    Отсортируйте по возрастанию четные столбцы заданного массива.
    """
    n = len(matrix)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if max(matrix[j]) > max(matrix[j + 1]):
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]
    return matrix

if __name__ == "__main__":
    main()
