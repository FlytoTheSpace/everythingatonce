
- [Back to Maths](./maths.md)
- [Back to Home](../../README.md)

# Algebra
**Algebra**: a field about Abstraction and Algebraic Systems

- [Elementary Algebra](#elementary-algebra)
- [Abstract Algebra](#abstract-algebra)
- [Boolean Algebra](#boolean-algebra)
	- [Units](#units)
	- [Logic Gates](#logic-gates)
	- [Latches](#latches)
	- [Arithmetic](#arithmetic)

# Elementary Algebra

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

## Operations

### Addition/Subtraction

- Terms can be added together if the Algebraic coefficients are the same

$$
ax \pm bx = (a + b)x
$$

eg.
$$
x + x = 2x
$$

### Product

$$
a \cdot (b + c + d + ...) = ab + ac + ad + ...
$$


$$
(a + b + c + ...)(u + v + w + ...) \newline
= a \cdot (u + v + w + ...) \newline
+\ b \cdot (u + v + w + ...) \newline
+\ c \cdot (u + v + w + ...) \newline
+\ ... \cdot (u + v + w + ...) \newline
= au + av + aw + a \cdot ... \newline
+\ bu + bv + bw + b \cdot ... \newline
+\ cu + cv + cw + c \cdot ... \newline
+ ...
$$

### Factorization

$$
ax + bx = x \cdot (a + b)
$$

## Equations

$$
LHS = RHS
$$

**Transposing**: Switch of Terms from one side to another, along with the inversion of Operand

- Addition/Subtraction

	$$x + y = z$$
	
	$$x = z - y$$

- Multiplication/Division

$$
x \times y = z
$$
$$
x = z \div y
$$

- Power/Root

$$
x = y^n
$$
$$
\sqrt[n]{x} = y
$$

More generally:

$$
x = y
$$
$$
f(x) = f(y) 
$$

$f$ an operating on both inputs

## Polynomials

Polynomials are of form:

$$
P(x) = a_0 +\sum_{k=1}^na_kx^k \newline
= a_0 + a_1x + a_2x^2 + a_3x^3 + a_4x^4 + a_5x^5 + a_6x^6 + ...
$$

The value `n` is called the Degree of the Polynomial, long as $a_n \neq 0$ 

### Roots of Polynomials

Roots of Polynomials are values of `x` such that the following is true:

$$
P(a) = 0
$$

graphically, they are the `X` cordinate of the point where the Graph of the Polynomials intersects the X axis


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

## Quadratic

where the degree of the polynomial is `2`

$$
ax^2 + bx + c
$$

Root of the Quadratic Polynomial

$$
ax^2 + bx + c = 0 \newline
$$

General Formula:
$$
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

**Factorization**:
Quadratic Polynomials can be factored into the following form
$$
ax^2 + bx + c = (px + m)(qx + n) \newline
= (pq)x^2 + (pn + qm) x + (mn)
$$
by matching the coefficients we get:

$a = pq$

$b = pn + qm$

$c = mn$

there are now 3 equations and 4 unknowns, it results in an undeterminate set of equation which can't be solved uniquely, so we have a few options:

- Trial and error: guessing and checking for solutions ($p, q, m, n$) (factor theorem may help)
- use the Quadratic Formula to factor it.

The Quadratic formula tells us that:

$$
ax^2 + bx + c = 0
$$
then:
$$
x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}
$$
we may call those solutions to the equation $c_1$ and $c_2$, so:
$$
c_1 := \frac{- b + \sqrt{b^2-4ac}}{2a}
$$
$$
c_2 := \frac{- b - \sqrt{b^2-4ac}}{2a}
$$

$$
x = c_1, c_2
$$
$$
x - c_1 = 0
$$
$$
x - c_2 = 0
$$
now the original expression can be written as:

$$
a \cdot (x - c_1)(x-c_2) = 0
$$

whether take $c_1$ or $c_2$ as the value of $x$ this equation will hold true.
define:

$$
a := pq \newline
b := pn + qm \newline
c := mn \newline
$$

for some value(*s*) of `x`
$$
ax^2 + bx + c = 0
$$
$$
x = \frac{- b \pm \sqrt{b^2 - 4ac}}{2a} \newline
$$
substitue values of `a`, `b` and `c`
$$
x = \frac{- (pn + qm) \pm \sqrt{(pn + qm)^2 - 4(pq)(mn)}}{2pq} \newline
= \frac{- (pn + qm) \pm \sqrt{\color{DodgerBlue}(pn)^2 + 2(pn)(qm) + (qm)^2\color{white} - 4pqmn}}{2pq} \newline
= \frac{- (pn + qm) \pm \sqrt{(pn)^2 \color{MediumSeaGreen} + 2pqnm\color{white} + (qm)^2 \color{orangered} - 4pqmn \color{white}}}{2pq} \newline
= \frac{- (pn + qm) \pm \sqrt{(pn)^2 \color{DodgerBlue} - 2pqnm\color{white} + (qm)^2 }}{2pq} \newline
= \frac{- (pn + qm) \pm \sqrt{(pn)^2 - 2(pn)(qm) + (qm)^2 }}{2pq} \newline 
= \frac{- (pn + qm) \pm \color{orangered}\sqrt{\color{DodgerBlue}(pn - qm)\color{MediumSeaGreen}^2\color{white}}}{2pq} \newline 
= \frac{- (pn + qm) \pm (pn - qm)\color{white}}{2pq} \newline 
$$
$$
c_1 = \frac{- pn - qm + (pn - qm)}{2pq} \newline 
= \frac{\color{orangered} - pn \color{white} - qm \color{MediumSeaGreen} + pn \color{white} - qm\color{white}}{2pq} \newline 
= \color{dodgerblue} - \frac{2qm}{\color{white}2pq}\color{white} \newline 
= - \frac{m}{\color{white}p} \newline 
$$

$$
c_2 = \frac{- pn - qm - (pn - qm)}{2pq} \newline 
= \frac{- pn \color{orangered} - qm \color{white} - pn \color{mediumseagreen} + qm\color{white}}{2pq} \newline 
= \color{dodgerblue} - \frac{2pn}{\color{white}2pq}\color{white} \newline 
= - \frac{n}{q} \newline 
$$

so this shows that infact The Roots of the Quadratic Polynomial are:

$$
c_1 = - \frac{m}{p}
$$
$$
c_2 = - \frac{n}{q}
$$

and in the Original expression:

$$
ax^2 + bx + c = (px + m)(qx + n) \newline
= pq(x + \frac{m}{p})(x + \frac{n}{q}) \newline
= pq(x - c_1)(x - c_2) \newline
$$


at this point the Quadratic can be factorized by Prime Factorization of $a$ and distributing those factors in such a way that all the denominators are cancelled out

> Note that it assumes expressions like $(px + m)$ are not futher factorable otherwise this method will simply factorize it futher, leaving $ax^2 + bx + c = S \cdot (sx + u)(tx + v)$

eg.

$p = 3, q = 4, m = 5, n = 6$

$4 \cdot 3 x^2 + (3 \cdot 6 + 4 \cdot 5)x + 5 \cdot 6 \newline$
$12 x^2 + (18 + 20)x + 30 \newline$

Q. $12 x^2 + 38x + 30 \newline$

Solution:

$$
12 x^2 + 38x + 30 = 0 \newline
x = \frac{-38 \pm \sqrt{38^2 - 4\cdot 12 \cdot 30}}{2 \cdot 12} \newline
= \frac{-38 \pm \sqrt{1444 - 1440}}{2 \cdot 12} \newline
= \frac{-38 \pm \sqrt{4}}{2 \cdot 12} \newline
= \frac{-38 \pm 2}{2 \cdot 12} \newline
= \frac{-19 \cdot 2 \pm 2}{2 \cdot 12} \newline
= \frac{-19 \pm 1}{12} \newline
$$
$$
c_1 = \frac{-19 + 1}{12} = \frac{- 2 \cdot 3 \cdot 3}{2 \cdot 2 \cdot 3} = - \frac{3}{2}
$$
$$
c_2 = \frac{-19 - 1}{12} = \frac{- 2 \cdot 2 \cdot 5}{2 \cdot 2 \cdot 3} = -\frac{5}{3}
$$

$$
12 x^2 + 38x + 30 = 12 (x - (- \frac{3}{2})) (x - (- \frac{5}{3})) \newline
= 2 \cdot 2 \cdot 3 (x + \frac{3}{2}) (x + \frac{5}{3}) \newline
= 2(2x + 2\frac{3}{2}) (3x + 3\frac{5}{3}) \newline
$$


$$
= 2(2x + 3) (3x + 5) \newline
$$
this result is an even more further factorized result than the original 
$(3x + 5)(4x + 6)$ expression, and notice $4x + 6$ can be factored into $2(2x + 3)$ turning into our answer.

## Cubic

where the degree of the Polynomial is `3`

$$ax^3 + bx^2 + cx + d = 0$$


Roots of The Polynomial:

- **Depressed Cubic**

are of the form:

$$ax^3 + bx + c$$
$$ax^3 + bx + c = 0$$
$$\frac{ax^3 + bx + c}{a} = \frac{0}{a}$$
$$x^3 + \frac{b}{a}x + \frac{c}{a} = 0$$

Binomial Expansion of $u + v$ raised to the power $3$:
$$ (u + v)^3 = u^3 + 3u^2v + 3uv^2 + v^3 \newline
= u^3 + 3uv(u + v) + v^3 \newline
(u + v)^3 - (u^3 + 3uv(u + v) + v^3) = 0 \newline
(\underbrace{u + v}_{x})^3 + (\underbrace{- 3uv}_{b/a})(\underbrace{u + v}_{x}) + \underbrace{(- u^3 - v^3)}_c{} = 0 \newline
$$

$$
x = u + v \newline
\frac{b}{a} = -3uv \newline
\frac{c}{a} = - (u^3+ v^3) \newline
uv = - \frac{b}{3a} \newline
u^3 + v^3 + \frac{c}{a} = 0\newline
u^3 (u^3 + v^3 + \frac{c}{a}) = u^3(0)\newline
u^6 + (uv)^3 + \frac{c}{a}u^3 = 0\newline
(u^3)^2 + \frac{c}{a}(u^3) + (- \frac{b}{3a})^3 = 0\newline
$$

using the quadratic:
$$
u^3 = \frac{- (c/a) \pm \sqrt{(c/a)^2 - 4\cdot 1 \cdot (- \frac{b}{3a})^3}}{2 \cdot 1} \newline
= \frac{- (c/a)}{2} \pm \frac{\sqrt{(c/a)^2 + 4 (\frac{b}{3a})^3}}{2} \newline
= - \frac{c}{2a} \pm \sqrt{\frac{1}{4}((\frac{c}{a})^2 + 4(\frac{b}{3a})^3)} \newline
u^3 = - \frac{c}{2a} \pm \sqrt{(\frac{c}{2a})^2 + (\frac{b}{3a})^3} \newline
u, v = \sqrt[3]{- \frac{c}{2a} \pm \sqrt{(\frac{c}{2a})^2 + (\frac{b}{3a})^3}} \newline

x = u + v \newline
$$

$$
x = \sqrt[3]{- \frac{c}{2a} \pm \sqrt{(\frac{c}{2a})^2 + (\frac{b}{3a})^3}} + \sqrt[3]{- \frac{c}{2a} \mp \sqrt{(\frac{c}{2a})^2 + (\frac{b}{3a})^3}}
$$ 

$b/a$ and $c/a$ are usually taken as `p` and `q` correspondingly, so it becomes

$$x^3 + px + q = 0$$
$$
x = \sqrt[3]{- \frac{q}{2} \pm \sqrt{(\frac{q}{2})^2 + (\frac{p}{3})^3}} + \sqrt[3]{- \frac{q}{2} \mp \sqrt{(\frac{q}{2})^2 + (\frac{p}{3})^3}}
$$

**General Solution**:

$$
ax^3 + bx^2 + cx + d = 0
$$
Inflication point
$$
\frac{d^2}{dx^2}(ax^3 + bx^2 + cx + d) = 0 \newline
6ax + 2b = 0 \newline
x = -\frac{b}{3a} \newline
$$
Substituion:

$$
x = y + (-\frac{b}{3a})
$$

$$
ax^3 + bx^2 + cx + d = 0 \newline

a(y - \frac{b}{3a})^3 + 
b(y - \frac{b}{3a})^2 + 
c(y - \frac{b}{3a}) + 
d = 0 \newline

a(y^3 - 3y^2\frac{b}{3a} + 3y(\frac{b}{3a})^2 - (\frac{b}{3a})^3 ) + 
b(y^2 - 2y\frac{b}{3a} + (\frac{b}{3a})^2) + 
cy - \frac{cb}{3a} + 
d = 0 \newline

a(y^3 - \frac{3by^2}{3a} + \frac{3b^2y}{9a^2} - \frac{b^3}{27a^3} ) + 
b(y^2 - \frac{2yb}{3a} + \frac{b^2}{9a^2}) + 
cy - \frac{cb}{3a} + 
d = 0 \newline

ay^3 - \frac{aby^2}{a} + \frac{ab^2y}{3a^2} - \frac{ab^3}{27a^3}+ 
by^2 - \frac{2yb^2}{3a} + \frac{b^3}{9a^2} + 
cy - \frac{cb}{3a} + 
d = 0 \newline

ay^3 - by^2 + \frac{b^2y}{3a} - \frac{b^3}{27a^2} + 
by^2 - \frac{2b^2y}{3a} + \frac{b^3}{9a^2} + 
cy - \frac{bc}{3a} + 
d = 0 \newline

ay^3 + \frac{b^2y}{3a} - \frac{b^3}{27a^2} 
- \frac{2b^2y}{3a} + \frac{b^3}{9a^2} + 
cy - \frac{bc}{3a} + 
d = 0 \newline

ay^3 + \frac{b^2}{3a}y - \frac{2b^2}{3a}y + cy - \frac{b^3}{27a^2} + \frac{b^3}{9a^2} - \frac{bc}{3a} + d = 0 \newline
ay^3 + (\frac{b^2}{3a} - \frac{2b^2}{3a} + c)y + (- \frac{b^3}{27a^2} + \frac{b^3}{9a^2} - \frac{bc}{3a} + d) = 0 \newline
ay^3 + (c - \frac{b^2}{3a})y + (\frac{3b^3 - b^3}{27a^2} - \frac{bc}{3a} + d) = 0 \newline

ay^3 + 
(c - \frac{b^2}{3a})y + 
(\frac{2b^3}{27a^2} - \frac{bc}{3a} + d) = 0 \newline
$$

Using the Depressed Cubic to solve for `y`

> Depressed Cubic general formula: ($a \neq 0$)
> $$ax^3 + bx + c = 0$$ 
> $$ x = \sqrt[3]{- \frac{c}{2a} \pm \sqrt{(\frac{c}{2a})^2 + (\frac{b}{3a})^3}} + \sqrt[3]{- \frac{c}{2a} \mp \sqrt{(\frac{c}{2a})^2 + (\frac{b}{3a})^3}}$$

$$
y = \sqrt[3]{- \frac{(\frac{2b^3}{27a^2} - \frac{bc}{3a} + d)}{2a} \pm \sqrt{(\frac{(\frac{2b^3}{27a^2} - \frac{bc}{3a} + d)}{2a})^2 + (\frac{(c - \frac{b^2}{3a})}{3a})^3}} + ... \newline
$$

$$
y = \sqrt[3]{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}) \pm \sqrt{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a})^2 + (\frac{c}{3a} - \frac{b^2}{9a^2})^3}} + \newline
\sqrt[3]{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}) \mp \sqrt{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a})^2 + (\frac{c}{3a} - \frac{b^2}{9a^2})^3}}
$$

