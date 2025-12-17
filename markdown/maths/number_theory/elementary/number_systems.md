
# Number System
Different Type of Number System that are used in Mathematics:

## Natural Numbers/Positive Numbers

**Natural Numbers**/**Positive Numbers**: $\mathbb{N}$ the Set of every number that be found in Nature.
$$
\mathbb{N} = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ... \}
$$
numbers within this set are usually denoted as $n$ for $n \in \mathbb{N}$

### Peano Axioms

The Origin of The Natural Numbers:

$\mathbb{N}$ and $s(n)$ must satisfy the following properties:

**A1**:
$$\exists 0[ 0 \in \mathbb{N}]$$
> The starting point

**A2**:
$$\forall n \in \mathbb{N} [s(n) \in \mathbb{N}]$$
> Closure

**A3**:
$$\forall a, b \in \mathbb{N} [a = b \iff s(a) = s(b)]$$
> s is bijective, and equality is preserved under it.

**A4**:
$$\lnot \exists n \in \mathbb{N} [s(n) = 0]$$
> ensures that the system doesn't cyclic back to the start.

**A5**:


## Negative Numbers

**Negative Numbers**: $\mathbb{Z}^-$ the Set of Negative Version of every Natural Numbers.
$$
\mathbb{Z}^{-} = \{ -n | n \in \mathbb{N} \} \newline
= \{...-10, -9, -8, -7, -6, -5, -4, -3, -2, -1\}
$$
## Integers

**Integers**: $\mathbb{Z}$ the Set containing All *Positive* and *Negative* Numbers also also `0`
$$
\mathbb{Z} = \mathbb{N} \cup \mathbb{Z}^{-} \newline
= \{...-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ...\}
$$

- **Additive Inverse**: switch of The Positive/Negative sign to it's Opposite:

- **Multiplication**:
$$
\pm a \pm b= a \times b = -a \times -b = c
$$
$$
\pm a \times \mp b = -a \times b = a \times -b = -c
$$

## Irrationals

**Irrational Numbers**: $\mathbb{Q}'$ numbers that can be represented on a number line but are not rational

e.g.
$$\sqrt{2}, \pi, e, \sqrt{5}, \sqrt{10}, ...$$

## Rational Numbers

**Rational Numbers**: $\mathbb{Q}$ every number that can be represented as a Fraction

$$
\mathbb{Q} = \left\{\frac{p}{q} \middle | p,q \in \mathbb{Z} \land q \neq 0 \right\}
$$

$$
...-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ...
$$
$$
...\frac{1}{2}, \frac{2}{2}, \frac{3}{2}, \frac{4}{2}..., \frac{1}{5}, \frac{2}{5}, \frac{3}{5},... \frac{11}{10}...
$$

Properties:
- In-between any 2 Rationals there's Always an Infinite Count of Rationals.

- **Multiplicative Inverse**, or **Reciprocals of Each-other**:
$$
\left(\frac{a}{b}\right) \times \left(\frac{b}{a}\right) = 1
$$

## Real Numbers

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

## Imaginary Numbers

**Imaginary Numbers**: are real-number with the Imaginary Unit as a Coefficient

$$\Im = \{ix | x \in \mathbb{R}\}$$

$$i^2 = -1$$

## Complex Numbers

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
