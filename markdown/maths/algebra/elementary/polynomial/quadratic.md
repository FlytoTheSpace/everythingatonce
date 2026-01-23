# Quadratic

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

# Factorization

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
