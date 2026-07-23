def gradient_descent(start_x, lr, steps):
    x = start_x

    print(f"\nMinimizing f(x) = x²")
    print(f"Start={start_x}, Learning Rate={lr}")

    for step in range(1, steps + 1):
        grad = 2 * x
        x = x - lr * grad
        loss = x ** 2

        print(f"Step {step} | x = {x} | f(x) = {loss}")


def gradient_descent_shifted(start_x, lr, steps):
    x = start_x

    print(f"\nMinimizing f(x) = (x-3)²")
    print(f"Start={start_x}, Learning Rate={lr}")

    for step in range(1, steps + 1):
        grad = 2 * (x - 3)
        x = x - lr * grad
        loss = (x - 3) ** 2

        print(f"Step {step} | x = {x} | f(x) = {loss}")


gradient_descent(5, 0.1, 20)
gradient_descent(5, 0.01, 20)
gradient_descent(5, 1.1, 20)

gradient_descent_shifted(5, 0.1, 20)