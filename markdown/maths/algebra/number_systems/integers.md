# Integers

$$\mathbb{N}[-1] = \mathbb{Z}$$

$$(a = b \iff f(a) = f(b)) \implies \exists p [s(p(a)) = p(s(a)) = a]$$

**A1**:
$$\mathbb{N} \subset \mathbb{Z}$$

**A2**:
$$\forall a \in \mathbb{Z}[p(a) \in \mathbb{Z}]$$

**A3**:
$$\forall a, b \in \mathbb{Z} [a = b \iff s(a) = s(b)]$$

**A4**: Induction.
$$
\forall A \subset \mathbb{Z}[ 0 \in A \land \forall n \in A(s(n) \in A \land p(n) \in A) \implies A = \mathbb{Z}]
$$

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

> Note-to-Self: NEEDS INDUCTION

$$p^{n}(0) := -n$$

$$p^{m}(n) = p^{n}(m)$$

## Addition

**Addition Axioms**:

**IA3**.

$$\forall a \in \mathbb{Z}[a + 0 = a]$$

**IA4**.

$$\forall a, b \in \mathbb{Z}[p(a + b) = a + p(b)]$$

---

> Note-to-Self: NEEDS MORE INDUCTION!!!!!!!!

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

Comparison:

$$\mathbb{Z}^{+} = \{n\ |\ n \in \mathbb{N}_{>0}\}$$

$$\mathbb{Z}^{-} = \{-n\ |\ n \in \mathbb{N}_{>0}\}$$

$$\forall a, b[a < b \iff \exist c \in \mathbb{Z}^{+}(a + c = b)]$$

$$\forall a, b[a > b \iff \exist c \in \mathbb{Z}^{+}(a = b + c)]$$

$$\forall a, b[a \leq b \iff \exist c \in \mathbb{Z}^{+}\cup\{0\}(a + c = b)]$$

$$\forall a, b[a \geq b \iff \exist c \in \mathbb{Z}^{+}\cup\{0\}(a = b + c)]$$