Final Step:
$$x = y - \frac{b}{3a}$$
$$
y - \frac{b}{3a} = \sqrt[3]{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}) \pm \sqrt{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a})^2 + (\frac{c}{3a} - \frac{b^2}{9a^2})^3}} + \newline
\sqrt[3]{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}) \mp \sqrt{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a})^2 + (\frac{c}{3a} - \frac{b^2}{9a^2})^3}} - \frac{b}{3a}
$$

**Full General Cubic Solution**:

$$
ax^3 + bx^2 + cx + d = 0
$$

$$
x = \sqrt[3]{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}) \pm \sqrt{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a})^2 + (\frac{c}{3a} - \frac{b^2}{9a^2})^3}} + \newline
\sqrt[3]{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a}) \mp \sqrt{(- \frac{b^3}{27a^3} + \frac{bc}{6a^2} - \frac{d}{2a})^2 + (\frac{c}{3a} - \frac{b^2}{9a^2})^3}} \newline - \frac{b}{3a}
$$



## Binomial Theorem

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


| k | 
| 0 |

# Abstract Algebra

# Boolean Algebra
**Boolean Algebra**: A Branch of Algebra where that works with Base 2 system

- `1` standing for **TRUE**, **ON**.
- `0` standing for **FALSE**, **OFF**.

