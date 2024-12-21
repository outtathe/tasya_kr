import numpy as np
import matplotlib.pyplot as plt

"""
    task 2
"""
def plus_sin(x):
    return np.sin(0.2 * np.pi * x)

def minus_sin(x):
    return - plus_sin(x)

def generate_data():
    x = np.arange(0, 10.1, 0.1)
    pos_y = plus_sin(x)
    neg_y = minus_sin(x)

    return x, pos_y, neg_y

def rotate(x_vals, y_vals, degrees):
    th = np.radians(degrees)
    R = np.array([[np.cos(th), -np.sin(th)],
                  [np.sin(th),  np.cos(th)]])
    points = np.vstack((x_vals, y_vals))
    rotated = R @ points
    return rotated[0, :], rotated[1, :]

def main():
    plt.figure(figsize=(8, 7))
    x, y_plus, y_minus = generate_data()
    x_copy = 5
    step = 360/x_copy
    for i in range(x_copy):
        angle = i * step
        x_rotated, y_rotated = rotate(x, y_plus, angle)
        x_rotated2, y_rotated2 = rotate(x, y_minus, angle)

        plt.plot(x_rotated, y_rotated)
        plt.plot(x_rotated2, y_rotated2)

    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Повернутые кривые')
    plt.show()

if __name__ == '__main__':
    main()

