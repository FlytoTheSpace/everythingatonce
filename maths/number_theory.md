
- [Back to Maths](./maths.md)
- [Back to Home](../README.md)

# Number Theory

# General Number Theory

## Base

### Base 10

---

Where the Numbers uses 10 Symbols to represent themselves

The most common set of symbols is the Western One's:

$$
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
$$



**Internation System of Numerals**: every *comma* `(,)` is placed after every 3rd digit

$
50,801,591
$

**Indian System of Numerals**: first *comma* `(,)` is placed after the 3rd digit and the rest of them are placed after every 2nd digit

$
5,08,01,591
$

**Roman Numerals**: using English Aplhabet to present Mathematical Number with a Known Quantity

- $I: 1$
- $V: 5$
- $X: 10$
- $L: 50$
- $C: 100$
- $D: 500$
- $M: 1000$

Rules:

- Every 2nd (eg $V, L, D... $) Roman Numeral Aplhabet is are Never:
	- Written behind the Symbol with Greater Value
	- Repeated
	- Subtracted
- Non Second Roman Number (eg $I, X, C, M ...$)
	- Not Repeated more then `3` times
	- Can only be used for Subtraction for Alphabets up to `+2` next to it

| Roman    | Western | Interpretation |
| -------- | ------- | -------------- |
| $$I   $$ | $$1  $$ | $$1         $$ |
| $$II  $$ | $$2  $$ | $$1+1       $$ |
| $$III $$ | $$3  $$ | $$1+1+1     $$ |
| $$IV $$  | $$4  $$ | $$-1+5      $$ |
| $$V $$   | $$5  $$ | $$5         $$ |
| $$...$$  | $$...$$ | $$...       $$ |

**Expanded Form**: large numbers are represeted as Unit Places, example:

$$
214 = 2 \times 100  + 1 \times 10 + 4 \times 1
$$

### Base 2

---

### Ratio

---

**Ratio**: Comparison of any 2 or more values, that shows the relative size of one to another.

$$
a \colon b
$$

Properties:
- Can only be compared with the same units
- **Equivalent Ratios**: when 2 Ratios are equivalent to one another

	$a : b = c : d$


### Proportion

---

**Proportion**: Property of Equality of 2 ratios

$$a : b = c : d$$

$$a : b :: c : d$$

$$a : b = ak : bk $$

Components:

- **Respective Terms**: all 4 Terms involved $\{a, b, c, d\}$

- **Extreme Terms**: First and the Last Terms $\{a, d\}$

- **Middle Terms**: Second and the Third Terms $\{b, c\}$

Types:

- **Direct Proportion**: when given the value $x$, the second value $y$ will be a obtained as the product of $x$ with a Constant $k$

$$(y = x \cdot k) \implies (y \propto x)$$

-  **Inverse Proportion**: when given the value $x$, $y$ will be obtained as $k$ over $x$

$$(y = \frac{k}{x}) \implies (y \propto \frac{1}{x})$$

## Factors

**Factors**: Numbers that can be multiplied to obtain a new Number, those number will become the factors of the new Numbers

$a \times b = c$

Properties:

- A Number is a multiple of each of it's factors

- **1** is The Factor of every Number

	$1\times a = a$ 

- Every Number is a Factor of itself

	$a \div a = 1 $

- Every factor is an Exact divisor of that number and The Remainder should be `0`

	$ a \mod b = 0$ ✅

	$ a \mod b \neq 0$ ❌

- Every factor is Either Equal or Less than the number

	$ a \geq b $
	
	- `b` is a factor of `a`

- Count of Factors is of a Number is **Finite**
- Count of Multiples of a Number is **Infinite**

