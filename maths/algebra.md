
- [Back to Maths](./maths.md)
- [Back to Home](../README.md)

# Algebra
**Algebra**: a field of Mathematics consisting of English Aplhabet Represeting Number, with many use cases such as Representing Unknown/Dynamic Values.

- [Core Algebra](#core-algebra)
	- [Addition/Subtraction](#additionsubtraction)
	- [Multiplication/Divison](#multiplicationdivison)
	- [Factorization](#factorization)
	- [Equations](#equations)
		- [Linear Equations](#linear-equations)
		- [Quadratics](#quadratics)
		- [Cubic](#cubics)
- [Abstract Algebra](#abstract-algebra)
- [Boolean Algebra](#boolean-algebra)
	- [Units](#units)
	- [Logic Gates](#logic-gates)
	- [Latches](#latches)
	- [Arithmetic](#arithmetic)

# Core Algebra

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

## Addition/Subtraction

- Terms can Only be Added together when the Algebraic Factors are the same

$$
a + a = 2a
$$
$$
ab \pm ac = a(b \pm c)
$$

Not Allowed:
$$
a^2 + a \neq 2a^2
$$

## Multiplication/Divison

- **Monomial**, **Monomial**

	- Multiplication
	$$a \times a = a^2$$
	$$a \times b = ab$$

	- Division:
	$$a^n \div a = a^{n-1}$$
	$$a \div b = \frac{a}{b}$$
	$$ab \div b = a$$

- **Monomial**, **Binomial**

	- Multiplication
	$$a \times (b + c) = ab + ac$$

	- Division
	> $a \neq 0$, $b + c \neq 0$


	$$\frac{a}{ab + ac} = \frac{a}{a} \cdot \frac{1}{b + c} = \frac{1}{b + c}$$

	$$\frac{ab + ac}{a} = \frac{a(b + c)}{a \cdot 1} = \frac{a}{a} \cdot \frac{b + c}{1} = b + c$$
- **Binomial**, **Binomial**

	- Multiplication
	$$(a + b)(c + d) = a(c + d) + b(c + d) = ac + ad + bc + bd$$

	$$(a + b)^2 = (a + b)(a + b) = a^2 + 2ab + b^2$$

	- Division
	> $c + d \neq 0$

	$$\frac{a + b}{c + d} = \frac{a}{c + d} + \frac{b}{c + d}$$

- **Binomial**, **Trinomial**

	- Multiplication

	$$(a + b)(x + y + z) = a(x + y + z) + b(x + y + z) = ax + ay + az + bx + by + bz$$

## Factorization

$$
a^2 \pm ab = a(a \pm b)
$$
$$
\pm ab \pm ac = \pm a(b + c) = a(\pm b \pm c)
$$
$$
\pm ab \mp ac = a(b \mp c) = \mp a ( \mp b \pm c)
$$


## Equations

$$
LHS = RHS
$$

**Transposing**: Switch of Terms from one side to another, along with the inversion of Operand

- Addition/Subtraction

	$$a + b = c$$
	
	$$a = c - b$$

- Multiplication/Division

$$
a \times b = c
$$
$$
a = c \div b
$$

<br>

$$
a \times b = c + d
$$
$$
a = \frac{c + d}{b}
$$


## Linear

**Linear**: a variable with either 0 or 1 as their power 

$x^1$, $x^0$

**One Variable**:

---

$2x - 3 = x + 2$

$2x - x - 3 = 2$

$x - 3 = 2$

$x = 2 + 3$

$x = 5$

## Quadratic

**Quadratic**: a where the variable is squared $x^2$

**Quadratic Equation**:

$$
ax^2 + bx + c = 0 \newline
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

- **Derivationation**:

$$ax^2 + bx + c = 0 $$
$$\frac{\color{DodgerBlue} a \color{white} x^2 + bx + c}{\color{orangered}a} = \frac{0}{\color{orangered}a}$$
$$x^2 + \frac{b}{a}x + \frac{c}{a} = 0$$
$$x^2 + \frac{b}{a}x \color{DodgerBlue} + \frac{c}{a} \color{orangered} - \frac{c}{a} \color{white} = 0 \color{orangered} - \frac{c}{a} \color{white}$$
$$x^2 + \frac{b}{a}x = - \frac{c}{a}$$
$$x^2 + \frac{b}{a}x \color{MediumSeaGreen} + (\frac{b}{2a})^2 \color{white} = - \frac{c}{a} \color{MediumSeaGreen} + (\frac{b}{2a})^2 \color{white}$$
$$\color{DodgerBlue} (x + \frac{b}{2a})^2 \color{white} = - \frac{c}{a} + (\frac{b}{2a})^2$$
$$(x + \frac{b}{2a})^2 = - \frac{c}{a} + \color{DodgerBlue} \frac{b^2}{4a^2} \color{white}$$
$$(x + \frac{b}{2a})^2 = - \frac{\color{MediumSeaGreen} 4a \cdot \color{white} c}{\color{MediumSeaGreen} 4a \cdot \color{white} a} + \frac{b^2}{4a^2}$$
$$(x + \frac{b}{2a})^2 = \frac{b^2}{4a^2} - \frac{4ac}{4a^2}$$
$$(x + \frac{b}{2a})^2 = \frac{\color{DodgerBlue} b^2 - 4ac}{4a^2}$$
$$\color{orangered}\sqrt{\color{white}(x + \frac{b}{2a})^{\color{DodgerBlue}2}} \color{white} = \color{orangered}\sqrt{\color{white}\frac{b^2 - 4ac}{4a^2}} \color{white}$$
$$(x + \frac{b}{2a}) = \frac{\color{DodgerBlue} \pm \sqrt{\color{white}b^2 - 4ac}}{\color{DodgerBlue}\sqrt{\color{white}4a^2}}$$
$$x + \frac{b}{2a} = \frac{\pm \sqrt{b^2 - 4ac}}{\color{DodgerBlue} 2a}$$
$$x \color{DodgerBlue} + \frac{b}{2a} \color{orangered} - \frac{b}{2a} \color{white} = \frac{\pm \sqrt{b^2 - 4ac}}{2a} \color{orangered} - \frac{b}{2a} \color{white}$$
$$x = \frac{\color{DodgerBlue}-b \color{white} \pm \sqrt{b^2 - 4ac}}{2a}$$
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$


## Cubic


**Cubic**: a where the variables can be cubed $x^2$

$$ax^3 + bx^2 + cx + d = 0$$


**Derivationation**:

## Binomial Theorem
> $n \in \mathbb{Z}^+$
$$(a + b)^n = \sum_{k = 0}^n \begin{pmatrix}n\cr k\end{pmatrix}a^{n-k}b^k = \sum_{k = 0}^n \frac{n!}{k!(n-k)!} a^{n-k}b^k$$
> $n \notin \mathbb{Z}^+$
$$(a + b)^n = \sum_{k = 0}^\infty \begin{pmatrix}n\cr k\end{pmatrix}a^{n-k}b^k = \sum_{k = 0}^\infty \frac{n!}{k!(n-k)!} a^{n-k}b^k$$

# Abstract Algebra

# Boolean Algebra
**Boolean Algebra**: A Branch of Algebra where the Variables can only have 2 possible states

- `1` standing for **TRUE**, **ON**.
- `0` standing for **FALSE**, **OFF**.

## Units

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
| **GigaByte** `GB`  | `1000 MegaBytes` | $10^{9}$  |
| **TeraByte** `TB`  | `1000 GigaBytes` | $10^{12}$ |
| **PetaByte** `PB`  | `1000 TeraBytes` | $10^{15}$ |
| **ExaByte** `EB`   | `1000 PetaBytes` | $10^{18}$ |
| **ZetaByte** `ZB`  | `1000 ExaBytes`  | $10^{21}$ |
| **YottaByte** `YB` | `1000 ZetaBytes` | $10^{24}$ |

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

## Logic Gates:

Logic Gates are Gates that Determine the Output of Certain Inputs based on Logic which they Represent

Main Logic Gates:

- **Conjunction**, **AND** `(2 inputs)`: returns `1` if both inputs are `1`.
- **Disjunction**,  **OR** `(2 inputs)`: returns `1` if any of the inputs are `1`.
- **Negation**, **NOT** `(1 input)`: Inverts the given Input.
- **Exclusive OR**, **XOR** `(2 inputs)`: returns `1` if both inputs are not the same.

| $a$ | `NOT` $\lnot a$ |
| --- | --------------- |
| $0$ | $1$             |
| $1$ | $0$             |

| $a$ | $b$ | `AND` $a\land b$ | `OR` $a\lor b$ | `XOR` $a \oplus b$ |
| --- | --- | ---------------- | -------------- | ------------------- |
| $0$ | $0$ | $0$              | $0$            | $0$                 |
| $0$ | $1$ | $0$              | $1$            | $1$                 |
| $1$ | $0$ | $0$              | $1$            | $1$                 |
| $1$ | $1$ | $1$              | $1$            | $0$                 |

**Inverted Logic Gates**:

- **NOT Conjunction**, **NAND** `(2 inputs)`: returns `1` if both inputs are NOT `1`.
- **NOT Disjunction**,  **NOR** `(2 inputs)`: returns `1` if any of the inputs are NOT `1`.
- **NOT Exclusive OR**, **XNOR** `(2 inputs)`: returns `1` if both inputs ARE the same.

| $a$ | $b$ | `NAND` $\lnot (a\land b)$ | `NOR` $\lnot (a\lor b)$ | `XNOR` $\lnot (a \oplus b)$ |
| --- | --- | ------------------------- | -------------- | ----------------------- |
| $0$ | $0$ | $1$                       | $1$            | $1$                     |
| $0$ | $1$ | $1$                       | $0$            | $0$                     |
| $1$ | $0$ | $1$                       | $0$            | $0$                     |
| $1$ | $1$ | $0$                       | $0$            | $1$                     |

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

## Latches

**SR Latch**: A Latch that can Hold upto 1 Bit of Data, with 2 Inputs and 2 Outputs

- $S$, $R$ Inputs
- $Q$, $\lnot Q$ Outputs
- $S$ Sets The Output $Q$ to 1, $\lnot Q$ to 0 
- $R$ Sets The Output $Q$ to 0, $\lnot Q$ to 1
- $\lnot Q$ is Invert of The Main Output $Q$
- value of $Q$ can be 0 or 1 depending on it's initial value
- $S$ and $R$ both 1 at the same is Invalid, as it's not supposed to happen and both Output $Q$ and $\lnot Q$ will be set to 0

Truth Table:

| $S$ | $R$ | $Q$    | $\lnot Q$   |
| --- | --- | ------ | ------ |
| $0$ | $0$ | $1, 0$ | $0, 1$ |
| $1$ | $0$ | $1$    | $0$    |
| $0$ | $1$ | $0$    | $1$    |
| $1$ | $1$ | $0$    | $0$    |

## Arithmetic

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

**Multiplication**: An `AND` Operation On Every Combination of Inputs `a` and `b`, there's no carry.

| $a$ | $b$ | $r$ |
| --- | --- | --- |
| $0$ | $0$ | $0$ |
| $0$ | $1$ | $0$ |
| $1$ | $0$ | $0$ |
| $1$ | $1$ | $1$ |

- for `n` count of inputs
