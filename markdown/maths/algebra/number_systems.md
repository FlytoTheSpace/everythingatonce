
# Bases

A way of representing Reals Numbers.
$b$ - for base, $a = a_0$

Naturals $\mathbb{N}$,

we write:
$$
a_0 = a_1 b + k_0 \newline
a_1 = a_2 b + k_1 \newline
a_2 = a_3 b + k_2 \newline
a_3 = a_4 b + k_3 \newline
... \newline
a_i = a_{i + 1} b + k_i \newline
$$

$$
a = a_1 b + k_0 \newline
a = (a_2 b + k_1) b + k_0 \newline
a = a_2 b^2 + k_1 b + k_0 \newline
a = (a_3 b + k_2) b^2 + k_1 b + k_0 \newline
a = a_3 b^3 + k_2 b^2 + k_1 b + k_0 \newline
... \newline
a = ... k_3 b^3 + k_2 b^2 + k_1 b^1 + k_0 b^0
$$

$$
a = \sum_{i = 0}^{\infty} k_i b^i
$$

$$
a_0 \bmod b = k_0 \newline
a_1 \bmod b = k_1 \newline
a_2 \bmod b = k_2 \newline
a_3 \bmod b = k_3 \newline
... \newline
a_i \bmod b = k_i \newline
$$

# Number Systems
Different Type of Number System that are used in Mathematics:

# Naturals

$$\mathbb{N} = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...\}$$

- in Detail: [`Natural Numbers`](./number_systems/naturals.md)

Summary:

$\forall a, b, c \in \mathbb{N}$ :

$$s^{a}(0) = a$$

$$s^{b}(a) = s^{a}(b)$$

$$a + b = s^{b}(a)$$

$$a + b \in \mathbb{N}$$

$$(a + b) + c = a + (b + c)$$

$$a + b = b + a$$

$$a + 0 = a$$

$$a \times b = \underbrace{(a + a + a + ...)}_{b}$$

$$a \times b \in \mathbb{N}$$
$$a \times b = b \times a$$

$$(a \times b) \times c = a \times (b \times c)$$

$$a \times 1 = a$$

$$a \times 0 = 0$$

$$a \times (b + c) = (a \times b) + (a \times c)$$

$$a < b \iff b > a$$

$$a < b \oplus a = b \oplus a > b$$

$$a < b \land b < c \implies a < c$$

$$a < b \implies a + c < b + c$$

$$a < b \implies a \times c < b \times c$$
long as $c \in \mathbb{N}_{>0}$

Notation:

$$\mathbb{N}_m = \{n\ |\ n \in \mathbb{N} \land n < m\}$$

$$\mathbb{N}_{> m} = \{n\ |\ n \in \mathbb{N} \land n > m\}$$

# Integers

$$\mathbb{Z} = \{..., -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, ...\}$$

- in Detail: [`Integers`](./number_systems/integers.md)

# Rationals

Inverse of Multiplication:

$$a \times \left(\frac{1}{a}\right) = 1$$

Rationals Axioms:

**QA1**:

$$\forall a, (b \neq 0) \in \mathbb{Z}\left[\frac{a}{b} \in \mathbb{Q}\right]$$


**QA2**: Axiom of Distributivity of inverse of multiplication over addition:

$$\forall a \neq 0, b, c \in \mathbb{Z} \left[\left(\frac{1}{a}\right) \times (b + c) = \left(\frac{1}{a}\right) \times b + \left(\frac{1}{a}\right) \times c\right]$$

Division by 1:

Inverse of Inverse:

$$
\left(\frac{1}{a}\right) \times \left(\frac{1}{\left(\frac{1}{a}\right)}\right) := 1 \newline
a \times \left(\frac{1}{a}\right) \times \left(\frac{1}{\left(\frac{1}{a}\right)}\right) = a \times 1 \newline
\left(a \times \left(\frac{1}{a}\right)\right) \times \left(\frac{1}{\left(\frac{1}{a}\right)}\right) = a \newline
1 \times \left(\frac{1}{\left(\frac{1}{a}\right)}\right) = a \newline
\left(\frac{1}{\left(\frac{1}{a}\right)}\right) = a \newline
1/(1/a) = a \newline
$$


Multiplication of Inverses:

$$
(a \times b) \times \frac{1}{(a \times b)} = 1 \newline
(a \times b) \times \frac{1}{(a \times b)} = 1 \times 1 \newline
(a \times b) \times \frac{1}{(a \times b)} = \left(a \times \left(\frac{1}{a}\right)\right) \times \left(b \times \left(\frac{1}{b}\right)\right) \newline
(a \times b) \times \frac{1}{(a \times b)} = a \times \left(\frac{1}{a}\right) \times b \times \left(\frac{1}{b}\right) \newline
(a \times b) \times \frac{1}{(a \times b)} = a \times b \times \left(\frac{1}{a}\right) \times \left(\frac{1}{b}\right) \newline
(a \times b) \times \frac{1}{(a \times b)} = (a \times b) \times \left(\frac{1}{a}\right) \times \left(\frac{1}{b}\right) \newline
\frac{1}{(a \times b)}\times (a \times b) \times \frac{1}{(a \times b)} = \frac{1}{(a \times b)}\times (a \times b) \times \left(\frac{1}{a}\right) \times \left(\frac{1}{b}\right) \newline
1 \times \frac{1}{(a \times b)} = 1 \times \left(\frac{1}{a}\right) \times \left(\frac{1}{b}\right) \newline
\frac{1}{(a \times b)} = \left(\frac{1}{a}\right) \times \left(\frac{1}{b}\right) \newline
\frac{1}{a \times b} = \frac{1}{a} \times \frac{1}{b} \newline
$$

