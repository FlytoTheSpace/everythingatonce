
# Number Systems
Different Type of Number System that are used in Mathematics:

# Natural Numbers
## Peano Axioms

The Origin of The Natural Numbers:

$\mathbb{N}$ and $s(n)$ must satisfy the following properties:

**NA1**:
$$\exists 0[ 0 \in \mathbb{N}]$$
> The starting point

**NA2**:
$$\forall n \in \mathbb{N} [s(n) \in \mathbb{N}]$$
> Closure

**NA3**:
$$\forall a, b \in \mathbb{N} [a = b \iff s(a) = s(b)]$$
> s is bijective, and equality is preserved under it.

**NA4**:
$$\lnot \exists n \in \mathbb{N} [s(n) = 0]$$
> ensures that the system doesn't cyclic back to the start.

**A5**: Induction.

> Author's comment: I have a habit of using this A5 axiom sub-conciously while I'm trying to prove a pattern, so keep it in mind.

---

by NA1:
$$0 \in \mathbb{N}$$
by NA2:
$$s(0) \in \mathbb{N}$$
a definition:
$$s(0) := 1$$
if we assume:
$$1 = 0$$
then:
$$s(0) = 0$$
but by NA4
$$\lnot \exists n \in \mathbb{N} [s(n) = 0]$$
$$\therefore 1 \neq 0$$

continue with our definitions:

$$
s(0) := 1 \newline
s(1) := 2 \newline
s(2) := 3 \newline
s(3) := 4 \newline
s(4) := 5 \newline
...
$$

via Induction, we can prove:

$$
s^{1}(0) = 1 \newline
s^{2}(0) = 2 \newline
s^{3}(0) = 3 \newline
s^{4}(0) = 4 \newline
... \newline
s^{n}(0) = n \newline
$$

$$
s^{0}(0) = 0 \newline
s^{0}(1) = 1 \newline
s^{0}(2) = 2 \newline
s^{0}(3) = 3 \newline
s^{0}(4) = 4 \newline
... \newline
s^{0}(n) = n
$$

we get:
$$
s^{0}(n) = s^{n}(0) = n \newline
s^{0}(n) = s^{n}(0) \newline
s^{1}(n) = s^{n}(1) \newline
s^{2}(n) = s^{n}(2) \newline
s^{3}(n) = s^{n}(3) \newline
... \newline
\dashv s^{m}(n) = s^{n}(m)
$$

**Addition**:

$\forall a, b \in \mathbb{N}$

**AA1**:

$$a + 0 = a$$

**AA2**:

$$s(a + b) = a + s(b)$$

---

by AA2:
$$s(a + b) = a + s(b) $$

$$s(a + 0) = a + s(0) $$

by AA1:

$$s(a) = a + s(0) $$

apply $s$ again

$$s(s(a)) = s(a + s(0))$$

simplify:

$$s^2(a) = s(a + s(0))$$

apply AA2:

$$s^2(a) = a + s(s(0))$$

simplify again:

$$s^2(a) = a + s^2(0)$$

now repeat:

$$
s^{2}(a) = a + s^{2}(0) \newline
s^{3}(a) = a + s^{3}(0) \newline
s^{4}(a) = a + s^{4}(0) \newline
s^{5}(a) = a + s^{5}(0) \newline
... \newline
s^{b}(a) = a + s^{b}(0) \newline
$$
apply:

$$s^{b}(0) = b$$

$$s^{b}(a) = a + s^{b}(0) \newline$$

$$s^{b}(a) = a + b$$

since:

$$
s^{b} (a) = s^{a}(b) = b + a
$$

we have proved **Commutativity** for addition:

$$\therefore a + b = b + a$$

we create:

$$
(a + b) + c \newline
= (a + b) + s^{c}(0) \newline
= s^{c}((a + b) + 0) \newline
= s^{c}(a + b) \newline
= a + s^{c}(b) \newline
= a + s^{c}(b + 0) \newline
= a + (b + s^{c}(0)) \newline
= a + (b + c) \newline
$$

$$\therefore (a + b) + c = a + (b + c)$$

Comparison Definition:

$$a < b \iff \exists k \in \mathbb{N} [k \neq 0 \land a + k = b]$$

$$a > b \iff \exists k \in \mathbb{N} [k \neq 0 \land a = b + k]$$

$$a \leq b \iff \exists k \in \mathbb{N} [a + k = b]$$

$$a \geq b \iff \exists k \in \mathbb{N} [a = b + k]$$