## Logic

Main Logic:

- **Conjunction**, **AND** `(2 inputs)`: True if both inputs are True.
- **Disjunction**,  **OR** `(2 inputs)`: True if any of the inputs are True.
- **Negation**, **NOT** `(1 input)`: Inverts the given Input.
- **Exclusive OR**, **XOR** `(2 inputs)`: True if both inputs are not the same.

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

**Inverted Logic**:

- **NOT Conjunction**, **NAND** `(2 inputs)`: returns `1` if both inputs are NOT `1`.
- **NOT Disjunction**,  **NOR** `(2 inputs)`: returns `1` if any of the inputs are NOT `1`.
- **NOT Exclusive OR**, **XNOR** `(2 inputs)`: returns `1` if both inputs ARE the same.

| $a$ | $b$ | `NAND` $\lnot (a\land b)$ | `NOR` $\lnot (a\lor b)$ | `XNOR` $\lnot (a \oplus b)$ |
| --- | --- | ------------------------- | -------------- | ----------------------- |
| $0$ | $0$ | $1$                       | $1$            | $1$                     |
| $0$ | $1$ | $1$                       | $0$            | $0$                     |
| $1$ | $0$ | $1$                       | $0$            | $0$                     |
| $1$ | $1$ | $0$                       | $0$            | $1$                     |

**Totality of Logic**:

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

