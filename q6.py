import numpy as np
from scipy.linalg import solve

# Coefficients of x and y
A = np.array([[2, 1],
              [1, -1]])

# Right-hand side values
B = np.array([10, 2])

# Solve equations
result = solve(A, B)

print("x =", result[0])
print("y =", result[1])
