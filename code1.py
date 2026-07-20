x = 4
y = 15

W = 2
b = 1

learning_rate = 0.1

y_hat = W * x + b

loss = 0.5 * (y - y_hat) ** 2

dL_dyhat = y_hat - y
dL_dW = dL_dyhat * x
dL_db = dL_dyhat

W_new = W - learning_rate * dL_dW
b_new = b - learning_rate * dL_db

print("Predicted Output (y_hat):", y_hat)
print("Loss:", loss)
print("dL/dW:", dL_dW)
print("dL/db:", dL_db)
print("Updated Weight:", W_new)
print("Updated Bias:", b_new)