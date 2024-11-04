import numpy as np

def main():
    run_tests()

def run_tests():
    matrix4 = [[3, 1, 2], [7, 5, 6], [9, 8, 4]]
    assert np.array_equal(variant_1(matrix4), [[3, 1, 2], [7, 5, 6], [9, 8, 4]])
    matrix5 = [[5, 2, 1], [9, 3, 4], [6, 8, 7]]
    assert np.array_equal(variant_1(matrix5), [[5, 2, 1], [6, 8, 7], [9, 3, 4]])
    matrix6 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert np.array_equal(variant_1(matrix6), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    
def variant_1(matrix):
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
