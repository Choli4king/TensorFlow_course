import numpy as np
import matplotlib as plt

def f(x):
    return 0.5 * x +0.25

def L(a, b, x, t):
    sum_loss = 0
    for x_point, t_point in zip(x, t):
        prediction = a* x_point + b
        sum_loss += (prediction - t_point)

    return sum_loss    

def main():
    x = np.linespace()
    y = f(x)

    noise = np.random.normal(loc=0, scale=0.25, size=(N,))

    y_noise = y + noise
    print(y, y_noise)

    plt.scatter(x, y, label="target")
    plt.scatter(x, y, label="target")
    plt.legend()
    #plt.show()