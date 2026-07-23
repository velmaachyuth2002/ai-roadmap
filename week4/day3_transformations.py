import numpy as np
w1=np.random.randn(4,3)
w2=np.random.randn(3,2)
x=np.random.randn(1,4)
result_two_step= (x @ w1) @ w2
w_combined= w1 @ w2
result_one_step=x @ w_combined

print("Shapes:")
print("x:", x.shape)
print("W1:", w1.shape)
print("W2:", w2.shape)
print("x @ W1:", (x @ w1).shape)
print("(x @ W1) @ W2:", result_two_step.shape)
print("W1 @ W2:", w_combined.shape)
print("x @ W_combined:", result_one_step.shape)

print("\nTwo step result:")
print(result_two_step)

print("\nOne step result:")
print(result_one_step)

print("\nAre they equal?")
print(np.allclose(result_two_step, result_one_step))

def relu(v):
    return np.maximum(0,v)
relu_result = relu(x @ w1) @ w2

print("\nWith ReLU:")
print(relu_result)

print("\nWithout ReLU:")
print(result_one_step)

print("\nAre they equal after ReLU?")
print(np.allclose(relu_result, result_one_step))