Fraction Notation:

$$
a \times \left(\frac{1}{b}\right) = \frac{a}{b}
$$

other notations:

$$\frac{1}{a} = a^{-1} = 1/a = 1 \div a$$

Properties:


Division by 1:

$$
a/1 = a \times 1 / 1 \newline
a/1 = a \times (1 / 1) \newline
a/1 = a \times 1 \newline
a/1 = a
$$

$$
\frac{a}{b} = \frac{a}{b} \newline
\frac{a}{b} \times \frac{c}{c} = \frac{a}{b} \times \frac{c}{c} \newline
\frac{a}{b} \times (1) = a \times \frac{1}{b} \times c \times \frac{1}{c} \newline
\frac{a}{b} = (a \times c) \times \left(\frac{1}{b} \times \frac{1}{c}\right) \newline
\frac{a}{b} = (a \times c) \times \left(\frac{1}{b \times c}\right) \newline
\frac{a}{b} = (a \times c) \times \frac{1}{b \times c} \newline
\frac{a}{b} = \frac{a \times c}{b \times c} \newline
$$

Addition:

$$
\frac{a}{b} + \frac{c}{d} = \frac{a}{b} + \frac{c}{d} \newline
= \frac{a \times d}{b \times d} + \frac{c \times b}{d \times b} \newline
= \frac{ad}{bd} + \frac{bc}{bd} \newline
= ad \cdot \left(\frac{1}{bd}\right) + bc \cdot \left(\frac{1}{bd}\right) \newline
= \left(\frac{1}{bd}\right)(ad + bc) \newline
= \frac{ad + bc}{bd} \newline
$$

Multiplication:

$$
\frac{a}{b} \times \frac{c}{d} = a \times \left(\frac{1}{b}\right) \times c \times \left(\frac{1}{d}\right) \newline
= (a \times c) \times \left(\frac{1}{b}\right) \times \left(\frac{1}{d}\right)\newline
= (a \times c) \times \left(\frac{1}{b \times d}\right)\newline
= \frac{a \times c}{b \times d}\newline
= \frac{ac}{bd}\newline
$$

Multiplicative Inverse:

$$
\left(\frac{a}{b}\right) \times \left(\frac{b}{a}\right) = 1
$$

in summary:

$$
\mathbb{Q} = \left\{\frac{p}{q}\ \middle |\ p,q \in \mathbb{Z} \land q \neq 0 \right\}
$$
$$
\mathbb{Q} = \{
...-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, ...
,\frac{1}{2}, \frac{2}{2}, \frac{3}{2}, \frac{4}{2}..., \frac{1}{5}, \frac{2}{5}, \frac{3}{5},... \frac{11}{10}, ... \}
$$

Comparison:

$$\mathbb{Q}^{+} = \left\{\frac{p}{q}\ \middle |\ p, q \in \mathbb{Z}^{+} \land q \neq 0\right\}$$

$$\mathbb{Q}^{-} = \left\{-\frac{p}{q}\ \middle |\ p, q \in \mathbb{Z}^{+} \land q \neq 0\right\}$$


$$\forall a, b[a < b \iff \exist c \in \mathbb{Q}^{+}(a + c = b)]$$

$$\forall a, b[a > b \iff \exist c \in \mathbb{Q}^{+}(a = b + c)]$$

$$\forall a, b[a \leq b \iff \exist c \in \mathbb{Q}^{+}\cup\{0\}(a + c = b)]$$

$$\forall a, b[a \geq b \iff \exist c \in \mathbb{Q}^{+}\cup\{0\}(a = b + c)]$$

# Irrationals

**Irrational Numbers**: $\mathbb{Q}'$ numbers that can be represented on a number line but are not rational

e.g.
$$\sqrt{2}, \pi, e, \sqrt{5}, \sqrt{10}, ...$$

- [$\sqrt{2}$ `Irrationality Proof`](../papers/irrationality.md)

# Real Numbers

**Real Numbers**: $\mathbb{R}$ are every number that can be found on the Real-Number Line includes all Rational and Irrationals.

Axioms for Reals:

**R0**. Subset:

$$\mathbb{Q} \subset \mathbb{R}$$

**R1**:

$$\forall x \in \mathbb{R}[x + 0 = x]$$

**R2**:

$$\forall x, y \in \mathbb{R}[s(x + y) = x + s(y)]$$


**R3**:

$$\forall x \in \mathbb{R}[x \times 1 = x]$$

**R3**:

$$\forall x, y, z \in \mathbb{R}[x \times (y + z) = (x \times y) + (x \times z)]$$


**R5**. Completeness Axiom:

$$\forall A[A \subset \mathbb{R} \land A \neq \emptyset \implies (\exist u \forall x \in A (x \leq u) \implies \exist s \in \mathbb{R}(\forall x \in A (x \leq s) \land \forall u \in \mathbb{R} \forall x \in A(x \leq u \implies s \leq u)))]$$




some functions:

$$\lfloor x \rfloor = \max(\{n | n \in \mathbb{Z}, n \leq x\})$$
$$\lceil x \rceil = \begin{cases}
x \notin \mathbb{N} : \lfloor x \rfloor + 1 \cr
x \in \mathbb{N} : x
\end{cases}$$
$$\lfloor x \rceil =
\begin{cases}
x - \lfloor x \rfloor < \lceil x \rceil - x : \lfloor x \rfloor \cr
x - \lfloor x \rfloor \geq \lceil x \rceil - x : \lceil x \rceil
\end{cases}$$

# Imaginary Numbers

**Imaginary Numbers**: are real-number with the Imaginary Unit as a Coefficient

$$\Im = \{ix | x \in \mathbb{R}\}$$

$$i^2 = -1$$

# Complex Numbers

**Complex Numbers**: numbers with a Real Number Term and an Imaginary Number Term

$$
\mathbb{C} = \{x + iy | x, y \in \mathbb{R}\}
$$


## Properties:

- `0` Additive Identity for Rationals
- `1` Multiplicative Identity for Rationals

**Closure**: Describes whether if certain Arithmetic Operations can result a value outside the established number systems

| Number System    | Addition  | Subtraction  | Multiplication  | Division  |
| ---------------- | --------- | ------------ | --------------- | --------- |
| Natural/Positive | ✅        | ❌           | ✅              | ❌        |
| Negative         | ✅        | ❌           | ❌              | ❌        |
| Integers         | ✅        | ✅           | ✅              | ❌        |
| Rationals        | ✅        | ✅           | ✅              | ❌        |
| Reals            | ✅        | ✅           | ✅              | ❌        |
| Complex          | ✅        | ✅           | ✅              | ❌        |

**Commutativity**: Describes whether changing the Order of Operands in an expression, results in the same output.

$$
a + b + c = b + a + c = c + a + b ✅
$$
$$
a - b - c \neq b - a - c \neq c - a - b ❌
$$

**Associativity**: Describes whether rearranging the Paranthesis in an express, results in the same output, only applies with 3 or more operands.

$$
(a + b) + c = a + (b + c) ✅
$$
$$
(a - b) - c \neq a - (b - c) ❌
$$

**Associativity and Commutativity For**:
| Number System    | Addition | Subtraction | Multiplication | Division |
| ---------------- | -------- | ----------- | -------------- | -------- |
| Natural/Positive | ✅        | ❌           | ✅              | ❌        |
| Negative         | ✅        | ❌           | ✅              | ❌        |
| Whole            | ✅        | ❌           | ✅              | ❌        |
| Integers         | ✅        | ❌           | ✅              | ❌        |
| Rationals        | ✅        | ❌           | ✅              | ❌        |

**Distributive**: 
$$
a(b + c) = ab + ac
$$



## Other Number Types:

**Even Numbers**: Numbers that can only be represeted as a Multiple of $2$

$$
2a
$$
- These Number must always have  any of $0, 2, 4, 6, 8$ in the *one's unit digit place*

- sum of `n` count of consecutive even numbers starting from 2
$$
\sum_{k=2}^n 2k = n(n+1)
$$

**Odd Numbers**: Numbers that can't be represeted as a Multiple of $2$

$$
2a+1
$$

- sum of `n` count of consecutive odd numbers starting from 1
$$
\sum_{k=1}^n (2k-1) = n^2
$$

- These Number must always have  any of $1, 3, 5, 6, 9$ in the *one's unit digit place*

**Composite Numbers**: Numbers that doesn't have exactly 2 factors

$$
1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36...
$$

**Decimals**: Floating Point Numbers that exists in-between Numbers
$$
1.001, 1.002, 1.0000434..., ...
$$

- **Unit Digit**: number in one's place of any number

$$
a \mod 10
$$

## Prime Numbers

Numbers that can only be divided by $1$ and *itself*, having exactly 2 factors

$$
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...
$$

- Every Prime Number is an Odd-Number except `2`
- **Twin Primes**: difference between 2 Prime Number is `2`
	
	$(a+2 = b) ⟹ a, b$

	`(Note: Both Numbers Need to Prime Numbers for this to be true)`

- **Co-Prime Numbers**: 2 numbers with only 1 as a common factor.

```python
def isPrime(n):
	if n < 2: return False;
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0: return False;
	return True
```
