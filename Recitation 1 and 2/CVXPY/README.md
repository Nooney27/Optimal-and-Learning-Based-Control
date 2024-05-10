# Least Squares Problem

## Problem Statement

The objective is to find the vector \(x\) that minimizes the Euclidean norm of the residual vector \( Ax - b \):

$$ \min_{x \in \mathbb{R}^m} \|Ax - b\|_2^2 $$


# Discrete LQR Problem

## Problem Statement

The objective is to minimize the cost function over a finite horizon \( T \):

$$
\min_{u \in \mathbb{R}^T} \left( \frac{1}{2} x_T^\top Q_T x_T + \frac{1}{2} \sum_{t=0}^{T-1} \left( x_t^\top Q x_t + u_t^\top R u_t \right) \right)
$$

## Subject to

-  x_{t+1} = A x_t + B u_t  for all  0 <= t <= T - 1 
-  x_0 = {initial condition} 


# CVXPY Examples

This repo was created to help teach `cvxpy` in AA203: Optimal and Learning-based Control

For the course website, see https://stanfordasl.github.io/aa203

More examples may be added in the future

## Usage

```
git clone https://github.com/danielpmorton/cvxpy_examples
cd cvxpy_examples
pip install -e .
```

I recommend working inside a virtual environment. I'm using Python 3.10.8, for reference.
