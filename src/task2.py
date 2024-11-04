import numpy as np

def main():
    run_tests()

def run_tests():
    assert task_2_var_1([[1, 2, 3], [4, 5, 6], [7, 8, -9]]) == 0
    assert task_2_var_1([[10, 3, 5], [6, -11, 8], [2, 4, -10]]) == -4
    assert task_2_var_1([[0, -3, 9], [4, -1, 6], [2, -8, 5]]) == -12
    
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


if __name__ == "__main__":
    main()
