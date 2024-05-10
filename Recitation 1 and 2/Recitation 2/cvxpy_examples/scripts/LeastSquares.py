import numpy as np
import cvxpy as cvx

# LS problem: minimize ||Ax - b||_2^2 , A is n x m matrix, b is n x 1 vector

# Problem Setup
n = 10
m = 5

A = np.random.normal(0, 1, (n, m))
b = np.random.normal(0, 1, (n,)) 


# Solving the problem
x = cvx.Variable(m)

objective = cvx.Minimize(cvx.sum_squares(A @ x - b))
constraints = []

prob = cvx.Problem(objective, constraints)
prob.solve()
print(prob.status)
print("Optimal value", prob.value)
print("Optimal solution", x.value)