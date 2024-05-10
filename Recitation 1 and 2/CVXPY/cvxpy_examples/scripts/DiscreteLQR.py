# Discrete LQR Problem: min 1/2 xT + 1/2 sum xTQx + uTRu 
# subject to x_{t+1} = Ax_t + Bu_t, x_0 = x0

# Problem Setup
import numpy as np
import cvxpy as cvx

n = 5 # state of x
m = 5 # control input u
T = 15 # time horizon
u_bound = 1.0 # bound of control input effort

Q = np.eye(n) # state deviation cost
R = 2 * np.eye(m) # control effort cost
A = np.random.normal(0, 1, (n, n))
B = np.random.normal(0, 1, (n, m))

x_0 = np.random.normal(0, 1, (n,)) # initial state

# Objective and constrains:

X = {}
U = {}
cost_terms = []
constraints = []

# iterative building of objective and constraints

for t in range(T):
    X[t] = cvx.Variable(n)
    U[t] = cvx.Variable(m)
    cost_terms.append(cvx.quad_form(X[t], Q)) # state deviation cost
    cost_terms.append(cvx.quad_form(U[t], R)) # control effort cost

    if t == 0:
        constraints.append(X[t] == x_0) # initial state constraint
    
    if t < T - 1 and t > 0:
        constraints.append(A @ X[t-1] + B @ U[t-1] == X[t]) # dynamics constraint


# Solve the problem
objective = cvx.Minimize(sum(cost_terms))
prob = cvx.Problem(objective, constraints)
prob.solve()
print(prob.status)
print("Optimal value", prob.value)
print("Optimal Control:", U[0].value)