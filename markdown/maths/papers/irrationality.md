
# Irrationality of $\sqrt{2}$

## Some Context:

**Fractions**: are defined as:

$$
\frac{p}{q}
$$
where $p, q \in \mathbb{Z}$ and $q \neq 0$ as it is `undefined` for divison.

---

**Fraction Coprime Theorem**:

"for p and q as Integers"

$$\forall p, q \in \mathbb{Z}$$

"p and q have a common factor of a":

$\exists a (\gcd(p, q) = a)$


$r := p/a$

$s := q/a$

"r and s do not a common factor bigger than 1":

$\implies \gcd(r, s) = 1$

we can rewrite our Fraction of $p, q$ as:
$$
\frac{p}{q} = \frac{a \cdot r}{a \cdot s} = \frac{r}{s}
$$
This new ratio should be a valid Fraction:
$$\frac{r}{s} \in \mathbb{Q}$$

---

**Squares of Even/Odd Integers**:

for $n \in \mathbb{Z}$

**Even Numbers** Defined as:
$$2n$$
**Odd Numbers** Defined as:
$$2n + 1$$

Squares:

"Even Numbered Squares always result in Even Numbers":
$$(2n)^2 = 2^2n^2 = \underbrace{2(2n^2)}_{\text{even}}$$

"Odd Numbered Squares always result in Odd Numbers":
$$
(2n + 1)^2 = (2n)^2 + 2(2n) + 1 \newline
= \underbrace{2(2n^2 + 2n) + 1}_{\text{odd}}
$$

This also goes in reverse so for some Square if it's even or odd it's *root* will also be the corresponding even/odd.

---

**Proof by Contradiction**: is an approach to prove that a **statement** is true, by creating a system where it is assumed that the statement is **False** and finding a situation where the this System *fails* in such a way that the *false* Assumtion is the only thing that can take the blame, thus the only possibility remaining is that original statement is **True** in a rigerous system.

## Proof of Irrationality of $\sqrt{2}$

assume that:
$$\sqrt{2} = \frac{p}{q}$$
where $p, q$ are components of the fraction, and the **Fraction Coprime Theorem** (i.e. $p$ and $q$ are coprime) is applied so they *must no longer have any common divisors*.

now continue:

$$
\sqrt{2} = \frac{p}{q} \newline
\sqrt{2}^2 = \left(\frac{p}{q}\right)^2 \newline
2 = \frac{p^2}{q^2} \newline
2q^2 = p^2 \newline
$$

$p^2 = 2(2a^2) = (2a)^2$

$$
2q^2 = (2a)^2 \newline
2q^2 = 2^2a^2 \newline
q^2 = 2a^2 \newline
$$

$q^2 = 2(2b^2) = (2b)^2$

from this we get:

$p = 2a$, $q = 2b$

they have a common factor of $2$ so the assumption that they can be and are in their in their co-prime ratio is **False**.

$$\therefore \sqrt{2} \notin \mathbb{Q}$$


