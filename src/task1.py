import numpy as np

def main():
    run_tests()

def run_tests():
    assert task_1_var_1([-6, -4, 0, 3, 5, 6]) == 4
    assert task_1_var_1([0, -3, -5, 5, 7, 8]) == -3
    assert task_1_var_1([10, 4, 3, -3, -10]) == 4

def task_1_var_1(array):
    """
    Найдите сумму элементов заданного массива, находящихся в диапазоне значений [-5, 5].
    """
    result = 0
    for x in array:
        if -5 <= x <= 5:
            result += x
    return result

if __name__ == "__main__":
    main()
