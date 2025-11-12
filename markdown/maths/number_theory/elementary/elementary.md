
# Elementary Number Theory

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

