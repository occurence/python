import numpy as np
import matplotlib.pyplot as plt
import torch

def function(x):
    return x**4 + x**3 - 5*x**2

def optimize_and_plot(lr=0.01, momentum=0.0):
    x = torch.tensor(2.0, requires_grad=True)
    buffer = torch.zeros_like(x.data)
    values = []

    for i in range(10):
        y = function(x)
        values.append((x.clone(), y.clone()))
        y.backward()

        d_p = x.grad.data
        if momentum != 0:
            buffer.mul_(momentum).add_(d_p)
            d_p = buffer

        x.data.add_(d_p, alpha=-lr)
        x.grad.zero_()

    # Plot the function
    x_vals = np.arange(-3, 2, 0.001)
    y_vals = function(torch.tensor(x_vals)).detach().numpy()

    # Plot optimizer steps
    xs = [v[0].detach().item() for v in values]
    ys = [v[1].detach().item() for v in values]

    plt.figure(figsize=(10, 5))
    plt.plot(xs, ys, 'r-X', linewidth=2, markersize=7)
    for i in range(10):
        plt.text(xs[i] + 0.1, ys[i], f'step {i}', color='r')
    plt.plot(x_vals, y_vals, linewidth=2)
    plt.grid()
    plt.tick_params(axis='both', which='major', labelsize=12)
    plt.legend(['Optimizer steps', 'Target function'])
    plt.show()

# Try a first value for momentum
mom0 = 0.85
optimize_and_plot(momentum=mom0)