Multiplication:

**MA1**:

$$a \times 1 = a$$

**MA2**:

$$a \times (b + c) = (a \times b) + (a \times c)$$

> ORDER OF OPERATION:
> 1. Multiplication.
> 2. Addition.

---

by MA2:

$$a \times (b + c) = (a \times b) + (a \times c)$$
$$a \times (b + 0) = (a \times b) + (a \times 0)$$
$$(a \times b) = (a \times b) + (a \times 0)$$

the only value we know of that can satisfy that is:

$$\implies a \times 0 = 0$$

for commutativity:

$$
a \times b \newline
= a \times (s^{b}(0)) \newline
= a \times (\underbrace{1 + 1 + 1 + ...}_{b}) \newline
= \underbrace{(a \times 1) + (a \times 1) + (a \times 1) + ...}_{b} \newline
= \underbrace{a + a + a + ...}_{b} \newline
= \underbrace{s^{a}(0) + s^{a}(0) + s^{a}(0) + ...}_{b}
$$

$$
= b \underbrace{\begin{cases}
(1  +  1  +  1  + 1 + ...) + \cr
(1  +  1  +  1  + 1 + ...) + \cr
(1  +  1  +  1  + 1 + ...) + \cr
(1  +  1  +  1  + 1 + ...) + \cr
(1  +  1  +  1  + 1 + ...) + \cr
\end{cases}}_{a}
$$

$$
= b \underbrace{\begin{cases}
1  +  1  +  1  + 1 + ... + \cr
1  +  1  +  1  + 1 + ... + \cr
1  +  1  +  1  + 1 + ... + \cr
1  +  1  +  1  + 1 + ... + \cr
1  +  1  +  1  + 1 + ... + \cr
\end{cases}}_{a}
$$

switch the columns and rows:

$$
= a \underbrace{\begin{cases}
1  +  1  +  1  + 1 + 1 + ... \cr
1  +  1  +  1  + 1 + 1 + ... \cr
1  +  1  +  1  + 1 + 1 + ... \cr
1  +  1  +  1  + 1 + 1 + ... \cr
\end{cases}}_{b}
$$

$$
= a \underbrace{\begin{cases}
(1  +  1  +  1  + 1 + 1 + ...) + \cr
(1  +  1  +  1  + 1 + 1 + ...) + \cr
(1  +  1  +  1  + 1 + 1 + ...) + \cr
(1  +  1  +  1  + 1 + 1 + ...) + \cr
\end{cases}}_{b}
$$

$$
= a \begin{cases}
(b) +\cr
(b) +\cr
(b) +\cr
(b) +\cr
\end{cases}
$$

$$
= a \begin{cases}
b +\cr
b +\cr
b +\cr
b +\cr
\end{cases}
$$

$$
= \underbrace{b + b + b + b +...}_{a} \newline
= \underbrace{(b \times 1) + (b \times 1) + (b \times 1) + (b \times 1) +...}_{a} \newline
= b \times \underbrace{(1 + 1 + 1 + 1 + ...)}_{a} \newline
= b \times \underbrace{(1 + 1 + 1 + 1 + ...)}_{a} \newline
= b \times (s^{a}(0)) \newline
= b \times (a) \newline
= b \times a \newline
$$

$$\therefore a \times b = b \times a$$

Associativity:

$$
(a \times b) \times c \newline
= \underbrace{(b + b + b + ...)}_{a} \times c \newline
= c \times \underbrace{(b + b + b + ...)}_{a} \newline
= \underbrace{((b \times c) + (b \times c) + (b \times c) + ...)}_{a} \newline
= a \times (b \times c) \newline
$$

---

in summary:

$$\mathbb{N} = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...\}$$

$\forall a, b, c \in \mathbb{N}$ :

$$s^{a}(0) = a$$

$$s^{b}(a) = s^{a}(b)$$

$$a + b = s^{b}(a)$$

$$(a + b) + c = a + (b + c)$$

$$a + b = b + a$$

$$a + 0 = a$$

$$a \times b = \underbrace{(a + a + a + ...)}_{b}$$

$$a \times b = b \times a$$

$$(a \times b) \times c = a \times (b \times c)$$

$$a \times 1 = a$$

$$a \times 0 = 0$$

$$a \times (b + c) = (a \times b) + (a \times c)$$

Extra Notation:

$$\mathbb{N}_m = \{n | n \in \mathbb{N} \land n \leq m\}$$

# Integers