| Number | Factors        | isPrime |
| ------ | -------------- | ------- |
| $1$    | $1$            | ❌       |
| $2$    | $1,2$          | ✅       |
| $3$    | $1,3$          | ✅       |
| $4$    | $1,2,4$        | ❌       |
| $5$    | $1,5$          | ✅       |
| $6$    | $1,2,3,6$      | ❌       |
| $7$    | $1,7$          | ✅       |
| $8$    | $1,2,4,8$      | ❌       |
| $9$    | $1,3,9$        | ❌       |
| $10$   | $1,2,5,10$     | ❌       |
| $11$   | $1,11$         | ✅       |
| $12$   | $1,2,3,4,6,12$ | ❌       |

Divisibility Rule

| Number | Rule                                          |
| ------ | --------------------------------------------- |
| $1$    | Always                                        |
| $2$    | If Even                                       |
| $3$    | Sum of All digits is Multiple of 3            |
| $4$    | with 3+ digits, last 2 digits divisible by it |
| $5$    | `0` or `5` in one's place                     |
| $6$    | Divisible by both 2 and 3                     |
| $8$    | with 4+ digits, last 3 digits divisible by it |
| $9$    | sum of all digits divisible by it             |
| $10$   | `0` in one's place                            |
| $11$   | -                                             |

### Prime Factorisation

---

**Prime Factorisation**: A type of Factorisation in which the only remaining Factors are Prime Numbers and `1`

- **Greatest Common Divisior** `GCD`: The Biggest Factor any 2 or more Numbers that are all divisible by it.


## Fractions

**Fractions**: Numbers that are obtained after divison between 2 numbers
$$
\frac{a}{b} = a \div b
$$

Properties:
- $b \neq 0$, `b` must not be equal to $0$
- **Nominator**/**Numerator**: value That Sits on Top of The Fraction
- **Dominator**/**Denomitor**: value That Sits on Bottom of The Fraction

$$
\frac{\text{Nominator}}{\text{Dominator}}
$$

- **Negative Sign Switch**
$$
-\frac{a}{b} = \frac{-a}{b} = \frac{a}{-b}
$$
- **Equivalent Fractions**: when 2 factions represent the same value

- Multiplication/Divison of the Nominator and the Dominator by the same number, doesn't changes the original value
$$
\frac{a}{b} = \frac{a\times c}{b\times c} = \frac{a\div c}{b\div c}
$$

**Proper Fractions**: fractions where Nominator is <u>smaller</u> than The Denominator

**Improper Fractions**: fractions where Nominator is <u>bigger</u> than The Denominator

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
## Exponentiation

**Exponentiation/Power**: A Level Above Multiplication where a Number is Multiplied by itself `n` count of times.

$$
a^n = a \times a ...
$$
$$
-a^{n} = -1( a^n )
$$
$$
(-a)^{n} = -a \times -a ...
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
$n \in \mathbb{Q}, n \neq 0$ <br>
$m \in \mathbb{Q}, m \neq 0$

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

More Rules:

- $1$ to the power of any integer exponent `n` always results in $1$
$$1^n = 1$$

- $-1$ to the power of even number exponent `2a` will result in $1$ and $-1$ if odd
$$(-1)^{2a} = 1$$

$$(-1)^{2a+1} = (-1)$$
- $10^n$ will result in $1$ followed by `n` count of zeros,

	$10^3 = 1000$

	- if `n` is negative then It'll be `n` count of decimal places and then a $1$

		$10^{-3} = 0.001$

- Odd Number to the Power of `n` will always result in an Odd Number
$$(2a + 1)^n = 2(\frac{(2a + 1)^n - 1}{2}) + 1$$
- Even Number to the Power of `n` will always result in an Even Number, as long as $n \neq 0$
$$(2a)^n = 2(\frac{(2a)^n}{2})$$

### Power

---

$$
a^{-n} = \frac{1}{a^n}
$$
$$
a^{1/n} = \sqrt[n]{a}
$$
$$
a^{m/n} = (\sqrt[n]{a})^m = \sqrt[n]{a^m}
$$

### Square

---


