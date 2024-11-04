import numpy as np

def main():
    run_tests()

def run_tests():
    matrix1 = [[2, 3, 4], [1, 5, 6], [3, 1, 7]]
    assert np.array_equal(variant_1(matrix1), [[1, 3, 4], [2, 5, 6], [3, 1, 7]])
    matrix2 = [[8, 3, 5], [4, 1, 6], [7, 2, 9]]
    assert np.array_equal(variant_1(matrix2), [[4, 3, 5], [7, 1, 6], [8, 2, 9]])
    matrix3 = [[10, 3, 7], [6, 4, 8], [2, 5, 9]]
    assert np.array_equal(variant_1(matrix3), [[2, 3, 7], [6, 4, 8], [10, 5, 9]])

def variant_1(matrix):
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

if __name__ == "__main__":
    main()
