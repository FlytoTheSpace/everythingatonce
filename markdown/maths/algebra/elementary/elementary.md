# Elementary Algebra

The Fundamentals of Algebra and common formula's

- [`Axioms`](#axioms): The Foundational assumptions in elementary algebra.
- [`Algebraic Arithmetic`](#algebraic-arithmetic): Contains Fractions, Ratio, Propotionality.
- [`Sum/Product Notation`](#sum-and-product): The Sum and the Product Notation.
- [`Exponents`](#exponents): The Exponents defined (mostly discrete).
- [`Root`](#root): The Inverse of the Power, for obtaining the Base.
- [`Logarithm`](#logarithm): The Inverse of the Power, for obtaining the Exponent.
- [`Factorial`](#factorial): The Factorial Function (introductory).
- [`Polynomial`](./polynomial/polynomial.md): The Polynomials and their solutions (upto degree `4`).
- [`Binomial Theorem`](./binomialtheorem.md): The Binomial Theorem and Pascal's Triangle.

# Axioms

These are some axioms which are built up on and often used throughout this archive

A1. **Equality Preservation**:

$$x = y \implies f(x) = f(y)$$

A2. **Identity**:

$$\exists I[I(x) = x]$$

A3. **Inverse**:

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
