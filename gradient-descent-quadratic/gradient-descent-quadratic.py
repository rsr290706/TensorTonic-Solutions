def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    for _ in range(steps):
        fdx = 2*a*x0 + b
        x = x0 - (lr * fdx)
        x0 = x

    return x