import numpy as np
import matplotlib.pyplot as plt

"""
    task 1
"""
def plus_sin(x):
    return np.sin(0.2 * np.pi * x)
def minus_sin(x):
    return - plus_sin(x)

def main():
    x = np.arange(0, 10.1, 0.1)
    pos_y = plus_sin(x)
    neg_y = minus_sin(x)

    plt.plot(x, pos_y, label='$y = \sin(0.2\pi x)$')
    plt.plot(x, neg_y, label='$y = -\sin(0.2\pi x)$')

    plt.xlim([-10, 10])
    plt.ylim([-10, 10])

    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Графики $y = \sin(0.2\pi x)$ и $y = -\sin(0.2\pi x)$')
    
    plt.show()


if __name__ == '__main__':
    main()