$$\mathbb{N}[-1] = \mathbb{Z}$$

$$(a = b \iff f(a) = f(b)) \implies \exists p [s(p(a)) = p(s(a)) = a]$$

Integer Axioms (non-standard):

IA1.

$$\mathbb{N} \subset \mathbb{Z}$$

IA2.

$$\forall a \in \mathbb{Z}[p(a) \in \mathbb{Z}]$$

---

by IA2.

$$
p(0) := -1 \newline
p(1) := -2 \newline
p(2) := -3 \newline
p(3) := -4 \newline
p(4) := -5 \newline
p(5) := -6 \newline
... \newline
$$

$$p^{n}(0) := -n$$

$$p^{m}(n) = p^{n}(m)$$

axiom for addition with Integers:

**AA3**.

$$p(a + b) = a + p(b)$$

---


$$p^{b}(a + 0) = a + p^{b}(0)$$
$$p^{b}(a) = a + p^{b}(0)$$
$$p^{b}(a) = a + (-b)$$
$$p^{b}(s^{b}(a)) = a + b + (-b)$$
$$a = a + b + (-b)$$
$$0 = 0 + b + (-b)$$
$$a + (-a) = 0$$

Definition of subtraction:

$$a - b := a + (-b)$$

$$
p(0) = -1 \newline
p(p(0)) = p(-1) \newline
p^2(0) = p(-1 + 0) \newline
p^2(0) = (-1) + p(0) \newline
p^2(0) = \underbrace{(-1) + (-1)}_{2} \newline
p^3(0) = \underbrace{(-1) + (-1) + (-1)}_{3} \newline
p^4(0) = \underbrace{(-1) + (-1) + (-1) + ...}_{4} \newline
p^n(0) = \underbrace{(-1) + (-1) + (-1) + ...}_{n} \newline
$$

Multiplication:

$$
p^n(0) = \underbrace{(-1) + (-1) + (-1) + ...}_{n} \newline
-n = \underbrace{(-1) + (-1) + (-1) + ...}_{n} \newline
-n = \underbrace{(-1) \times 1 + (-1) \times 1 + (-1) \times 1 + ...}_{n} \newline
-n = (-1) \times (\underbrace{1 + 1 + 1 + ...}_{n}) \newline
-n = (-1) \times n \newline
$$

$$
(-a) + a  = 0
$$

$$
(-a) + (-(-a)) := 0
$$

$$
(-a) + a = (-a) + (-(-a)) \newline
a +(-a) + a = a +(-a) + (-(-a)) \newline
(a +(-a)) + a = (a +(-a)) + (-(-a)) \newline
0 + a = 0 + (-(-a)) \newline
a = (-(-a)) \newline
(1) \times a = ((- 1) \times (-1)) \times a \newline
$$
$$\therefore (-1)(-1) = 1$$

in summary:

$$p^n(0) = \underbrace{(-1) + (-1) + (-1) + ...}_{n}$$

$$a - b = a + (-b)$$

$$-n = (-1) \times n$$

$$(-1) \times (-1) = 1$$

$$\mathbb{Z} = \{..., -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, ...\}$$

# Rationals

Inverse of Multiplication:

$$a \times \left(\frac{1}{a}\right) = 1$$

long as $a \neq 0$ as if defined it must map to all possible values at once which a function isn't allowed to do traditionally.

**MA3**: Axiom of Distributivity of inverse of multiplication over addition:

$$\left(\frac{1}{a}\right) \times (b + c) = \left(\frac{1}{a}\right) \times b + \left(\frac{1}{a}\right) \times c$$

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
\mathbb{Q} = \left\{\frac{p}{q} \middle | p,q \in \mathbb{Z} \land q \neq 0 \right\}
$$
$$
\mathbb{Q} = \{
...-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, ...
,\frac{1}{2}, \frac{2}{2}, \frac{3}{2}, \frac{4}{2}..., \frac{1}{5}, \frac{2}{5}, \frac{3}{5},... \frac{11}{10}, ... \}
$$

# Irrationals

**Irrational Numbers**: $\mathbb{Q}'$ numbers that can be represented on a number line but are not rational

e.g.
$$\sqrt{2}, \pi, e, \sqrt{5}, \sqrt{10}, ...$$

- [$\sqrt{2}$ `Irrationality Proof`](../papers/irrationality.md)

# Real Numbers

**Real Numbers**: $\mathbb{R}$ are every number that can be found on the Real-Number Line includes all Rational and Irrationals

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
