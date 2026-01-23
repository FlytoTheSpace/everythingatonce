
# Systems of Linear Equations

define: $x_0 = 1$

$$
\begin{cases}
\displaystyle \sum_{j = 0}^{n} a_{1,j} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n} a_{2,j} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n} a_{3,j} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n} a_{4,j} x_{j} = 0 \cr
... \cr
\displaystyle \sum_{j = 0}^{n} a_{i,j} x_{j} = 0 \cr
... \cr
\displaystyle \sum_{j = 0}^{n} a_{n,j} x_{j} = 0 \cr
\end{cases}
$$

solve for $x_n$ in each

$$
x_n 
= - \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{1,j}}{a_{1,n}} x_{j}
= - \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{2,j}}{a_{2,n}} x_{j}
= - \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{3,j}}{a_{3,n}} x_{j}
= - \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{4,j}}{a_{4,n}} x_{j}
= ...
= - \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{i,j}}{a_{i,n}} x_{j}
= ...
= - \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{n,j}}{a_{n,n}} x_{j}
$$

variable $x_n$ is now eliminated from the set of equations

$$
  \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{1,j}}{a_{1,n}} x_{j}
= \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{2,j}}{a_{2,n}} x_{j}
= \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{3,j}}{a_{3,n}} x_{j}
= \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{4,j}}{a_{4,n}} x_{j}
= ...
= \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{i,j}}{a_{i,n}} x_{j}
= ...
= \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{n,j}}{a_{n,n}} x_{j}
$$

create pairs of equations with 2 expressions from this, It will result in $n - 1$ count of set equations with $n - 1$ count of variables:

$$
\begin{cases}
\displaystyle \sum_{j = 0}^{n - 1} \frac{a_{n,j}}{a_{n,n}} x_{j} = \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{1, j}}{a_{1,n}} x_{j} \cr
\displaystyle \sum_{j = 0}^{n - 1} \frac{a_{n,j}}{a_{n,n}} x_{j} = \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{2, j}}{a_{2,n}} x_{j} \cr
\displaystyle \sum_{j = 0}^{n - 1} \frac{a_{n,j}}{a_{n,n}} x_{j} = \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{3, j}}{a_{3,n}} x_{j} \cr
\displaystyle \sum_{j = 0}^{n - 1} \frac{a_{n,j}}{a_{n,n}} x_{j} = \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{4, j}}{a_{4,n}} x_{j} \cr
... \cr
\displaystyle \sum_{j = 0}^{n - 1} \frac{a_{n,j}}{a_{n,n}} x_{j} = \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{i, j}}{a_{i,n}} x_{j} \cr
... \cr
\displaystyle \sum_{j = 0}^{n - 1} \frac{a_{n,j}}{a_{n,n}} x_{j} = \displaystyle \sum_{j = 0}^{n - 1} \frac{a_{n - 1, j}}{a_{n - 1,n}} x_{j} \cr
\end{cases}
$$

simplify:

$$
\begin{cases}
\displaystyle \sum_{j = 0}^{n - 1} \left(\frac{a_{n,j}}{a_{n,n}} - \frac{a_{1, j}}{a_{1,n}}\right) x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - 1} \left(\frac{a_{n,j}}{a_{n,n}} - \frac{a_{2, j}}{a_{2,n}}\right) x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - 1} \left(\frac{a_{n,j}}{a_{n,n}} - \frac{a_{3, j}}{a_{3,n}}\right) x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - 1} \left(\frac{a_{n,j}}{a_{n,n}} - \frac{a_{4, j}}{a_{4,n}}\right) x_{j} = 0 \cr
... \cr
\displaystyle \sum_{j = 0}^{n - 1} \left(\frac{a_{n,j}}{a_{n,n}} - \frac{a_{i, j}}{a_{i,n}}\right) x_{j} = 0 \cr
... \cr
\displaystyle \sum_{j = 0}^{n - 1} \left(\frac{a_{n,j}}{a_{n,n}} - \frac{a_{n - 1, j}}{a_{n - 1,n}}\right) x_{j} = 0 \cr
\end{cases}
$$

define:

$$
R_{i,j}^{0} = a_{i,j}
$$

$$
R_{i,j}^{1} = \frac{a_{n,j}}{a_{n,n}} - \frac{a_{i, j}}{a_{i,n}}
$$

Now Repeat:

1st Iteration:
$$
\begin{cases}
\displaystyle \sum_{j = 0}^{n - 1} R_{1, j}^{1} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - 1} R_{2, j}^{1} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - 1} R_{3, j}^{1} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - 1} R_{4, j}^{1} x_{j} = 0 \cr
... \cr
\displaystyle \sum_{j = 0}^{n - 1} R_{i, j}^{1} x_{j} = 0 \cr
... \cr
\displaystyle \sum_{j = 0}^{n - 1} R_{n - 1, j}^{1} x_{j} = 0 \cr
\end{cases}
$$

