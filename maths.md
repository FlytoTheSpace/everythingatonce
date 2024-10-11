Sections:

Pure Mathematics

- [Arithmetic](#arithmetic)
- [Algebra](#algebra)
- [Linear Alegbra](#linear-alegbra)
- [Geometry](#geometry)
- [Trignometry](#trignometry)
- [Number Theory](#number-theory)
- [Calculus](#calculus)
- [Differential Equations](#differential-equations)
- [Combinatorics](#combinatorics)
- [Topology](#topology)
- [Logic](#logic)
  - [Set Theory](#set-theory)

Applied Mathematics

- [Financial Mathematics](#financial-mathematics)
- [Turing Machine](#turing-machine)
- [Information Theory](#information-theory)
- [Statistics](#statistics)
- [Game Theory](#game-theory)



# Pure Mathematics

# Arithmetic

**Arithmetic**: a field of Mathematics containing the very Foundational Basics about it

## Successor, Predecessor

**Successor**: A Number `+1` of The Previous One

$
a+1
$

**Predecessor**: A Number `-1` for the Previous one

$
a-1
$

## Addition, Subtraction
**Addition** `(Add)`: Sum of any 2 Numbers

$
a+b
$

- Repeated Succession $b$ count of times on $a$

**Subtraction** `(Subtract)`: Subtraction of One Number from another

$
a-b
$

- Repeated Predecession $b$ count of times on $a$

## Multiplication, Division
**Multiplication** `(Multiply)`: Multiplication

$
a \times b
$
- Repeated Addition of `a` with itself `b` count of times

**Division** `(Divide)`: Divison of a Number in `b`  count of peices

$ a / b $

$ a \div b $
- Divison of $a$ into `b` count of Parts/Components Evenly

# Algebra
**Algebra**: a field of Mathematics consisting of English Aplhabet Represeting Number, with many use cases such as Representing Unknown/Dynamic Values.

## Identities

**Binomial**:
$$
(a + b)^2 = a^2 + 2ab + b^2
$$
$$
(a - b)^2 = a^2 - 2ab + b^2
$$
$$
(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3
$$
$$
(a - b)^3 = a^3 - 3a^2b + 3ab^2 + b^3
$$
**Factorization**:
$$
ab + ac = a(b + c )
$$
$$
-a(b) + a(c) = -a(b -c) = a(-b + c)
$$

## Boolean Algebra
**Boolean Algebra**: A Branch of Algebra where the Variables can only have 2 possible states

- `1` standing for **TRUE**, **ON**.
- `0` standing for **FALSE**, **OFF**.

### Units
These Boolean Algebra Variables are used in Sets when representing Data
- **Bit**: A Single Variable, with only possible states of `0` and `1`.
- **Nibble**: a set of 4 Bits, with $2^4$ combinations with `0`'s and `1`'s.
- **Byte**: a set of 8 Bits, can represent a Single ASCII Character.
- **Octet**: a set of 4 Bytes or 32 bits, with a Total of $2^{32}$ combinations.

| Unit       | Comparison | Cominations       |
| ---------- | ---------- | ----------------- |
| **Bit**    | *Lowest*   | $2^{1}$, `0`, `1` |
| **Nibble** | `4 Bits`   | $2^{4}$           |
| **Byte**   | `8 Bits`   | $2^{8}$           |
| **Octet**  | `4 Bytes`  | $2^{32}$          |

**Exponential Units**:


**Bytes**,  `(base 10)`:
| Unit               | Comparison       | Bytes     |
| ------------------ | ---------------- | --------- |
| **KiloByte** `KB`  | `1000 Bytes`     | $10^{3}$  |
| **MegaByte** `MB`  | `1000 KiloBytes` | $10^{6}$  |
| **GigaByte** `GB`  | `1000 MegaBytes`  | $10^{9}$  |
| **TeraByte** `TB`  | `1000 GigaBytes`  | $10^{12}$ |
| **PetaByte** `PB`  | `1000 TeraBytes`  | $10^{15}$ |
| **ExaByte** `EB`   | `1000 PetaBytes`  | $10^{18}$ |
| **ZetaByte** `ZB`  | `1000 ExaBytes`   | $10^{21}$ |
| **YottaByte** `YB` | `1000 ZetaBytes`  | $10^{24}$ |

**Bytes**,  `(base 2)`:
| Unit               | Comparison       | Bytes    |
| ------------------ | ---------------- | -------- |
| **KibiByte** `KiB` | `1024 Bytes`     | $2^{10}$ |
| **MibiByte** `MiB` | `1024 KibiBytes` | $2^{20}$ |
| **GibiByte** `GiB` | `1024 MibiBytes` | $2^{30}$ |
| **TibiByte** `TiB` | `1024 GibiBytes` | $2^{40}$ |
| **PibiByte** `PiB` | `1024 TibiBytes` | $2^{50}$ |
| **ExbiByte** `EiB` | `1024 PibiBytes` | $2^{60}$ |
| **ZibiByte** `ZiB` | `1024 ExbiBytes` | $2^{70}$ |
| **YobiByte** `YiB` | `1024 ZibiBytes` | $2^{80}$ |

---
### Logic Gates:

Logic Gates are Gates that Determine the Output of Certain Inputs based on Logic which they Represent

Main Logic Gates:

- **Conjunction**, **AND** `(2 inputs)`: returns `1` if both inputs are `1`.
- **Disjunction**,  **OR** `(2 inputs)`: returns `1` if any of the inputs are `1`.
- **Negation**, **NOT** `(1 input)`: Inverts the given Input.
- **Exclusive OR**, **XOR** `(2 inputs)`: returns `1` if both inputs are not the same.

| $a$ | `NOT` $¬a$ |
| --- | ---------- |
| $0$ | $1$        |
| $1$ | $0$        |

| $a$ | $b$ | `AND` $a∧b$ | `OR` $a∨b$ | `XOR` $a \otimes b$ |
| --- | --- | ----------- | ---------- | ------------------- |
| $0$ | $0$ | $0$         | $0$        | $0$                 |
| $0$ | $1$ | $0$         | $1$        | $1$                 |
| $1$ | $0$ | $0$         | $1$        | $1$                 |
| $1$ | $1$ | $1$         | $1$        | $0$                 |

**Inverted Logic Gates**:

- **NOT Conjunction**, **NAND** `(2 inputs)`: returns `1` if both inputs are NOT `1`.
- **NOT Disjunction**,  **NOR** `(2 inputs)`: returns `1` if any of the inputs are NOT `1`.
- **NOT Exclusive OR**, **XNOR** `(2 inputs)`: returns `1` if both inputs ARE the same.

| $a$ | $b$ | `NAND` $¬(a∧b)$ | `NOR` $¬(a∨b)$ | `XNOR` $¬(a \otimes b)$ |
| --- | --- | --------------- | -------------- | ----------------------- |
| $0$ | $0$ | $1$             | $1$            | $1$                     |
| $0$ | $1$ | $1$             | $0$            | $0$                     |
| $1$ | $0$ | $1$             | $0$            | $0$                     |
| $1$ | $1$ | $0$             | $0$            | $1$                     |

**Totality of Logic Gates / Truth Tables**:

**Single Input**:
| $a$ | `BUFFER` | `NOT` |
| --- | -------- | ----- |
| $0$ | $0$      | $1$   |
| $1$ | $1$      | $0$   |

**Double Input**:
| $a$ | $b$ | `AND` | `OR` | `XOR` | `NAND` | `NOR` | `XNOR` |
| --- | --- | ----- | ---- | ----- | ------ | ----- | ------ |
| $0$ | $0$ | $0$   | $0$  | $0$   | $1$    | $1$   | $1$    |
| $0$ | $1$ | $0$   | $1$  | $1$   | $1$    | $0$   | $0$    |
| $1$ | $0$ | $0$   | $1$  | $1$   | $1$    | $0$   | $0$    |
| $1$ | $1$ | $1$   | $1$  | $0$   | $0$    | $0$   | $1$    |

### Latches

**SR Latch**: A Latch that can Hold upto 1 Bit of Data, with 2 Inputs and 2 Outputs

- `S`, `R` Inputs
- `Q`, `¬Q` Outputs
- `S` Sets The Output `Q` to 1, `¬Q` to 0 
- `R` Sets The Output `Q` to 0, `¬Q` to 1
- `¬Q` is Invert of The Main Output `Q`
- value of `Q` can be 0 or 1 depending on it's initial value
- `S` and `R` both 1 at the same is Invalid, as it's not supposed to happen and both Output `Q` and `¬Q` will be set to 0

Truth Table:

| `S` | `R` | `Q`    | `¬Q`   |
| --- | --- | ------ | ------ |
| $0$ | $0$ | $1, 0$ | $0, 1$ |
| $1$ | $0$ | $1$    | $0$    |
| $0$ | $1$ | $0$    | $1$    |
| $1$ | $1$ | $0$    | $0$    |

---
### Arithmetic

**Addition**: An Special Type of XOR Operation of Inputs, `a`, `b` and *Carry*

- $r = 1$, $c = 0$: IF any 1 is ON
- $r = 0$, $c = 1$: IF any 2 is ON
- $r = 1$, $c = 1$: IF all 3 is ON

| Carry | $a$ | $b$ | ($r$) result | Next Carry |
| ----- | --- | --- | ------------ | ---------- |
| $0$   | $0$ | $0$ | $0$          | $0$        |
| $0$   | $0$ | $1$ | $1$          | $0$        |
| $0$   | $1$ | $0$ | $1$          | $0$        |
| $0$   | $1$ | $1$ | $0$          | $1$        |
| $1$   | $0$ | $0$ | $1$          | $0$        |
| $1$   | $0$ | $1$ | $0$          | $1$        |
| $1$   | $1$ | $0$ | $0$          | $1$        |
| $1$   | $1$ | $1$ | $1$          | $1$        |

**Subtraction**: An Special Type of XOR Operation of Inputs, `a`, `-b` and *Carry*
- `Carry` acts as a Negative Value
- `0` Carry and `0` result if any 2 is `1`

| Carry | $a$ | $-b$ | ($r$) result | Next Carry |
| ----- | --- | ---- | ------------ | ---------- |
| $0$   | $0$ | $0$  | $0$          | $0$        |
| $0$   | $0$ | $1$  | $1$          | $1$        |
| $0$   | $1$ | $0$  | $1$          | $0$        |
| $0$   | $1$ | $1$  | $0$          | $0$        |
| $1$   | $0$ | $0$  | $1$          | $1$        |
| $1$   | $0$ | $1$  | $0$          | $1$        |
| $1$   | $1$ | $0$  | $0$          | $0$        |
| $1$   | $1$ | $1$  | $1$          | $1$        |

# Linear Alegbra
**Linear**: a subfield of Algebra where All the Algebraic factors in an expression have a power of 1


# Geometry
**Geometry**: a field of Mathematics consisting Entirely of Geometric Shapes and their Properties

Properties:
- **Adjacent sides**: lines that share a common vertex.
- **Adjacent angles**: angles that share a common side.

## 2D

### Polygon
**Polygon**: A simple closed Shape made up only line segments

Properties:
- **Equiangular**: All interior angles equivalent to each-other.
- **Equilateral**: Length of all sides equivalent to each-other.
- **Diagonals**: lines that join any 2 opposite vertex of a Polygon.
- Sum of all exterior angles of any Polygon is `360°`deg.

Types:

**Regular Polygon**: A Polygon which is Both Equiangular and Equilateral
**Concave Polygon**: A Polygon with an In-words Curve
**Convex Polygon**: A Polygon with no In-words Curve

---
#### **Quadrilateral**: A type of Polygon with only 4 Sides and Vertex

**Trapezium**: A Quadrilateral with a Set of parallel lines

![123](./img/shapes/trapezium.png)

**Kite**: a Quadrilateral with 2 distinct consecutive pairs of equal length

**Parallelogram**: a Quadrilateral with 2 Pairs of Parallel Lines

**Rhombus**: a Quadrilateral, Equilateral

**Rectangle**: a Quadrilateral, Equiangular with 2 pairs of parallel lines

**Square**: a Quadrilateral, Regular Polygon, Equilateral and Equiangular.

## 3D

# Trignometry
**Trignometry**: a sub-field of Geometry only consisting of Triangles and Their Angles related Geometry
# Number Theory
## Number Writing System:

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

| Roman    | Normal  | Interpretation |
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

**Measurement Units**

- **Metric System**

| Unit | Unit (Expanded) | Comparison |
| ---- | --------------- | ---------- |
**Length**
| mm   | Milimeter       | 0.001m     |
| cm   | Centimeter      | 0.01m      |
| dm   | Decimeter       | 0.1m       |
| m    | Meter           | Base Unit  |
| dam  | Decameter       | 10m        |
| hm   | Hectometer      | 100m       |
| km   | Kilometer       | 1,000m     |

- **Imperial System**

| Unit | Unit (Expanded) | Comparison |
| ---- | --------------- | ---------- |
**Length**
| in   | Inch            | $ft\div12$ |
| ft   | Foot            | Base Unit  |
| yd   | Yard            | 3ft        |
| mi   | Mile            | 5,280 ft   |

## Number System
Different Type of Number System that are used in Mathematics:

### Natural Numbers/Positive Numbers
**Natural Numbers**/**Positive Numbers**: a Set of every number that be found in Nature and it does Exists.
$$
1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ...
$$
---
### Negative Numbers
**Negative Numbers**: a Set of Negative Version of every *Positive Numbers*.
$$
...-10, -9, -8, -7, -6, -5, -4, -3, -2, -1
$$
---
### Whole Numbers
**Whole Numbers**: A Set of every *Positive Numbers* and The Number `0`.
$$
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ...
$$
---
### Integers
**Integers**: A Set containing All *Positive* and *Negative* Numbers also also `0`
$$
...-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ...
$$

- **Additive Inverse**: switch of The Positive/Negative sign to it's Opposite:

$$a ⟹ -a$$

$$-a ⟹ a$$

- **Multiplication**:
$$
\pm a \pm b= a \times b = -a \times -b = c
$$
$$
\pm a \times \mp b = -a \times b = a \times -b = -c
$$
---
### Fractions
**Fractions**: Numbers that can be represented as a Fraction of a Number, can be both Positive/Negative, can also Represent *some* Decimal Numbers
$$
\frac{a}{b}
$$

Properties:
- $a/0$ is Not Allowed
- **Nominator**/**Numerator**: value That Sits on Top of The Fraction
- **Dominator**/**Denomitor** */: value That Sits on Bottom of The Fraction

$$
\frac{Nominator}{Dominator}
$$

- Negative Sign Switch
$$
\frac{-a}{b} = \frac{a}{-b}
$$
- No Value Change if both Nemoniator and Denominator are Multiply/Divided by the same value, Also caleld **Equivalent Fractions**
$$
\frac{a}{b} = \frac{a\times c}{b\times c} = \frac{a\div c}{b\div c}
$$

**Proper Fractions**: fractions where Nominator is <u>smaller</u> than The Denominator

**Improper Fractions**: fractions where Nominator is <u>Bigger</u> than The Denominator

**Mixed Fractions**: A mix of an Integer and A Fraction

$$
c + \frac{a}{b}
$$
- To Mixed:
  - `c` must be floored to the Nearest Integer
$$
n \mod b = a
$$
$$
n \div b = c
$$
$$
\frac{n}{b} = (n \div b) + \frac{(n \mod b)}{b} = c + \frac{a}{b}
$$
- From Mixed:
$$
c + \frac{a}{b} = \frac{cb + a}{b} = \frac{n}{b}
$$
**Arithmetic Operations**:

Addition:
$$
\frac{a}{b} + c = \frac{a}{b} + \frac{c}{1} = \frac{a}{b} + \frac{bc}{b} = \frac{a + bc}{b}
$$
$$
\frac{a}{b} + \frac{c}{d} = \frac{ad}{bd} + \frac{bc}{bd} = \frac{ad + bc}{bd}
$$

Subtraction
$$
\frac{a}{b} - c = \frac{a}{b} - \frac{c}{1} = \frac{a}{b} - \frac{bc}{b} = \frac{a - bc}{b}
$$
$$
\frac{a}{b} - \frac{c}{d} = \frac{ad}{bd} - \frac{bc}{bd} = \frac{ad - bc}{bd}
$$
Multiplication
$$
\frac{a}{b} \times c = \frac{a}{b} \times \frac{c}{1} = \frac{a \times c}{b} = \frac{a}{b \div c}
$$
$$
\frac{a}{b} \times \frac{c}{d} = \frac{a \times c}{b \times d} = \frac{a \div d}{b \div c}
$$
Division
$$
\frac{a}{b} \div c = \frac{a}{b} \div \frac{c}{1} = \frac{a \div c}{b} = \frac{a}{b \times c}
$$
$$
\frac{a}{b} \div \frac{c}{d} = \frac{a \div c}{b \div d} = \frac{a \times d}{b \times c}
$$
---
### Rational Numbers
**Rational Numbers**: Includes All of The Integers and Fractions
$$
...-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ...
$$
$$
...\frac{1}{2}, \frac{2}{2}, \frac{3}{2}, \frac{4}{2}..., \frac{1}{5}, \frac{2}{5}, \frac{3}{5},... \frac{11}{10}...
$$

Properties:
- In-between 2 Rationals there's Always an Infinite Count of Rationals.

- **Multiplicative Inverse**
$$
\frac{a}{b} \times \frac{b}{a} = \frac{a \div a}{b \div b} = \frac{1}{1} = 1
$$

---
### Number System Properties:

- `0` Additive Identity for Rationals
- `1` Multiplicative Identity for Rationals

**Closure**: Describes whether if certain Arithmetic Operations and Comination can make The Result Escape The it's Number System.

| Number System    | Addition | Subtraction | Multiplication | Division |
| ---------------- | -------- | ----------- | -------------- | -------- |
| Natural/Positive | ✅      | ❌          | ✅            | ❌       |
| Negative         | ✅      | ❌          | ❌            | ❌       |
| Whole            | ✅      | ❌          | ✅            | ❌       |
| Integers         | ✅      | ✅          | ✅            | ❌       |
| Rationals        | ✅      | ✅          | ✅            | ❌       |

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
| Natural/Positive | ✅      | ❌          | ✅            | ❌       |
| Negative         | ✅      | ❌          | ✅            | ❌       |
| Whole            | ✅      | ❌          | ✅            | ❌       |
| Integers         | ✅      | ❌          | ✅            | ❌       |
| Rationals        | ✅      | ❌          | ✅            | ❌       |

**Distributive**: 
$$
a(b + c) = ab + ac
$$



---
### Other Number Types:
**Even Numbers**: Numbers that can only be represeted as a Multiple of $2$

$$
2a
$$
- These Number must always have  any of $0, 2, 4, 6, 8$ in the *one's unit digit place*

**Odd Numbers**: Numbers that can't be represeted as a Multiple of $2$

$$
2a+1
$$
- These Number must always have  any of $1, 3, 5, 6, 9$ in the *one's unit digit place*

**Prime Numbers**: Numbers that can only be divided by $1$ and *itself*, having exactly 2 factors

$$
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...
$$

- Every Prime Number is an Odd-Number except `2`
- **Twin Primes**: difference between 2 Prime Number is `2`
  
  $(a+2 = b) ⟹ a, b$

  `(Note: Both Numbers Need to Prime Numbers for this to be true)`

- **Co-Prime Numbers**: 2 numbers with only 1 as a common factor.


**Composite Numbers**: Numbers that doesn't have exactly 2 factors

$$
1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36...
$$

**Decimals**: Floating Point Numbers that exists in-between Numbers
$$
1.001, 1.002, 1.0000434 ...
$$



## Factors

A Number is a multiple of each of it's factors

- **1** is The Factor of every Number

  $1\times a = a$ 

- Every Number is a Factor of itself

  $a \div a = 1 $

- Every factor is an Exact divisor of that number and The Remainder should be `0`

  $ a \mod b = 0$ ✅

  $ a \mod b \neq 0$ ❌

- Every factor is Either Equal or Less than the number

  $ a \geq b $
  
  - `b` is factor of `a`

- Count of Factors is of a Number is **Finite**
- Count of Multiples of a Number is **Infinite**

| Number | Factors        | isPrime |
| ------ | -------------- | ------- |
| $1$    | $1$            | ❌      |
| $2$    | $1,2$          | ✅      |
| $3$    | $1,3$          | ✅      |
| $4$    | $1,2,4$        | ❌      |
| $5$    | $1,5$          | ✅      |
| $6$    | $1,2,3,6$      | ❌      |
| $7$    | $1,7$          | ✅      |
| $8$    | $1,2,4,8$      | ❌      |
| $9$    | $1,3,9$        | ❌      |
| $10$   | $1,2,5,10$     | ❌      |
| $11$   | $1,11$         | ✅      |
| $12$   | $1,2,3,4,6,12$ | ❌      |

Divisibility Rule

| Number | Rule                                          |
| ------ | --------------------------------------------- |
| 1      | Always                                        |
| 2      | If Even                                       |
| 3      | Sum of All digits is Multiple of 3            |
| 4      | with 3+ digits, last 2 digits divisible by it |
| 5      | `0` or `5` in one's place                     |
| 6      | Divisible by both 2 and 3                     |
| 8      | with 4+ digits, last 3 digits divisible by it |
| 9      | sum of all digits divisible by it             |
| 10     | `0` in one's place                            |
| 11     | -                                             |

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


**Exponent Table**:
| Base | 2     | 3      | 4        |
| ---- | ----- | ------ | -------- |
| $1$  | $1$   | $1$    | $1$
| $2$  | $4$   | $8$    | $16$
| $3$  | $9$   | $27$   |
| $4$  | $16$  | $64$   |
| $5$  | $25$  | $125$  |
| $6$  | $36$  | $216$  |
| $7$  | $49$  | $343$  |
| $8$  | $64$  | $516$  |
| $9$  | $81$  | $729$  |
| $10$ | $100$ | $1000$ |
| $11$ | $121$ | $1331$ |
| $12$ | $144$ | $1728$ |
| $13$ | $169$ | $2197$ |
| $14$ | $196$ | $2744$ |
| $15$ | $225$ | $3375$ |
| $16$ | $256$ | $4096$ |
| $17$ | $289$ | $4913$ |
| $18$ | $324$ | $5832$ |
| $19$ | $361$ | $6859$ |
| $20$ | $400$ | $8000$ |

**Standard Form**: Representation of Very Large/Small Numbers using:
$$a \times 10^n$$

### Laws of Exponent

$$
a^m \times a^n = a^{m+n}
$$
$$
(a^m)^n = a^{mn}
$$
$$
a^m \times b^m = (ab)^m
$$


**Integer Exponents**: where `n` is Integer

$$
a^n = a \times a...
$$
$$
a^3 = a \times a \times a
$$
$$
a^2 = a \times a
$$
$$
a^1 = a \times \frac{a}{a} = a
$$
$$
a^0 = \frac{a}{a} = 1
$$
$$
a^{-1} = \frac{1}{a}
$$
$$
a^{-2} = \frac{1}{a} \times \frac{1}{a} = \frac{1}{a^2}
$$
$$
a^{-3} = \frac{1}{a} \times \frac{1}{a} \times \frac{1}{a} = \frac{1}{a^3}
$$
$$
a^{-n} = \frac{1}{a} \times \frac{1}{a} ... = \frac{1}{a^n}
$$

## Square
**Square**: Where Numbers are Exponentiated to The Power of 2, and It create a Geometric 2 Dimentional Square
$$
a^2 = a \times a
$$


## Cube
**Cube**: Where Numbers are Exponentiated to The Power of 3, and It create a Geometric 3 Dimentional Cube
$$
a^3
$$

# Calculus
# Differential Equations
# Combinatorics
# Topology
# Logic
## Set Theory





# Applied Mathematics

# Financial Mathematics
# Turing Machine
# Information Theory
# Statistics
# Game Theory
# Cryptography