**Square**: Where Numbers are Exponentiated to The Power of 2, and It create a Geometric 2 Dimentional Square
$$
a^2 = a \times a
$$

$$(a + b)^2 = a^2 + 2ab = b^2$$
$$(a - b)^2 = a^2 - 2ab = b^2$$
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
	
	$$(n = 2x) \implies \frac{n}{2}$$
	$$(n = 2x + 1) \implies \frac{n + 1}{2}$$

**Triangular Number**: where the Number can Geometrically arranged to create a Triangle

$$
a = \sum_{k=1}^n k
$$
- Sum 2 Consecutive Square Number Results in a Square number
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

## Root

**Root**: the inverse operation of Exponentiation, it returns the Base of an exponentiation

**Radical Sign** is used to denote Root of a quantity
"$\sqrt{}$".

$$x^n = y$$
$$\sqrt[n]{y} = x$$


**Prime Factorization**: where the Number $y$ is factorised, the same numbers are grouped in set of $n$ the exponent, and if all the numbers can't be grouped with the same number in pairs of $n$ elements then root of the base isn't a Natural Number

$\sqrt{576} = \sqrt{2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3} \newline = \sqrt{2^2 \cdot 2^2 \cdot 2^2 \cdot 3^2} \newline = \sqrt{(2 \cdot 2 \cdot 2 \cdot 3)^2} \newline = 2 \cdot 2 \cdot 2 \cdot 3 = 24 \newline
\sqrt{576} = 24$

### Laws of Root
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

### Logarithm

---

## Factorial

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


# Number System
Different Type of Number System that are used in Mathematics:

## Natural Numbers/Positive Numbers

**Natural Numbers**/**Positive Numbers**: $\mathbb{N}$ the Set of every number that be found in Nature.
$$
1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ...
$$
## Negative Numbers

**Negative Numbers**: $\mathbb{Z}^-$ the Set of Negative Version of every *Positive Numbers*.
$$
...-10, -9, -8, -7, -6, -5, -4, -3, -2, -1
$$
## Whole Numbers

**Whole Numbers**: $\mathbb{W}$ the Set of every *Positive Numbers* and The Number `0`.
$$
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ...
$$
## Integers

**Integers**: $\mathbb{Z}$ the Set containing All *Positive* and *Negative* Numbers also also `0`
$$
...-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ...
$$

- **Additive Inverse**: switch of The Positive/Negative sign to it's Opposite:

- **Multiplication**:
$$
\pm a \pm b= a \times b = -a \times -b = c
$$
$$
\pm a \times \mp b = -a \times b = a \times -b = -c
$$

## Rational Numbers

**Rational Numbers**: $\mathbb{Q}$ every number that can be represented as a Fraction
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
\frac{a}{b} \times \frac{b}{a} = \frac{a \div a}{b \div b} = \frac{1}{1} = 1
$$

## Properties:

- `0` Additive Identity for Rationals
- `1` Multiplicative Identity for Rationals

**Closure**: Describes whether if certain Arithmetic Operations can result a value outside the established number systems

| Number System    | Addition | Subtraction | Multiplication | Division |
| ---------------- | -------- | ----------- | -------------- | -------- |
| Natural/Positive | ✅        | ❌           | ✅              | ❌        |
| Negative         | ✅        | ❌           | ❌              | ❌        |
| Whole            | ✅        | ❌           | ✅              | ❌        |
| Integers         | ✅        | ✅           | ✅              | ❌        |
| Rationals        | ✅        | ✅           | ✅              | ❌        |

**Communicativity**: Describes whether changing the Order of Operands in an expression, results in the same output.

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

**Associativity and Communicativity For**:
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

To Fraction:
> `n` is count of Decimal Digits after the Decimal point before $0$ or repeat, and `a` is the decimal number
$$
a = \frac{a \times 10^n}{10^n} = \frac{10^na}{10^n}
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