2st Iteration:

$$
R_{i,j}^{2} = \frac{R_{n - 1,j}^{1}}{R_{n - 1,n - 1}^{1}} - \frac{R_{i,j}^{1}}{R_{i, n - 1}^{1}}
$$

$$
\begin{cases}
\displaystyle \sum_{j = 0}^{n - 2} R_{1,j}^{2} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - 2} R_{2,j}^{2} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - 2} R_{3,j}^{2} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - 2} R_{4,j}^{2} x_{j} = 0 \cr
... \cr
\displaystyle \sum_{j = 0}^{n - 2} R_{i,j}^{2} x_{j} = 0 \cr
... \cr
\displaystyle \sum_{j = 0}^{n - 2} R_{n - 2,j}^{2} x_{j} = 0 \cr
\end{cases}
$$

3rd Iteration:

$$
R_{i,j}^{3} = \frac{R_{n - 2,j}^{2}}{R_{n - 2, n - 2}^{2}} - \frac{R_{i,j}^{2}}{R_{i,n - 2}^{2}}
$$

$$
\begin{cases}
\displaystyle \sum_{j = 0}^{n - 3} R_{1,j}^{3} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - 3} R_{2,j}^{3} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - 3} R_{3,j}^{3} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - 3} R_{4,j}^{3} x_{j} = 0 \cr
... \cr
\displaystyle \sum_{j = 0}^{n - 3} R_{i,j}^{3} x_{j} = 0 \cr
... \cr
\displaystyle \sum_{j = 0}^{n - 3} R_{n - 3,j}^{3} x_{j} = 0 \cr
\end{cases}
$$

`m`'th Iteration:

$$
R_{i,j}^{m} = \frac{R_{n - (m - 1), j}^{m - 1}}{R_{n - (m - 1), n - (m - 1)}^{m - 1}} - \frac{R_{i,j}^{m - 1}}{R_{i, n - (m - 1)}^{m - 1}}
$$

$$
\begin{cases}
\displaystyle \sum_{j = 0}^{n - m} R_{1,j}^{m} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - m} R_{2,j}^{m} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - m} R_{3,j}^{m} x_{j} = 0 \cr
\displaystyle \sum_{j = 0}^{n - m} R_{4,j}^{m} x_{j} = 0 \cr
... \cr
\displaystyle \sum_{j = 0}^{n - m} R_{i,j}^{m} x_{j} = 0 \cr
... \cr
\displaystyle \sum_{j = 0}^{n - m} R_{n - m,j}^{m} x_{j} = 0 \cr
\end{cases}
$$

$n - 1$ Iteration:

$$
R_{i,j}^{n - 1} = \frac{R_{2,j}^{n - 2}}{R_{2,2}^{n - 2}} - \frac{R_{i,j}^{n - 2}}{R_{i,2}^{n - 2}}
$$

$$
\begin{cases}
\displaystyle \sum_{j = 0}^{1} R_{1,j}^{n - 1} x_{j} = 0 \cr
\end{cases}
$$

solve for the final variable in a single Linear Equation:

$$
\displaystyle \sum_{j = 0}^{1} R_{1, j}^{n - 1} x_{j} = 0 \newline
R_{1, 0}^{n - 1}x_{0} + R_{1, 1}^{n - 1}x_{1} = 0 \newline
$$

> previous definition: $x_0 = 1$

$$
R_{1, 0}^{n - 1} + R_{1, 1}^{n - 1}x_{1} = 0 \newline
$$

$$
x_1 = - \frac{R_{1, 0}^{n - 1}}{R_{1, 1}^{n - 1}} \newline
$$

## Optimizing $R_{i,j}^{m}$

$$
R_{i,j}^{m} = \frac{R_{n - (m - 1), j}^{m - 1}}{R_{n - (m - 1), n - (m - 1)}^{m - 1}} - \frac{R_{i,j}^{m - 1}}{R_{i, n - (m - 1)}^{m - 1}}
$$

at any `m`'th iteration:

$$
\displaystyle \sum_{j = 0}^{n - m} R_{i,j}^{m} x_{j} = 0 \newline
\displaystyle \sum_{j = 0}^{n - m} \left(\frac{R_{n - (m - 1), j}^{m - 1}}{R_{n - (m - 1), n - (m - 1)}^{m - 1}} - \frac{R_{i,j}^{m - 1}}{R_{i, n - (m - 1)}^{m - 1}}\right) x_{j} = 0 \newline
\displaystyle \sum_{j = 0}^{n - m} \left(\frac{R_{n - (m - 1), j}^{m - 1}}{R_{n - (m - 1), n - (m - 1)}^{m - 1}}\right) x_{j} = \displaystyle \sum_{j = 0}^{n - m} \left(\frac{R_{i,j}^{m - 1}}{R_{i, n - (m - 1)}^{m - 1}}\right) x_{j} \newline
\displaystyle \sum_{j = 0}^{n - m} \left(R_{n - (m - 1), j}^{m - 1}\right)\left(R_{i, n - (m - 1)}^{m - 1}\right) x_{j} = \displaystyle \sum_{j = 0}^{n - m} \left(R_{i,j}^{m - 1}\right)\left(R_{n - (m - 1), n - (m - 1)}^{m - 1}\right) x_{j} \newline
\displaystyle \sum_{j = 0}^{n - m} \left(R_{i, n - (m - 1)}^{m - 1} R_{n - (m - 1), j}^{m - 1}\right) x_{j} = \displaystyle \sum_{j = 0}^{n - m} \left(R_{i,j}^{m - 1} R_{n - (m - 1), n - (m - 1)}^{m - 1}\right) x_{j} \newline
\displaystyle \sum_{j = 0}^{n - m} \left(R_{i, n - (m - 1)}^{m - 1} R_{n - (m - 1), j}^{m - 1} - R_{i,j}^{m - 1} R_{n - (m - 1), n - (m - 1)}^{m - 1}\right) x_{j} = 0 \newline


$$
now define a new $A$ in place of $R$ so we get:

$$
A_{i,j}^{0} = a_{ij}
$$
$$
A_{i,j}^{m} = A_{i,n - (m - 1)}^{m - 1} A_{n - (m - 1), j}^{m - 1} - A_{i,j}^{m - 1} A_{n - (m - 1), n - (m - 1)}^{m - 1} \newline
$$

$$
\displaystyle \sum_{j = 0}^{n - m} R_{i, j}^{m} x_{j} = \displaystyle \sum_{j = 0}^{n - m} A_{i, j}^{m} x_{j} = 0
$$

now it involves no division, which is known for it's slowness in computations

## Solutions

Coefficients:

$$
A_{i,j}^{0} = a_{i,j}
$$

$$
A_{i,j}^{m} = A_{i,n - (m - 1)}^{m - 1} A_{n - (m - 1), j}^{m - 1} - A_{i,j}^{m - 1} A_{n - (m - 1), n - (m - 1)}^{m - 1} \newline
$$

first solution:

$$
x_1 = - \frac{A_{1,0}^{n - 1}}{A_{1,1}^{n - 1}} \newline
$$

other solutions:
$$
x_k = - \frac{1}{A_{i, k}^{n - k}} \displaystyle \sum_{j = 0}^{k - 1} A_{i, j}^{n - k} x_{j}
$$

- $1 \leq i \leq k$

## Program

now as a final thing let's program this, we'll do it in python:

```python
def LinearEquations(a0: list[list[float]]):
    # check dimensions
    n = len(a0)
    if (n != (len(a0[0]) - 1)):
        return
    
    # compute coefficients:

    A = [a0]
    for m in range(1, n):
        pm = m - 1
        A.append([])
        for i in range(0, n - m):
            A[m].append([])
            for j in range(0, n - pm):
                acur = (A[pm][i][n - pm] * A[pm][n - pm - 1][j]) - (A[pm][i][j] * A[pm][n - pm - 1][n - pm])
                A[m][i].append(acur)

    x: list[float] = [1]

    # solution computation:
    for k in range(1, n + 1):  
        xk = 0
        nnk = n - k
        i;
        # search for an i value where it's coefficient is non-zero.
        for eq in range(0, k):
            if A[nnk][eq][k] == 0:
                continue
            i = eq
        if i == None:
            print("Overdetermined system")
            return
        # compute the solution:
        for j in range(0, k):
            xk += A[nnk][i][j] * x[j]
        xk = - xk / A[nnk][i][k]

        x.append(xk)
    return x


def checkSolutions(a0: list[list[float]], x: list[float]):
    # check dimensions
    n = len(a0)
    if (n != (len(a0[0]) - 1)):
        return
    
    # check solutions:

    print(a0)
    print(x)
    for i in range(0, n):
        sum = 0
        for j in range(0, n + 1):
            sum += a0[i][j] * x[j]
        if sum == 0:
            print(f"{i} [✅] Correct Solution")
            continue
        print(f"{i} [❌] Incorrect Solution")


a0 = [
    [-5,  2, 3], # -5 +  2x + 3y = 0
    [-3, 10, 4], # -3 + 10x + 3y = 0
]

checkSolutions(a0, LinearEquations(a0))
# Output:
# [[-5, 2, 3], [-3, 10, 4]]
# [1, -0.5, 2.0]
# 0 [✅] Correct Solution
# 1 [✅] Correct Solution
```
