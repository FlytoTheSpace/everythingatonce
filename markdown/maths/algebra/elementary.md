# Elementary Algebra

The Fundamentals of Algebra and common formula's

# Axioms:

These are some axioms which are built up on and often used throughout this library

$\forall a, b$

1. **Predictability**: functions `f` always return the same output given the same input:
$$
f(a) = f(a)
$$
some obvious exceptions are `random()`, `time()` etc. but they don't belong here.

2. **Subtitutivity**: if `a` satisfies some condition `C` and `b` is equal to `a` then `b` also satisfies that condition
$$
(a = b) \implies (C(a) \iff C(b))
$$
3. **Equality Preservation**: if $a = b$ then performing some operation $f$ on both sides, yields a true statement.
$$
a = b\newline
\implies f(a) = f(b)
$$
4. **Inverse**: for bijective functions, operations and can be cancelled by their inverses
$$
\exists!a(f(a) = y) \newline
\implies f^{-1}(f(a)) = f(f^{-1}(a)) = a
$$
5. **Identity**: there exists a value such that it essentially does "nothing" under some operation
$$
\exists e (a \circ e = e \circ a = a)
$$

## Common Notion

These are simple commonly accepted facts that arise from addition and multiplication, not being basic or general enough to be axioms and not complex enough to be full blown theorems. also includes names and intrepretation of expressions

### Additon:

- **Closure**:
depends on The Group (mostly `yes`)
- **Associativity**:
$$ (a + b) + c = a + (b + c) $$
- **Identity (Neutral)** `0`:
$$ a + 0 = 0 + a = a $$
- **Inverse**:
$$ a + (-a) = a - a = 0 $$
- **Communicativity (Abelian)**:
$$ a + b = b + a $$

### Multiplication:

- **Closure**:
depends on The Group (mostly `yes`)
- **Associativity**:
$$ (ab)c = a(bc) $$
- **Identity (Neutral)** `1`:
$$ a \cdot 1 = 1 \cdot a = a $$
- **Inverse**:
$$ a \cdot \left(\frac{1}{a}\right) = \frac{a}{a} = 1 $$
- **Communicativity (Abelian)**:
$$ ab = ba $$

- **Distributive Property** (Addition and Multiplication):
$$ a(b + c) = ab + ac $$


### Terminology

**Constant**: a Number with a Fixed Value

**Components**:
- **Equation**: A Statement with atleast 2 Expressions divided by an Equality Sign

$\color{MediumSeaGreen}4x^2 - 3xy = \color{MediumSeaGreen}6x^2 - 2x^2 - 3xy$

- **Expression**: contains all the terms and operands

	$\color{MediumSeaGreen}4x^2 - 3xy$

- **Terms**: Parts that needs to be solved independently
	
	$\color{MediumSeaGreen}{4x^2} \color{white}{ - } \color{MediumSeaGreen}{3xy}$ 

	- **Like Terms**: when Algebraic Factors of 2 terms are the same
	- **Unlike Terms**: when Algebraic Factors of 2 terms are not the same

- **Factors**: all of the individual factors of the expression

	$(\color{MediumSeaGreen}4 \color{white}\times \color{MediumSeaGreen}x \color{white}\times \color{MediumSeaGreen}x\color{white}) - (\color{MediumSeaGreen}3 \color{white}\times \color{MediumSeaGreen}x \color{white}\times \color{MediumSeaGreen}y\color{white})$ 
- **Coefficient**: The Other Factors in the Same Term

	- **Numerical Coefficients/Factors**: Constants in a term

		$\color{MediumSeaGreen}3\color{white}xy$ 

	- **Algebraic Coefficients/Factors**: Algebraic variables in a term

		$3\color{MediumSeaGreen}xy\color{white}$ 


# Polynomials

Polynomials are of form:

$$
P(x) = a_0 +\sum_{k=1}^na_kx^k \newline
= a_0 + a_1x + a_2x^2 + a_3x^3 + a_4x^4 + a_5x^5 + a_6x^6 + ...
$$

The value `n` is called the Degree of the Polynomial, long as $a_n \neq 0$ 

## Roots of Polynomials

Roots of Polynomials are values of `x` such that the following is true:

$$
P(a) = 0
$$

graphically, they are the `X` cordinate of the point where the Graph of the Polynomials intersects the X axis


## Polynomial Types:

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

no root of this type of polynomials exists, and the degree is `0`

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

[`quadratic.md`](./elementary/quadratic.md)

### Cubic

[`cubic.md`](./elementary/cubic.md)

### Quartic

[`quartic.md`](./elementary/quartic.md)

# Binomial Theorem

The Standard Binomial Theorem Implies that:

> $n \in \mathbb{Z}^+$
$$(a + b)^n = \sum_{k = 0}^n \begin{pmatrix}n\cr k\end{pmatrix}a^{n-k}b^k$$


### Pascal's Triangle:

`n` is the Row
`k` is the Column
|       | `0`   | `1`   | `2`   | `3`   | `4`   | `5`   | `6`   | `7`   | `8`   | `9`   | `10`  | `...` |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ---- |
| `0`   | $1$   |       |       |       |       |       |       |       |       |       |       |      |
| `1`   | $1$   | $1$   |       |       |       |       |       |       |       |       |       |      |
| `2`   | $1$   | $2$   | $1$   |       |       |       |       |       |       |       |       |      |
| `3`   | $1$   | $3$   | $3$   | $1$   |       |       |       |       |       |       |       |      |
| `4`   | $1$   | $4$   | $6$   | $4$   | $1$   |       |       |       |       |       |       |      |
| `5`   | $1$   | $5$   | $10$  | $10$  | $5$   | $1$   |       |       |       |       |       |      |
| `6`   | $1$   | $6$   | $15$  | $20$  | $15$  | $6$   | $1$   |       |       |       |       |      |
| `7`   | $1$   | $7$   | $21$  | $35$  | $35$  | $21$  | $7$   | $1$   |       |       |       |      |
| `8`   | $1$   | $8$   | $28$  | $56$  | $70$  | $56$  | $28$  | $7$   | $1$   |       |       |      |
| `9`   | $1$   | $9$   | $36$  | $84$  | $126$ | $126$ | $84$  | $36$  | $9$   | $1$   |       |      |
| `10`  | $1$   | $10$  | $45$  | $120$ | $210$ | $252$ | $210$ | $120$ | $45$  | $10$  | $1$   |      |
| $...$ | $...$ | $...$ | $...$ | $...$ | $...$ | $...$ | $...$ | $...$ | $...$ | $...$ | $...$ | $...$ |

any entry within this can accessed by:

$$
\begin{pmatrix}n\cr k\end{pmatrix} = \frac{n!}{k!(n-k)!} = \underbrace{\frac{1}{k!}\left(\displaystyle\prod_{s=0}^{k -1}(n - s)\right)}_{n \neq \mathbb{Z}}
$$


