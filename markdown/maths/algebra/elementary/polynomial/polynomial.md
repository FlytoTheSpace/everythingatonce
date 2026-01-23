# Polynomials

Polynomials are of form:

$$
P(x) = \sum_{k=0}^na_kx^k \newline
= a_0 + a_1x + a_2x^2 + a_3x^3 + a_4x^4 + a_5x^5 + a_6x^6 + ...
$$

The value $n$ is called the Degree of the Polynomial, long as $a_n \neq 0$ 

$a_0^{0}$ is taken as $1$ for notational purpose.

### Term Count

The Number of terms in a polynomial with a unique power to each other of $x$ is called are following:

- Monomial

    $$ax^p$$

- Binomial

    $$ax^p + bx^q$$

- Trinomial

    $$ax^p + bx^q + cx^r$$

...

## Polynomial Based Theorems

### Theorem 1

Every $n$'th degree polynomial can be expressed as the following

$$
\sum_{k=0}^na_kx^k = a_n \prod_{i = 1}^{n}(x + r_i)
$$

$$
a_n x^n + a_{n - 1} x^{n - 1} + ...  + a_{2} x^{2} + a_{1} x^{1} + a_0 = a_n(x + r_n)(x + r_{n - 1})...(x + r_2)(x + r_1)
$$

### Remainder Theorem

$$D(x) = x + a$$
$$P(x) = D(x)\ Q(x) + R(x)$$

$R(x)$ degree < $D(x)$ $\therefore R(x) = r$

$$P(x) = D(x)\ Q(x) + r$$

$$
P(x) = (x + a)\ Q(x) + r \newline
P(- a) = ((-a) + a)\ Q(-a) + r \newline
P(- a) = r \newline
$$

$$
P(- a) = r \newline
$$

### Factor Theorem

$$(x + a)\ |\ P(x) \iff P(- a) = 0$$

## Roots of Polynomials

Roots of Polynomials are values of `x` such that the following is true:

$$
P(a) = 0
$$

graphically, they are the `X` cordinate of the point where the Graph of the Polynomials intersects the X axis


## Types:

### Zero Polynomial

where the polynomials doesn't consits of any terms

$\forall x$

$$
P(x) = 0 
$$

all possible values of x are roots of this polynomils, degree is `undefined`

### Constant Polynomial

where the polynomials only consists of a Constant Term

$$
P(x) = a
$$

no root of this type of polynomials exists (unless $a = 0$), and the degree is `0`

### Linear

where the degree of the polynomials is `1`


$$
P(x) = ax + b
$$

roots of this type of polynomial can be found by:

$
P(x) = 0\newline
ax + b = 0\newline
x = -b/a \newline
$

$$
x = -\frac{b}{a}
$$

longs as $(a \neq 0) \newline$

### Quadratic

[`quadratic.md`](./quadratic.md)

### Cubic

[`cubic.md`](./cubic.md)

### Quartic

[`quartic.md`](./quartic.md)

# Multivariable Polynomials

They are of the form:

$$P(x, y, z, ...) = \LARGE \sum_{\footnotesize i = 0}^{\footnotesize n} \left(\sum_{\footnotesize k_1 + k_2 + k_3 + ... = i} \normalsize a_{k_1,k_2,k_3, ...} x^{k_1} y^{k_2} z^{k_3} ...\right)$$


## Multilinear Polynomial

$$P(x, y, z, ...) = a_{0,0,0,0}+\LARGE \left(\sum_{\footnotesize k_1 + k_2 + k_3 + ... = 1} \normalsize a_{k_1,k_2,k_3, ...} x^{k_1} y^{k_2} z^{k_3} ...\right)$$

when written properly where $N$ is the count of variables:

$$
P(x_1, x_2, x_3, ..., x_N) = a_{0} + \sum_{i = 1}^{N} a_i x_i
$$

**System of Linear Equations** are when multiple Multilinear Polynomial equations are given like the following:

$$
\begin{cases}
P(x_1, x_2, x_3, ..., x_N) = 0 \newline
G(x_1, x_2, x_3, ..., x_N) = 0 \newline
H(x_1, x_2, x_3, ..., x_N) = 0 \newline
...
\end{cases}
$$

Solutions to these:
- [`Systems of Linear Equations`](./linear_equations.md)

