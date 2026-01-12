# Elementary Algebra

The Fundamentals of Algebra and common formula's

- [`Axioms`](#axioms): The Foundational assumptions in elementary algebra.
- [`Algebraic Arithmetic`](#algebraic-arithmetic): Contains Fractions, Ratio, Propotionality.
- [`Sum/Product Notation`](#sum-and-product): The Sum and the Product Notation.
- [`Exponents`](#exponents): The Exponents defined (mostly discrete).
- [`Root`](#root): The Inverse of the Power, for obtaining the Base.
- [`Logarithm`](#logarithm): The Inverse of the Power, for obtaining the Exponent.
- [`Factorial`](#factorial): The Factorial Function (introductory).
- [`Polynomial`](#polynomials): The Polynomials and their solutions (upto degree `4`).
- [`Binomial Theorem`](#binomial-theorem): The Binomial Theorem and Pascal's Triangle.
- [`Systems of Linear Equations`](#systems-of-linear-equations): Solution to the Systems of Linear Equations of `n` degrees.

# Axioms:

These are some axioms which are built up on and often used throughout this archive

$\forall x$

A1. **Reflexitivity**:

$$x = x$$

A2. **Symmetry**:

$$x = y \iff y = x$$

A3. **Transitivity**:

$$x = y \land y = z \implies x = z$$

A4. **Equality Preservation**:

$$x = y \implies f(x) = f(y)$$

A5. **Identity**:

$$\exists I[I(x) = x]$$

A6. **Inverse**:

$$[x = y \iff f(x) = f(y)] \implies \exists f^{-1} [f(f^{-1}(x)) = f^{-1}(f(x)) = I(x)]$$

## Common Operations

These are simple commonly accepted facts that arise from addition and multiplication, not being basic or general enough to be axioms and not complex enough to be full blown theorems. also includes names and intrepretation of expressions

### Additon:

> **Addition Axioms**:
> $$\exists 0 \in \mathbb{N}[a + 0 = a]$$
> $$s(a + b) = a + s(b)$$

from those, the following properties can be established:

- **Closure**:
depends on The Group (mostly `yes`)
- **Associativity**:
$$ (a + b) + c = a + (b + c) $$
- **Identity (Neutral)** `0`:
$$ a + 0 = 0 + a = a $$
- **Inverse**:
$$ a + (-a) = a - a = 0 $$
- **Commutativity (Abelian)**:
$$ a + b = b + a $$

### Multiplication:

> **Multiplication Axioms**:
> $$\exists 1 \in \mathbb{N}[ 1 \neq 0 \implies a \times 1 = a]$$
> $$a(b + c) = ab + ac$$

- **Closure**:
depends on The Group (mostly `yes`)
- **Associativity**:
$$ (ab)c = a(bc) $$
- **Identity (Neutral)** `1`:
$$ a \cdot 1 = 1 \cdot a = a $$
- **Inverse**:
$$ a \cdot \left(\frac{1}{a}\right) = \frac{a}{a} = 1 $$
- **Commutativity (Abelian)**:
$$ ab = ba $$

- **Distributive Property** (Addition and Multiplication):
$$ a(b + c) = ab + ac $$


## Terminology

**Constant**: a Number with a Fixed Value

**Components**:
- **Equation**: A Statement with atleast 2 Expressions divided by an Equality Sign

$\color{MediumSeaGreen}4x^2 - 3xy = \color{MediumSeaGreen}6x^2 - 2x^2 - 3xy$

- **Expression**: contains all the terms and operands

	$\color{MediumSeaGreen}4x^2 - 3xy$
a^2he expression

	$(\color{MediumSeaGreen}4 \color{white}\times \color{MediumSeaGreen}x \color{white}\times \color{MediumSeaGreen}x\color{white}) - (\color{MediumSeaGreen}3 \color{white}\times \color{MediumSeaGreen}x \color{white}\times \color{MediumSeaGreen}y\color{white})$ 
- **Coefficient**: The Other Factors in the Same Term

	- **Numerical Coefficients/Factors**: Constants in a term

		$\color{MediumSeaGreen}3\color{white}xy$ 

	- **Algebraic Coefficients/Factors**: Algebraic variables in a term

		$3\color{MediumSeaGreen}xy\color{white}$ 

# Algebraic Arithmetic

- [`Fractions`](#fractions): Algebraic variant of fractions from basic arithmetic
- [`Ratio`](#ratio): Algebraic variant of fractions from basic arithmetic
- [`Proportion`](#proportion): Algebraic variant of fractions from basic arithmetic

## Fractions

**Fractions**: Numbers that are obtained after divison between 2 numbers
$$
\frac{a}{b} = a \div b
$$

- long as $b \neq 0$
- **Numerator**: value on Top of The Fraction
- **Denomitor**: value on Bottom of The Fraction

$$
\frac{\text{Numerator}}{\text{Denomitor}}
$$

Properties:

$$
-\frac{a}{b} = \frac{-a}{b} = \frac{a}{-b}
$$
$$
\frac{a}{b} = \frac{a\times c}{b\times c} = \frac{a\div c}{b\div c}
$$

**Proper Fractions**: $a < b$

**Improper Fractions**: $a > b$

**Mixed Fractions**: A mix of an Integer and A Fraction

$$
c \frac{a}{b} = c + \frac{a}{b}
$$

- To Mixed:

$$
n \mod b = a
$$
$$
\lfloor n \div b \rfloor = c
$$
$$
\frac{n}{b} = (\lfloor n \div b \rfloor) + \frac{(n \mod b)}{b} = c \frac{a}{b}
$$
- From Mixed:
$$
c \frac{a}{b} = \frac{cb + a}{b} = \frac{n}{b}
$$

**Arithmetic Operations**:

Addition:

$$
\frac{a}{b} + \frac{c}{d} = \frac{ad}{bd} + \frac{bc}{bd} = \frac{ad + bc}{bd}
$$

Subtraction

$$
\frac{a}{b} - \frac{c}{d} = \frac{ad}{bd} - \frac{bc}{bd} = \frac{ad - bc}{bd}
$$

Multiplication

$$
\frac{a}{b} \times \frac{c}{d} = \frac{ac}{bd} = \frac{a \div d}{b \div c}
$$

Division

$$
\frac{a}{b} \div \frac{c}{d} = \frac{a \div c}{b \div d} = \frac{ad}{bc}
$$

Decimal Representation To Fraction:
> `n` is the count of digits that are repeating, `m` is the count of digits after the decimal point and before the repeating pattern, `b` is the base number that you're working in (base 10)

$$
x = \frac{b^{m + n}x - b^m x}{b^{m + n} - b^m}
$$
e.g.
$$x = 5.25\bar{1}$$

$n = 1, m = 2, b = 10$

$$
x = \frac{10^{2 + 1}x - 10^2 x}{10^{2 + 1} - 10^2} \newline
x = \frac{10^{3}(5.25\bar{1}) - 10^2 (5.25\bar{1})}{10^{3} - 10^2} \newline
x = \frac{1000(5.25\bar{1}) - 100(5.25\bar{1})}{1000 - 100} \newline
x = \frac{5251.\bar{1} - 525.\bar{1}}{900} \newline
x = \frac{4726}{900} \newline
x = \frac{2363 \cdot 2}{450 \cdot 2} \newline
x = \frac{2363}{450} \newline
$$


## Ratio

**Ratio**: Comparison of any 2 or more values, that shows the relative size of one to another (this is the same as a fraction).

$$
a \colon b
$$

Properties:
- Can only be compared with the same units
- **Equivalent Ratios**: when 2 Ratios are equivalent to one another

	$a : b = c : d$

## Proportion

**Proportion**: Property of Equality of 2 ratios

$$
y \propto x \implies \exists k[ y = k \cdot x]
$$

**Inverse Proportion**:

$$
y \propto \frac{1}{x} \implies \exists k\left[ y = \frac{k}{x}\right]
$$

# Sum and Product

## Sum Notation

The Sum Notation Denotes a consecutive summations over some bounded or unbounded range:

$$
\displaystyle \sum_{k = a}^{b} f(k) = f(a) + f(a + 1) + f(a + 2) + ... + f(b - 1) + f(b)
$$

$a, b \in \mathbb{W} \land a \leq b$

**Some Properties**:


$$
b < a \implies \displaystyle \sum_{k = a}^{b} f(k) = 0
$$

$$
\displaystyle \sum_{i = 1}^{b} a = a \cdot b
$$

$$
\sum_{i = a}^{b} c \cdot f(i) = c \sum_{i = a}^{b} f(i)
$$

$$
\sum_{i = a}^{b} f(i) = \sum_{i = a}^{c} f(i) + \sum_{i = c + 1}^{b} f(i)
$$

**Change in Index Variable**:
$$
\displaystyle \sum_{k = a}^b f(k) = \displaystyle \sum_{i = g^{-1}(a)}^{g^{-1}(b)}f(g(i))
$$

## Product Notation

The Product Notation Denotes a consecutive product over some bounded or unbounded range:

$$
\displaystyle \prod_{k = a}^{b} f(k) = f(a) \cdot f(a + 1) \cdot f(a + 2) \cdot ... \cdot f(b - 1) \cdot f(b)
$$

$a, b \in \mathbb{W} \land a \leq b$

**Some Properties**:

$$
b < a \implies \displaystyle \prod_{i = a}^{b} f(i) = 1
$$

$$
\displaystyle \prod_{i = 1}^{b} a = a^b
$$

$$
\prod_{i = a}^{b} f(i)^{n} = \left(\prod_{i = a}^{b} f(i)\right)^{n}
$$

$$
\prod_{i = a}^{b} f(i) = \left(\prod_{i = a}^{c} f(i) \right)\left( \prod_{i = c + 1}^{b} f(i) \right)
$$

**Change in Index Variable**:
$$
\displaystyle \prod_{k = a}^b f(k) = \displaystyle \prod_{i = g^{-1}(a)}^{g^{-1}(b)}f(g(i))
$$

# Exponents

**Exponentiation/Power**: A Level Above Multiplication where a Number is Multiplied by itself `n` count of times.

$$
a^n = \underbrace{a \times a ...}_{n\text{ times}}
$$
$$
\prod_{k=1}^n a = a^n
$$


**Exponent Table**:
| Base | 2     | 3      | 4        | 5         |
| ---- | ----- | ------ | -------- | --------- |
| $1$  | $1$   | $1$    | $1$      | $1$       |
| $2$  | $4$   | $8$    | $16$     | $32$      |
| $3$  | $9$   | $27$   | $81$     | $243$     |
| $4$  | $16$  | $64$   | $256$    | $1024$    |
| $5$  | $25$  | $125$  | $625$    | $3125$    |
| $6$  | $36$  | $216$  | $1296$   | $7776$    |
| $7$  | $49$  | $343$  | $2401$   | $16807$   |
| $8$  | $64$  | $516$  | $4096$   | $32768$   |
| $9$  | $81$  | $729$  | $6561$   | $59049$   |
| $10$ | $100$ | $1000$ | $10000$  | $100000$  |
| $11$ | $121$ | $1331$ | $14641$  | $161051$  |
| $12$ | $144$ | $1728$ | $20736$  | $248832$  |
| $13$ | $169$ | $2197$ | $28561$  | $371293$  |
| $14$ | $196$ | $2744$ | $38416$  | $537824$  |
| $15$ | $225$ | $3375$ | $50625$  | $759375$  |
| $16$ | $256$ | $4096$ | $65536$  | $1048576$ |
| $17$ | $289$ | $4913$ | $83521$  | $1419857$ |
| $18$ | $324$ | $5832$ | $104976$ | $1889568$ |
| $19$ | $361$ | $6859$ | $130321$ | $2476099$ |
| $20$ | $400$ | $8000$ | $160000$ | $3200000$ |

**Standard Form**: Representation of Very Large/Small Numbers using:
$$a \times 10^n$$

### Laws of Exponent


> Conditions: <br> $a \in \R, a > 0$ <br>
$b \in \R, b > 0$ <br>
$n \in \mathbb{Q}$ <br>
$m \in \mathbb{Q}$

$$
a^m \cdot a^n = a^{m+n}
$$
$$
a^m \div a^n = a^{m-n}
$$
$$
a^mb^m = (ab)^m
$$
$$
a^m \cdot b^m = (a \cdot b)^m
$$
$$
(a^m)^n = a^{mn}
$$

**Special Cases**:

$n \in \mathbb{Z}$

$$1^n = 1$$

$$(-1)^{2a} = 1$$

$$(-1)^{2a+1} = (-1)$$

$n \in \mathbb{N}$

- ***Odd Number*** to the Power of `n` will always result in an ***Odd Number***
$$(2a + 1)^n = 2\left(\sum_{k = 1}^n \begin{pmatrix}n\cr k\end{pmatrix}2^{k - 1}a^k\right) + 1$$
- **Even Number** to the Power of `n` will always result in an **Even Number**, as long as $n \neq 0$
$$(2a)^n = 2((2)^{n - 1}a^n)$$

### Square

---


**Square**: Where Numbers are Exponentiated to The Power of 2, and It create a Geometric 2 Dimentional Square
$$
a^2 = a \times a
$$

$$(a + b)^2 = a^2 + 2ab + b^2$$
$$(a - b)^2 = a^2 - 2ab + b^2$$
$$a^2 - b^2 = (a + b)(a - b)$$

**Square Numbers**/ **Perfect Square Numbers**: numbers that can be expressed as $a^2$, where $a$ is an Integer
$$
a^2 = b
$$

| Number | Square Unit Digit |
| ------ | ----------------- |
| $1, 9$ | $1$               |
| $2, 8$ | $4$               |
| $3, 7$ | $9$               |
| $4, 6$ | $6$               |
| $5$    | $5$               |

- `n` is the Count of Digits in $\sqrt{a}$, the amount of digits in the Square Root of the Number will be:
	
	$$(n = 2a) \implies \frac{n}{2}$$
	$$(n = 2a + 1) \implies \frac{n + 1}{2}$$

**Triangular Number**: where the Number can Geometrically arranged to create a Triangle

$$
a = \sum_{k=1}^n k
$$
- Sum 2 Consecutive Triangular Numbers Results in a Square number
$$
(\sum_{k=1}^n k) + (\sum_{k=1}^{n-1} k) = n^2
$$
**Odd Numbers**: sum of `n` count of consecutive odd numbers starting from 1 is $n^2$

$$
\sum_{k=1}^n (2k-1) = n^2
$$
$$
a - (\sum_{k=1}^n (2k -1)) = 0 \implies \sqrt{a} = n
$$

Square Rule of 5: any Number `a` where the Unit Digit of it is 5, then It'll follow this rule:

$$a \mod 10 = 5 \implies$$

$$a = 10k + 5$$
$$k = \frac{a - 5}{10}$$
$$a^2 = 100k(k + 1) + 25$$

**Pythagorian Triplets**:
$$
2m, m^2 - 1, m^2 + 1
$$
$$
a = 2m
$$
$$
b = m^2 - 1
$$
$$
c = m^2 + 1
$$
$$
a^2 + b^2 = c^2
$$
$$
(2m)^2 + (m^2 - 1)^2 = (m^2 + 1)^2
$$



<details>
<summary>
Patterns:
</summary>

$1^2 = 1$

$11^2 = 121$

$111^2 = 12321$

$1111^2 = 1234321$

$11111^2 = 123454321$

$...$

$7^2 = 49$

$67^2 = 4489$

$667^2 = 444889$

$6667^2 = 44448889$

$66667^2 = 4444488889$

$666667^2 = 444444888889$

$...$

$11^2 = 121$
$101^2 = 10201$
$1001^2 = 1002001$
$10001^2 = 100020001$

$...$

$11^2 = 121$

$101^2 = 10201$

$10101^2 = 102030201$

$1010101^2 = 1020304030201$

$...$

</details>

### Cube

---

**Cube**: Where Numbers are Exponentiated to The Power of 3, and It create a Geometric 3 Dimentional Cube
$$
a^3 = a \times a \times a
$$

$$(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$$
$$(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$$

$$
a^2 - b^2 = (a)(a) - (b)(b) = (a-b)(a+b)
$$
$$
a^3 - b^3 = (a)(a)(a) - (b)(b)(b) = (a-b)(a+b)^2
$$

**Cube Numbers**/ **Perfect Cube Numbers**: numbers that can be expressed as $a^3$, where $a$ is an Integer
$$
a^3 = b
$$

| Number | Cube Unit Digit |
| ------ | --------------- |
| $1, 9$ | $1$             |
| $2, 8$ | $4$             |
| $3, 7$ | $9$             |
| $4, 6$ | $6$             |
| $5$    | $5$             |

# Root

**Root**: the inverse operation of the power, it the returns the first parameter (i.e. The Base)

here's the thing, roots of exponents often don't just have 1 but many solutions if we allow our scope to include the Negative variations, Complex Numbers, Quarternions, etc, this arises from the fact that exponents are *NOT* ***Bijective***. so a *true* inverse of the exponent for the base should be one that considers all solutions.

$$ x = r^n $$

$x \in \mathbb{R}^{+}$

$$ r_1 := \sqrt[n]{x}$$

we have defined the **Principal Root** here it's made to always return a postive root for a given Positive Real Number ( $x$ ).

$$\exists ! r (r \in \mathbb{R}^{+}, r^n = x)$$

now we can define it for The Complex Plane and have many solutions.


$$
z = r_k^n
$$
$$
r_k = r_1 e^{i2\pi k /n}
$$
$k \in \mathbb{Z}$

whenever `n` is a real Number it a another Real Solution as $ - \sqrt[2n]{x}$

### when $n \in \mathbb{Z}$:

**Prime Factorization**: where the Number $y$ is factorised, the same numbers are grouped in set of $n$ the exponent, and if all the numbers can't be grouped with the same number in pairs of $n$ elements then root of the base isn't a Natural Number

$\sqrt{576} = \sqrt{2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3} \newline = \sqrt{2^2 \cdot 2^2 \cdot 2^2 \cdot 3^2} \newline = \sqrt{(2 \cdot 2 \cdot 2 \cdot 3)^2} \newline = 2 \cdot 2 \cdot 2 \cdot 3 = 24 \newline
\sqrt{576} = 24$

### Laws of Root

These following laws of root are for $\sqrt{}$

> Conditions: <br> $a \in \R, a > 0$ <br> $b \in \R, b > 0$ <br> $n \in \Z, n \neq 0 $ <br> $m \in \Z, m \neq 0$

$$
\sqrt[n]{ab} = \sqrt[n]{a} \cdot \sqrt[n]{b}
$$
$$
\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}
$$
$$
\sqrt[-n]{a} = \frac{1}{\sqrt[n]{a}}
$$
$$
(\sqrt[n]{a})^m = \sqrt[n]{a^m}
$$

$$
\sqrt[0]{a} = a^{1/\color{orangered}0} = \text{undefined}
$$

# Logarithm

The Logarithm is defined at inverse of the power, which returns the 2nd paramter (i.e the exponent)

$$a^n = b$$

$$\log_a{b} = n$$

## Logarithm Rules:

$$a^{\log_{a}{x}} = \log_{a}{a^{x}} = x$$

**Power Rule**:

$$\log_{a}(x^n) = n \cdot \log_{a}{x}$$

**Sum/Difference Rule**:

$$\log_{a}(xy) = \log_{a}{x} + \log_{a}{y}$$

$$\log_{a}\left(\frac{x}{y}\right) = \log_{a}{x} - \log_{a}{y}$$

**Change of Basis**:

$$\log_{a}{x} = \frac{\log_{b}{x}}{\log_{b}{a}}$$

## Special Logarithms

### Log of 10

by far the most common found in most calculators

$$\log{x} = \log_{10}{x}$$

### Natural Logarithm

a special kind of logarithm whose base is $e$ (the euler's number)

$$\log_{e}(x) = \ln(x)$$

$$\frac{d}{dx}\ln(x) = \frac{1}{x}$$

## Extention of the Logarithm

To the **Negatives**:
$$
\log_{a}{x}
\begin{cases}
x \in \mathbb{R}^{+} &: \log_{a}{x} \cr
x \in \mathbb{R}^{-}, k \in \mathbb{Z} &: \log_{a}{x} + i \pi(2k + 1) \cdot \log_{a}{e} \cr
\end{cases}
$$
To the **Complex Plane**:

$$\log_{a}{z} = p + iq$$
$$\theta = \arctan\left(\frac{\Im(z)}{\Re(z)}\right)$$
$$p = \log_{a}\left(\frac{\Re(z)}{\cos(\theta)}\right) = \log_{a}\left(\frac{\Im(z)}{\sin(\theta)}\right)$$
$$q = \frac{\theta}{\ln(a)}$$

# Factorial

**Factorial**: product of `n` count of successive numbers

$a \in \Z^{+}$

$$
a!
$$

$$
a! = \prod_{k = 1}^{a}k
$$

$$
(a - b)! = a! \cdot \prod_{k = 0}^{b} \frac{1}{a-k} = \frac{a!}{a(a-1)(a-2 )...}
$$

# Algebraic Factorization

$$ab + ac = a(b + c)$$

$$(a + b)(a + c) = a^2 + a(b + c) + bc$$

$$a^n - b^n = (a - b)\sum_{i + j = n - 1} a^j b^j$$

$$x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 -xy - xz - yz)$$

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
a_n x^n + a_{n - 1} x^{n - 1} + ...  + a_{2} x^{2} +  + a_{1} x^{1} + a_0 = a_n(x + r_n)(x + r_{n - 1})...(x + r_2)(x + r_1)
$$

### Remainder Theorem

$$D(x) = x + c$$
$$P(x) = D(x)\ Q(x) + R(x)$$

$R(x)$ degree < $D(x)$ $\therefore R(x) = r$

$$P(x) = D(x)\ Q(x) + r$$

$$
P(x) = (x + c)\ Q(x) + r \newline
P(- c) = ((-c) + c)\ Q(-c) + r \newline
P(- c) = r \newline
$$

$$
P(- c) = r \newline
$$

### Factor Theorem

$$P(x)\ |\ (x - c) \iff P(- c) = 0$$

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

## Exponents Extention

This is an extention of exponent in the Standard Binomial theorem to the Reals

$$(a + b)^n = \sum_{k = 0}^n \begin{pmatrix}n\cr k\end{pmatrix}a^{n-k}b^k$$
$$(1 + x)^n = \sum_{k = 0}^n \begin{pmatrix}n\cr k\end{pmatrix}x^k$$

$$
\begin{pmatrix}n\cr k\end{pmatrix} = \frac{\Gamma(n + 1)!}{k! \cdot \Gamma(n-k + 1)!} = \frac{1}{k!}\left(\displaystyle\prod_{s=0}^{k -1}(n - s)\right)
$$

this may diverge when $x > 1$

## Terms Extention


**Binomial Theorem**:

$$
(x+y)^n =
\sum_{k=0}^{n} \begin{pmatrix} n \cr k \end{pmatrix} x^{n-k}y^k
$$

$$
\begin{pmatrix} n \cr k \end{pmatrix} = \left( \prod_{s=0}^{k -1}(n - s) \right)\frac{1}{k!}
$$

**Trinomial Theorem**:

for proofs of all these theorems see (excluding the binomial)

[`nomialtheorem.md`](./../../papers/nomialtheorem.md)

$$
(x + y + z)^n = 
\sum_{i=0}^{n}\left(\sum_{k=0}^{n - i}

\begin{pmatrix} n \cr i \end{pmatrix}
\begin{pmatrix} n - i \cr k \end{pmatrix}

x^{n-i-k}y^{k}z^{i}

\right)
$$

**Quartic-Nomial**:

$$
(x + y + z + w)^n = 
\sum_{j = 0}^{n}\left(\sum_{i=0}^{n - j}\left(\sum_{k=0}^{n - (j + i)}

\begin{pmatrix} n \cr j \end{pmatrix}
\begin{pmatrix} n - j \cr i \end{pmatrix}
\begin{pmatrix} n - (j +i) \cr i \end{pmatrix}

x^{n - (j + i + k)} y^{k} z^{i} w^{j}

\right)\right)
$$

**N-OMIAL THEOREM**:

$$
(x + y + z + t + w + ...)^n = \newline

\Huge \sum_{\small \forall k_i(k_i \in S_i)} \left( \normalsize
C(n, k_1, k_2, ..., k_{N-1})
\cdot x^{n - \displaystyle\sum_{j = 1}^{N-1} k_j}
y^{k_1}
z^{k_2}
t^{k_3}
w^{k_4}
...
\right)
$$

where:
$$C(n, k_1, k_2, k_3, ..., k_{N - 1} ) = \displaystyle \prod_{i = 1}^{N - 1} \begin{pmatrix} n - \displaystyle \sum_{j = 1}^{i - 1} k_{j} \cr k_i \end{pmatrix} \newline$$

$$
S_i = \left\{x | x \in \mathbb{Z} \land 1 \leq i \leq N - 1  \land 0 \leq k_i \leq n - \displaystyle \sum_{j = 0}^{i - 1} k_j\right\}
$$

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
